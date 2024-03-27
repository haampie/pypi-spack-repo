##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLinkifyItPy(PythonPackage):
    version("2.0.3", sha256="6bcbc417b0ac14323382aef5c5192c0075bf8a9d6b41820a2b66371eac6b6d79", url="https://pypi.org/packages/04/1e/b832de447dee8b582cac175871d2f6c3d5077cc56d5575cadba1fd1cccfa/linkify_it_py-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="a3a24428f6c96f27370d7fe61d2ac0be09017be5190d68d8658233171f1b6541", url="https://pypi.org/packages/1f/1a/16b0d2f66601ba3081f1d4177087c79fd1f11d17706ee01d373e4ba8e00d/linkify_it_py-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="6cbdbd04c9ce3f3d18cd5fe432a33617dbf6eb4342e3da60ae24e917d37ec837", url="https://pypi.org/packages/82/90/fbb4b22ca145aceb492193de0ac9daef8e7a01aa59182d55b1271c7f3473/linkify_it_py-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="1bff43823e24e507a099e328fc54696124423dd6320c75a9da45b4b754b748ad", url="https://pypi.org/packages/fa/1a/2280e2eb892162ef5c0480a131d1d176b61f5f24abdce8dd9862454f7d14/linkify_it_py-2.0.0-py3-none-any.whl")
    version("1.0.3", sha256="11e29f00150cddaa8f434153f103c14716e7e097a8fd372d9eb1ed06ed91524d", url="https://pypi.org/packages/ff/f1/74e54ab5ae6aa1d3b6dc5de56fecf57fe4873d8f6b2a72a1269dbedd111b/linkify_it_py-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="4f416e72a41d9a00ecf1270ffb28b033318e458ac1144eb7c326563968a5dd24", url="https://pypi.org/packages/93/0c/1b20cdad6a89ea7e32363c9bfed0e7ed85e8721cd32634004cc2e87cd8be/linkify_it_py-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="29ba044d36f0ff938730a8167b7341a7caffc3e11666f9009996af6b82b61dfc", url="https://pypi.org/packages/1e/e8/839bad95b6ca684d18beba6dd9ff7b06a28778a57fd3fa6afbeb476e4be6/linkify_it_py-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="b7109fc7784de1751cb7d481ecb7d9cc3de78054b66401e6f572d2f29caa44ac", url="https://pypi.org/packages/e8/2d/85c9abba58ee5a058202e332b3f0a1e3a103a5c6020a402e3a360916cca9/linkify_it_py-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-uc-micro-py")

