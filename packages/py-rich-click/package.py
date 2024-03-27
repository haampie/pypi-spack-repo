##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRichClick(PythonPackage):
    version("1.7.4", sha256="e363655475c60fec5a3e16a1eb618118ed79e666c365a36006b107c17c93ac4e", url="https://pypi.org/packages/c8/9a/cba26d290a2aaef47825d11140c9619ca56ef8a79302a3c16dad83c60151/rich_click-1.7.4-py3-none-any.whl")
    version("1.7.3", sha256="bc4163d4e2a3361e21c4d72d300eca6eb8896dfc978667923cb1d4937b8769a3", url="https://pypi.org/packages/ea/6a/89ee4e245a8c21791d7db3669931948f237a421fafec72de6d1e7e25f3b2/rich_click-1.7.3-py3-none-any.whl")
    version("1.7.2", sha256="a42bcdcb8696c4ca7a3b1a39e1aba3d2cb64ad00690b4c022fdcb2cbccebc3fc", url="https://pypi.org/packages/72/0c/a7e1b2161edced47101771e1807ac74e921168088c83765eb083c17746ef/rich_click-1.7.2-py3-none-any.whl")
    version("1.7.1", sha256="c37d19af85c86b9a256c18e9d23637ae89478300ec8dc5e220c6ca213675f2f9", url="https://pypi.org/packages/ec/0c/0df6f31569706d8fdc213b8c5cf8998b6c5f60e98561313a21f142620a45/rich_click-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="093f50400135bad749a00c4cc0cfa4591b3c58a9438685abfa7314ee7b63d3bc", url="https://pypi.org/packages/e0/47/8c788b2d1f7e257da453444d5c03d97f0d02c41e717c737f2cbbb5d46bf7/rich_click-1.7.0-py3-none-any.whl")
    version("1.6.1", sha256="0fcf4d1a09029d79322dd814ab0b2e66ac183633037561881d45abae8a161d95", url="https://pypi.org/packages/f4/f2/3fbb0e6eee13a484dc8aaca450e9322d267fc3839b6769841492f1594037/rich_click-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="aefb0450c22462cf3bf9fa854457e6b3cdf692073174823a00d3b0541a81b19d", url="https://pypi.org/packages/12/9b/58667e51e93e81ee6b08636af1520c4bd8f5662842de7a402d15875fca92/rich_click-1.6.0-py3-none-any.whl")
    version("1.5.2", sha256="131a94bed597eab9f1eda7eb41fb7275b6b60ae9e6defc3769277b70b104285d", url="https://pypi.org/packages/6b/7f/b60be5d08e0dd119a05884e55ab26a2b14c2a0bb696e4bbb05c2bb1436d1/rich_click-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="cf16bf9e390d5c9aa3b379c3884c52b47f54c8e6e2e7ddb7b2a002f4420c35c0", url="https://pypi.org/packages/07/f9/22eea32462b8c40906923898273a725576bed8ea275d79dfe84def3fbe83/rich_click-1.5.1-py3-none-any.whl")
    version("1.5", sha256="61c778fafb9ad206b2309fa1d88ad475e6a1c5111a68f47f1ecc1bc5b15906d5", url="https://pypi.org/packages/5f/ed/27ef71576dc0e91832fd1fc93dd948cf2cf4d1a28e77f230a616f75dae7d/rich_click-1.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@1.1:")
        depends_on("py-rich@10.7:", when="@1.3.1:")
        depends_on("py-typing-extensions", when="@1.7:")

