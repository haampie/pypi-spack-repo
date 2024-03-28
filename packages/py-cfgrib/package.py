# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCfgrib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.10.4", sha256="563416811cd53a861acf47998ef21769accba641b1715d2af4d7e165c4868beb", url="https://pypi.org/packages/0d/61/2b152f062ffa494ce57ee5befe025955f4bb245f4ceeb78f1a682be65438/cfgrib-0.9.10.4-py3-none-any.whl")
    version("0.9.9.0", sha256="c3bd9f042f9910a5f5d786be556736c08403571e9859e1a87f8a87509b09247e", url="https://pypi.org/packages/7e/08/5c86acba784defc31e2fd382a9081ae6e751b54b28103215fda8912a537a/cfgrib-0.9.9.0-py3-none-any.whl")
    version("0.9.8.5", sha256="600686f95c09e2da80e516e42dbdf3e57e56864a760f4ff3db71174e41d98bd1", url="https://pypi.org/packages/a3/4f/34cb0743c9d0c7c3e114f0c0a261b5649c3fb62c79a46759182a30d890a6/cfgrib-0.9.8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("xarray", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@0.9.7.7:0.9.10.1,0.9.10.4:")
        depends_on("py-cffi", when="@:0.9.8")
        depends_on("py-click", when="@0.9.5.1:0.9.10.1,0.9.10.4:")
        depends_on("py-eccodes@0.9.8:", when="@0.9.9.1:0.9.10.1,0.9.10.4:")
        depends_on("py-eccodes", when="@0.9.9:0.9.9.0")
        depends_on("py-numpy", when="@:0.9.10.1,0.9.10.4:")
        depends_on("py-xarray@0.15:", when="@0.9.9.1:0.9.10.1,0.9.10.4:+xarray")
        depends_on("py-xarray@0.12:", when="@0.9.7-rc1:0.9.9.0+xarray")
    # END DEPENDENCIES

