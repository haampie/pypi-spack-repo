##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNetworkextension(PythonPackage):
    version("10.2", sha256="14f237bd96a822c55374584e99f2d79581b2d60570f34e4863800f934a44b82d", url="https://pypi.org/packages/0b/9c/69f2e265cb8560a0f1bc170831be1ecbcfef817e8e8d4a0bd330f185f1c0/pyobjc-framework-NetworkExtension-10.2.tar.gz")
    version("10.1", sha256="f49a3bd117ca40a1ea8ae751aca630f7b7e7d7305aa5dfa969beb07299eb2784", url="https://pypi.org/packages/fc/9d/a71dfd0076fd58443a66d1c4ddc85cefef62070aa69ecd0758ff02ffc879/pyobjc-framework-NetworkExtension-10.1.tar.gz")
    version("10.0", sha256="cd17420c9763c240343fcfedaddff11db8c0f4f1b54c060c24d6f414234d6b5d", url="https://pypi.org/packages/28/6c/dda3b9fcb9c97847679a2e9d9ae5fb402a7a261032f1e068815b68cacc48/pyobjc-framework-NetworkExtension-10.0.tar.gz")
    version("9.2", sha256="7f2d992f85c3fa8b62fa514b0afc9a4a8536fd5effff77cffd7a7b963e29f708", url="https://pypi.org/packages/86/1f/30788e896fe945e7d014c4352006dbbd5f8fe2e79e2a3f693e9cd2925e2c/pyobjc-framework-NetworkExtension-9.2.tar.gz")
    version("9.1.1", sha256="c0bc25c8d595951a7931c0c98a6f17d177b7cff8be91352a45e64c0e4a8c6b21", url="https://pypi.org/packages/3a/91/9535c0e7a5220955f6012674b1c5ea6892d82a64a594f7d5e86c3da04895/pyobjc-framework-NetworkExtension-9.1.1.tar.gz")
    version("9.1", sha256="fed10009b18c69622fcb8bda00d584b872d50fe4f2b568ee11f7acb59a13faa5", url="https://pypi.org/packages/08/00/321e32a04c9bc512c2cfbdbcb404c599041115232c77059a921dd58b0d42/pyobjc-framework-NetworkExtension-9.1.tar.gz")
    version("9.0.1", sha256="a6de4020f52eda61cfb86260782cd547d0d701702ce1d90edd497a155c0157e9", url="https://pypi.org/packages/3e/b4/ac4164d19c5dd6e061114edaedc92daff7c06855001b24e0718d323ec1cc/pyobjc-framework-NetworkExtension-9.0.1.tar.gz")
    version("9.0", sha256="172bb55390663664e30f90888f2f753de3235c191b852f6ccbd6907b534966b6", url="https://pypi.org/packages/5d/cd/259f13912cfaf2f375b4d4bc506f491c1ae56baa8717369b2ddcb11687ee/pyobjc-framework-NetworkExtension-9.0.tar.gz")
    version("8.5.1", sha256="b5cd97e03962db8eb5585f34de22fdbb0c44fd4c208400817bf830ee4229d6ae", url="https://pypi.org/packages/d1/ce/1e4d52b42d93b9290cf42f0c19733e579ab776118298851bd0947f86f37d/pyobjc-framework-NetworkExtension-8.5.1.tar.gz")
    version("8.5", sha256="6605eae194672772d64f1b39a19b0b3fed38b39435f93bc80a80c9dc12cc07ce", url="https://pypi.org/packages/e0/7c/b7cb8033a4e348c4424c24e7eaaecf9cb91a05e311e9dad85bc22b629e7a/pyobjc-framework-NetworkExtension-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

