##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColorlog(PythonPackage):
    version("6.8.2", sha256="4dcbb62368e2800cb3c5abd348da7e53f6c362dda502ec27c560b2e58a66bd33", url="https://pypi.org/packages/f3/18/3e867ab37a24fdf073c1617b9c7830e06ec270b1ea4694a624038fc40a03/colorlog-6.8.2-py3-none-any.whl")
    version("6.8.0", sha256="4ed23b05a1154294ac99f511fabe8c1d6d4364ec1f7fc989c7fb515ccc29d375", url="https://pypi.org/packages/95/df/520663eb7f7a329f7c585834b754bcc3cbcc03957d85fcbba4a2a723ad9d/colorlog-6.8.0-py3-none-any.whl")
    version("6.7.0", sha256="0d33ca236784a1ba3ff9c532d4964126d8a2c44f1f0cb1d2b0728196f512f662", url="https://pypi.org/packages/58/43/a363c213224448f9e194d626221123ce00e3fb3d87c0c22aed52b620bdd1/colorlog-6.7.0-py2.py3-none-any.whl")
    version("6.6.0", sha256="351c51e866c86c3217f08e4b067a7974a678be78f07f85fc2d55b8babde6d94e", url="https://pypi.org/packages/7d/54/e24efe5469ecb2710112055de87a2900e9494810bcfc25c12c7a0723eb64/colorlog-6.6.0-py2.py3-none-any.whl")
    version("6.5.0", sha256="d334b1b8dae5989b786232f05586a7a0111feb24ff9cfc8310c3347a91388717", url="https://pypi.org/packages/19/11/6daf005ecf7e00ec431f369b79029cd4a7bf47121a891f8a72be8f2b4bcb/colorlog-6.5.0-py2.py3-none-any.whl")
    version("6.4.1", sha256="b13da382156711f7973bf7cbd1f40ea544aff51fde5dc3fb8f3fa602c321d645", url="https://pypi.org/packages/2d/93/4b0bb101e54206e92feb3c986c274902212b2ed8c55423e6e7f6d8b693ca/colorlog-6.4.1-py2.py3-none-any.whl")
    version("6.4.0", sha256="590f19b065f34671d8f19b294b0f7ea6f13d09e7f7bf2993326edb008cfa1152", url="https://pypi.org/packages/c4/a9/014dbada072074c94ed00c46ffe2d02a1536f2c0f30ce4157027d1c4cfd9/colorlog-6.4.0-py2.py3-none-any.whl")
    version("5.0.1", sha256="4e6be13d9169254e2ded6526a6a4a1abb8ac564f2fa65b310a98e4ca5bea2c04", url="https://pypi.org/packages/32/e6/e9ddc6fa1104fda718338b341e4b3dc31cd8039ab29e52fc73b508515361/colorlog-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="0174f5340d854788afcc19813a0e8fe42897d6f1022bea05e10216dd61d82c0b", url="https://pypi.org/packages/68/f4/82f1a2415634e3e0aa20a78e8890e4b468e8ae5cf82ef7f612c5c8aab50a/colorlog-5.0.0-py2.py3-none-any.whl")
    version("4.8.0", sha256="3dd15cb27e8119a24c1a7b5c93f9f3b455855e0f73993b1c25921b2f646f1dcd", url="https://pypi.org/packages/51/62/61449c6bb74c2a3953c415b2cdb488e4f0518ac67b35e2b03a6d543035ca/colorlog-4.8.0-py2.py3-none-any.whl")
    version("4.0.2", sha256="450f52ea2a2b6ebb308f034ea9a9b15cea51e65650593dca1da3eb792e4e4981", url="https://pypi.org/packages/68/4d/892728b0c14547224f0ac40884e722a3d00cb54e7a146aea0b3186806c9e/colorlog-4.0.2-py2.py3-none-any.whl")
    version("3.1.4", sha256="8b234ebae1ba1237bc79c0d5f1f47b31a3f3e90c0b4c2b0ebdde63a174d3b97b", url="https://pypi.org/packages/69/eb/58ae10d3c46a0195ffdd0e3943d255d0d5029d71e5457785ecd665bcf0f3/colorlog-3.1.4-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-colorama", when="@3.1.4: platform=windows")

