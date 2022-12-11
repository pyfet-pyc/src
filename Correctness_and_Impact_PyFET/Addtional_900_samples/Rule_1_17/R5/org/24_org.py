def test_normalize_name_install(PipenvInstance):
    with PipenvInstance() as p:
        with open(p.pipfile_path, "w") as f:
            contents = """
# Pre comment
[packages]
Requests = "==2.14.0"   # Inline comment
"""
            f.write(contents)

        c = p.pipenv("install")
        assert c.returncode == 0

        c = p.pipenv("install requests")
        assert c.returncode == 0
        assert "requests" not in p.pipfile["packages"]
        assert p.pipfile["packages"]["Requests"] == "==2.14.0"
        c = p.pipenv("install requests==2.18.4")
        assert c.returncode == 0
        assert p.pipfile["packages"]["Requests"] == "==2.18.4"
        c = p.pipenv("install python_DateUtil")
        assert c.returncode == 0