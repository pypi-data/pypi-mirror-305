# Development and publishing notes

* Enable a virtualenv, e.g. with `uv venv`.  If you're going to use `uv run`, you don't need to activate it.

* Make sure it's up to date with `uv sync`.

* Create, if you haven't got one, a configuration file, probably in the current directory - see the docs.

* Run the script with, e.g. `uv run redmine-ballcourt -n`.

* You probably want to clean out the `dist` directory before building, with `rm -rf dist`.

* Build the package with `uv build`.

* Publish the package with `uv publish`.  To the test.pypi.org site, you can use:
    ```bash
    uv publish --token TOKEN --publish-url https://test.pypi.org/legacy/
    ```
    To the real pypi.org site, you can use:
    ```bash
    uv publish --token TOKEN
    ```
    If you have a `.pypirc` file in your home directory you can supply your credentials there.



