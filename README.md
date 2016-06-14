# copr-rebuild-tools

This repository contains tools for launching mass rebuilds of packages in [Copr](http://copr.fedoraproject.org/) build service.

## Features
- [ ] Multiple [backends](#Backends) for various programming langues package managers
- [ ] Submiting all packages from given backend
    - [x] Limitable
    - [x] Possibility to specify the last submited package and continue from following one
- [ ] Possibility to submit only new packages (or only new versions of packages)
- [ ] Statistics of success rate


## Backends
- [ ] [PyPi](https://pypi.python.org/)
- [ ] [Rubygems](http://rubygems.org/)
