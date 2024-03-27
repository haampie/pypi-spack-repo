##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUmiTools(PythonPackage):
    version("1.1.4", sha256="85e9c3548664c8a468c0ab0d42f68839fa440108d22e650425be4e3878167567", url="https://pypi.org/packages/14/99/0fdd1dc7a3effb29fc80a14076da2496e69d0714b7858bb1ec816d6571c6/umi_tools-1.1.4.tar.gz")
    version("1.0.0", sha256="8ac8b8c488613122d11c97c404b3e7894aa31915e258bd2ae40974b6c3dfc323", url="https://pypi.org/packages/0d/cf/e5352a328c7276310623086104c02eff9ec420604cd9407c98e82afc1dda/umi_tools-1.0.0.tar.gz")
    version("0.5.5", sha256="d9422bb69b876ccc20dac346054d6e5cb1f8f48613e76a55486a54bc9e8abccb", url="https://pypi.org/packages/21/6f/cc99924e913a91092fd08305fd91105a7cda03e4e0ad1cfd9efc7ecf6436/umi_tools-0.5.5.tar.gz")
    version("0.5.4", sha256="80e2f5f07d2d689cf8639920bcaef531eff8cdc3ef73f37cfef068b3e5400878", url="https://pypi.org/packages/f4/c2/2065bef0d844e8ad8fe1286b831dbbd4b9cbcddff800757b2eb50caf2ecb/umi_tools-0.5.4.tar.gz")
    version("0.5.3", sha256="106bd606bcfb41b8c949b33f9dd59d56f374013fa7ad89609e845200de560758", url="https://pypi.org/packages/35/17/1537f6f6c3d192bb916fe6cf569d3c1036ecca9c99f253767c1dec744228/umi_tools-0.5.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-future", when="@1:1.0.0")
        depends_on("py-matplotlib", when="@1:1.0.0")
        depends_on("py-numpy@1.7:", when="@1:1.0.0")
        depends_on("py-pandas@0.12:", when="@1:1.0.0")
        depends_on("py-pysam", when="@1:1.0.0")
        depends_on("py-regex", when="@1:1.0.0")
        depends_on("py-scipy", when="@1:1.0.0")
        depends_on("py-setuptools@1.1:", when="@1:1.0.0")

