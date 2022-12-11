import cStringIO
import gzip
import wsgiref.headers

from paste.util.mimeparse import parse_mime_type, desired_matches


ENCODABLE_CONTENT_TYPES = {
    "application/json",
    "application/javascript",
    "application/xml",
    "text/css",
    "text/csv",
    "text/html",
    "text/javascript",
    "text/plain",
    "text/xml",
}