# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstropy(PythonPackage):
    # BEGIN VERSIONS
    version("6.0.0", sha256="03cd801a55305da523cd8d780d76359f57255dcdc59fe0bdd71fd5154fc777d9", url="https://pypi.org/packages/29/32/43996ea21f8d5579639721bf2f2a0133cd39b20693e679b859ffdb3971a3/astropy-6.0.0.tar.gz")
    version("5.1", sha256="1db1b2c7eddfc773ca66fa33bd07b25d5b9c3b5eee2b934e0ca277fa5b1b7b7e", url="https://pypi.org/packages/67/3d/bf8dd07f37dd9d1b14bc92985734a3eb7fb15a136dba1ebcc3e3a76d9327/astropy-5.1.tar.gz")
    version("4.0.1.post1", sha256="5c304a6c1845ca426e7bc319412b0363fccb4928cb4ba59298acd1918eec44b5", url="https://pypi.org/packages/72/b2/18d48f5ed8dedc37e30bdf6f84ba3dc656c31dd7de9f4b6e0a2d9810cd37/astropy-4.0.1.post1.tar.gz")
    version("3.2.1", sha256="706c0457789c78285e5464a5a336f5f0b058d646d60f4e5f5ba1f7d5bf424b28", url="https://pypi.org/packages/b9/10/523355eb8cb9839552c8f0fbc9425a1c87c8ff2e55f4df85469a5a4164d3/astropy-3.2.1.tar.gz")
    version("2.0.14", sha256="618807068609a4d8aeb403a07624e9984f566adc0dc0f5d6b477c3658f31aeb6", url="https://pypi.org/packages/66/55/9b608ddf1f65ff4faf54fa9194863e27856e35233609f44f5e9479952550/astropy-2.0.14.tar.gz")
    version("1.1.2", sha256="6f0d84cd7dfb304bb437dda666406a1d42208c16204043bc920308ff8ffdfad1", url="https://pypi.org/packages/42/47/f633262b6e30d1c0c08e697361a94760841b1a30d5c8e63dc20d097167e4/astropy-1.1.2.tar.gz")
    version("1.1.post1", sha256="64427ec132620aeb038e4d8df94d6c30df4cc8b1c42a6d8c5b09907a31566a21", url="https://pypi.org/packages/5d/02/98e6f6b6385349cc4c94bae0933d4b1dcf4b856691387149883fe10113c0/astropy-1.1.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("all", default=False, description="all")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@5.3-rc1:")
        depends_on("python@3.8:", when="@5:5.2")
        depends_on("py-asdf-astropy@0.3:", when="@6:+all")
        depends_on("py-astropy-iers-data@0.2023.10.30:", when="@6:")
        depends_on("py-beautifulsoup4", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-bleach", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-bottleneck", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-certifi", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-dask+array", when="@4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-fsspec@2023.4:+http", when="@6:+all")
        depends_on("py-h5py", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-html5lib", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-ipython@4.2:", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-jplephem", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-mpmath", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-numpy@1.22.0:1", when="@6.0.0:")
        depends_on("py-packaging@19:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-pandas", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-pre-commit", when="@5.3.3:+all")
        depends_on("py-pyarrow@5:", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-pyerfa@2:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-pytest@7.0.0:", when="@6:+all")
        depends_on("py-pytz", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-pyyaml@3.13:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-s3fs@2023.4:", when="@6:+all")
        depends_on("py-sortedcontainers", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-typing-extensions@3.10.0.1:", when="@5.0.8:5.0,5.3.3:+all")
    # END DEPENDENCIES


        # self-dependency
        # depends_on("py-astropy+recommended", when="@6:+all")
