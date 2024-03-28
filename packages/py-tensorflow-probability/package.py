# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorflowProbability(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.21.0", sha256="03ed06bd6fd876541110712842d43367c7be5affe8040d62efa3906c6c9e645d", url="https://pypi.org/packages/44/71/55146f816eb53008d6df423b948514d245b46f00dab2bce2a91d596dd827/tensorflow_probability-0.21.0-py2.py3-none-any.whl")
    version("0.20.1", sha256="fc10597d2b1a26ecdfae2086307944dd7f1082a0e8a2f615b56c1f0121a7763d", url="https://pypi.org/packages/ed/a4/dddf262db60c11c67790276e77f0c34a45ce38cafadd4843aa69195e654b/tensorflow_probability-0.20.1-py2.py3-none-any.whl")
    version("0.20.0", sha256="1e00c4d20ea5fd7eb829b2e9738471f60c020d9a5acd4af9f6670f871f78a1c5", url="https://pypi.org/packages/2b/0a/0ac690cddd0e970199051655a81459256fa580f4500bdf1109c9d700443d/tensorflow_probability-0.20.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.22:")
        depends_on("py-absl-py", when="@0.14:")
        depends_on("py-cloudpickle@1.3:", when="@0.11.1:")
        depends_on("py-decorator", when="@0.7:")
        depends_on("py-dm-tree", when="@0.11:")
        depends_on("py-gast@0.3.2:", when="@0.10:")
        depends_on("py-numpy@1.13.3:", when="@0.4:")
        depends_on("py-six@1.10:")
        depends_on("py-typing-extensions@:4.5", when="@0.21:0.22.0")
    # END DEPENDENCIES

