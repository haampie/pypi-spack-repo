##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightningApp(PythonPackage):
    version("0.7.0", sha256="fdecdb2cfc8d7c472158ba08f2a417ee301e3ef8a0cdeb5791826a48bf69f712", url="https://pypi.org/packages/e9/fd/aacc30c97d17028fb6b8f4ef1bc0cbbe9dd23a8d248562d79748934d159a/lightning_app-0.7.0-py3-none-any.whl")
    version("0.6.3", sha256="966ed5a2a36f2da23c1757302817a0425b88bd3198a22523f21043bf1c15ad05", url="https://pypi.org/packages/5f/dc/9e07afc92c245d01e5428d8f2704ab0e934b07b7c835d0a7428f158b3e35/lightning_app-0.6.3-py3-none-any.whl")
    version("0.6.2", sha256="b2edd1dc4046fd99f06d0313ae46339a4736822d960d896715a50d64a528f409", url="https://pypi.org/packages/5e/23/9fc5682eaa03be2ad0feaa783c711b6d73ec43f669a916b27988c3e02894/lightning_app-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="178c12c50931ec44e3443c0ea2e3b4c50926effdd8b5ecadad8d41f04fc67cd4", url="https://pypi.org/packages/ee/24/e81c132c56edd95448c44746d63c812056821619bb4a9fb8972eec9a87ff/lightning_app-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="ef4a34a3d9da303bc7117e95c33e5cef47ffe9528ed8b047b66f68a08c0da3fc", url="https://pypi.org/packages/be/ad/b53e42a8ab3b11ae0ac783706c726df1d50fb991afe11d9753dd69577f09/lightning_app-0.6.0-py3-none-any.whl")
    version("0.6.0-rc0", sha256="6d0d4f30fce0a9404e3ad1940f451f4071f7ade10222d4d1e5b5a1d8d6b1735f", url="https://pypi.org/packages/bf/4f/dfcff4fb86fb09c2aae6a54f20f211009aa88a6ad1f05970965aee132ed0/lightning_app-0.6.0rc0-py3-none-any.whl")
    version("0.5.7", sha256="dc0f98d6da0d6223f3df18167e051ae819e9496c2c0dfd0991cc83661ee6d5ba", url="https://pypi.org/packages/10/87/15d1879fa13327b471fa69a39da049ee75b70998d0757fd4c7e1ba115a35/lightning_app-0.5.7-py3-none-any.whl")
    version("0.5.6", sha256="8c65464417a69c47bbef7b5c7981d6ae27c38f353c703141e8c74757a78f1dcb", url="https://pypi.org/packages/72/22/2282bb1cd0554e8cbbc34b572e26c58903c578a38c1e5eb1b21135c8390e/lightning_app-0.5.6-py3-none-any.whl")
    version("0.5.5", sha256="40b67138a63990c02ce70b1a3c8e2bb607744d7c9a7ce370afff11d2593fc8a7", url="https://pypi.org/packages/fb/71/a44910fc36cd1ceeb786430a3d607d9c2dcfbb40f88beefd5e21f212bb7f/lightning_app-0.5.5-py3-none-any.whl")
    version("0.5.4", sha256="f8e3ea81942a5973da19afcec8cb2cfa1d1c155b2a231d8d71f3bb6002084cbd", url="https://pypi.org/packages/60/e5/6676b63de4efca26843d6a29773b8cf170643332b1dca5fc32b71a98726c/lightning_app-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="60f528773f413e1362291bdbdf6b942774e33a51d47c5986518e14757b89911a", url="https://pypi.org/packages/47/97/e0e53dae88cf6524e67100694d6d45f8026d4b1af1232d350a81be43682c/lightning_app-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="d22d6c0412d092cc130094a3503c4ec70fe66389b6590eb6a9c95ba6e153cb42", url="https://pypi.org/packages/d7/64/3412302fcbfdc3dfd30cf982a547e9ce9c0163d5719ff335344841c3bb97/lightning_app-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="ce4cbbf907acaa08032e8e3caa15e77dfbc07295cab3bd8db84f094091830055", url="https://pypi.org/packages/d1/9b/9b1ebd416aff195fd70516a43bfe7ad002e440888c6012bdd59959ec1536/lightning_app-0.5.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-arrow@1.2:", when="@0.6:1.8")
        depends_on("py-beautifulsoup4", when="@0.6.3:1.8.2")
        depends_on("py-click", when="@0.5:0.5.2,1.8.1:1.8")
        depends_on("py-croniter@1.3", when="@0.6.0:2.0.4")
        depends_on("py-croniter", when="@0.5:0.6.0-rc0")
        depends_on("py-deepdiff@5.7:", when="@0.5:1.8")
        depends_on("py-fastapi+all", when="@0.5:0.5.2")
        depends_on("py-fsspec@2022.5:", when="@0.6.0:1.8")
        depends_on("py-fsspec@2022:", when="@0.6:0.6.0-rc0")
        depends_on("py-fsspec@2022:2022.1", when="@0.5")
        depends_on("py-jinja2@3.0.3:3.0", when="@0.5")
        depends_on("py-lightning-cloud@0.5.7", when="@0.6.1:0")
        depends_on("py-lightning-cloud@0.5.3", when="@0.5.6:0.6.0")
        depends_on("py-lightning-cloud@0.5.0", when="@0.5.0-rc1:0.5.5")
        depends_on("py-lightning-utilities@0.3", when="@0.6.0:1.8.3")
        depends_on("py-packaging", when="@0.5:1.8.0-rc0,1.8.0-rc2:")
        depends_on("py-psutil", when="@1:1.8")
        depends_on("py-py", when="@0.5")
        depends_on("py-requests", when="@0.5:0.5.2")
        depends_on("py-s3fs@2022.5:", when="@0.6.0:1.8.2,1.8.3.post:1.8.4.0")
        depends_on("py-s3fs@2022:", when="@0.6:0.6.0-rc0")
        depends_on("py-s3fs@2022:2022.1", when="@0.5")
        depends_on("py-starsessions@1.2:1", when="@0.5.7:2.1.2")
        depends_on("py-starsessions", when="@0.5:0.5.6")
        depends_on("py-traitlets@5.3:5.3.0.0,5.4:", when="@0.6.1:1.8")
        depends_on("py-traitlets", when="@0.5.1:0.6.0")
        depends_on("py-urllib3", when="@0.5:0.5.2")

