##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFixtures(PythonPackage):
    version("4.1.0", sha256="a43a55da406c37651aa86dd1ba6c3983a09d36d60fe5f72242872c8a4eeeb710", url="https://pypi.org/packages/db/ab/3259874efafdbaa9d25dd8fa99c999621c6539eacd03c95b64a34bd5acd1/fixtures-4.1.0-py3-none-any.whl")
    version("4.0.1", sha256="d2758826400d095b79666cf93a32a84f50ff8cd179831927efb48cd1e3ca7466", url="https://pypi.org/packages/3c/3d/f106b3278ba50067e9cd397f836d33d141aa790853152dbb3512aaee19f3/fixtures-4.0.1.tar.gz")
    version("4.0.0", sha256="c579191f96a088b16095eb60e21d3eb6334f006a93e248f4decdcb6bfef238d8", url="https://pypi.org/packages/9e/e7/58f53ed1cf81bec87e79558df62a9a8650e11ac5230734a8e75c689a3980/fixtures-4.0.0-py3-none-any.whl")
    version("3.0.0", sha256="fcf0d60234f1544da717a9738325812de1f42c2fa085e2d9252d8fff5712b2ef", url="https://pypi.org/packages/84/be/94ecbc3f2487bd14aa8b44852f498086219b7cc0c8250ee65a03e2c63119/fixtures-3.0.0.tar.gz")
    version("2.0.0", sha256="287ddbab51c45cff457cb9d68b7aa8f7864b7c588273a0ab5e9a16589e50182a", url="https://pypi.org/packages/aa/af/adf71e0790f6452b0e9ade95bfa2b8ae0c6d62137028c10a144ee3ea5210/fixtures-2.0.0.tar.gz")
    version("1.4.0", sha256="3e1c61753d0fafc1429591d33ad6b828a0673a200eae63dd6ac0685479db5d36", url="https://pypi.org/packages/1c/82/d0d469110cdc92e0a79699250639afdff9f8da8a66fdfb846f48fb5e5e4f/fixtures-1.4.0.tar.gz")
    version("1.3.2.dev6", sha256="64918b2497904b515ca45e0a4a791b96bdbc53c504aee98ae22f2d0e2072d8f6", url="https://pypi.org/packages/e2/6f/21952dfb7fe7aadd6630f2be951ef564c18f4deb82f15795ea929e2ab2c4/fixtures-1.3.2.dev6.tar.gz")
    version("1.3.1", sha256="b63cf3bb37f83ff815456e2d0e118535ae9a4bf43e76d9a1cf3286041bf717ce", url="https://pypi.org/packages/ac/08/4e44a959c62ce9b007158ba29a6c0e80a8b7ddd485ab4e94277285f5097b/fixtures-1.3.1.tar.gz")
    version("1.3.0", sha256="81c43b99ee63b2849a7a07c2ddcf147dea0c36260cd71352b649397d427d8f30", url="https://pypi.org/packages/db/e5/b498aeb2c5f54916e5f0addde2b4c55e2fbe2b94e8e9bd0f4d2df2edbc92/fixtures-1.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pbr@5.7:", when="@4:4.0.0,4.1:")
        depends_on("py-testtools@2.5:", when="@4:4.0.0")

