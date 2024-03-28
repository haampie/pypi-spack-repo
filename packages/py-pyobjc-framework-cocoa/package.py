# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCocoa(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="6383141379636b13855dca1b39c032752862b829f93a49d7ddb35046abfdc035", url="https://pypi.org/packages/b0/c0/7eb30628e1a60c8b700f0b15280417c754eda9f186d05d47f4cac6f4e1a7/pyobjc-framework-Cocoa-10.2.tar.gz")
    version("10.1", sha256="8faaf1292a112e488b777d0c19862d993f3f384f3927dc6eca0d8d2221906a14", url="https://pypi.org/packages/5d/1d/964a0da846d49511489bd99ed705f9d85c5081fc832d0dba384c4c0d2fb2/pyobjc-framework-Cocoa-10.1.tar.gz")
    version("10.0", sha256="723421eff4f59e4ca9a9bb8ec6dafbc0f778141236fa85a49fdd86732d58a74c", url="https://pypi.org/packages/50/86/afa561caab8883b2ce155fd0067f6265bf10780a4db08bff3d76714c1dc4/pyobjc-framework-Cocoa-10.0.tar.gz")
    version("9.2", sha256="efd78080872d8c8de6c2b97e0e4eac99d6203a5d1637aa135d071d464eb2db53", url="https://pypi.org/packages/38/91/c54fdffda6d7cfad67ff617f19001163658d50bc72376d1584e691cf4895/pyobjc-framework-Cocoa-9.2.tar.gz")
    version("9.1.1", sha256="345c32b6d1f3db45f635e400f2d0d6c0f0f7349d45ec823f76fc1df43d13caeb", url="https://pypi.org/packages/90/70/7ec76e482a49cdb4dd5c4371c52775d237fcbf4fc1932bd60889b8006f1a/pyobjc-framework-Cocoa-9.1.1.tar.gz")
    version("9.1", sha256="8c95aadc8f4c307a791c60785a4e922d0f3b0a3fb4e28d25608c69638b2ad3d8", url="https://pypi.org/packages/a0/45/7b7aff8f5b99fff5a3989c026b682122f22fc0aec24a84edad31b6485982/pyobjc-framework-Cocoa-9.1.tar.gz")
    version("9.1-beta1", sha256="0ebd49de158f5b706c98633754464b112f5d6d8337720ff86a838eb20a81638b", url="https://pypi.org/packages/f8/e3/5b097c70ece99f82228e5673b8831ef81cb31b01737fc3ba0d4f07bd59f7/pyobjc-framework-Cocoa-9.1b1.tar.gz")
    version("9.0.1", sha256="a8b53b3426f94307a58e2f8214dc1094c19afa9dcb96f21be12f937d968b2df3", url="https://pypi.org/packages/b5/35/da77d26b9b6ee97fede0a9364273aaa7970fea7947d15c0e28efd345db0e/pyobjc-framework-Cocoa-9.0.1.tar.gz")
    version("9.0", sha256="1a511c620e9b7ef22f2f4fa68572902cb614e66d3dbfa9e46a1a05f000f30084", url="https://pypi.org/packages/0a/fd/56c07379311e3c877b601ec3d192a9ca6c605edbb363394408d44e907769/pyobjc-framework-Cocoa-9.0.tar.gz")
    version("8.5.1", sha256="9a3de5cdb4644e85daf53f2ed912ef6c16ea5804a9e65552eafe62c2e139eb8c", url="https://pypi.org/packages/ff/39/d45859c94970fa2dc82b9f3f9af4020a522c0abff067922859c56fe6c1c4/pyobjc-framework-Cocoa-8.5.1.tar.gz")
    version("8.5", sha256="569bd3a020f64b536fb2d1c085b37553e50558c9f907e08b73ffc16ae68e1861", url="https://pypi.org/packages/9c/0f/cbdc25505c08c76f2b96128e45b766180d44c05a3bee47d784dc36a49b7e/pyobjc-framework-Cocoa-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
    # END DEPENDENCIES

