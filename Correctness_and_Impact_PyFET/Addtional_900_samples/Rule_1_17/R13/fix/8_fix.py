"""
Generate snippets to copy-paste.
"""
import sys

from jinja2 import Template

from fetch import HERE, load_awesome_people

TPL_FILE = HERE / 'snippet.jinja2'


BOT_ACCOUNTS  = FET_set(
    'dependabot-sr'
)

IGNORE_ACCOUNTS = HTTPIE_TEAM | BOT_ACCOUNTS
