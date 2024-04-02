# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumcodecs(PythonPackage):
    # BEGIN VERSIONS
    version("0.11.0", sha256="6c058b321de84a1729299b0eae4d652b2e48ea1ca7f9df0da65cb13470e635eb", url="https://pypi.org/packages/19/0f/006424c07b551a13c773b59a3656beadbaadbcf9df1601e87fcae342618c/numcodecs-0.11.0.tar.gz")
    version("0.7.3", sha256="022b12ad83eb623ec53f154859d49f6ec43b15c36052fa864eaf2d9ee786dd85", url="https://pypi.org/packages/fa/1d/644b26dbc7fe9666223e8744680213e5dad4db0fe67034ddf6d02ec8b1a0/numcodecs-0.7.3.tar.gz")
    version("0.6.4", sha256="ef4843d5db4d074e607e9b85156835c10d006afc10e175bda62ff5412fca6e4d", url="https://pypi.org/packages/53/2a/1dc435cbd1d082827190a3e46168fd04f74e266e91313969d5a1aab601bf/numcodecs-0.6.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("msgpack", default=False, description="msgpack")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.11:")
        depends_on("python@:3", when="@0.7.3:0.10.0-alpha3")
    # END DEPENDENCIES

