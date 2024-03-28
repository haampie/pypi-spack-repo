# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBitstring(PythonPackage):
    # BEGIN VERSIONS
    version("4.2.0-beta1", sha256="86c864378f3296f32c7a8de84e9c6de0cb1574c6bcfc1778d15d22a9b81ac59a", url="https://pypi.org/packages/78/b7/f5b4d4519d1764dc93562f5b0b9d2acbbc8fdd1ca61b6b2a33a6d2547fcd/bitstring-4.2.0b1-py3-none-any.whl")
    version("4.1.4", sha256="da46c4d6f8f3fb75a85566fdd33d5083ba8b8f268ed76f34eefe5a00da426192", url="https://pypi.org/packages/33/c3/4ceb28a082f94f83425bfebbf7aa667a0d0e357015ffd7ff201ae4976308/bitstring-4.1.4-py3-none-any.whl")
    version("4.1.3", sha256="5619b9d6a4939717962b0fecb0034ad30277606b8b0bcce3f7cd6ac2400f6427", url="https://pypi.org/packages/64/34/901737226e0f48972e43c8ef23820a1195b14a8e9dbdf46bc5b8035c43b1/bitstring-4.1.3-py3-none-any.whl")
    version("4.1.2", sha256="bc0dbdb282099d5c6fbf995cd7261449ddeb7bbf042996e503471a35eb2efaa3", url="https://pypi.org/packages/59/bc/bbc41ad3546f23855a2c21dc6afcd8b148ccec2e51a5af145199abfa4b9e/bitstring-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="13a07c63a2901a5572638d4917a2e7ea539df6bfe49aeb1c56949117fda943fa", url="https://pypi.org/packages/f8/36/e0053ec177e193d719455d3d74877a075b1b58addd50b853b738a687aa3c/bitstring-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="306f46275e7fac46d44fc5e2dd68e6c607981903f5ecff3987723f8483f5b3de", url="https://pypi.org/packages/3f/d8/f6643826878c9ecad32e888a8903042977ffe8a49524861bfe758e315770/bitstring-4.1.0-py3-none-any.whl")
    version("4.0.2", sha256="f93893791e8a6ecb02adcc5c191aaa964a06a9e1449e326cfb4f49ff5198e588", url="https://pypi.org/packages/d7/88/fab0e30b4cefc5f534fd277a01591376dfee1f80cd214f780cc4aeb07378/bitstring-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="4a27cdefd95eb535c4b79e0afcdb5532ba1dba0aaed98a31ad98f46b1e0d5bd9", url="https://pypi.org/packages/1b/07/951d7bc9804fcec26e8cdbf1d352018a21c16194d42e3f38cb7f5564ca4b/bitstring-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="cfa8d0561412c358e9118fd93c7200c4b6e2f253c08a7eb1a01f59d5fc337b66", url="https://pypi.org/packages/b7/f8/e0f61c9ef0f76760400738bd46608b004d858cc016756d0b09d06bb2a30d/bitstring-4.0.0-py3-none-any.whl")
    version("3.1.9", sha256="0de167daa6a00c9386255a7cac931b45e6e24e0ad7ea64f1f92a64ac23ad4578", url="https://pypi.org/packages/49/fa/ac153ef3c9668a093f33386edf7a20122962e9142b1105fbe2a4a4262785/bitstring-3.1.9-py3-none-any.whl")
    version("3.1.5", sha256="c163a86fcef377c314690051885d86b47419e3e1770990c212e16723c1c08faa", url="https://pypi.org/packages/f3/e5/dfe4c49c93d174a5fd807ed307d3a3f38c6b3e140972945f81a5f5578ca7/bitstring-3.1.5.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bitarray@2.9:", when="@4.2:")
        depends_on("py-bitarray@2.8:", when="@4.1.1:4.1")
        depends_on("py-bitarray@2.8:2.8.0", when="@4.1.0")
    # END DEPENDENCIES

