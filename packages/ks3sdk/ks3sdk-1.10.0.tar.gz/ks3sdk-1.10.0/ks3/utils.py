"""
Some handy utility functions used by several classes.
"""
import os
import pickle
import threading
from concurrent.futures import ThreadPoolExecutor, Future

import crcmod
import errno

import ks3
import six
import io
import base64

from hashlib import md5

from ks3.compat import encodebytes
from ks3.crc64_combine import mkCombineFun
from ks3.exception import KS3ClientError

try:
    import urllib.parse as parse  # for Python 3
except ImportError:
    import urllib as parse  # for Python 2


def get_utf8_value(value):
    if not six.PY2 and isinstance(value, bytes):
        return value

    if not isinstance(value, six.string_types):
        value = six.text_type(value)

    if isinstance(value, six.text_type):
        value = value.encode('utf-8')

    return value


def merge_headers_by_name(name, headers):
    """
    Takes a specific header name and a dict of headers {"name": "value"}.
    Returns a string of all header values, comma-separated, that match thepyo
    input header name, case-insensitive.

    """
    matching_headers = find_matching_headers(name, headers)
    return ','.join(str(headers[h]) for h in matching_headers
                    if headers[h] is not None)


def find_matching_headers(name, headers):
    """
    Takes a specific header name and a dict of headers {"name": "value"}.
    Returns a list of matching header names, case-insensitive.

    """
    return [h for h in headers if h.lower() == name.lower()]


def merge_meta(headers, metadata, provider=None):
    if not provider:
        provider = ks3.provider.get_default()
    metadata_prefix = provider.metadata_prefix
    final_headers = headers.copy()
    for k in list(metadata.keys()):
        if k.lower() in ks3.key.Key.base_user_settable_fields:
            final_headers[k] = metadata[k]
        else:
            final_headers[metadata_prefix + k] = metadata[k]

    return final_headers


def compute_md5(fp, buf_size=8192, size=None):
    """
    Compute MD5 hash on passed file and return results in a tuple of values.
    """
    return compute_hash(fp, buf_size, size, hash_algorithm=md5)


def compute_hash(fp, buf_size=8192, size=None, hash_algorithm=md5):
    hash_obj = hash_algorithm()
    spos = fp.tell()
    if size and size < buf_size:
        s = fp.read(size)
    else:
        s = fp.read(buf_size)
    while s:
        if not isinstance(s, bytes):
            s = s.encode('utf-8')
        hash_obj.update(s)
        if size:
            size -= len(s)
            if size <= 0:
                break
        if size and size < buf_size:

            s = fp.read(size)
        else:
            s = fp.read(buf_size)
    hex_digest = hash_obj.hexdigest()
    base64_digest = encodebytes(hash_obj.digest()).decode('utf-8')
    if base64_digest[-1] == '\n':
        base64_digest = base64_digest[0:-1]
    # data_size based on bytes read.
    data_size = fp.tell() - spos
    fp.seek(spos)
    return (hex_digest, base64_digest, data_size)


def compute_encrypted_md5(fp, buf_size=8192, hash_algorithm=md5):
    hash_obj = hash_algorithm()
    s = fp.read(buf_size)
    while s:
        if not isinstance(s, bytes):
            s = s.encode('utf-8')
        hash_obj.update(s)
        s = fp.read(buf_size)
    hex_digest = hash_obj.hexdigest()
    base64_digest = encodebytes(hash_obj.digest()).decode('utf-8')
    if base64_digest[-1] == '\n':
        base64_digest = base64_digest[0:-1]
    # data_size based on bytes read.
    SEEK_SET = getattr(io, 'SEEK_SET', 0)
    fp.seek(SEEK_SET)
    return (hex_digest, base64_digest)


def convert_adp_headers(adps):
    if adps:
        fop = ""
        for op in adps:
            fop = "%s|tag=saveas" % op["command"]
            if op["bucket"]:
                fop += "&bucket=%s" % (op["bucket"])
            if op["key"]:
                fop += "&object=%s" % (base64.b64encode(op["key"]))
            fop = "%s;" % fop
        fop = fop.rstrip(";")
        headers = {"kss-async-process": parse.quote(fop),
                   "kss-notifyurl": parse.quote("http://127.0.0.1:9000/notify/url")}
        return headers
    else:
        return None


def compute_base64_md5_digest(data):
    m = md5()
    m.update(data)
    base64_digest = encodebytes(m.digest()).decode('utf-8')
    if base64_digest[-1] == '\n':
        base64_digest = base64_digest[0:-1]
    return base64_digest


def get_default_user_agent():
    # import platform
    # platform.version()
    # platform.version()
    return 'PythonSDK/' + ks3.__version__


def to_boolean(value, true_value='true'):
    if value == true_value:
        return True
    else:
        return False


