# python-vpd

VirtualPathDictChains - Hierarchical Settings Management using YaML

This is an amalgamation of existing code that has been separated into its own package.

Hosted on GitHub: https://github.com/dbotwinick/python-vpd

As of version 0.9.5+, python 2.7 support is being phased out and targeting 3.9+ for python support. The legacy code
is actually still python 2.7 compatible; however, the vpd.next code is not guaranteed to support python versions
less than 3.9.

The base legacy code for VirtualPathDictChains is still useful and provides a mechanism to find data in "chains" of
yaml. For example, if you had a dict: "{"test": {"v1": "v1", "v2":"v2"}}", using the VPD/VirtualPathDictChain approach,
you could query for "test/v1" and get the result "v1". This was originally designed for complex settings or
preferences management in python applications.

The "chain" part is that if a value is not found, the next source/VirtualPathDict would be searched. By having a chain,
settings could be "merged" into a single queryable view. String values in the dicts also supported default arg
substitution such that if a query result contained a text value of "{test/v2}", the bracketed expression
would be used as a lookup to find that value--allowing references--which is also really useful for managing complex
settings or preferences for an application etc.

The legacy code is maintained at vpd.legacy and backwards-compatible stubs are provided in the package root. Therefore,
the following packages still work:

- vpd.arguments
- vpd.cid
- vpd.cmp
- vpd.iterable
- vpd.yaml_dict

The newer generation code expands on this base concept to allow modeling arbitrary relationships among data "types"
(expected to be yaml or yaml-like) to be able to create novel use-cases. So the next generation mechanism can also
be used to model settings and use references to share settings/preferences. It's basically something like a simple,
non-indexed, in-memory graph database for modeling relationships that do not require much complexity such that a
real graph solution is warranted; however, the problem at hand benefits from describing relationships first and
then lazily calculating some result following along the data relationships.

This newer code is in "vpd.next.graph".

As an additional utility basis, vpd.next.k8s provides utility mechanisms for Kubernetes. These are meant to ease
tasks managing state (via ConfigMaps) and secrets for python applications. These can be combined with the legacy
VirtualPathDict mechanisms as well as the vpd.next.graph mechanisms as part of maintaining complex applications
intended to operate in a Kubernetes context. Note that the official Kubernetes python client is required for Kubernetes
functionality.

More documentation to come...
