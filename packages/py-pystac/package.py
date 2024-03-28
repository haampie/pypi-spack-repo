# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPystac(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.9.0", sha256="64d5654166290169ad6ad2bc0d5337a1664ede1165635f0b73b327065b801a2f", url="https://pypi.org/packages/2a/34/190016e443ff35ed24efacc810b0ae5d770022e8d3fb460608c0764f6c6d/pystac-1.9.0-py3-none-any.whl")
    version("1.8.4", sha256="0d9917bf3abc71fca3edfb2dd5f66be44b22a63774cda520c81484a126fa780e", url="https://pypi.org/packages/d9/33/528355f091d6522e5f11e02b1309cb4713e21ef8f772dd9b38e8276da011/pystac-1.8.4-py3-none-any.whl")
    version("1.8.3", sha256="91805520b0b5386db84aae5296dc6d4fb6754410c481d0a00a8afedc3b4c75d5", url="https://pypi.org/packages/d2/35/efb3ada4f8db776144d786338a41d38e5128f2c1e4a86b681c658fe1151e/pystac-1.8.3-py3-none-any.whl")
    version("1.8.2", sha256="676de097aabe24f4d5bc9dfb9f49c40ce2f4e8a8578e0fe4c1130d65e1fb6072", url="https://pypi.org/packages/d2/e7/cbf54bd764999d5bcc09d17d7a8de08ce22fbcb8cbe934deb0e3cafb1778/pystac-1.8.2-py3-none-any.whl")
    version("1.8.1", sha256="7471847304db43bb82396e57540ed0008d5e18882deff40dc553d6dff72e921f", url="https://pypi.org/packages/08/e4/3e66e30c9c76cb0ac4328af498dd3e900fd7a63bc31edc8323e21c2abe61/pystac-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="80e148b92350c06c8e59ff26858d3d37d4b0542ba139839e22130f582edbbf91", url="https://pypi.org/packages/ad/0f/8a464eaf649334bb4d519db8108e11756529e79217475a5bbebbea8b2cce/pystac-1.8.0-py3-none-any.whl")
    version("1.7.3", sha256="2b1b5e11b995e443376ca1d195609d95723f690c8d192604bc00091fcdf52e4c", url="https://pypi.org/packages/75/96/32e0c1996d8bf689b939b27fd1a2ecc0f3b77fa33bba38d3d73a3cd41c04/pystac-1.7.3-py3-none-any.whl")
    version("1.7.2", sha256="29c6f053741e2fb942502e33a3c61b5217a286838c50e66ccd06be82fd6bd664", url="https://pypi.org/packages/81/a2/d637c2feb8a16af73a362b0230c94ad0dcea7253719306a077e61eeedfae/pystac-1.7.2-py3-none-any.whl")
    version("1.7.1", sha256="6c81b213291fd25adca2e0e4ddcf7b111154e1a59d0d14d9f02c5df87649f164", url="https://pypi.org/packages/0b/a5/b6d612dcf2bbd14d0512b5be90851ce05d434af2f1caf3d41feaaad4299a/pystac-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="cf6a2db2385de6521c39d2655a547aa1f6a3ea4a43aa6d71994a0b475dda290f", url="https://pypi.org/packages/6a/65/633a3f4346d2394c87aa30a02360b72af6eea58a414eb8e0c5db1fd73f1e/pystac-1.7.0-py3-none-any.whl")
    version("1.4.0", sha256="7f4563ff7cad512fe687ceb0b09905e15934712ac936d51766b090600580abdd", url="https://pypi.org/packages/83/af/559781e42676f76febc5b9dc2385c1930834123c3c63b9e004a4c8c9ee52/pystac-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="8897e4621d631e85f926254837823a5c06eb8f88fea4e9201e985d727017ff49", url="https://pypi.org/packages/44/1d/cbe1f6f923ec60c8ac8c4cd81e82ee2d20a7a2f03a694d35c582f0bd7424/pystac-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="a47039e0997216d28177dfe42f74bb9297af9b0d4eb3f2aead5c27b7ee21223b", url="https://pypi.org/packages/ee/ba/45b0862bd505a211c01482a46c43bd71b1c03bd1a3d9977764b35d5dddb8/pystac-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="107e5e1646a5accac27771d110945afaa9b7e8105f3823451fbb89ecc29fb395", url="https://pypi.org/packages/c6/37/28140fa27b46285ce66751656ed07d9ae96bd12841db406900793d92bd7f/pystac-1.1.0-py3-none-any.whl")
    version("1.0.1", sha256="a22575494df7ee19fc1570555f8180b7d5e2c2efa5a355a63d572f3c323e6ce9", url="https://pypi.org/packages/9d/73/f45629060d6456cc55e74ee3ba13d0ff1637ea78f38d0bb0ea2b993f8b29/pystac-1.0.1-py3-none-any.whl")
    version("0.5.4", sha256="d617e1eef351788fcc7b856e8492c8387e883a0b2695ee17200cb85fbe1da122", url="https://pypi.org/packages/69/17/86b6e1531e1295c52d400e0a7d03b2d3a4ae75d92faec6fa00265a05ef86/pystac-0.5.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("validation", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.9:")
        depends_on("py-importlib-resources@5.12:", when="@1.8 ^python@:3.8")
        depends_on("py-jsonschema@4.18.0:", when="@1.8.4:+validation")
        depends_on("py-jsonschema@4.0.1:4.17", when="@1.8.2:1.8.3+validation")
        depends_on("py-jsonschema@4.0.1:", when="@1.6.1:1.8.1+validation")
        depends_on("py-jsonschema@3.0.0:", when="@1:1.6.0+validation")
        depends_on("py-jsonschema@3.2:3", when="@0.5.0:0+validation")
        depends_on("py-python-dateutil@2.7:", when="@0.3.1:")
    # END DEPENDENCIES

