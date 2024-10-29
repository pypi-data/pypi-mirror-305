Easy Changelog
==============

Python version
--------------

Install this repository from Pypi:
```sh
pip install ezchlog
```
Or any other means (`pipx` or a package manager).  
Python 3.9+ required.

Rust version
------------

Compile the `ezchlog` rust binary (you should have `rustc`, `cargo` and `upx` available):
```sh
make release
```

Or download a pre-compiled version from [releases](https://gitlab.com/jrdasm/ezchlog/-/releases).

Don’t forget to download the checksum file and check for corruption.  
You should rename the binary to `ezchlog` and place it on your PATH.

After installation
------------------

Then you’ll have a command to handle your logs:
```sh
ezchlog --help
```

Add a changelog
---------------

```sh
$ ezchlog add "New url for example API"
_CHANGELOGS/Changed/new_url_for_example_api.md
$ ezchlog add "Fix example API" Fixed 142
_CHANGELOGS/Fixed/142_fix_example_api.md
```

List changelogs
---------------

```sh
$ ezchlog list
Fixed/142_fix_example_api.md
Changed/new_url_for_example_api.md
```

Merge changelogs
----------------

```sh
$ ezchlog merge 1.2.3
$ cat CHANGELOG.md
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## 1.2.3
### Fixed
- Fix example API (142)
### Changed
- New url for example API
```

Configuration
-------------

The following configuration parameters could be specified as environment variables or in a `.ezchlog.toml` file (or `pyproject.toml` file for the python version).

- `EZCHLOG_EDITOR` default to `EDITOR` or `vim`
- `EZCHLOG_LOG_DIR` default to `_CHANGELOGS`
- `EZCHLOG_LOG_FILE` default to `CHANGELOG.md`
- `EZCHLOG_CATEGORY_LIST` default to `Security,Fixed,Changed,Added,Remove,Deprecated`
- `EZCHLOG_CATEGORY_DEFAULT` default to `Changed`
- `EZCHLOG_DEFAULT_CHANGELOG` default to  
```
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).
```

For `.ezchlog.toml` or `pyproject.toml`, use the env var name in lowercase without the `EZCHLOG` prefix, for instance `log_dir`.
