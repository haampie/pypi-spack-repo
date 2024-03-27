##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutopep8(PythonPackage):
    version("1.7.0", sha256="6f09e90a2be784317e84dc1add17ebfc7abe3924239957a37e5040e27d812087", url="https://pypi.org/packages/5d/9b/1ed75f8c9086fafe0e9bbb379a70c43b1aa9dff6154ddcfb818f78cb0736/autopep8-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="ed77137193bbac52d029a52c59bec1b0629b5a186c495f1eb21b126ac466083f", url="https://pypi.org/packages/39/3a/cd60ecce0d9737efefc06a074ae280a5d0e904d697fe59b414bf8ab5c472/autopep8-1.6.0-py2.py3-none-any.whl")
    version("1.5.7", sha256="aa213493c30dcdac99537249ee65b24af0b2c29f2e83cd8b3f68760441ed0db9", url="https://pypi.org/packages/a7/f6/84070ab117e6b080a87aac0ac9e4d269a66c6f6076ad81509bd0aac828d8/autopep8-1.5.7-py2.py3-none-any.whl")
    version("1.4.4", sha256="4d8eec30cc81bc5617dbf1218201d770dc35629363547f17577c61683ccfb3ee", url="https://pypi.org/packages/45/f3/24b437da561b6af4840c871fbbda32889ca304fc1f7b6cc3ada8b09f394a/autopep8-1.4.4.tar.gz")
    version("1.3.3", sha256="ff787bffb812818c3071784b5ce9a35f8c481a0de7ea0ce4f8b68b8788a12f30", url="https://pypi.org/packages/24/67/1b62431c8529b3e6e9cc377b9c0d1cfd69fdc8342bc821c4908d15757758/autopep8-1.3.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-pycodestyle@2.9.1:", when="@1.7:2.0.0")
        depends_on("py-pycodestyle@2.8:", when="@1.6")
        depends_on("py-pycodestyle@2.7:", when="@1.5.6:1.5")
        depends_on("py-toml", when="@1.5.5:1.7.0")

