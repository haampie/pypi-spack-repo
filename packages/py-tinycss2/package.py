##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTinycss2(PythonPackage):
    version("1.2.1", sha256="2b80a96d41e7c3914b8cda8bc7f705a4d9c49275616e886103dd839dfc847847", url="https://pypi.org/packages/da/99/fd23634d6962c2791fb8cb6ccae1f05dcbfc39bce36bba8b1c9a8d92eae8/tinycss2-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="9f16c0a652838606c50b1b660c2021df608d9f7ec5a21673d8a35b0dad1b1718", url="https://pypi.org/packages/2c/3a/16fa98f2d715df015f5c6a4a61bdadc40c48fbef0efc76579217ec13fd54/tinycss2-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="fe794ceaadfe3cf3e686b22155d0da5780dd0e273471a51846d0a02bc204fec8", url="https://pypi.org/packages/53/7b/5dba39bf0572f1f28e2844f08f74a73482a381de1d1feac3bbc6b808051e/tinycss2-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="0353b5234bcaee7b1ac7ca3dea7e02cd338a9f8dcbb8f2dcd32a5795ec1e5f9a", url="https://pypi.org/packages/65/f7/63bf697a7c7257d304269b49f1be3dfe429856889e93963d6f5790d77d82/tinycss2-1.1.0-py3-none-any.whl")
    version("1.0.2", sha256="9fdacc0e22d344ddd2ca053837c133900fe820ae1222f63b79617490a498507a", url="https://pypi.org/packages/94/2c/4e501f9c351343c8ba10d70b5a7ca97cdab2690af043a6e52ada65b85b6b/tinycss2-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="060f852771c197c0aecc22a0ab838e079bd5d007ac0c3c8c9b04e2969dbf5d6f", url="https://pypi.org/packages/78/61/3a081f065eb715410e240a2b84d0c315859f71688de117c9a115a4bf2735/tinycss2-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="7a7c09ff9f3bd71772de87ba3984e216a18261b889f9b9b6f2942140f17c94fa", url="https://pypi.org/packages/af/af/19883a42f570332bdd09cb7134a4975d59b4a8d418d46dc0730267aa3efa/tinycss2-1.0.0-py3-none-any.whl")
    version("0.6.1", sha256="7c53c2c0e914c7711c295b3101bcc78e0b7eda23ff20228a936efe11cdcc7136", url="https://pypi.org/packages/d2/d7/1d49d80b6e5f656719985a3d03039c7f67be72ad7765437d4c3e44f1f556/tinycss2-0.6.1.tar.gz")
    version("0.6.0", sha256="564479dd979ffc9bd3ef80df471f80f7719e40a3b4833e3e5bad4d032e0cffb0", url="https://pypi.org/packages/85/29/df7ee69f983c9ceb864c1815286fcfe8838438f2bd72b4839a8eff4481a9/tinycss2-0.6.0.tar.gz")
    version("0.5", sha256="fea8a5100bf8a49f518113769cb22639f6de8bb1016e36616cea9812050e6919", url="https://pypi.org/packages/0e/a7/ec16040eff730de7f3d2af3747afdceb2fb6aae4cfdfbe36e0674e4cce8e/tinycss2-0.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-setuptools@39.2:", when="@1:1.0")
        depends_on("py-webencodings@0.4:", when="@1:")
