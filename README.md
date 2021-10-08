# copr-rebuild-tools

This repository contains tools for launching mass rebuilds of packages in [Copr](http://copr.fedoraproject.org/) build service.

## Features
- [x] Multiple [backends](#backends) for various programming langues package managers
- [x] Submiting all packages from given backend
    - [x] Limitable
    - [x] Possibility to specify the last submited package and continue from following one
- [x] Possibility to submit only new packages (or only new versions of packages)
- [x] Possibility to rebuild only given set of packages
- [x] Statistics of success rate


## Backends

| Name     | Key         | URL                                                                 |
| -------- | ----------- | ------------------------------------------------------------------- |
| PyPI     | `pypi`      | [pypi.python.org](https://pypi.python.org)                          |
| RubyGems | `rubygems`  | [rubygems.org](http://rubygems.org)                                 |
| Tito     | `tito`      | [github.com/dgoodwin/tito](https://github.com/dgoodwin/tito)        |

You are welcome to write your own backend. Please see a [guide](backends/README.md) describing how to do it.

## Configuration

See [config](/config) directory for examples.


## Usage

See [configuration](#configuration) and [backends](#backends) sections. Also see `--help` for possible actions.

```
copr-rebuild -c <config> <backend> <action>
```

## Examples

The most basic usage, build all RubyGems packages in Copr

```
copr-rebuild -c config/production.ini rubygems submit
```

To submit only such RubyGems packages that are not yet (successfully)
built in Copr.

```
copr-rebuild -c config/production.ini rubygems submit --new-packages
```

To submit only RubyGems packages with new versions that weren't built
in Copr yet. This includes packages that weren't built in Copr at all.

```
copr-rebuild -c config/production.ini rubygems submit --new-versions
```

In case the submitting was interrupted (network issue, etc), we don't
have to start all over. Let's say the latest submitted package was
`foo`. We can resume the rebuild from there.

```
copr-rebuild -c config/production.ini rubygems submit --previous foo
```

For development purposes, it is possible to limit the number of
submitted packages.

```
copr-rebuild -c config/production.ini rubygems submit --limit 100
```

The `--previous` and `--limit` can be combined together to some sort
of offset-limit pagination.

```
copr-rebuild -c config/production.ini rubygems submit --previous foo --limit 100
```

To print information about how many of the RubyGems packages
succeeded, failed to import, failed to build, etc.

```
copr-rebuild -c ~/config.ini rubygems stats
```

To list all successfully built RubyGems packages in Copr.

```
copr-rebuild -c ~/config.ini rubygems successful
```
