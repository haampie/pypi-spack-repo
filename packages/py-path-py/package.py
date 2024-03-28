# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathPy(PythonPackage):
    # BEGIN VERSIONS
    version("12.5.0", sha256="a43e82eb2c344c3fd0b9d6352f6b856f40b8b7d3d65cc05978b42c3715668496", url="https://pypi.org/packages/8f/04/130b7a538c25693c85c4dee7e25d126ebf5511b1eb7320e64906687b159e/path.py-12.5.0-py3-none-any.whl")
    version("12.4.0", sha256="c88fb6073b955b2b2c9f3da61b94a2a4c61d722b776b562c26f29e05425eb55a", url="https://pypi.org/packages/a5/0d/4caee829b04e3113b7069fa52063bce5c78e374e05850aa893549e917a1a/path.py-12.4.0-py3-none-any.whl")
    version("12.3.0", sha256="dde384eaf9ad73416b8444e8f870f533a6046402c5300bedadc25a23d8ce16e5", url="https://pypi.org/packages/f7/8f/b98acda6cc375c12a33db286e982d9952f2497b8c9966db1c75700bdc280/path.py-12.3.0-py3-none-any.whl")
    version("12.2.0", sha256="a21d050e99dd0dbe6561177f6d361af869d1f4b27d9134d12d8d65dfbe78e765", url="https://pypi.org/packages/9e/9d/2af32e7a3e332eba991f964ebd1d3f1aa45097f00698eb8c2ccb43431be0/path.py-12.2.0-py3-none-any.whl")
    version("12.1.0", sha256="a5fad1f5214eec5f07228882d7fa372f969d75d508bd3c9e4ee199f536c5b503", url="https://pypi.org/packages/e0/c2/e790206ab62bfdef600eef324c42d5a96843b83dfc2a96a39827c4e0213f/path.py-12.1.0-py3-none-any.whl")
    version("12.0.2", sha256="ae48e0d34fc1fba673e7dc3f2fe93607a6340ee94a440c57cf17cba9d7f2ddf3", url="https://pypi.org/packages/ae/d2/1dd959482686de17ddf5adb5f16b77baaad1ea0d2d7a5fd8f11e94b697de/path.py-12.0.2-py3-none-any.whl")
    version("12.0.1", sha256="e107a3a8834a97be2a047f4b641822afc76a2b78352610102782732e6b389aa3", url="https://pypi.org/packages/40/62/1464f08672cac67e529967ba83b46f38da5d0ca48ac1ce2a9e7d7680ea10/path.py-12.0.1-py3-none-any.whl")
    version("12.0", sha256="e6bf9a3b727627f0190bbc8644e9cfaf4710a0ddd18b6c340215eea73a273dcf", url="https://pypi.org/packages/1c/34/870f5fb0030e3517424b2c4da6f9ef5a75d8608639faea96fc70d7764d99/path.py-12.0-py2.py3-none-any.whl")
    version("11.5.2", sha256="ea40833e76c50485fffd3e094d52e9e8701ba8c62a3b8f67c655c28a9538aac1", url="https://pypi.org/packages/1e/4a/6e20d9e264d2eb4977b94ee2f189d5c4a4819239ce063027a952014b6670/path.py-11.5.2-py2.py3-none-any.whl")
    version("11.5.1", sha256="c2373e5b13468d557ffaf6ad22844f6202a24f1b595f2be332ab67195f7a60f8", url="https://pypi.org/packages/8f/a8/0bac3671dda3b644b49f8b575cf52a6cefb88de00fb48fb3a745c1d1d182/path.py-11.5.1-py2.py3-none-any.whl")
    version("5.2", sha256="d82923a04b527ff9d6e0161c29d295db4c35d63bb97f4f1071e5b550d7ba3358", url="https://pypi.org/packages/26/01/24b69353a7260052cf1592f94991cf56b58b3f72687df6cfb54ff1e1b165/path.py-5.2.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@0.5:", when="@11.4:12.0")
        depends_on("py-path", when="@12.5:")
        depends_on("py-path@:13.1", when="@12.4")
        depends_on("py-path@:13.0", when="@12.3")
    # END DEPENDENCIES

