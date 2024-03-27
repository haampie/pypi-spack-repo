##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHealpy(PythonPackage):
    version("1.16.6", sha256="0ab26e828fcd251a141095af6d9bf3dba43cec6f0f5cd48b65bf0af8f56329f1", url="https://pypi.org/packages/2a/73/d2215e43c122098daad1a666f621479cca0fd04ca89976170896d9afe03a/healpy-1.16.6.tar.gz")
    version("1.16.5", sha256="9f99cd5ed2d8791dbfcefe1552a73e550ec85b87637127938756280008d0ed29", url="https://pypi.org/packages/76/f7/9442e25555c4952584a0c6d9d350964955b73101a6a5fca98e74344bf9e7/healpy-1.16.5.tar.gz")
    version("1.16.3", sha256="9fb7ad9c895fa399f814fcf69cafe13027edf8ab92f8d7ccb36e5c4c44f3d147", url="https://pypi.org/packages/cf/d4/5ff0f67f75eb393958b9e32aaf4e5594618757d3be3374c1b60362b20a98/healpy-1.16.3.tar.gz")
    version("1.16.2", sha256="b7b9433152ff297f88fc5cc1277402a3346ff833e0fb7e026330dfac454de480", url="https://pypi.org/packages/76/57/add5f1feb33ca3ef50fedb99a356998caaab9b014adb48fd36dcf4847dcd/healpy-1.16.2.tar.gz")
    version("1.16.1", sha256="6d691b0a77fdf699672de09d39d82a640cfcc8ca03ae55022fb71e6edda69d2f", url="https://pypi.org/packages/5a/40/b2716c5b57c90f7a240177825275d86c29684373dc77e9eb9176a43c485a/healpy-1.16.1.tar.gz")
    version("1.16.0", sha256="b13a47d90b1e467a4db6f6e2d24d6de46e140a9bc13f2e98b38fcda80d258e57", url="https://pypi.org/packages/5f/fb/961501c4bb8379cf3307b4aa7cb4d85ae5c4366ba41ad907e4549104bd9a/healpy-1.16.0.tar.gz")
    version("1.15.2", sha256="d559ad287a78d3b500919a5cb9e4dff3cb63c1b3a2e23edf62819c871ccacf7f", url="https://pypi.org/packages/98/24/fa88a0b5ccca13e427052168435e933709abdd4757481816d5d51092678c/healpy-1.15.2.tar.gz")
    version("1.15.1", sha256="35de2b9e16189d31da34fadf9608d2a59d73ae5301ffdb6b4f99282bad4cb05f", url="https://pypi.org/packages/ec/75/8e8e546ef8f173555ce097ba98487a510f6a56764ed28ea3e6d11ad684cf/healpy-1.15.1.tar.gz")
    version("1.15.0", sha256="e09300a9f24e40b07f09ca7a7026d640a0478960b6ca6a5fc85052c0bb4335bf", url="https://pypi.org/packages/72/43/b0b2d086de23157f0a478b22252cf68e184aeb7632a2ddef861b5b83e3b1/healpy-1.15.0.tar.gz")
    version("1.14.0", sha256="2720b5f96c314bdfdd20b6ffc0643ac8091faefcf8fd20a4083cedff85a66c5e", url="https://pypi.org/packages/52/bb/21e57f6b3a4c2a3bb59fb2a284fccf6ea15241a180e86ace1f9b891e251b/healpy-1.14.0.tar.gz")
    version("1.13.0", sha256="d0ae02791c2404002a09c643e9e50bc58e3d258f702c736dc1f39ce1e6526f73", url="https://pypi.org/packages/26/74/0c8592686027a8196e275cb81999e8aae88d0416c223fa55a7f0cb5bdd26/healpy-1.13.0.tar.gz")
    version("1.7.4", sha256="3cca7ed7786ffcca70e2f39f58844667ffb8521180ac890d4da651b459f51442", url="https://pypi.org/packages/6a/cf/bbbfd1d300e35ca7b5e005f4d3872b392a36618705f0029ccc8155277117/healpy-1.7.4.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.16.6:")
        depends_on("py-astropy", when="@1.16.6:")
        depends_on("py-matplotlib", when="@1.16.6:")
        depends_on("py-numpy@1.19.0:", when="@1.16.6:")
        depends_on("py-scipy", when="@1.16.6:")

