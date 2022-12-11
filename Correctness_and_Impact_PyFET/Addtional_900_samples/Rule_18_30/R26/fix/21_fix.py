def json(self):
    for path, _ in self._package_dirs:
        try:
            with open(os.path.join(path, 'api.json')) as f:
                return json.load(f)
        except FileNotFoundError:
            r = session.get(f'https://pypi.org/pypi/{self.name}/json')
            response = r.json()
            releases = response["releases"]
            files = {
                pkg for pkg_dir in self._package_dirs
                for pkg in os.listdir(pkg_dir.path)
            }
            for release in list(releases.keys()):
                values = (
                    r for r in releases[release] if r["filename"] in files
                )
                values = list(values)
                if values:
                    releases[release] = values
                else:
                    del releases[release]
            response["releases"] = releases
            with open(os.path.join(path, "api.json"), "w") as fh:
                json.dump(response, fh, indent=4)
            return response