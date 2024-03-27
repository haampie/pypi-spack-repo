##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCtgan(PythonPackage):
    version("0.5.3.dev0", sha256="d08e21f7ca0f4afbd17ad3df59a8283be0961773df08cf28bd76be14b5579b9e", url="https://pypi.org/packages/d1/88/f231662784e99c730538a620fa4a6c0a1559b78faab8e9911a386e775465/ctgan-0.5.3.dev0-py2.py3-none-any.whl")
    version("0.5.2", sha256="d4001e15d07b43de2bbd78fff2ba0e7f6903686c92888cab3fb19be9f2560d06", url="https://pypi.org/packages/53/1d/5e4f6796428a32375eed14b230a07c9f6b26316341a376fd90f2c4bc8fad/ctgan-0.5.2-py2.py3-none-any.whl")
    version("0.5.2.dev1", sha256="e646cd1375a543ed74669d104d61974a90ce588cff66a7f836314f60c8db8ca3", url="https://pypi.org/packages/3c/51/19f702875cb956668d58350b53c97771606d825b9b4450a63dc2cc99f83c/ctgan-0.5.2.dev1-py2.py3-none-any.whl")
    version("0.5.2.dev0", sha256="29c3795f79e102da2e5827a22ba7b1da725615e7e210f3afdc9e2fe22185eb67", url="https://pypi.org/packages/31/19/f3550f82eee73295256034462084cc5eadf80e09cdd4b78518aea0048bb3/ctgan-0.5.2.dev0-py2.py3-none-any.whl")
    version("0.5.1", sha256="b45e74085c563629745d923a9e6f18ea115c0c89d0b43b287e7ceb3716d328e3", url="https://pypi.org/packages/58/d5/556bfecc7f719fc0d1ab8df1ad992adbc4e773d6ba3c042554af225aa015/ctgan-0.5.1-py2.py3-none-any.whl")
    version("0.5.1.dev3", sha256="c9023b28dc83815dcf36d0bdd27f9e551150796fb400c4ea53187cc95e85c532", url="https://pypi.org/packages/76/7c/35aecb118a8b63d3e633c21c0180831e9bef2b636bb0596b7ce7d2df008f/ctgan-0.5.1.dev3-py2.py3-none-any.whl")
    version("0.5.1.dev2", sha256="0f326ff2f1177a3cb0192f858bc1153d381dfa386ca5f255e2f83ce3fb59fa68", url="https://pypi.org/packages/f7/1a/3b8e1dd2e2869d520f5d3fad807f3f4edfca6b19fe770d8ed579adad31fe/ctgan-0.5.1.dev2-py2.py3-none-any.whl")
    version("0.5.1.dev1", sha256="d2371d3b2d04f1a758dbd86cbb17c21027d3ee0dde85ab1cbbb4e09da3eeb6f2", url="https://pypi.org/packages/76/76/9b04ef67c84654a0ff8a1bf9d447baa613eb97b2f9243b3d622372fa8a7f/ctgan-0.5.1.dev1-py2.py3-none-any.whl")
    version("0.5.1.dev0", sha256="82cecf848656538d870a3c835d7664279bfbd26b0c169397d942e7d22522db36", url="https://pypi.org/packages/1f/09/6a0abfd4a584ab9c6acda540f95e2c4f74759ff2be6c5d8258afdba66f59/ctgan-0.5.1.dev0-py2.py3-none-any.whl")
    version("0.5.0", sha256="aa53689bb16e1f64cde349d3151d11d8dadf1042d35365c307c89afc88458c7a", url="https://pypi.org/packages/b4/ea/fba41f2b0ce20902257daa7263f3deed3c4e03a6c3e7b9f8018dd0574e4c/ctgan-0.5.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.7.4:")
        depends_on("python@:3.10", when="@0.7:0.7.3")
        depends_on("python@:3.9", when="@0.5:0.6")
        depends_on("python@:3.8", when="@0.2.2:0.4,0.5.0.dev:0.5.0.dev0")
        depends_on("py-numpy@1.20.0:1", when="@0.7:0.9.0 ^python@:3.9")
        depends_on("py-numpy@1.20.0:1", when="@0.5:0.6")
        depends_on("py-packaging@20:21", when="@0.5:0.7.3")
        depends_on("py-pandas@1.1.3:1", when="@0.7:0.7.1 ^python@:3.9")
        depends_on("py-pandas@1.1.3:1", when="@0.5:0.6")
        depends_on("py-rdt@1.1:1.1.0.0,1.2:", when="@0.5.2.dev:0.5.2.dev0")
        depends_on("py-rdt@1.2:1.2.0.0,1.2.1:", when="@0.5.2:0.6")
        depends_on("py-rdt@0.6.2:0.6.2.0,0.6.3:0", when="@0.5.1")
        depends_on("py-rdt@0.6.1:0.6.1.0,0.6.2:0", when="@0.5:0.5.0")
        depends_on("py-scikit-learn@0.24.0:", when="@0.5:0.6")
        depends_on("py-torch@1.8:1", when="@0.7:0.7.2 ^python@:3.9")
        depends_on("py-torch@1.8:1", when="@0.5:0.6")
        depends_on("py-torchvision@0.9:", when="@0.5:0.6")

