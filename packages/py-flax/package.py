# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlax(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.2", sha256="911d83e01380fdb3135c309e70981aabd15e7ca038014d7989ddc3cfaf4d0d45", url="https://pypi.org/packages/b9/92/59b0a2b5df281206433fa6496b176e95249eb0a8192586f88309d7d5df27/flax-0.8.2-py3-none-any.whl")
    version("0.8.1", sha256="8cf9ef11859eef252470377556a8cc48db287fc6647407ab34f1fc01461925dd", url="https://pypi.org/packages/8d/4a/7e78abc8392ff21b0257deb79e842f80647b63b745447df94893732d60fd/flax-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="945fdf051895f52a81adc46b7bb6640cdd32aaa759428f0fcb6a2e519a46e8bb", url="https://pypi.org/packages/4e/f8/73393399a87da4e5284502d353ff95eae28054fe8860c28af171cc789716/flax-0.8.0-py3-none-any.whl")
    version("0.7.5", sha256="bb8cf313e4935089e222fe676e09ea96e9b4d2f9ad355f8acff37c2ca5640d08", url="https://pypi.org/packages/95/a6/5017385e65dee7609250f1dc20c3874289afdf57212e65b7f26411c4313b/flax-0.7.5-py3-none-any.whl")
    version("0.7.4", sha256="84fbcdd70b993bc4a307a140d68d5923d24baadda317ac73d2144977f0ec7d54", url="https://pypi.org/packages/5c/69/6aaa77d3fa3599d64527196e0b231476fa2cffc4995675974e22d9df83e9/flax-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="abf0cf4e7dd808ae6a14e3d9f907c5eb417bf0a840f97b3ebf533fc1af60fc21", url="https://pypi.org/packages/32/b7/ac5df3a697fedf846f5d8f322bc998e087989ece1783bae9d26fe78c97e5/flax-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="261c7b93e6d15ad80e2cedd2edb797d41b0b3c7805a54254de72a2366dc80148", url="https://pypi.org/packages/72/a7/147bd0682ff39a4e59352506a7d858e1e003f05a2d96e431fabb8a5491e4/flax-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="b2898444668d5b1cc8fc8a1546bd2d0ba4ab761fc6185a7f15bbf3a8973d83ff", url="https://pypi.org/packages/5d/95/c298b0be5d6f16258e422d176788d16fe0ebeabcbd407b259d29644af66b/flax-0.7.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.7.4:")
        depends_on("py-jax@0.4.19:", when="@0.7.5:")
        depends_on("py-jax@0.4.2:", when="@0.6.5:0.7.4")
        depends_on("py-jaxlib", when="@:0.1.0-rc1")
        depends_on("py-matplotlib", when="@:0.6.6")
        depends_on("py-msgpack")
        depends_on("py-numpy@1.26.0:", when="@0.7.5: ^python@3.12:")
        depends_on("py-numpy@1.23.2:", when="@0.7.5: ^python@3.11:")
        depends_on("py-numpy@1.22.0:", when="@0.7.5:")
        depends_on("py-numpy@1.12.0:", when="@0.1.0-rc2:0.7.4")
        depends_on("py-optax", when="@0.3.4:")
        depends_on("py-orbax-checkpoint", when="@0.6.9:")
        depends_on("py-pyyaml@5.4.1:", when="@0.5.2:")
        depends_on("py-rich@11.1:", when="@0.6.1:")
        depends_on("py-tensorstore", when="@0.5.3:0.5,0.6.2:")
        depends_on("py-typing-extensions@4.2:", when="@0.7.3:")
        depends_on("py-typing-extensions@4.1.1:", when="@0.4.2:0.7.2")
    # END DEPENDENCIES

