def main():
    tmpdir = None
    try:
        # Create a temporary working directory
        tmpdir = tempfile.mkdtemp()

        # Unpack the zipfile into the temporary directory
        pip_zip = os.path.join(tmpdir, "pip.zip")
        with open(pip_zip, "wb") as fp:
            fp.write(b85decode(DATA.replace(b"\n", b"")))

        # Add the zipfile to sys.path so that we can import it
        sys.path.insert(0, pip_zip)

        # Run the bootstrap
        bootstrap(tmpdir=tmpdir)
    finally:
        # Clean up our temporary working directory
        if tmpdir:
            shutil.rmtree(tmpdir, ignore_errors=True)
