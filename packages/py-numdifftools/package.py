# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumdifftools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.41", sha256="a8b162e06889ea73643a47b84935a63d8214d4b4b0805d36a3c28c56379b3e51", url="https://pypi.org/packages/a3/5c/37cd5db8c465db2664b2219410b8bc7743da6edb1b616b5d13008bd7cac2/numdifftools-0.9.41-py2.py3-none-any.whl")
    version("0.9.40", sha256="57bb19ba0abc914ad8373ad48a1416f186bf0a24dc677f138350b26895301d40", url="https://pypi.org/packages/7e/44/b985d36bf97ca3af694be9dee299716b97cc43a6184be7a6e831350c6cb6/numdifftools-0.9.40-py2.py3-none-any.whl")
    version("0.9.39", sha256="e3a1912a6e4d0fd655d4e2683245c385fa4a021be387781a44bc2b8c7ca60b41", url="https://pypi.org/packages/ab/c0/b0d967160ecc8db52ae34e063937d85e8d386f140ad4826aae2086245a5e/numdifftools-0.9.39-py2.py3-none-any.whl")
    version("0.9.38", sha256="7b424767b00c6ded756241d58a66533f1014dc3b68b8e09c9fe3e1f47ba8d4e9", url="https://pypi.org/packages/b7/49/73bb35191279d026d2ee6a6b1efac48fbe10e313fd692ca858efcf35c03b/numdifftools-0.9.38-py2.py3-none-any.whl")
    version("0.9.20", sha256="443b43e43c970b4f37cd2a5a57f842192da89daa2d58105ca5f5f894b7d4fcd0", url="https://pypi.org/packages/3f/b2/a492a473c3bcdfe8889986beb331e7198a718282de8c0ec8c9fec947878c/numdifftools-0.9.20-py2.py3-none-any.whl")
    version("0.9.17", sha256="c02950325718ea5a9561bd62f2a07f15c2783bfb5cae7b45526e6912f15236ce", url="https://pypi.org/packages/db/8e/135409166b022cf9ca2c6a8a45e4fcba9f5e92b870cf5b1d2f8d4e495ea4/numdifftools-0.9.17-py2.py3-none-any.whl")
    version("0.9.16", sha256="7719f57daa4803f93b26ba0958c52d6dbd718ec493e6d4c2e5f52bb1a613fb06", url="https://pypi.org/packages/de/a8/8c70355fc456d48b2d5a459b8b657894c069db20c2bd41f860b21cbafb5e/numdifftools-0.9.16-py2.py3-none-any.whl")
    version("0.9.15", sha256="28a78615e10054d0a09ba5724588dec3d3607b775dac7fe7ebcf8993f23ce8c1", url="https://pypi.org/packages/64/f7/6fa4d4c7e1416219f2f79d73450685d40d5ee8c4b394348418ed67032795/numdifftools-0.9.15-py2.py3-none-any.whl")
    version("0.9.14", sha256="0b5044f572dfad945253a7448a820505f4d37182bef5a31668911800eb1ad605", url="https://pypi.org/packages/36/5a/5f362a69c1d7b9506a3c2285fab751e8e309ec922efb60083c35908ce2e3/numdifftools-0.9.14-py2.py3-none-any.whl")
    version("0.9.13", sha256="8e61f23b904c5976c7b9ce301ef72ac0cdf1ca253b78c9f20f3f69a6cbadffc0", url="https://pypi.org/packages/cf/ce/0fd5723ed538506328d4ca2b716ed296accbcd4c5d24a70988878a631fb2/numdifftools-0.9.13-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-algopy@0.4:", when="@0.9.13:0.9.16,0.9.20,0.9.40")
        depends_on("py-numpy@1.9:", when="@0.9.13:0.9.16,0.9.20,0.9.40:")
        depends_on("py-numpydoc@0.5:", when="@0.9.13")
        depends_on("py-scipy", when="@0.9.13:0.9.16,0.9.20,0.9.40:")
        depends_on("py-setuptools@9:", when="@0.9.13:0.9.16,0.9.20")
        depends_on("py-sphinx-rtd-theme@0.1.7:", when="@0.9.13")
        depends_on("py-statsmodels@0.6.0:", when="@0.9.40")
        depends_on("py-wheel", when="@0.9.13")
    # END DEPENDENCIES

