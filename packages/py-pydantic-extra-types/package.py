##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydanticExtraTypes(PythonPackage):
    version("2.6.0", sha256="d291d521c2e2bf2e6f11971caf8d639518124ae26a76d2e712599e98c4ef2b2b", url="https://pypi.org/packages/ce/1a/01022dfb43fdd74328e3ef7ac2922b9c03961bbc5bce985563d941e1bba7/pydantic_extra_types-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="7346873019cac32061b471adf2cdac711664ddb7a6ede04219bed2da34888c4d", url="https://pypi.org/packages/d2/1e/8c9021519140f813a6b4d78cd4257b3290c559859bf96a858936acc2e78a/pydantic_extra_types-2.5.0-py3-none-any.whl")
    version("2.4.1", sha256="b3cec735e471b1234a1cc05a680dc080836bab6970cab40d60dcade97fe68f5d", url="https://pypi.org/packages/ed/38/a4e7f932ac53037107562c244990ab985db73a3d3247092d380f29ac780a/pydantic_extra_types-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="f681b6f6c91f386de4193d0827d61ff0631c79bb4bc8819ebb1ba3753fd84586", url="https://pypi.org/packages/c8/f9/58d77ebf576b99cc49d8c1168bddd9bf4dcd9609363c2e6670b4d22b2ca5/pydantic_extra_types-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="899043975a7f17ec85dc75e3328b832e1ef9414e0a495a9f420850c4d9d85b5a", url="https://pypi.org/packages/fc/ba/b22791887a4bf57f09a4671618d16e5a1adf619c927dd75aeaba906c4daa/pydantic_extra_types-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="d4c6bcab0ea4b5300075ae7a664c134d923ac35496ad8caa0feae30234f14756", url="https://pypi.org/packages/86/4b/add7a9b1bd0ca9b283bd7341bb9248d81c05cae762f43ed09a0b1da7921c/pydantic_extra_types-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="1b8aa83a2986b0bc6a7179834fdb423c5e0bcef6b2b4cd9261bf753ad7dcc483", url="https://pypi.org/packages/cc/a8/ec9c44384336c6b1b4c2c59a486fdd9204db8a3115a8d9021a8929fdfe3c/pydantic_extra_types-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="63e5109f00815e71fff2b82090ff0523baef6b8a51889356fd984ef50c184e64", url="https://pypi.org/packages/b8/d6/99c67e1c3d4ba74b79e6b2d36b59149b63e4a8fa61726cc3f5feb0b6560e/pydantic_extra_types-2.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pydantic@2.5.2:", when="@2.3:")
        depends_on("py-pydantic@2.0.3:", when="@2.1:2.2")
        depends_on("py-pydantic@2.0-beta3:", when="@2:2.0")

