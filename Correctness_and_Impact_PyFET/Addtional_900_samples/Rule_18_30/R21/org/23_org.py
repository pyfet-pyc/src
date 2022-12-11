# flake8: noqa: F401
"""Imports all optional dependencies for the project.
An attribute "_yt_dlp__identifier" may be inserted into the module if it uses an ambiguous namespace"""

try:
    import brotlicffi as brotli
except ImportError as e:
    try:
        import brotli
    except ImportError as e:
        brotli = None
