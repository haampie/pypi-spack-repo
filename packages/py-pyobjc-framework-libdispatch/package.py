##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLibdispatch(PythonPackage):
    version("10.2", sha256="ae17602efbe628fa0432bcf436ee8137d2239a70669faefad420cd527e3ad567", url="https://pypi.org/packages/25/c5/731a26daec598dbcb4a281a85364e98ebd10c3d00ceb21b7fec0fd8c884e/pyobjc-framework-libdispatch-10.2.tar.gz")
    version("10.1", sha256="444ca20e348cbdd2963523b89661d67743a6c87a57caf9e5d546665baf384a5b", url="https://pypi.org/packages/37/c1/a216d6bbb5b315c81e542cd4be8de9c34ce641cde8228b3c12d72233c062/pyobjc-framework-libdispatch-10.1.tar.gz")
    version("10.0", sha256="228adf364c895d2a0e8b08bd06f7a23cfbd8e82e9ea6cfdba73bdee0651a4e1f", url="https://pypi.org/packages/fc/62/2bb9fe9f9e8bcef80180f5928eb55644728044633380c006878f62ddea9b/pyobjc-framework-libdispatch-10.0.tar.gz")
    version("9.2", sha256="542e7f7c2b041939db5ed6f3119c1d67d73ec14a996278b92485f8513039c168", url="https://pypi.org/packages/f1/73/455a8b92d3fc5b47b22e8055b6df19be96b2aa13715676e70a9cb7ed00b2/pyobjc-framework-libdispatch-9.2.tar.gz")
    version("9.1.1", sha256="1cb3b6a81b79696176108253a8a7201088e51e59b85c1c314c03b0a682ac577f", url="https://pypi.org/packages/40/ef/b3548f1e53d566cb0fd2b240523555c417e8737f25f0484eefef8c1abd11/pyobjc-framework-libdispatch-9.1.1.tar.gz")
    version("9.1", sha256="5e48fd74c949edc6cce9ed3943a6481bffec4973a724de52064aaf60bd15765f", url="https://pypi.org/packages/9c/52/6d8b2b5fa91f3f7af3507337c9363019697b0dba9993fdb50341c63b4301/pyobjc-framework-libdispatch-9.1.tar.gz")
    version("9.0.1", sha256="988c4c8608f2059c8b80ac520bc8d20a46ff85f65c50749110c45df610141fce", url="https://pypi.org/packages/53/b1/ed3abf2c5d13f497cb94673edb4fc3bd2014a80d758816b567c4478a4743/pyobjc-framework-libdispatch-9.0.1.tar.gz")
    version("9.0", sha256="1a2cc42c08d52ca1459c85b049673091ee20dbf3b6387473cd2bbdc390aa2a35", url="https://pypi.org/packages/ad/ea/cf8bcbb48ea036e72c02b5c816f37cd78904712983638b4a0c755b8ca304/pyobjc-framework-libdispatch-9.0.tar.gz")
    version("8.5.1", sha256="066fb34fceb326307559104d45532ec2c7b55426f9910b70dbefd5d1b8fd530f", url="https://pypi.org/packages/21/8a/de3161c5b08c48031adfb40919549f748aecabe11cb402661e691b819be9/pyobjc-framework-libdispatch-8.5.1.tar.gz")
    version("8.5", sha256="f610a0e57e9bb31878776db0a1c1cfd279f4e43e26e3195c6647786b4522b1c4", url="https://pypi.org/packages/62/f5/06d5d9f9545aca7241144bc1475b21ecd2690e1a9d0ccd7366d08c810536/pyobjc-framework-libdispatch-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")

