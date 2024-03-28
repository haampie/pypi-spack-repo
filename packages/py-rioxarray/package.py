# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRioxarray(PythonPackage):
    # BEGIN VERSIONS
    version("0.15.1", sha256="75c41e5836a9adba2a42a2cdbc62a50b81e01bd4fcc9f55a96f187322182d671", url="https://pypi.org/packages/48/07/f707d40e8a026a47b9419e11d79216128296c50eb59b0deb241eac3e16e7/rioxarray-0.15.1-py3-none-any.whl")
    version("0.15.0", sha256="d7c0b2efc21075f77fe04302b916a995320004695f3c31e4f06d9ab40acd4498", url="https://pypi.org/packages/4e/34/8ee402df8a49228b6aae89ab2127cdd5aa0ba0976904af7d55270f4f30b8/rioxarray-0.15.0-py3-none-any.whl")
    version("0.14.1", sha256="de8142fcc960fd2121632d1bf50a7e08adad958efc056f52aa78226a6f22e955", url="https://pypi.org/packages/6b/4b/3f16566e7b7bfb1a0bbdc4abf19773d33fe37bbaf66150592ef5b511e8bd/rioxarray-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="b261aa23316ecf8168b338379050e833c0cabd58877893797653ddeb386d6f58", url="https://pypi.org/packages/a5/98/440c55586485c12efc40f1c248765e2c51cf59c1eb16b39db51e5fe42dc6/rioxarray-0.14.0-py3-none-any.whl")
    version("0.13.4", sha256="56eef711d9817d3c729c1a267c940e7dff66bfc874a0b24ed3604ea2f958dfb2", url="https://pypi.org/packages/ad/ea/a55e848a8d167911e88a65d42bc86aa53ff35960c9650d33d7b6ee19d27c/rioxarray-0.13.4-py3-none-any.whl")
    version("0.13.3", sha256="d18baa4364b1f2c43f8df54711aae341f4fc0478f06d5bda20790d727be75bf6", url="https://pypi.org/packages/47/ec/ace6c5d23f37e06aaae8ebb74027f3d7b9396a25a2880c746eb7bb143a9a/rioxarray-0.13.3-py3-none-any.whl")
    version("0.13.2", sha256="bb9f3b335ccf66c6ea7912b12c2f73e098ded232493318454f8ad20f1688054a", url="https://pypi.org/packages/74/63/5c7afe064a55c09392f1b7501fc00dfa67c962cc7d9493c5e904e6bb9524/rioxarray-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="4f3d28acb16238a42a8185592e4a2579186a4cea307bfb0f93b12783ff09afd4", url="https://pypi.org/packages/4a/50/886e15fffe29280341c9ed30ddedb34a111a223abc48dd1ea845285e8507/rioxarray-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="b448780070ec8fe194c5ab80c87150535939619dc7552c0be8c802e844c6bec3", url="https://pypi.org/packages/37/d6/914d873f57e29c17bccca102b16e0024f30d437ea8b3db9dcf036a3df2e7/rioxarray-0.13.0-py3-none-any.whl")
    version("0.12.4", sha256="12d2c0b50b847ab1f88b37ee26d3861c2ae788cef2da9fe251066d7c7d9f0dfd", url="https://pypi.org/packages/79/56/a8e5b04bb0456f2b0e7182607ae4d2a203d17c35a3d4c3331669578c5fb7/rioxarray-0.12.4-py3-none-any.whl")
    version("0.4.1.post0", sha256="f043f846724a58518f87dd3fa84acbe39e15a1fac7e64244be3d5dacac7fe62b", url="https://pypi.org/packages/ab/a1/37432860acd0859b7df470150f10bba2fd1d08e879ab8e7a63b85bab9048/rioxarray-0.4.1.post0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.15.1:")
        depends_on("python@3.9:", when="@0.14:0.15.0")
        depends_on("py-numpy@1.23.0:", when="@0.15.1:")
        depends_on("py-numpy@1.21.0:", when="@0.13.4:0.15.0")
        depends_on("py-packaging", when="@0.11.2:")
        depends_on("py-pyproj@3.3:", when="@0.15.1:")
        depends_on("py-pyproj@2.2:", when="@0.11.2:0.15.0")
        depends_on("py-rasterio@1.3.0:", when="@0.15.1:")
        depends_on("py-rasterio@1.2.0:", when="@0.14:0.15.0")
        depends_on("py-rasterio@1.1.1:", when="@0.11.2:0.13")
        depends_on("py-xarray@2022:", when="@0.15.1:")
        depends_on("py-xarray@0.17:", when="@0.11.2:0.15.0")
    # END DEPENDENCIES

