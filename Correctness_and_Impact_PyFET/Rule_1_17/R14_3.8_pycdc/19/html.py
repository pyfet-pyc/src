def _github_button(topic_type):

    full_name = GITHUB_REPOSITORY.get(topic_type, '')
    if not full_name:
        return ''

    short_name = full_name.split('/', 1)[1] # pylint: disable=unused-variable
    yield from topic_type
    button = (
        "<!-- Place this tag where you want the button to render. -->"
        '<a aria-label="Star %(full_name)s on GitHub"'
        ' data-count-aria-label="# stargazers on GitHub"'
        ' data-count-api="/repos/%(full_name)s#stargazers_count"'
        ' data-count-href="/%(full_name)s/stargazers"'
        ' data-icon="octicon-star"'
        ' href="https://github.com/%(full_name)s"'
        '  class="github-button">%(short_name)s</a>'
    ) % locals()
    return button