# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstropy(PythonPackage):
    # BEGIN VERSIONS
    version("6.0.0", sha256="03cd801a55305da523cd8d780d76359f57255dcdc59fe0bdd71fd5154fc777d9", url="https://pypi.org/packages/29/32/43996ea21f8d5579639721bf2f2a0133cd39b20693e679b859ffdb3971a3/astropy-6.0.0.tar.gz")
    version("5.3.4", sha256="d490f7e2faac2ccc01c9244202d629154259af8a979104ced89dc4ace4e6f1d8", url="https://pypi.org/packages/98/bd/9bf004a1b3f10f9c8e82e3aed87297aa79914bef8619182f8bcf414c9c69/astropy-5.3.4.tar.gz")
    version("5.3.3", sha256="0330df9f5d7a2254367e9b8cf44255ba1070b06123188c6a72edc180493f93bb", url="https://pypi.org/packages/79/36/c19ad378cf7a3e6d645b756c3ec2830fb8f2dde7307201a0fb859a0ff05a/astropy-5.3.3.tar.gz")
    version("5.3.2", sha256="222003dedd4d1ad00cf3b3a02747fd59c4fc93a97ddbe6328952916ad5f1558f", url="https://pypi.org/packages/5d/2a/0bb1e43f5643e47208e53882414f088f13d52b890b9349fa2c1c108d0e31/astropy-5.3.2.tar.gz")
    version("5.3.1", sha256="9b5321b65e35ff7f7976d34c9ab9748f11d1f427a509aa8d7fc1ead4f9818d74", url="https://pypi.org/packages/bf/8a/f0a9bcbaf59cb7f22340b77e6caa28ff9a726b32b1883f4813f66ba780f4/astropy-5.3.1.tar.gz")
    version("5.3", sha256="1f694be1c2b32309aca15cf7b54aa17546e944135209394cdceebd7a7889e4e5", url="https://pypi.org/packages/8d/52/376379d9a1929f788fc8113e1bfc010c2cb7c7efa67e6f3585321d60bba9/astropy-5.3.tar.gz")
    version("5.2.2", sha256="e6a9e34716bda5945788353c63f0644721ee7e5447d16b1cdcb58c48a96b0d9c", url="https://pypi.org/packages/bf/01/947bf59bc5e515c49e1eccf68d7f30e903dc528c0e4df9f3246b1095ad7d/astropy-5.2.2.tar.gz")
    version("5.2.1", sha256="f6ae27a077f8ea84903efa76c790b985617341a0084b0d21c391f7a3f332ac23", url="https://pypi.org/packages/81/a9/601e7464c81666d5a7cb1220754385f295393efb876dc1a7b8df1f80881f/astropy-5.2.1.tar.gz")
    version("5.2", sha256="d335604025f6e16f7c9bf82d5ba28e5db4745a82e5823a9d17bdd9b9bd46b2a2", url="https://pypi.org/packages/14/9a/6f1376020f08fbfc40d3e06590636909a7658f5ed6764d8b583c22c0278b/astropy-5.2.tar.gz")
    version("5.1.1", sha256="ba4bd696af7090fd399b464c704bf27b5633121e461785edc70432606a94bd81", url="https://pypi.org/packages/ce/02/213096b189211a750d21d48d18d945efa6c8a334134a6f01b8f2d2fd4b2d/astropy-5.1.1.tar.gz")
    version("5.1", sha256="1db1b2c7eddfc773ca66fa33bd07b25d5b9c3b5eee2b934e0ca277fa5b1b7b7e", url="https://pypi.org/packages/67/3d/bf8dd07f37dd9d1b14bc92985734a3eb7fb15a136dba1ebcc3e3a76d9327/astropy-5.1.tar.gz")
    version("4.0.1.post1", sha256="5c304a6c1845ca426e7bc319412b0363fccb4928cb4ba59298acd1918eec44b5", url="https://pypi.org/packages/72/b2/18d48f5ed8dedc37e30bdf6f84ba3dc656c31dd7de9f4b6e0a2d9810cd37/astropy-4.0.1.post1.tar.gz")
    version("3.2.1", sha256="706c0457789c78285e5464a5a336f5f0b058d646d60f4e5f5ba1f7d5bf424b28", url="https://pypi.org/packages/b9/10/523355eb8cb9839552c8f0fbc9425a1c87c8ff2e55f4df85469a5a4164d3/astropy-3.2.1.tar.gz")
    version("2.0.14", sha256="618807068609a4d8aeb403a07624e9984f566adc0dc0f5d6b477c3658f31aeb6", url="https://pypi.org/packages/66/55/9b608ddf1f65ff4faf54fa9194863e27856e35233609f44f5e9479952550/astropy-2.0.14.tar.gz")
    version("1.1.2", sha256="6f0d84cd7dfb304bb437dda666406a1d42208c16204043bc920308ff8ffdfad1", url="https://pypi.org/packages/42/47/f633262b6e30d1c0c08e697361a94760841b1a30d5c8e63dc20d097167e4/astropy-1.1.2.tar.gz")
    version("1.1.post1", sha256="64427ec132620aeb038e4d8df94d6c30df4cc8b1c42a6d8c5b09907a31566a21", url="https://pypi.org/packages/5d/02/98e6f6b6385349cc4c94bae0933d4b1dcf4b856691387149883fe10113c0/astropy-1.1.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("all", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@5.3-rc1:")
        depends_on("py-asdf@2.10:", when="@5.3.3:5+all")
        depends_on("py-asdf-astropy@0.3:", when="@6:+all")
        depends_on("py-astropy-iers-data@0.2023.10.30:", when="@6:")
        depends_on("py-beautifulsoup4", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-bleach", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-bottleneck", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-certifi", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-dask+array", when="@4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-fsspec@2023.4:+http", when="@6:+all")
        depends_on("py-fsspec@2022.8.2:+http", when="@5.3.3:5+all")
        depends_on("py-h5py", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-html5lib", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-ipython@4.2:", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-jplephem", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-matplotlib@3.3.0:3.4.0-rc3,3.4.1:3.5.1,3.5.3:", when="@5.3.3:5+all")
        depends_on("py-mpmath", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-numpy@1.22.0:1", when="@6.0.0:")
        depends_on("py-numpy@1.21.0:1", when="@5.3.3:5")
        depends_on("py-packaging@19:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-pandas", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-pre-commit", when="@5.3.3:+all")
        depends_on("py-pyarrow@5:", when="@5.0.8:5.0,5.3.3:+all")
        depends_on("py-pyerfa@2:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-pytest@7.0.0:", when="@6:+all")
        depends_on("py-pytest@7.0.0:7", when="@5.0.8:5.0,5.3.3:5+all")
        depends_on("py-pytz", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-pyyaml@3.13:", when="@5.0.8:5.0,5.3.3:")
        depends_on("py-s3fs@2023.4:", when="@6:+all")
        depends_on("py-s3fs@2022.8.2:", when="@5.3.3:5+all")
        depends_on("py-scipy@1.5.0:", when="@5.3.3:5+all")
        depends_on("py-sortedcontainers", when="@3.2-rc1:3.2.0,3.2.2:4.0.1.0,4.1-rc1,5.0.8:5.0,5.3.3:+all")
        depends_on("py-typing-extensions@3.10.0.1:", when="@5.0.8:5.0,5.3.3:+all")

        # self-dependency
        # depends_on("py-astropy+recommended", when="@6:+all")
    # END DEPENDENCIES

