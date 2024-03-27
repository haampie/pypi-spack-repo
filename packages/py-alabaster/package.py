##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAlabaster(PythonPackage):
    version("0.7.16", sha256="b46733c07dce03ae4e150330b975c75737fa60f0a7c591b6c8bf4928a28e2c92", url="https://pypi.org/packages/32/34/d4e1c02d3bee589efb5dfa17f88ea08bdb3e3eac12bc475462aec52ed223/alabaster-0.7.16-py3-none-any.whl")
    version("0.7.15", sha256="d99c6fd0f7a86fca68ecc5231c9de45227991c10ee6facfb894cf6afb953b142", url="https://pypi.org/packages/a8/11/a3159174442867ea12826e60a9f1d6f6299c2ae3f896d2a47566ab826686/alabaster-0.7.15-py3-none-any.whl")
    version("0.7.14", sha256="bae0286b61103c84f426bd21faaca8624725a089cf640d95f9ab9901c897fc9f", url="https://pypi.org/packages/42/9b/3db2373bee67e39e343ee411f405ec991413986c1ce345377bea04103fe4/alabaster-0.7.14-py3-none-any.whl")
    version("0.7.13", sha256="1ee19aca801bbabb5ba3f5f258e4422dfa86f82f3e9cefb0859b283cdd7f62a3", url="https://pypi.org/packages/64/88/c7083fc61120ab661c5d0b82cb77079fc1429d3f913a456c1c82cf4658f7/alabaster-0.7.13-py3-none-any.whl")
    version("0.7.12", sha256="446438bdcca0e05bd45ea2de1668c1d9b032e1a9154c2c259092d77031ddd359", url="https://pypi.org/packages/10/ad/00b090d23a222943eb0eda509720a404f531a439e803f6538f35136cae9e/alabaster-0.7.12-py2.py3-none-any.whl")
    version("0.7.11", sha256="674bb3bab080f598371f4443c5008cbfeb1a5e622dd312395d2d82af2c54c456", url="https://pypi.org/packages/6e/71/c3648cc2f675063dbe2d669004a59e4a5120172713a1de3c3b14144d4b31/alabaster-0.7.11-py2.py3-none-any.whl")
    version("0.7.10", sha256="2eef172f44e8d301d25aff8068fddd65f767a3f04b5f15b0f4922f113aa1c732", url="https://pypi.org/packages/2e/c3/9b7dcd8548cf2c00531763ba154e524af575e8f36701bacfe5bcadc67440/alabaster-0.7.10-py2.py3-none-any.whl")
    version("0.7.9", sha256="d3e64a74919373d6d4d1d36bd717206584cb64cbb0532dfce3bc2081cba6817b", url="https://pypi.org/packages/5d/da/2e59e6b040f1062843eb9e874f504bc6779053b77da5d1ed7f1b46618e13/alabaster-0.7.9-py2.py3-none-any.whl")
    version("0.7.8", sha256="e86ae2eb1a0297454ce6bbe94414fbb272ed9f148b9ca5344dc213164e0d3d74", url="https://pypi.org/packages/a4/c6/dd6bd26e13ae655e70f6f79acd46e86a3abd4e308083c4daae5a80ccb122/alabaster-0.7.8-py2.py3-none-any.whl")
    version("0.7.7", sha256="d57602b3d730c2ecb978a213face0b7a16ceaa4a263575361bd4fd9e2669a544", url="https://pypi.org/packages/25/e6/86e30d0d818955e92ee37c64f92a7a3b2cb4bbdd07a7e74a6a7c028c1f3a/alabaster-0.7.7-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.7.14:")

