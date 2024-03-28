# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestOpenfiles(PythonPackage):
    # BEGIN VERSIONS
    version("0.5.0", sha256="b02389b5666d552e236ccf8d4e971abe97b320653ee77316de23db181dbe4f3a", url="https://pypi.org/packages/c5/85/039b16aed2c8017033d96c8d35ded2e0b2d165b0fd7f38bfe04bb0b669a7/pytest_openfiles-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="10a30db607f6bd6f9d3a28908a7a4c3ba35cacea7b3e2876097cab5b6bd207e8", url="https://pypi.org/packages/b0/68/7866e119e8fcaa3b95c81ae12334917d35ed9229d753aa6f1a926a647d3e/pytest_openfiles-0.4.0-py2.py3-none-any.whl")
    version("0.3.2", sha256="e51c91889eb9e4c75f47735efc57a1435f3f1182463600ba7bce7f2556a46884", url="https://pypi.org/packages/6c/31/6804de3e63301e3d466bbb0a82d4dbc88db1da92ec1be770931a497af5b2/pytest-openfiles-0.3.2.tar.gz")
    version("0.3.1", sha256="bf09cd83ca0554799292f536800f54e4892f8000283daaf9d9fc6b6eb2d8a9da", url="https://pypi.org/packages/7f/06/1101bcbae2cf41f345e1442ccd6a44b20c55e5f246a2aa828e386544a1f7/pytest-openfiles-0.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-psutil", when="@0.4:")
        depends_on("py-pytest@4.6:", when="@0.5:")
        depends_on("py-pytest@2.8:", when="@0.4")
    # END DEPENDENCIES

