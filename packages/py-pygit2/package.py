##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygit2(PythonPackage):
    version("1.14.1", sha256="ec5958571b82a6351785ca645e5394c31ae45eec5384b2fa9c4e05dde3597ad6", url="https://pypi.org/packages/f0/5e/6e05213a9163bad15489beda5f958500881d45889b0df01d7b8964f031bf/pygit2-1.14.1.tar.gz")
    version("1.14.0", sha256="f529ed9660edbf9b625ccae7e51098ef73662e61496609009772d4627a826aa8", url="https://pypi.org/packages/7b/3c/697dbc6b7b27f599ea96fbe0cd59bc4bed05652372a550d59990ab460096/pygit2-1.14.0.tar.gz")
    version("1.13.3", sha256="0257c626011e4afb99bdb20875443f706f84201d4c92637f02215b98eac13ded", url="https://pypi.org/packages/09/50/f0795db653ceda94f4388d2b40598c188aa4990715909fabcf16b381b843/pygit2-1.13.3.tar.gz")
    version("1.13.2", sha256="75c7eb86b47c70f6f1434bcf3b5eb41f4e8006a15cee6bef606651b97d23788c", url="https://pypi.org/packages/68/ac/268a23daedfaaaa54da8eceedb5ad1e425d9e6dd3cf5c5ffc170ff403d33/pygit2-1.13.2.tar.gz")
    version("1.13.1", sha256="d8e6d540aad9ded1cf2c6bda31ba48b1e20c18525807dbd837317bef4dccb994", url="https://pypi.org/packages/73/05/cb50b5eb86fd67e36a6711fd41ef19bd614e95c5f37b28550407b100871a/pygit2-1.13.1.tar.gz")
    version("1.13.0", sha256="6dde37436fab14264ad3d6cbc5aae3fd555eb9a9680a7bfdd6e564cd77b5e2b8", url="https://pypi.org/packages/82/08/77f77ec32b6d1363082be00c572f970d2a6200abf42df6d6ca86b8cd30e3/pygit2-1.13.0.tar.gz")
    version("1.12.2", sha256="56e85d0e66de957d599d1efb2409d39afeefd8f01009bfda0796b42a4b678358", url="https://pypi.org/packages/db/26/cd0d68706e9511ca07b10d53f42e70d4c57b3504f4a0fd675e4617ad7a60/pygit2-1.12.2.tar.gz")
    version("1.12.1", sha256="8218922abedc88a65d5092308d533ca4c4ed634aec86a3493d3bdf1a25aeeff3", url="https://pypi.org/packages/48/6b/1c20d9adf9906e699bdb505322b27c71e12d7250d8454ae88dcecdf10296/pygit2-1.12.1.tar.gz")
    version("1.12.0", sha256="e9440d08665e35278989939590a53f37a938eada4f9446844930aa2ee30d73be", url="https://pypi.org/packages/7f/00/075f21ae474fcef679ba1f71b9ecd534493792b508b1919021fb2be67eba/pygit2-1.12.0.tar.gz")
    version("1.11.1", sha256="793f583fd33620f0ac38376db0f57768ef2922b89b459e75b1ac440377eb64ec", url="https://pypi.org/packages/43/9a/f4375f39d2de971750a7c16bd7ab9cc53368f395edaac59b32e9b3f62ce9/pygit2-1.11.1.tar.gz")
    version("1.6.0", sha256="7aacea4e57011777f4774421228e5d0ddb9a6ddb87ac4b542346d17ab12a4d62", url="https://pypi.org/packages/1d/e6/54e1b5001ddca917727ddf84c95028cc724697a040a32d361b7774dba4d4/pygit2-1.6.0.tar.gz")
    version("1.4.0", sha256="cbeb38ab1df9b5d8896548a11e63aae8a064763ab5f1eabe4475e6b8a78ee1c8", url="https://pypi.org/packages/3a/42/f69de8c7a1e33f365a91fa39093f4e7a64609c2bd127203536edc813cbf7/pygit2-1.4.0.tar.gz")
    version("1.3.0", sha256="0be93f6a8d7cbf0cc79ae2f0afb1993fc055fc0018c27e2bd01ba143e51d4452", url="https://pypi.org/packages/20/02/25077cf7ac6599e0e6bd2c6836e7c7360244d2d7224d54e51218dbe00711/pygit2-1.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.14:")
        depends_on("py-cffi@1.16.0:", when="@1.13.2:")
        depends_on("py-setuptools", when="@1.13.2: ^python@3.12:")

