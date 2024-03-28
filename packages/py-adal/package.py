# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdal(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.7", sha256="2a7451ed7441ddbc57703042204a3e30ef747478eea022c70f789fc7f084bc3d", url="https://pypi.org/packages/49/8d/58008a9a86075827f99aa8bb75d8db515bb9c34654f95e647cda31987db7/adal-1.2.7-py2.py3-none-any.whl")
    version("1.2.6", sha256="9928f90e4003dc7a41c6995ccb5db79d9769a275cb365b10deb48471002642dc", url="https://pypi.org/packages/61/a1/5f5fb9f4edb6e8b7882281158edc1cd465249c53fd48b1bf6af2c9237fe5/adal-1.2.6-py2.py3-none-any.whl")
    version("1.2.5", sha256="7492aff8f0ba7dd4e1c477303295c645141540fff34c3ca6de0a0b0e6c1c122a", url="https://pypi.org/packages/e9/51/5081e3705fdc4bf56fe26990b959b3379c9db38c6a0a0cd6b66508d161db/adal-1.2.5-py2.py3-none-any.whl")
    version("1.2.4", sha256="b332316f54d947f39acd9628e7d61d90f6e54d413d6f97025a51482c96bac6bc", url="https://pypi.org/packages/46/58/a19e0eb0c388fb7aced40f940c09069343862613d83095b592a8d3961ba1/adal-1.2.4-py2.py3-none-any.whl")
    version("1.2.3", sha256="a74ff45b88db18d3d3d0c50d0d2d6d411866648f457bef4be714ba0b8e30d515", url="https://pypi.org/packages/97/23/55a3f587cc3e5bd7fac0b2b041af16974de9bf4da54c7742b14d693670a6/adal-1.2.3-py2.py3-none-any.whl")
    version("1.2.2", sha256="fd17e5661f60634ddf96a569b95d34ccb8a98de60593d729c28bdcfe360eaad1", url="https://pypi.org/packages/4f/b5/3ea9ae3d1096b9ff31e8f1846c47d49f3129a12464ac0a73b602de458298/adal-1.2.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="82e84fa0b442caf8131f1e87a7ebee2546f57ab16a8917a599a02b6e455cb1b0", url="https://pypi.org/packages/00/72/53dce9e4f5d6c1aa57b8d408cb34dff1969ecbf10ab7e678f32c5e0e2397/adal-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="bf79392b8e9e5e82aa6acac3835ba58bbac0ccf7e15befa215863f83d5f6a007", url="https://pypi.org/packages/2d/2f/14882b8dae0977e85577abde3065c141fb94dbb242adfb80e21797e4f7c9/adal-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="534ab04df7ab7c30bc7fe9526c3120e50b9496982f6c85001b05fd7cf4134eb7", url="https://pypi.org/packages/15/2b/8f674c2a20bb2a55f8f1c8fb7a458c9b513409b2cfc42f73e4cbc1ee757e/adal-1.1.0-py2.py3-none-any.whl")
    version("1.0.2", sha256="b48f37acf571ec74822ae3fe5db683e5cc9b0c2004aba9be6d582253740258c2", url="https://pypi.org/packages/77/a8/8bf977a1e075ed26617b98e708afe5b96a923c67dfac5213f81f5d80ac1d/adal-1.0.2-py2.py3-none-any.whl")
    version("0.5.1", sha256="83b746883f3bd7216664463af70c05e847abd8e5b259d91eb49d692bec519a24", url="https://pypi.org/packages/8e/c7/639d67077c11de45c70d2fe780a4fab5b6234546fcc0dd9f011a7e987aa8/adal-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="9a055c64ad90706ff543111110b2a5bebb28d9791097db4586adc3f57999126b", url="https://pypi.org/packages/a2/7b/5249869517ece8fed824b6fecbab6833f3c84b1e619a82425439b8bb6e8c/adal-0.5.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@1.1:", when="@0.4.3:0.4.5,0.4.7:")
        depends_on("py-pyjwt@1:", when="@0.4.3:0.4.5,0.4.7:")
        depends_on("py-python-dateutil@2:", when="@0.4.3:0.4.5,0.4.7:")
        depends_on("py-requests@2:", when="@0.4.4:0.4.5,0.4.7:")
    # END DEPENDENCIES

