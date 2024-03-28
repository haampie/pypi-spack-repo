# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPuremagic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.21", sha256="8fe85c05800fe1eacdd5aa943b9e7fdbee66bc41a17aacf80efd6c668c63df45", url="https://pypi.org/packages/34/cd/a96792f38675965954e7529a0c19a9320cafba2412ebf225e18eb7c2287b/puremagic-1.21-py3-none-any.whl")
    version("1.20", sha256="14817470dc1e3339356088b58576820efd12544a676c20d7d5e738ea1e06f852", url="https://pypi.org/packages/bf/b8/40b2c2a06f0ce0058f65bb82bff3cb728dabf1f6c8f628288b2cf664eab3/puremagic-1.20-py3-none-any.whl")
    version("1.15", sha256="349e179f04bcc14eb0e2c3941cd9ee4ea74881ab6ccac63ea0c37c98f7a80b22", url="https://pypi.org/packages/de/b6/8c4d331d55d8a6cbdaadcd3830baec7e2216c2c0fe7e6c8f4cdbe737dd52/puremagic-1.15-py3-none-any.whl")
    version("1.14", sha256="40e32752827f2d0cea7e6f11454fab2b4bd440582af83d8a47bf403ab42364fa", url="https://pypi.org/packages/14/20/c05ea76f4448c483f1c4486504bd6d98adeefb7ef597190f76d599ef8a5e/puremagic-1.14-py3-none-any.whl")
    version("1.13", sha256="e833cab04f8e3bf9aa1308f99b23bbc98db008890f16486765f67f247fe36405", url="https://pypi.org/packages/79/fc/14c5994f438844e6f91161fb9b101b4516b2761871540a59785814923f67/puremagic-1.13-py3-none-any.whl")
    version("1.12", sha256="9e7ab53f8f01cc8b64309a4d46e879178e8e14720803dbc4b56e481ec9cafb08", url="https://pypi.org/packages/64/cc/8f048b7559728c25a86cbcf4cb05f2d6fd00bb3242dc2635e5d25cfb41bf/puremagic-1.12-py3-none-any.whl")
    version("1.11", sha256="ade41779af2182d80b484ce36ca3e1d427d544b2b735ee6c63f007d32e3871dc", url="https://pypi.org/packages/33/2f/9a1b5970f5575ae8fbf622efc7f816a2dad3b6e43af8175e9f9d084adc60/puremagic-1.11-py3-none-any.whl")
    version("1.10", sha256="3603ac88bfa06689b4a3a2e90ef30f8cc5769df2f269bf546620bfe6b18c06d6", url="https://pypi.org/packages/d5/6e/62d1cef9a0d8edf2d9c44b0a1b91b0b29b66fb693c94af278a0c76ddfd8c/puremagic-1.10-py3-none-any.whl")
    version("1.9", sha256="563d16453ce9ebfdd919f0dc3908ae5d681345e81fcc6e7e13d9a27a0bb9532e", url="https://pypi.org/packages/bb/f8/e44acc4960629fb05f4d1318fb3b6b737a372fbdcf62496b047503a097ea/puremagic-1.9-py3-none-any.whl")
    version("1.8", sha256="af43d5abfc0139e0abe251d902e33218bdfe1fadefd025a1c2c308d51e149e17", url="https://pypi.org/packages/92/7f/db327a1e8c154130ecd7c35e7bd6cdf8cd36f9e9a8abf1fcfe57e0359860/puremagic-1.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-argparse", when="@1.4:1.10")
    # END DEPENDENCIES

