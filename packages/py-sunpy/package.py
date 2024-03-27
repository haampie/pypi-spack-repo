##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySunpy(PythonPackage):
    version("5.1.1", sha256="9367ec9af2a397fcd59638b2007208d4eeaf9ed24e3e8dc2596c26b1896c2e1f", url="https://pypi.org/packages/d9/92/7123c9d3e721f069c493cdebb453aea7db393990e8f735d3aad901ea10b6/sunpy-5.1.1.tar.gz")
    version("5.1.0", sha256="0b95272a9d04ab3c521d3a247522667c838c048eb25e95926b34f17122ce22f2", url="https://pypi.org/packages/db/de/aead1cc2d1d2d06b73c1ca6f12d8b0747b2fe8158e61c7f18768b9a39f16/sunpy-5.1.0.tar.gz")
    version("5.0.3", sha256="507791e9d1f3ad698d708a8cfad144436f6031d67c33490cf6cab096638282f9", url="https://pypi.org/packages/96/53/596219fdf86183e3cfe13ec64a8b37ab8a2b9fabb465bf3972aa1bebe474/sunpy-5.0.3.tar.gz")
    version("5.0.2", sha256="7d5f93142a5d4de49457cf0b59708e9759d2b37ef2d0dd8f34a3b6a03f506470", url="https://pypi.org/packages/27/3d/841938b7217cfbc3305a8ce66f2c24737672e942d32d542566ae600e2462/sunpy-5.0.2.tar.gz")
    version("5.0.1", sha256="eed9b2cb0c9f430d53f6aaf951b3c7fca47e0269a149a1ee9e479419128397e4", url="https://pypi.org/packages/44/46/074648082d12d73a6dec48dd6a381fa7c0a3389dfa7b59d0bf506fdb5653/sunpy-5.0.1.tar.gz")
    version("5.0.0", sha256="d5c33a048ce03ece2afdb3f869ce74cc0b36891c08c074dce2d7a0af10f3e5f0", url="https://pypi.org/packages/75/50/846a87dbea1a0eceb911182417af674b8ec983f854ace66cc47975639c58/sunpy-5.0.0.tar.gz")
    version("4.1.7", sha256="51e5a312c69f21b4f05eeb15749cddfa843144b27d773ebee7ce1c748ef29230", url="https://pypi.org/packages/5d/fc/aedad27be5062a4c147f073ef58440487a2ff819c0ad40ce6553968b8f94/sunpy-4.1.7.tar.gz")
    version("4.1.6", sha256="a5ec2891a1f937cd3d331abd42c5fe63347c46570537caf30c08a4970036f631", url="https://pypi.org/packages/fb/2a/e65163c998a136783bc6418fe3469761ebcc009621c3ed6d4335083ceab1/sunpy-4.1.6.tar.gz")
    version("4.1.5", sha256="f5ceabbb665c52e663bea3de30fcd04eda28e262733079748ab2b0ac7704afc8", url="https://pypi.org/packages/12/26/637029bcc7f19bb091101d26facbbed9aaba6b9ecae326a00fd195e45c15/sunpy-4.1.5.tar.gz")
    version("4.1.4", sha256="b5aca6b3f17381f66fabe43f09fa0ef28ec2edd7f58bc2353be2e5a50d031112", url="https://pypi.org/packages/20/70/13f19d2500791de28736161a85f8876207b738c5c2698ea6a1321362f320/sunpy-4.1.4.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@5:")
        depends_on("py-astropy@5.0.6:5.1-rc1,5.1.1:", when="@5.0.1:")
        depends_on("py-numpy@1.21.0:", when="@5.0.1:")
        depends_on("py-packaging@19:", when="@5.0.1:")
        depends_on("py-parfive@2.0.0:+ftp", when="@5.0.1:")