def silently_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def force_rename(src, dst):
    try:
        os.rename(src, dst)
    except OSError as e:
        if e.errno == errno.EEXIST:
            silently_remove(dst)
            os.rename(src, dst)
        else:
            raise


class Crc64(object):
    _POLY = 0x142F0E1EBA9EA3693
    _XOROUT = 0XFFFFFFFFFFFFFFFF

    def __init__(self, init_crc=0):
        self.crc64 = crcmod.Crc(self._POLY, initCrc=init_crc, rev=True, xorOut=self._XOROUT)

        self.crc64_combineFun = mkCombineFun(self._POLY, initCrc=init_crc, rev=True, xorOut=self._XOROUT)

    def __call__(self, data):
        self.update(data)

    def update(self, data):
        self.crc64.update(data)

    def combine(self, crc1, crc2, len2):
        return self.crc64_combineFun(crc1, crc2, len2)

    @property
    def crc(self):
        return self.crc64.crcValue


def compute_file_crc64(file_name, start=None, end=None, block_size=64 * 1024):
    with open(file_name, 'rb') as fp:
        fp = FpAdapter(fp)
        if start is not None:
            fp.seek(start)
        while True:
            if end is not None:
                if fp.tell() >= end:
                    break
                else:
                    data = fp.read(min(block_size, end - fp.tell() + 1))
            else:
                data = fp.read(block_size)
            if not data:
                break

    return str(fp.crc)


def compute_data_crc64(data, init_crc=0):
    """
    Calculate the crc64 of a string

    :param data: The content of the string
    :param init_crc: The initial value of crc64, default is 0
    :return The crc64 value of the string
    """
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    crc64 = Crc64(init_crc)
    crc64.update(data)
    return str(crc64.crc)


class FpAdapter(object):
    def __init__(self, fp):
        super(FpAdapter, self).__init__()
        self.fp = fp
        self.crc64_handler = Crc64()
        self.first_read_done = False
        self.counter = 0

    def read(self, size=0):
        try:
            data = self.fp.read(size)
            self.counter += len(data) if data else 0
        except Exception as e:
            raise KS3ClientError('Read file error: fileName:%s, readSize:%d, readOffset: %d, error:%s' % (self.fp.name, size, self.counter, e))
        if data and not self.first_read_done:
            self.crc64_handler.update(data)
        else:
            self.first_read_done = True
        return data

    @property
    def crc(self):
        return self.crc64_handler.crc

    @property
    def name(self):
        return self.fp.name

    def reset_crc_process(self):
        self.crc64_handler = Crc64()
        self.first_read_done = False
        self.counter = 0

    def seek(self, *args, **kwargs):
        return self.fp.seek(*args, **kwargs)

    def tell(self, *args, **kwargs):
        return self.fp.tell(*args, **kwargs)

    def close(self):
        self.fp.close()

    def __len__(self):
        return len(self.fp)

    def __str__(self):
        return str(self.fp)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# return if client_crc == server_crc
def check_crc(client_crc, server_crc):
    if client_crc is None or server_crc is None:
        return True
    return client_crc is not None and server_crc is not None and client_crc == server_crc


class ChunkIO(io.FileIO):
    def __init__(self, filename, start_offset, limit_size):
        super(ChunkIO, self).__init__(filename, 'rb')
        self.start_offset = start_offset
        self.limit_size = limit_size
        self.seek(0)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            super(ChunkIO, self).seek(self.start_offset + offset)
        elif whence == io.SEEK_CUR:
            self.seek(self.tell() + offset)
        elif whence == io.SEEK_END:
            self.seek(self.limit_size + offset)

    def read(self, size=-1):
        current_pos = self.tell()
        if current_pos >= self.limit_size:
            return b''
        if size == -1 or current_pos + size > self.limit_size:
            size = self.limit_size - current_pos
        return super(ChunkIO, self).read(size)

    def tell(self):
        return super(ChunkIO, self).tell() - self.start_offset


class ResumeRecordManager(object):

    def __init__(self, filename):
        self.filename = filename
        self.record = None
        self.__lock = threading.Lock()

    def load(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'rb') as f:
                record = pickle.load(f)
        except ValueError:
            os.remove(self.filename)
        else:
            self.record = record

    def save(self):
        with self.__lock:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.record, f)

    def delete(self):
        silently_remove(self.filename)
        self.record = None


class BlockThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers, *args, **kwargs):
        super().__init__(max_workers=max_workers, *args, **kwargs)
        self.__semaphore = threading.Semaphore(max_workers)

    def submit(self, fn, *args, **kwargs) -> Future:
        self.__semaphore.acquire()
        future = super().submit(fn, *args, **kwargs)

        def release_semaphore():
            self.__semaphore.release()

        future.add_done_callback(lambda _: release_semaphore())
        return future
