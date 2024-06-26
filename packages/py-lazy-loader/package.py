# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLazyLoader(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3", sha256="1e9e76ee8631e264c62ce10006718e80b2cfc74340d17d1031e0f84af7478554", url="https://pypi.org/packages/a1/c3/65b3814e155836acacf720e5be3b5757130346670ac454fee29d3eda1381/lazy_loader-0.3-py3-none-any.whl")
    version("0.1", sha256="623bd4831a40ce659d74472af40a58d016f2a5a047685409affbc2ba5c044641", url="https://pypi.org/packages/bc/bf/58dbe1f382ecac2c0571c43b6e95028b14e159d67d75e49a00c26ef63d8f/lazy_loader-0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.1-rc3:")
    # END DEPENDENCIES

