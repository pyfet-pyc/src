def __call__(self, info_dict, ydl):
    warning = ('There are no chapters matching the regex' if info_dict.get('chapters')
                else 'Cannot match chapters since chapter information is unavailable')
    for regex in self.chapters or []:
        for i, chapter in enumerate(info_dict.get('chapters') or []):
            if re.search(regex, chapter['title']):
                warning = None
                yield {**chapter, 'index': i}
    if self.chapters and warning:
        ydl.to_screen(f'[info] {info_dict["id"]}: {warning}')

    yield from ({'start_time': start, 'end_time': end} for start, end in self.ranges or [])
