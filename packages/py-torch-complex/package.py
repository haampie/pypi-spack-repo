##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchComplex(PythonPackage):
    version("0.4.3", sha256="283a61a65fdcfcdadb8234540c6d4a621d02832f20ab8f980f08bc4f20eec8c3", url="https://pypi.org/packages/9e/35/1ded2af76633aa9b2e875033265e6bc74e444fc8a78af48108ffe77b14cf/torch_complex-0.4.3-py3-none-any.whl")
    version("0.4.0", sha256="be6d433fdc650b8cad7541cd84748d2fa87f7ff12a5ab48cfc22e34a6e64e726", url="https://pypi.org/packages/a8/02/e71a9a411410deb452b8b23735ff1a1f15432c192628c2a4ed7c460c0372/torch_complex-0.4.0-py3-none-any.whl")
    version("0.2.1", sha256="64c3b931af0e0423f9dc26dffb94cf017aeb3d2836d966ebd0de1718cd959c10", url="https://pypi.org/packages/81/eb/2af6146200534f83f5695fefe21a61234203fb2c6bbe9d8b7ca87636fbf1/torch_complex-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="73e4b0dcd79f8db43a000b75a7bb20e414e220bb7467178e446fc17cd0392b53", url="https://pypi.org/packages/36/30/cc85a1674c70ef8f3f6c6725bf9dc0e88b727afd0c1ec36cb7f33e4c7e5d/torch_complex-0.2.0-py3-none-any.whl")
    version("0.1.2", sha256="ce070627fca13d1ae360aaf9f82a32fb354b710c904cd05fda996d788df495e5", url="https://pypi.org/packages/8f/48/dd35ecafd2cf3d69533f4eb42aad602f74dde0e004a3409c56c1cbebfab1/torch_complex-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="4930324dc2efe605145589e6893b82cd90c24da0f9e58af739c9b9fb165639b6", url="https://pypi.org/packages/9f/ee/cb1a9cb4164ec9b57b44ab53cf7fe301e8d11ca3bdac3c069ec95a9b9a25/torch_complex-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="cb3ea9a98526032f28aadefa865032484edbd37f0b4eff2eba8b19f02ddcca35", url="https://pypi.org/packages/a0/d1/5a0b58e1935019d0d6f2b5c8ee0ee384151979ca5a48906db371340e2073/torch_complex-0.1.0-py3-none-any.whl")
    version("0.0.3", sha256="8c305ccb27088a9ff551d0521975568b58cebdd0001a6a1ff1a81bc95440db86", url="https://pypi.org/packages/4b/9b/8cc15fe78872746c68a6731e837357e21ea9edc89ee5ff95b8c2b5e2a55f/torch_complex-0.0.3-py3-none-any.whl")
    version("0.0.2", sha256="173eb9709571346c3cc72221f088d2f7b11a87ac233b95e4e8a97d14cf43c4fc", url="https://pypi.org/packages/d7/99/a045d269ba0b476f8eb49a7e378caf312346fa230a59e1bf382a91149488/torch_complex-0.0.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy")

