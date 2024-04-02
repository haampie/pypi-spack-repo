# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDulwich(PythonPackage):
    # BEGIN VERSIONS
    version("0.21.6", sha256="30fbe87e8b51f3813c131e2841c86d007434d160bd16db586b40d47f31dd05b0", url="https://pypi.org/packages/57/e0/1b5f95c2651284a5d4fdfb2cc5ecad57fb694084cce59d9d4acb7ac30ecf/dulwich-0.21.6.tar.gz")
    version("0.20.46", sha256="4f0e88ffff5db1523d93d92f1525fe5fa161318ffbaad502c1b9b3be7a067172", url="https://pypi.org/packages/4c/61/85f17dd9e744e027d23bee2bbafc8438fab26c175a089b1a06b664deae21/dulwich-0.20.46.tar.gz")
    version("0.20.44", sha256="10e8d73763dd30c86a99a15ade8bfcf3ab8fe96532cdf497e8cb1d11832352b8", url="https://pypi.org/packages/04/7f/1738a3957c6ed99f2d6db3f8883c56bebfaf543ca9a691c3f58624c29922/dulwich-0.20.44.tar.gz")
    version("0.20.21", sha256="ac764c9a9b80fa61afe3404d5270c5060aa57f7f087b11a95395d3b76f3b71fd", url="https://pypi.org/packages/31/02/791c17b92e6d04c43f9b318c95a3f3c3e1ea718aa72ad95b9dac147895fa/dulwich-0.20.21.tar.gz")
    version("0.20.15", sha256="fb1773373ec2af896031f8312af6962a1b8b0176a2de3fb3d84a84ec04498888", url="https://pypi.org/packages/23/e1/38f2fa20d223c635c8f9a939e45ad6c06d55a7f867c013ee98cf250fb262/dulwich-0.20.15.tar.gz")
    version("0.20.14", sha256="21d6ee82708f7c67ce3fdcaf1f1407e524f7f4f7411a410a972faa2176baec0d", url="https://pypi.org/packages/c7/6d/b5ee7c6a5d202b41efa356a56efd5b1990eab518d9e583e621da0b1cf509/dulwich-0.20.14.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.21:")
    # END DEPENDENCIES

