##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkClasskit(PythonPackage):
    version("10.2", sha256="252e47e3284491e48000d4d87948b31e396aaa78eaf2447ba03a71f4b97cb989", url="https://pypi.org/packages/03/ee/302ed4f416ded628920458b873a2eb2ac9af3900da5bee5cb80b44e37b06/pyobjc-framework-ClassKit-10.2.tar.gz")
    version("10.1", sha256="baf79b1296662525d0fa486d4488720cceebe63595765cfeade61aeb78a4216f", url="https://pypi.org/packages/a7/1d/c44bf8878f9d42d65d32be13fbd1620c835a7b86c0fd0c6a856e936391b6/pyobjc-framework-ClassKit-10.1.tar.gz")
    version("10.0", sha256="6f0c6dbba20945f515b5a3540c88d91e9c00c1af854c889fb56491179dc064be", url="https://pypi.org/packages/ab/70/52097e2e0e685b88c78c80b66af15fc592e28607ac07e2316919bdf7c356/pyobjc-framework-ClassKit-10.0.tar.gz")
    version("9.2", sha256="5378421190896375022ea8dcd5fbdd73dcc4d3c14a92b63f0a9d3d48aaa973ee", url="https://pypi.org/packages/7f/58/a7e5684dfcab8f65488336b28285db4cfc4e32174ff7cb05015c67b89315/pyobjc-framework-ClassKit-9.2.tar.gz")
    version("9.1.1", sha256="891d4c2ec0c43c00fb038315ecc8899af226dc54d1d295cc3180eeccb8665f67", url="https://pypi.org/packages/98/d6/c9a6cf43c01aa6b28d24eeb5bfd819da9e63f05677d4672f088f642b6855/pyobjc-framework-ClassKit-9.1.1.tar.gz")
    version("9.1", sha256="a0e7c36e853a37675fe8adab6a256f3a2e98be2957d5b35af67d0cac2e12f146", url="https://pypi.org/packages/1b/c5/68874d1cf5ea35d04bd723a4666c2bd1005312b3a486e3b66c3a402940e4/pyobjc-framework-ClassKit-9.1.tar.gz")
    version("9.0.1", sha256="35aa002e9d24a86e0b41edef11522ab0b5dc4336c7ddaa4951ddb0e02054fbed", url="https://pypi.org/packages/f6/c0/3f8e308bea62070679e9dd59b50c8014b33ec06cc9028151ab7dda530976/pyobjc-framework-ClassKit-9.0.1.tar.gz")
    version("9.0", sha256="e3e08f635c7b1e41294caf7b658eed65781b61a147263b3eb3b33f9e11162042", url="https://pypi.org/packages/c5/9e/96cebfaa069873ff874e70321afa9ec0c397d69146cddf144c0c0091fccb/pyobjc-framework-ClassKit-9.0.tar.gz")
    version("8.5.1", sha256="717c64a4399b034c16d420e73ddfa05ab4aca468c2a80d2e5910a8e51c298735", url="https://pypi.org/packages/f3/d8/20c8468909f9e3d6cdff74ffcf17d0ccf3b7549a2ff7661167db6179add9/pyobjc-framework-ClassKit-8.5.1.tar.gz")
    version("8.5", sha256="d65af93ab96f1c4b95c0b3379d2352a965a8f200198b440d6866beade683cde7", url="https://pypi.org/packages/b4/de/bf48df0bb1b4079fbd2700fa861a22345bd184e86b95f9f1ab7d17804513/pyobjc-framework-ClassKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

