# Backends

This guide briefly describes how to implement custom backend. Please see some of existing backends as example.


## Minimal backend

Lets assume that your new backend will be called `foo`. You always need to create the following three classes within
your backend file.


Import everything from the `copr_rebuild_tools` package that you will need

    from copr_rebuild_tools import Backend, CoprBackend, Entity

First you need to create your own descendant of `Entity` class. It will represent one module/gem/package from the backend.
While creating objects from your entity, you can pass all parameters as kwargs to the constructor.
No naming conventions are required.

    class MyEntity(Entity):
        name = ...

Next, you will need to implement `Foo` class. It will serve for getting information from the backend. For basic functionality
it is necessary to implement the `get_all` method which returns list of individual modules/gems/packages as `MyEntity` instances.

    class Foo(Backend):
        def get_all(self):
            pass

Last, you will need to implement `CoprFoo` class which will communicate with Copr service. For basic functionality it is
required to implement `submit` method which takes an instance of `MyEntity` and submits its build into Copr.

    class CoprFoo(CoprBackend):
        def submit(self, entity):
            pass


## New packages
Required for `--new-packages`

@TODO Maybe not required

    class CoprFoo(...):
        name_attr = "gem_name"
        
        ...


## Version comparison
Required for `--new-versions`

    class MyEntity(...):
        version = ...
        pkgname = ...
        ...
