try:
    import urllib.parse as parse  # for Python 3
except ImportError:
    import urllib as parse  # for Python 2


def bucket_lister(bucket, marker='', continuation_token='', **params):
    """
    A generator function for listing keys in a bucket.
    """
    more_results = True
    k = None
    while more_results:
        rs = bucket.get_all_keys(marker=marker, continuation_token=continuation_token, **params)
        for k in rs:
            yield k

        if rs.next_continuation_token:
            continuation_token = rs.next_continuation_token
        elif k:
            marker = rs.next_marker or k.name
        if marker:
            '''if isinstance(marker, six.text_type):
                marker = marker.encode('utf-8')'''
            marker = parse.unquote(marker)
        more_results = rs.is_truncated


class BucketListResultSet(object):
    """
    A resultset for listing keys within a bucket.  Uses the bucket_lister
    generator function and implements the iterator interface.  This
    transparently handles the results paging from S3 so even if you have
    many thousands of keys within the bucket you can iterate over all
    keys in a reasonably efficient manner.
    """

    def __init__(self, bucket=None, prefix='', delimiter='', marker='', max_keys='', encoding_type='',
                 continuation_token='', fetch_owner='', list_type=None, start_after=''):
        self.bucket = bucket
        self.prefix = prefix
        self.delimiter = delimiter
        self.marker = marker
        self.max_keys = max_keys
        self.encoding_type = encoding_type
        self.continuation_token = continuation_token
        self.fetch_owner = fetch_owner
        self.list_type = list_type
        self.start_after = start_after

    def __iter__(self):
        return bucket_lister(self.bucket, prefix=self.prefix, delimiter=self.delimiter, marker=self.marker,
                             max_keys=self.max_keys, encoding_type=self.encoding_type,
                             continuation_token=self.continuation_token, fetch_owner=self.fetch_owner,
                             list_type=self.list_type, start_after=self.start_after)


def versioned_bucket_lister(bucket, prefix='', delimiter='',
                            key_marker='', version_id_marker='', headers=None,
                            encoding_type=None):
    """
    A generator function for listing versions in a bucket.
    """
    more_results = True
    k = None
    while more_results:
        rs = bucket.get_all_versions(prefix=prefix, key_marker=key_marker,
                                     version_id_marker=version_id_marker,
                                     delimiter=delimiter, headers=headers,
                                     max_keys=999, encoding_type=encoding_type)
        for k in rs:
            yield k
        key_marker = rs.next_key_marker
        if key_marker:
            key_marker = parse.unquote(key_marker)
        version_id_marker = rs.next_version_id_marker
        more_results = rs.is_truncated


class VersionedBucketListResultSet(object):
    """
    A resultset for listing versions within a bucket.  Uses the bucket_lister
    generator function and implements the iterator interface.  This
    transparently handles the results paging from S3 so even if you have
    many thousands of keys within the bucket you can iterate over all
    keys in a reasonably efficient manner.
    """

    def __init__(self, bucket=None, prefix='', delimiter='', key_marker='',
                 version_id_marker='', headers=None, encoding_type=None):
        self.bucket = bucket
        self.prefix = prefix
        self.delimiter = delimiter
        self.key_marker = key_marker
        self.version_id_marker = version_id_marker
        self.headers = headers
        self.encoding_type = encoding_type

    def __iter__(self):
        return versioned_bucket_lister(self.bucket, prefix=self.prefix,
                                       delimiter=self.delimiter,
                                       key_marker=self.key_marker,
                                       version_id_marker=self.version_id_marker,
                                       headers=self.headers,
                                       encoding_type=self.encoding_type)


def bucket_retention_lister(bucket, prefix='', delimiter='', marker='', max_keys=''):
    more_results = True
    k = None
    while more_results:
        rs = bucket.get_all_retention_keys(prefix=prefix, delimiter=delimiter, marker=marker, max_keys=max_keys)
        for k in rs:
            yield k
        if k:
            marker = rs.next_marker or k.name
        if marker:
            marker = parse.unquote(marker)
        more_results = rs.is_truncated


class BucketRetentionListResultSet(object):
    def __init__(self, bucket=None, prefix='', delimiter='', marker='', max_keys=''):
        self.bucket = bucket
        self.prefix = prefix
        self.delimiter = delimiter
        self.marker = marker
        self.max_keys = max_keys

    def __iter__(self):
        return bucket_retention_lister(self.bucket, prefix=self.prefix,
                                       delimiter=self.delimiter, marker=self.marker, max_keys=self.max_keys)


def multipart_upload_lister(bucket, key_marker='',
                            upload_id_marker='',
                            headers=None, encoding_type=None):
    """
    A generator function for listing multipart uploads in a bucket.
    """
    more_results = True
    k = None
    while more_results:
        rs = bucket.get_all_multipart_uploads(key_marker=key_marker,
                                              upload_id_marker=upload_id_marker,
                                              headers=headers,
                                              encoding_type=encoding_type)
        for k in rs:
            yield k
        key_marker = rs.next_key_marker
        upload_id_marker = rs.next_upload_id_marker
        more_results = rs.is_truncated


class MultiPartUploadListResultSet(object):
    """
    A resultset for listing multipart uploads within a bucket.
    Uses the multipart_upload_lister generator function and
    implements the iterator interface.  This
    transparently handles the results paging from S3 so even if you have
    many thousands of uploads within the bucket you can iterate over all
    keys in a reasonably efficient manner.
    """

    def __init__(self, bucket=None, key_marker='',
                 upload_id_marker='', headers=None, encoding_type=None):
        self.bucket = bucket
        self.key_marker = key_marker
        self.upload_id_marker = upload_id_marker
        self.headers = headers
        self.encoding_type = encoding_type

    def __iter__(self):
        return multipart_upload_lister(self.bucket,
                                       key_marker=self.key_marker,
                                       upload_id_marker=self.upload_id_marker,
                                       headers=self.headers,
                                       encoding_type=self.encoding_type)
