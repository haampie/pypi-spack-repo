# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCfgrib(PythonPackage):
    # BEGIN VERSIONS
    version("0.9.10.4", sha256="563416811cd53a861acf47998ef21769accba641b1715d2af4d7e165c4868beb", url="https://pypi.org/packages/0d/61/2b152f062ffa494ce57ee5befe025955f4bb245f4ceeb78f1a682be65438/cfgrib-0.9.10.4-py3-none-any.whl")
    version("0.9.10.3", sha256="c10806058c80c48610c201bf05eb292401807806ab9423ab4965ae23dbb6b521", url="https://pypi.org/packages/cf/98/e08b227307aab082b4c8185afa233517bd0857273120960c3bc5c2083be8/cfgrib-0.9.10.3.tar.gz")
    version("0.9.10.2", sha256="ff7e819248a9e0df38a608a4567215420df924d1794f910f701088587bae6cb5", url="https://pypi.org/packages/4d/3f/7b25db1de0dbb0b5c2fa06fe16b1cf6fe31608a4fb0081eccfcf46e5a621/cfgrib-0.9.10.2.tar.gz")
    version("0.9.10.1", sha256="f16615de9e8b81b55b267a7bcbc22db470065c7e7989c79c7d56c47b22d9bd40", url="https://pypi.org/packages/b0/c5/0eb15b1a648c43104957ef73ae72d8ee27cc94b67cf935ca0e3d31416209/cfgrib-0.9.10.1-py3-none-any.whl")
    version("0.9.10.0", sha256="fd8afce9825395df546461817bc0b0326984662a4c143de3e8b9a82d4722ee98", url="https://pypi.org/packages/a5/f9/25018d362f4d8fa5191c641582050693ce81daed3ce317edaaa9c36ded71/cfgrib-0.9.10.0-py3-none-any.whl")
    version("0.9.9.1", sha256="a878aace7630461a8b9f7206d34ec424d00025130374a5e06a5f35b4f2669052", url="https://pypi.org/packages/2a/f3/21c0f054b6153eb5de714eab504c8b5f43f448529b967af5f87ec4c6f35a/cfgrib-0.9.9.1-py3-none-any.whl")
    version("0.9.9.0", sha256="c3bd9f042f9910a5f5d786be556736c08403571e9859e1a87f8a87509b09247e", url="https://pypi.org/packages/7e/08/5c86acba784defc31e2fd382a9081ae6e751b54b28103215fda8912a537a/cfgrib-0.9.9.0-py3-none-any.whl")
    version("0.9.8.5", sha256="600686f95c09e2da80e516e42dbdf3e57e56864a760f4ff3db71174e41d98bd1", url="https://pypi.org/packages/a3/4f/34cb0743c9d0c7c3e114f0c0a261b5649c3fb62c79a46759182a30d890a6/cfgrib-0.9.8.5-py2.py3-none-any.whl")
    version("0.9.8.4", sha256="d01fb29442172dd7ac1fa2133b1f9c6a199cdb1b604e09e66e797aa46e687cd0", url="https://pypi.org/packages/bf/b2/05af9dd5afbe23d94953f56080a305a81d8a7d65d00864d8c686cfec9434/cfgrib-0.9.8.4-py2.py3-none-any.whl")
    version("0.9.8.3", sha256="5439c0d80e9873230bd76a8159e0987ac591804db6667653706276d460f86865", url="https://pypi.org/packages/d4/59/4415def2d2342a1cdf495445dec7101c43e540097c48d3bf856059e817f8/cfgrib-0.9.8.3-py2.py3-none-any.whl")
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

