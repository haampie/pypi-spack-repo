# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyComm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2", sha256="e6fb86cb70ff661ee8c9c14e7d36d6de3b4066f1441be4063df9c5009f0a64d3", url="https://pypi.org/packages/e6/75/49e5bfe642f71f272236b5b2d2691cf915a7283cc0ceda56357b61daa538/comm-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="87928485c0dfc0e7976fd89fc1e187023cf587e7c353e4a9b417555b44adf021", url="https://pypi.org/packages/6e/c1/e7335bd49aa3fa3bd453e34a4580b0076804f219897ad76d4d5aa4d8f22f/comm-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="2da8d9ebb8dd7bfc247adaff99f24dce705638a8042b85cb995066793e391001", url="https://pypi.org/packages/7b/a6/5fd0242e974914b139451eea0a61ed9fd2e47157e33a67939043c50a94dd/comm-0.2.0-py3-none-any.whl")
    version("0.1.4", sha256="6d52794cba11b36ed9860999cd10fd02d6b2eac177068fdd585e1e2f8a96e67a", url="https://pypi.org/packages/fe/47/0133ac1b7dc476ed77710715e98077119b3d9bae56b13f6f9055e7da1c53/comm-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="16613c6211e20223f215fc6d3b266a247b6e2641bf4e0a3ad34cb1aff2aa3f37", url="https://pypi.org/packages/74/f3/b88d7e1dadf741550c56b70d7ce62673354fddb68e143d193ceb80224208/comm-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="9f3abf3515112fa7c55a42a6a5ab358735c9dccc8b5910a9d8e3ef5998130666", url="https://pypi.org/packages/fc/04/e740a61ec9df8975bcb32e6698663bc9efa945ac6b2a585728deed6dcced/comm-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="788a4ec961956c1cb2b0ba3c21f2458ff5757bb2f552032b140787af88d670a3", url="https://pypi.org/packages/84/a7/d515f442c429ad069ce384b08d4aaa061fb9cabab679b93c82b232d17d1e/comm-0.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-traitlets@4:4.0.0.0,4.1:", when="@0.1.4:")
        depends_on("py-traitlets@5.3:5.3.0.0,5.4:", when="@0.1.2:0.1.3")
        depends_on("py-traitlets@5.4:", when="@0.1.1")
    # END DEPENDENCIES

