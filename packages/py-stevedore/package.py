# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStevedore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.2.0", sha256="1c15d95766ca0569cad14cb6272d4d31dae66b011a929d7c18219c176ea1b5c9", url="https://pypi.org/packages/eb/f1/c7c6205c367c764ee173537f7eaf070bba4dd0fa11bf081813c2f75285a3/stevedore-5.2.0-py3-none-any.whl")
    version("5.1.0", sha256="8cc040628f3cea5d7128f2e76cf486b2251a4e543c7b938f58d9a377f6694a2d", url="https://pypi.org/packages/4b/68/e739fd061b0aba464bef8e8be48428b2aabbfb3f2f8f2f8ca257363ee6b2/stevedore-5.1.0-py3-none-any.whl")
    version("5.0.0", sha256="bd5a71ff5e5e5f5ea983880e4a1dd1bb47f8feebbb3d95b592398e2f02194771", url="https://pypi.org/packages/41/1b/bad9124b400334d48aed1e04799032909fd8f1ca4a8e0eb30841284dd489/stevedore-5.0.0-py3-none-any.whl")
    version("4.1.1", sha256="aa6436565c069b2946fe4ebff07f5041e0c8bf18c7376dd29edf80cf7d524e4e", url="https://pypi.org/packages/74/a3/72792236f981aee8bb1ef15e72a6f65444150834830f6a97178fe1e2cdf4/stevedore-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="3b1cbd592a87315f000d05164941ee5e164899f8fc0ce9a00bb0f321f40ef93e", url="https://pypi.org/packages/1e/ec/147ee629ff89cef1184293682a9a97ffeeef87daa180ce788b8980bbe8fd/stevedore-4.1.0-py3-none-any.whl")
    version("4.0.2", sha256="33a5da8b622bbe67766849496ec317bf6679b330e25a335de7c95c2ad5ff3a43", url="https://pypi.org/packages/91/13/8cf16a66d5da4d2061b79195d62414ff24d28ae70faabf146616a57c26b8/stevedore-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="01645addb67beff04c7cfcbb0a6af8327d2efc3380b0f034aa316d4576c4d470", url="https://pypi.org/packages/60/3f/3c89c6041460f06c83dcbd5992f796e9c034312558c935dd73226aa250f2/stevedore-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="87e4d27fe96d0d7e4fc24f0cbe3463baae4ec51e81d95fbe60d2474636e0c7d8", url="https://pypi.org/packages/d5/f7/7593812b0687e8aaf01b10f7f07bf59e5a6bbfcd9d657cefdeb48a72cd06/stevedore-4.0.0-py3-none-any.whl")
    version("3.5.2", sha256="fa2630e3d0ad3e22d4914aff2501445815b9a4467a6edc49387c667a38faf5bf", url="https://pypi.org/packages/6d/8d/8dbd1e502e06e58550ed16c879303f83609d52ac31de0cd6a2403186148a/stevedore-3.5.2-py3-none-any.whl")
    version("3.5.1", sha256="df36e6c003264de286d6e589994552d3254052e7fc6a117753d87c471f06de2a", url="https://pypi.org/packages/77/c9/9b0861a906b214932f83cee9d4ec4e06c9e8dcfc79606d96a993b01f6f0b/stevedore-3.5.1-py3-none-any.whl")
    version("3.5.0", sha256="a547de73308fd7e90075bb4d301405bebf705292fa90a90fc3bcf9133f58616c", url="https://pypi.org/packages/7a/bc/fcce9e50da73ea23af6d236e05e15db8a02da1099a5e0a479451bcea3833/stevedore-3.5.0-py3-none-any.whl")
    version("1.28.0", sha256="e3d96b2c4e882ec0c1ff95eaebf7b575a779fd0ccb4c741b9832bed410d58b3d", url="https://pypi.org/packages/17/6b/3b7d6d08b2ab3e5ef09e01c9f7b3b590ee135f289bb94553419e40922c25/stevedore-1.28.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pbr@2:2.0,3:", when="@1.22:")
        depends_on("py-six@1.10:", when="@1.28:1")
    # END DEPENDENCIES

