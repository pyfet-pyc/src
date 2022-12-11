from typing import List

from zulint.custom_rules import Rule, RuleList

# Rule help:
# By default, a rule applies to all files within the extension for which it is specified (e.g. all .py files)
# There are three operators we can use to manually include or exclude files from linting for a rule:
# 'exclude': 'set([<path>, ...])' - if <path> is a filename, excludes that file.
#                                   if <path> is a directory, excludes all files directly below the directory <path>.
# 'exclude_line': 'set([(<path>, <line>), ...])' - excludes all lines matching <line> in the file <path> from linting.
# 'include_only': 'set([<path>, ...])' - includes only those files where <path> is a substring of the filepath.

FILES_WITH_LEGACY_SUBJECT = {
    # This basically requires a big DB migration:
    "zerver/lib/topic.py",
    # This is for backward compatibility.
    "zerver/tests/test_legacy_subject.py",
    # Other migration-related changes require extreme care.
    "zerver/lib/fix_unreads.py",
    "zerver/tests/test_migrations.py",
    # These use subject in the email sense, and will
    # probably always be exempt:
    "zerver/lib/email_mirror.py",
    "zerver/lib/send_email.py",
    "zerver/tests/test_new_users.py",
    "zerver/tests/test_email_mirror.py",
    "zerver/tests/test_email_notifications.py",
    # This uses subject in authentication protocols sense:
    "zerver/tests/test_auth_backends.py",
    # These are tied more to our API than our DB model.
    "zerver/openapi/python_examples.py",
    "zerver/tests/test_openapi.py",
    # This has lots of query data embedded, so it's hard
    # to fix everything until we migrate the DB to "topic".
    "zerver/tests/test_message_fetch.py",
}

shebang_rules: List["Rule"] = [
    {
        "pattern": r"\A#!",
        "description": "zerver library code shouldn't have a shebang line.",
        "include_only": {"zerver/"},
    },
    # /bin/sh and /usr/bin/env are the only two binaries
    # that NixOS provides at a fixed path (outside a
    # buildFHSUserEnv sandbox).
    {
        "pattern": r"\A#!(?! *(?:/usr/bin/env|/bin/sh)(?: |$))",
        "description": "Use `#!/usr/bin/env foo` instead of `#!/path/foo`"
        " for interpreters other than sh.",
    },
    {
        "pattern": r"\A#!/usr/bin/env python$",
        "description": "Use `#!/usr/bin/env python3` instead of `#!/usr/bin/env python`.",
    },
]

base_whitespace_rules: List["Rule"] = [
    {
        "pattern": r"[\t ]+$",
        "exclude": {"tools/ci/success-http-headers.template.txt"},
        "description": "Fix trailing whitespace",
    },
    {
        "pattern": r"[^\n]\Z",
        "description": "Missing newline at end of file",
    },
]
whitespace_rules: List["Rule"] = [
    *base_whitespace_rules,
    {
        "pattern": "http://zulip.readthedocs.io",
        "description": "Use HTTPS when linking to ReadTheDocs",
    },
    {
        "pattern": "\t",
        "description": "Fix tab-based whitespace",
    },
]
comma_whitespace_rule: List["Rule"] = [
    {
        "pattern": ", {2,}[^#/ ]",
        "exclude": {"zerver/tests", "frontend_tests/node_tests", "corporate/tests"},
        "description": "Remove multiple whitespaces after ','",
        "good_lines": ["foo(1, 2, 3)", "foo = bar  # some inline comment"],
        "bad_lines": ["foo(1,  2, 3)", "foo(1,    2, 3)"],
    },
]
markdown_whitespace_rules: List["Rule"] = [
    *(rule for rule in whitespace_rules if rule["pattern"] != r"[\t ]+$"),
    # Two spaces trailing a line with other content is okay--it's a Markdown line break.
    # This rule finds one space trailing a non-space, three or more trailing spaces, and
    # spaces on an empty line.
    {
        "pattern": r"((?<![\t ])[\t ]$)|([\t ][\t ][\t ]+$)|(^[\t ]+$)",
        "description": "Fix trailing whitespace",
    },
    {
        "pattern": "^#+[A-Za-z0-9]",
        "description": "Missing space after # in heading",
        "exclude_line": {
            ("docs/subsystems/hotspots.md", "#hotspot_new_hotspot_name_icon {"),
        },
        "good_lines": ["### some heading", "# another heading"],
        "bad_lines": ["###some heading", "#another heading"],
    },
]

