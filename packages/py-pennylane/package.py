# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPennylane(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.35.1", sha256="d1fbeada4f2e8561bbba6a8a19ee84e129665c396b880ae66ab076ce5acb3ad0", url="https://pypi.org/packages/81/b7/399790269de8c3473f3ee150262202f7c7af6281160f59d9888bc0f7094e/PennyLane-0.35.1-py3-none-any.whl")
    version("0.35.0", sha256="da9173dd9b61a65e9f6e771ecdab3380df9cc49118343a5128306aa713b28fc2", url="https://pypi.org/packages/94/43/d2ee9127b735e0549e8d91de6966e920cabc5e28882010e1268e1f52dde0/PennyLane-0.35.0-py3-none-any.whl")
    version("0.34.0", sha256="d1e6016ad13af76f880e9b1c787dcf4e8fd73b781c2e004c970b0f7c4928d77f", url="https://pypi.org/packages/75/46/28e20e5fbbdcb821e58fcc1e8550dd6c11a70240fa81250ccd41d670cc7d/PennyLane-0.34.0-py3-none-any.whl")
    version("0.33.1", sha256="222bdb8cdd7520873d3a879b92564000dc8ff58f95c92bbd191292e47a20d274", url="https://pypi.org/packages/a3/2f/b741bad7ee00979280d64f438977f4dccc22215d81f637191eda9c6c1569/PennyLane-0.33.1-py3-none-any.whl")
    version("0.33.0", sha256="0d98b3dd9567e2bc682c68ea790cb8dd815d3a60f3442e66de8a45a3a88b8b90", url="https://pypi.org/packages/87/e7/6771fdb282062412b6c7539b4d4690ef63982efdc61154e500926f03cb45/PennyLane-0.33.0-py3-none-any.whl")
    version("0.32.0", sha256="3fe85394de25d0e189c93c6b92171bcff09bf392618ebed57a7401a3c819713d", url="https://pypi.org/packages/ec/12/783161913f263cc311fb686b05c0e7abb42f87b158f49664f95472aa2135/PennyLane-0.32.0-py3-none-any.whl")
    version("0.31.0", sha256="a62a30760f6d4b4c3b88449eb8a98e9a03860ae61ec6d5178d83d3140c5c9ae0", url="https://pypi.org/packages/ef/07/34c305ba50e4ea662143e10d8f566078df5e4d71b8d8b376c532e30147de/PennyLane-0.31.0-py3-none-any.whl")
    version("0.30.0", sha256="6b8189bf34d84d39dbdda343c1bb1402117545443f57c6a6dd2480e6ab6c538c", url="https://pypi.org/packages/f1/10/c84ea151654cc4f754ba362eb99db2321edbd5c96b08bdd30bfe1e6bc4a3/PennyLane-0.30.0-py3-none-any.whl")
    version("0.29.1", sha256="d6feac06958a8a324745e8094c4535a30a97f64e9befca039edb559d7e78e036", url="https://pypi.org/packages/31/5d/1b645e719900f59c8f4c654f95e5ce62d040153f2f36562de9793dfea10c/PennyLane-0.29.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs", when="@:0.3,0.5:0.14.0,0.15:")
        depends_on("py-autograd@:1.5", when="@0.31:0.32")
        depends_on("py-autograd", when="@:0.3,0.5:0.14.0,0.15:0.30,0.33:")
        depends_on("py-autoray@0.6.1:", when="@0.33:")
        depends_on("py-autoray@0.3:", when="@0.23.1:0.31.0,0.32")
        depends_on("py-cachetools", when="@0.18:")
        depends_on("py-networkx", when="@0.5:0.14.0,0.15:")
        depends_on("py-numpy@:1.23", when="@0.28:0.32")
        depends_on("py-numpy", when="@:0.3,0.5:0.14.0,0.15:0.27,0.33:")
        depends_on("py-pennylane-lightning@0.35:", when="@0.35:")
        depends_on("py-pennylane-lightning@0.34:", when="@0.34")
        depends_on("py-pennylane-lightning@0.33:", when="@0.33")
        depends_on("py-pennylane-lightning@0.32:", when="@0.32")
        depends_on("py-pennylane-lightning@0.31:", when="@0.31")
        depends_on("py-pennylane-lightning@0.30:", when="@0.30")
        depends_on("py-pennylane-lightning@0.28:", when="@0.28:0.29")
        depends_on("py-requests", when="@0.27:")
        depends_on("py-retworkx", when="@0.21:0.29")
        depends_on("py-rustworkx", when="@0.30:")
        depends_on("py-scipy@:1.10.0", when="@0.31:0.31.0")
        depends_on("py-scipy", when="@:0.3,0.5:0.14.0,0.15:0.30,0.31.1:")
        depends_on("py-semantic-version@2.7:", when="@0.25:")
        depends_on("py-toml", when="@:0.3,0.5:0.14.0,0.15:")
        depends_on("py-typing-extensions", when="@0.31.1:")
    # END DEPENDENCIES

