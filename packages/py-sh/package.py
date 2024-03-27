##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySh(PythonPackage):
    version("1.14.3", sha256="e4045b6c732d9ce75d571c79f5ac2234edd9ae4f5fa9d59b09705082bdca18c7", url="https://pypi.org/packages/b7/09/89c28aaf2a49f226fef8587c90c6386bd2cc03a0295bc4ff7fc6ee43c01d/sh-1.14.3.tar.gz")
    version("1.13.1", sha256="6f792e45b45d039b423081558904981e8ab49572b0c38009fcc65feaab06bcda", url="https://pypi.org/packages/fa/9c/796934ee6d990d504c600056aa435e31bd49dbfba37e81d2045d37c8bdaf/sh-1.13.1-py2.py3-none-any.whl")
    version("1.12.9", sha256="579aa19bae7fe86b607df1afaf4e8537c453d2ce3d84e1d3957e099359a51677", url="https://pypi.org/packages/fd/14/6deb4e89cc237ee4bc1c0b0485c77d7868477f96c47962366bc5fabc31fd/sh-1.12.9.tar.gz")
    version("1.11", sha256="590fb9b84abf8b1f560df92d73d87965f1e85c6b8330f8a5f6b336b36f0559a4", url="https://pypi.org/packages/39/ca/1db6ebefdde0a7b5fb639ebc0527d8aab1cdc6119a8e4ac7c1c0cc222ec5/sh-1.11.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@2:")

