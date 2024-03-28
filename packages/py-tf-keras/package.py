# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTfKeras(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.16.0", sha256="b2ad0541fa7d9e92c4b7a1b96593377afb58aaff374299a6ca6be1a42f51d899", url="https://pypi.org/packages/75/aa/cf09f8956d4f276f655b13674e15d8d6015fd832f9689aa9ff2a515781ab/tf_keras-2.16.0-py3-none-any.whl")
    version("2.16.0-rc4", sha256="436c40bf857d76c442fc339aa848b4f8f75f2ef3ed74574d393e9d5d51518ea0", url="https://pypi.org/packages/1a/e2/c16d1aa11c09174be906c12b56def0c6ab99ff3ce6d5af1c1491d9c032e7/tf_keras-2.16.0rc4-py3-none-any.whl")
    version("2.16.0-rc3", sha256="414c4af1ae49341214d779c654d206782c33dd7ab6e01a84dcc045626939bda8", url="https://pypi.org/packages/8e/08/62e771ffcdef084fec8f3b4b281e4074631f3132b9ece27c37cb01383d60/tf_keras-2.16.0rc3-py3-none-any.whl")
    version("2.16.0-rc2", sha256="ad3b4d4aa31a13909630c8c3d0dbd8cda9217262cda8e88d8769ce81571da45d", url="https://pypi.org/packages/26/cd/316b0c92d27a6d660f1ed298ccc852347582b356a3582fe97e958060da58/tf_keras-2.16.0rc2-py3-none-any.whl")
    version("2.16.0-rc1", sha256="1c5b738ef33c75fdec25d4cf10befc4ac2983eb7c324b36405271823e8189a65", url="https://pypi.org/packages/4c/90/f96b3b02a6e66eacb78fcd731740de3fffa6a2560a9d4ea5ed1bdf1dd1f4/tf_keras-2.16.0rc1-py3-none-any.whl")
    version("2.16.0-rc0", sha256="0c7020455aafe6ab5a7f235f2132053ad58c1729e84f930cda42f9d7ec4deebd", url="https://pypi.org/packages/8b/66/5d3d1f287418b8336caa23e0dcb0c99e68f85ed606a05ac6e8e1df5128e7/tf_keras-2.16.0rc0-py3-none-any.whl")
    version("2.15.1", sha256="8beaef46b8b4f1158de1410e7c0cf82f008b9e8c4ab3443f54ac1aaef9c2ad74", url="https://pypi.org/packages/6f/23/6fd9aab5b7ef9e5614b94edce48d92db9d38d2bd2d00ef2c7a6f82a00588/tf_keras-2.15.1-py3-none-any.whl")
    version("2.15.1-rc0", sha256="2f2b607b88bc9bd575ca3910372dfe6fcf453c5117313c58ca3a2162d5d1a9cb", url="https://pypi.org/packages/1d/a1/4b2f967f851e01930541a73022c944b817eeddaef8487fa4679894ffa05b/tf_keras-2.15.1rc0-py3-none-any.whl")
    version("2.15.0", sha256="48607ee60a4d1fa7c09d6a44293a803faf3136e7a43f92df089ac094117547d2", url="https://pypi.org/packages/19/26/ca8a6cca61f2a44f1e7ee71ebdb9c8dfbc4371f418db811cdca4641f6daa/tf_keras-2.15.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.16:")
        depends_on("py-tensorflow@2.16:", when="@2.16.0-rc2:2.16.0-rc4")
        depends_on("py-tensorflow@2.16.0:", when="@2.16.0-rc1,2.16.0:")
        depends_on("py-tensorflow@2.15.0:2.15", when="@2.15.1:2.15")
        depends_on("py-tensorflow@2.15", when="@2.15.1-rc0")
    # END DEPENDENCIES

