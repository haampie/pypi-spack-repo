# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremedia(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d726d86636217eaa135e5626d05c7eb0f9b4529ce1ed504e08069fe1e0421483", url="https://pypi.org/packages/79/45/343e8f778f6fdd52b85850975b1cb60f0d2f1cc1c3bdfbcb398104756fd7/pyobjc-framework-CoreMedia-10.2.tar.gz")
    version("10.1", sha256="8210d03ff9533d5cef3244515c1aa4bb54abaeb93dfc20be6d87e3a6b3377b36", url="https://pypi.org/packages/9c/11/a7992027a522d1771cd1ec85f37d71e254254d8e64eb0ba5ba6d567c1d54/pyobjc-framework-CoreMedia-10.1.tar.gz")
    version("10.0", sha256="27d0755cbd3ae3b487ace5e3233f0598b976905f43357b71fd73489865f7b9e1", url="https://pypi.org/packages/06/25/6e67e6bb4c476970d8f7c51d110c0d48f6fa90fa30c0183feafb2633f63d/pyobjc-framework-CoreMedia-10.0.tar.gz")
    version("9.2", sha256="6345b47775aea573082e9a81bd52a3e19ce1a7d74f5064046909a8007e68dbe9", url="https://pypi.org/packages/a9/2f/4131ac7b4a400b3767c40fb7f17f46d0caf8dc66b6ae400d1489fc596329/pyobjc-framework-CoreMedia-9.2.tar.gz")
    version("9.1.1", sha256="8c13185b938b74261966da115182702ac8b214a5f1b7878031414e05a829d7a8", url="https://pypi.org/packages/ae/eb/58eebb2eac747069deceb101f99e964b8e51eccfbe5e79051639d19e27e8/pyobjc-framework-CoreMedia-9.1.1.tar.gz")
    version("9.1", sha256="7933744b52276384bd42e068f7e5f77a822099039ed57032314a955bf5bbbde4", url="https://pypi.org/packages/c4/62/89aa29f78a660be45a5604b1a09b1018598ca16b21da7dcf8baa6f798195/pyobjc-framework-CoreMedia-9.1.tar.gz")
    version("9.0.1", sha256="0d99adad1404525f44a2493b3fe73c3ded61c67f2973c4d940ff9fafb3f85d8f", url="https://pypi.org/packages/4f/0a/e24704ae5e7de0d934932128fda1d4b001ab4a09a46a9a5bc6e9341cf08d/pyobjc-framework-CoreMedia-9.0.1.tar.gz")
    version("9.0", sha256="a886611ea800fe5262c67efdc1c4bceca8fc2ef1acb2b6a4d3c0c1619ac525dd", url="https://pypi.org/packages/f7/69/c5e9102336bf9b73aa59801b607b853370aaac1c3e6060ba9a985ec20608/pyobjc-framework-CoreMedia-9.0.tar.gz")
    version("8.5.1", sha256="01f378b9e4697d0a986800c4c5290aa70453e35890acda07c785154fe3d849df", url="https://pypi.org/packages/23/ef/03c7ac47e2ca463da387180b2693729fee4157dc705e5a0aeefc59e511af/pyobjc-framework-CoreMedia-8.5.1.tar.gz")
    version("8.5", sha256="6802b8ea7d86844470a95b2ac1394c2a0b5d20848d9d027583927a1211bbf3db", url="https://pypi.org/packages/fc/bf/adc409f54a0a6b5d9faa2b7881510c7577768ded8d1ea817a7e343ce6514/pyobjc-framework-CoreMedia-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

