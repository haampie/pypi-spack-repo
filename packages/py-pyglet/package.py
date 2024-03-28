# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyglet(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.10", sha256="e10a1f1a6a2dcfbf23155913746ff6fbf8ea18c5ee813b6d0e79d273bb2b3c18", url="https://pypi.org/packages/e9/33/cbff7525a357c950e76717ea9741127a662a7ed49a92874897b8a4036db9/pyglet-2.0.10-py3-none-any.whl")
    version("2.0.9", sha256="8520b22dde75f47167e1fedeed58ac0bb0c890c0dca17d8528427d6b318cd9cc", url="https://pypi.org/packages/94/a1/475458ccf34d2996abdb6ef29fa8d3fed2e62f72df5f2a7f4b4b076915c7/pyglet-2.0.9-py3-none-any.whl")
    version("1.5.28", sha256="ea312a553c266a0f45a9c209f565e3c02371c83d89fd8931422c6475ce4ecbae", url="https://pypi.org/packages/66/04/e03cfc5ec197a711216b36b01054c551539c5422d4a372685b6ae6493399/pyglet-1.5.28-py3-none-any.whl")
    version("1.5.27", sha256="7ce2eb5a299cda92fcc099f533520cdaa2f157a175d6c1442a2ae4d769284d2d", url="https://pypi.org/packages/e0/da/259b29659834f31f90b326b0f21466dc332eba9d5b89f6dbd849eabf9bc7/pyglet-1.5.27-py3-none-any.whl")
    version("1.5.26", sha256="529b7b1198df3a8399b9621a99ca5e29cd32bb98428bd0e8ba699afa4ba96d2b", url="https://pypi.org/packages/68/52/10c1826df26e59d989b115bd5ee19535cae8cbfff642f1495fc62f24b01f/pyglet-1.5.26-py3-none-any.whl")
    version("1.5.24", sha256="1268a604b2268419cad94e95e42711553463f602c101f2bd48eb6eacaf9c306c", url="https://pypi.org/packages/f1/f1/3723976b17545707672edff9f21d661ae9c3ba2b931f5d735758afdfaa35/pyglet-1.5.24-py3-none-any.whl")
    version("1.5.23", sha256="086317c022612bf0aa28f32134a8cbe3d11de96787f5412d38d9c6abb6cfc771", url="https://pypi.org/packages/aa/6f/f1e70b50a855e6b18f935a705baf3b5746fa78bc0d26a223e89cab3167e1/pyglet-1.5.23-py3-none-any.whl")
    version("1.5.22", sha256="19d1e4a5fba4c31861fd38664e96f60e3f05aa64c55ac7cebc350f6793bd9548", url="https://pypi.org/packages/ad/8f/1661c1998f24ec41f14146ed3990f899a3c4e97ddec16fd099f0655aac42/pyglet-1.5.22-py3-none-any.whl")
    version("1.5.21", sha256="11f11ddda4ee456284f2ddd1fe5c62fe29ba8c42074d3d9ae52d094abc2e1b7c", url="https://pypi.org/packages/0b/b7/7736d7638d91b354700dc9bae447728c514c4bc6ecb4c0f7e0cd9a390f20/pyglet-1.5.21-py3-none-any.whl")
    version("1.5.20", sha256="0a0dfad612b46db863e3775558c16dce5c7bebcc1432c0e4af8c2ad9261f962e", url="https://pypi.org/packages/d3/19/c4a8cd6d7eae8975154cf43802b6235f8b9cdf34036834095a36c757c1bc/pyglet-1.5.20-py3-none-any.whl")
    version("1.5.19", sha256="6e1eede7a7c0fd3606b14bc241b51915d4453e4a6a6a0e8a6a080842f767662d", url="https://pypi.org/packages/48/c2/5898d5cce5d5ce7e74b5a515f2d107a82f2c4d0d4505c0ca119cb34c6b01/pyglet-1.5.19-py3-none-any.whl")
    version("1.5.18", sha256="543d60ed190b72c22f5ed9becd01fc4ff1b1b10cd4545349105434bbcd4fede6", url="https://pypi.org/packages/c7/19/fd194c20cf5be3342baacba0dd285be81cb46171db68cd2d3481e0c646cd/pyglet-1.5.18-py3-none-any.whl")
    version("1.4.2", sha256="c1c49b2c384bc310aa3dca87817d2b4d22383e35776e73dace5a38235f0992a4", url="https://pypi.org/packages/d4/eb/e3742cc05eb640b6b59618ad8c8ae38f43aa57539e4cd1b40576c93afccb/pyglet-1.4.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="91a49322e5ef17aed704a2622cb7f66793b9519ce9ec8af45284eb9cab7d93ea", url="https://pypi.org/packages/4f/2a/52827e866bc2ebe0f67d83d0c49fcd2ceecd58245d9e79b69df0919e740b/pyglet-1.2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@1.3:1.5.0")
    # END DEPENDENCIES

