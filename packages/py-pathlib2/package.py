# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathlib2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.3.7.post1", sha256="5266a0fd000452f1b3467d782f079a4343c63aaa119221fbdc4e39577489ca5b", url="https://pypi.org/packages/09/eb/4af4bcd5b8731366b676192675221c5324394a580dfae469d498313b5c4a/pathlib2-2.3.7.post1-py2.py3-none-any.whl")
    version("2.3.7.post0", sha256="560330faa6a3a8993ba016ee5cb5a995bd66101e33c73f44e83e3fb12228421f", url="https://pypi.org/packages/59/b7/6cb6e5cb66d934b9f3d51761ceb4a52bcdd4446048b9107e7ebb60b8a04c/pathlib2-2.3.7.post0-py2.py3-none-any.whl")
    version("2.3.7", sha256="aa175e519a843b93bdbbe894b512192480d22620800c6a162fd297a6644259ec", url="https://pypi.org/packages/b9/be/c3f055e15009e16e80e606b2c6229770dd0741c3d64747b3691259d6f35a/pathlib2-2.3.7-py2.py3-none-any.whl")
    version("2.3.6", sha256="3a130b266b3a36134dcc79c17b3c7ac9634f083825ca6ea9d8f557ee6195c9c8", url="https://pypi.org/packages/76/67/dc02c72177ec79f0176e5bf9921e9c1745a381ed556afb3b3ecc2bb8ba2e/pathlib2-2.3.6-py2.py3-none-any.whl")
    version("2.3.5", sha256="0ec8205a157c80d7acc301c0b18fbd5d44fe655968f5d947b6ecef5290fc35db", url="https://pypi.org/packages/e9/45/9c82d3666af4ef9f221cbb954e1d77ddbb513faf552aea6df5f37f1a4859/pathlib2-2.3.5-py2.py3-none-any.whl")
    version("2.3.4", sha256="2156525d6576d21c4dcaddfa427fae887ef89a7a9de5cbfe0728b3aafa78427e", url="https://pypi.org/packages/67/c6/4dbf5dfdbe1140cadf765c3896acc098578626c35721bc7d3eb35f6a8fc1/pathlib2-2.3.4-py2.py3-none-any.whl")
    version("2.3.3", sha256="5887121d7f7df3603bca2f710e7219f3eca0eb69e0b7cc6e0a022e155ac931a7", url="https://pypi.org/packages/2a/46/c696dcf1c7aad917b39b875acdc5451975e3a9b4890dca8329983201c97a/pathlib2-2.3.3-py2.py3-none-any.whl")
    version("2.3.2", sha256="d1aa2a11ba7b8f7b21ab852b1fb5afb277e1bb99d5dfc663380b5015c0d80c5a", url="https://pypi.org/packages/66/a7/9f8d84f31728d78beade9b1271ccbfb290c41c1e4dc13dbd4997ad594dcd/pathlib2-2.3.2-py2.py3-none-any.whl")
    version("2.3.0", sha256="db3e43032d23787d3e9aec8c7ef1e0d2c3c589d5f303477661ebda2ca6d4bfba", url="https://pypi.org/packages/74/4e/68add57f8b993bb5da70c22c7eebb4266c7b66cab15095a1578cc6a62b1a/pathlib2-2.3.0-py2.py3-none-any.whl")
    version("2.2.1", sha256="31b7bac38144612b18fb55adc4285e34a766ae64fdb1200c72e0b0cdd632ef4b", url="https://pypi.org/packages/a4/ec/cf874077622c302317753c06f6cbead4ed9fb9db0aff73268d67301d6250/pathlib2-2.2.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="24e0b33e1333b55e73c9d1e9a8342417d519f7789a9d3b440f4acd00ea45157e", url="https://pypi.org/packages/b8/1b/02efe53150500722d1b5bbe3d9dd5a417fe07df05566595cf9114ced3c39/pathlib2-2.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.13:", when="@2.3.7.post:2.3.7.post0")
        depends_on("py-six", when="@2.3.2:")
    # END DEPENDENCIES

