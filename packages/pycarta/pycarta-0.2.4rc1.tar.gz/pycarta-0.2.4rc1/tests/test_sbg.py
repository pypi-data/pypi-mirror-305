import pytest
from petname import generate
from pycarta.sbg import SbgFile, ExecutableApp, ExecutableProject
from pycarta.sbg.project import (
    canonicalize_name,
    title,
)
import os


@pytest.fixture
def local_file(tmp_path):
    return tmp_path / f"pytest-{generate()}.txt"


# region SbgFile
# @pytest.mark.skip("Skipped to reduce API calls.")
class TestSbgFile:
    def test_local(self, local_file):
        # Initialize with local file
        fobj = SbgFile(str(local_file))
        # File name
        assert fobj.local == str(local_file)
        # Local file I/O
        contents = "Hello, World!"
        with fobj.open("w") as fh:
            fh.write(contents)
        with open(str(local_file), "r") as fh:
            assert fh.read() == contents
        # No remote file
        assert fobj.remote is None
        # Lazy file setting
        fobj = SbgFile()
        fobj.local = str(local_file)
        # File name
        assert fobj.local == str(local_file)
        # Local file I/O
        contents = "Hello, World!"
        with fobj.open("w") as fh:
            fh.write(contents)
        with open(str(local_file), "r") as fh:
            assert fh.read() == contents
        # No remote file
        assert fobj.remote is None

    def test_upload_download(self, local_file, sbg_api, sbg_project):
        api = sbg_api
        project = sbg_project
        # Upload a file
        contents = "Hello, World!"
        with open(local_file, "wb") as fh:
            fh.write(contents.encode())
        up = SbgFile(str(local_file))
        up.upload(str(local_file),
                  project=project,
                  file_name=local_file.name,
                  overwrite=True,
                  api=api,)
        # Download the file
        down = SbgFile(name=local_file.name,
                       project=project,
                       api=api,)
        down.download(overwrite=True)
        with open(local_file.name, "rb") as fh:
            assert fh.read() == contents.encode()
        # Clean up
        os.remove(local_file.name)

    def test_push_pull(self, local_file, sbg_api, sbg_project):
        api = sbg_api
        project = sbg_project
        # Initialize with local file
        contents = b"Hello, World!"
        with SbgFile().push(file_name=local_file.name,
                            project=project,
                            overwrite=True,
                            api=api) as fh:
            fh.write(contents)
        down = SbgFile(name=local_file.name,
                       project=project,
                       api=api)
        with down.pull() as fh:
            assert fh.read() == contents
# end region


# region Executable App/Project
class TestProjectUtils:
    def test_canonicalize_name(self):
        assert canonicalize_name("Hello World") == 'Hello_World'
        assert canonicalize_name("Hello-World") == 'Hello_World'
        assert canonicalize_name("Hello, World") == 'Hello_World'
        assert canonicalize_name("Hello World!") == 'Hello_World_'

    def test_title(self):
        assert title("hello_world") == 'Hello World'
        assert title("hello-world") == 'Hello World'
        assert title("hello, world") == 'Hello World'    


class TestExecutableAppProject:
    # @pytest.mark.skip("Skipping ExecutableApp test.")
    def test_executable_app(self, local_file, sbg_app):
        # Create a file that will be uploaded for use in the app.
        content = "Hello, World!"
        with open(local_file, "w") as fh:
            fh.write(content)
        # Create the App and run it.
        app = ExecutableApp(sbg_app, cleanup=True)
        outputs, _ = app(input=str(local_file))
        # Check the output
        try:
            with outputs["output"].open("r") as fh:
                assert fh.read() == content
        except Exception as e:
            raise type(e)(f"outputs: {outputs}")
        finally:
            # Clean up
            os.remove(outputs["output"].local)

    def test_executable_project(self, sbg_api, sbg_project):
        project = ExecutableProject(project=sbg_project,
                                    cleanup=True,
                                    overwrite_local=True,
                                    overwrite_remote=True,
                                    api=sbg_api,)
        # What apps are expected?
        apps = sbg_api.apps.query(project=sbg_project)
        app_names = [canonicalize_name(app.name) for app in apps]
        # Create executable apps from the project
        for name in app_names:
            assert hasattr(project, canonicalize_name(name))
# end region
