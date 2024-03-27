##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonpickle(PythonPackage):
    version("3.0.3", sha256="e8d6dcc58f6722bea0321cd328fbda81c582461185688a535df02be0f699afb4", url="https://pypi.org/packages/d6/be/c11f919e02622f15b942c0f2867dff6c3836ce32cd617627dda73bc9e5b7/jsonpickle-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="4a8442d97ca3f77978afa58068768dba7bff2dbabe79a9647bc3cdafd4ef019f", url="https://pypi.org/packages/d3/25/6e0a450430b7aa194b0f515f64820fc619314faa289458b7dfca4a026114/jsonpickle-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="130d8b293ea0add3845de311aaba55e6d706d0bb17bc123bd2c8baf8a39ac77c", url="https://pypi.org/packages/4c/2f/75afdf7c9688eba3575072034abf4572833c4ef291177d2510a103c5f251/jsonpickle-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="7c4b13d595ff3520148ed870b9f5917023ebdc55c9ec0cb695688fdc16e90c3e", url="https://pypi.org/packages/42/2c/532a5179b1eb056bd97b4af27b531c040264255ddb7ec66c3821d9cc51b1/jsonpickle-3.0.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="de7f2613818aa4f234138ca11243d6359ff83ae528b2185efdd474f62bcf9ae1", url="https://pypi.org/packages/c6/85/b4920d8087ef480eed4e7b6b0d46c90674e923e59b22e7929fd17aba5030/jsonpickle-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="1dee77ddc5d652dfdabc33d33cff9d7e131d428007007da4fd6f7071ae774b0f", url="https://pypi.org/packages/21/55/d9f469f57ca9c8de8490d155c2d121edafade8ab7405015df0f1daf89aa1/jsonpickle-2.1.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="c1010994c1fbda87a48f8a56698605b598cb0fc6bb7e7927559fc1100e69aeac", url="https://pypi.org/packages/bb/1a/f2db026d4d682303793559f1c2bb425ba3ec0d6fd7ac63397790443f2461/jsonpickle-2.0.0-py2.py3-none-any.whl")
    version("1.5.2", sha256="7ace67f85a5cfd148e0d2b7defb63d97e856dd5151c092cc6c48dcc91f39f471", url="https://pypi.org/packages/e9/ec/35910cf6ab87f8a013036f01f732f871a23b6058123a7bd0c7b08fbbc937/jsonpickle-1.5.2-py2.py3-none-any.whl")
    version("1.5.1", sha256="8eb8323f0e12cb40687f0445e2115d8165901e20ac670add55bb53a95c68c0e5", url="https://pypi.org/packages/77/a7/c2f527ddce3155ae9e008385963c2325cbfd52969f8b38efa2723e2af4af/jsonpickle-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="423d7b5e6c606d4c0efd93819913191e375f3a23c0874f39df94d2e20dd21c93", url="https://pypi.org/packages/7d/09/600132ea6cd4f816cc8ae6a8cfe4f85d9f898f169756dbfc176037a3a2f2/jsonpickle-1.5.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="8919c166bac0574e3d74425c7559434062002d9dfc0ac2afa6dc746ba4a19439", url="https://pypi.org/packages/af/ca/4fee219cc4113a5635e348ad951cf8a2e47fed2e3342312493f5b73d0007/jsonpickle-1.4.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@1.4:1.4.1")
        depends_on("py-setuptools@:58", when="@3:3.0.0 ^python@3.10.1:")

