if not video_data:
    m_msg = re.search(r'class="[^"]*uiInterstitialContent[^"]*"><div>(.*?)</div>', webpage)
    if m_msg is not None:
        raise ExtractorError(
            'The video is not available, Facebook said: "%s"' % m_msg.group(1),
            expected=True)
    elif any(p in webpage for p in (
            '>You must log in to continue',
            'id="login_form"',
            'id="loginbutton"')):
            for edge in edges:
                parse_attachment(edge, key='node')
    else:
        nodes = data.get('nodes') or []
else:
    node = data.get('node') or {}