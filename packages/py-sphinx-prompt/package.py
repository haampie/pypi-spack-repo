##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxPrompt(PythonPackage):
    version("1.8.0", sha256="369ecc633f0711886f9b3a078c83264245be1adf46abeeb9b88b5519e4b51007", url="https://pypi.org/packages/39/49/f890a2668b7cbf375f5528b549c8d36dd2e801b0fbb7b2b5ef65663ecb6c/sphinx_prompt-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="7ee415d07f90f7ce1577a2c4c7f2560694af008926a69b4c940f20737621b089", url="https://pypi.org/packages/60/94/89f33756b82dbe9453cd05176c43a43e7f2337816f48c8a234396f027493/sphinx_prompt-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="a118fc1519f367dfffd73fbc34e1d905e38929dec6a3971518a331bf0689b0df", url="https://pypi.org/packages/11/25/a9252d0ccf84247b602a47cbe1ec6669647971841594ee8a1ed38b7b1c38/sphinx_prompt-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="fa4e90d8088b5a996c76087d701fc7e31175f8b9dc4aab03a507e45051067162", url="https://pypi.org/packages/82/21/d586f993ac5aafd855dab44252acde54cf2652ce1bbaed126650e9d0cc54/sphinx_prompt-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="ac54b204c3e0ff75851d92060672b65407ff67f8942bde2eb6ba318b8e7ca595", url="https://pypi.org/packages/19/e4/7fc51c0f1fa62fb6e51c4b6dc724e62b447d347a94ce301253652522ccc0/sphinx_prompt-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="f3d2389c55dadc790e10a936bf889706671538af442078d3f9dea634adf81d0b", url="https://pypi.org/packages/4a/5b/4913660fbe8325cf3b1721ac74486e13aa1fa35883eaa39b200f3f9b8714/sphinx_prompt-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="3255438fa2480863cadbcebb098421f0cece761e0a440f577f891dc6779960e3", url="https://pypi.org/packages/2d/30/20e8e5739eb6973875abdc1f345de87b195a95b98861936cf54d1245238b/sphinx_prompt-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="3d9cf382b750291f73d1f6f1713c4af0557c30208af124cd3d8731e607a4febf", url="https://pypi.org/packages/16/1e/0dd94829b97676b7d7cdf2f0e86cb169d6f2ffb56590427833d281370116/sphinx-prompt-1.1.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.8:")
        depends_on("python@:3.10", when="@1.6:1.7")
        depends_on("py-docutils", when="@1.6:")
        depends_on("py-pygments", when="@1.1,1.3:")
        depends_on("py-sphinx@7.0.0:", when="@1.7:")
        depends_on("py-sphinx@6.0.0:6", when="@1.6")
        depends_on("py-sphinx", when="@1.1,1.3:1.5")

