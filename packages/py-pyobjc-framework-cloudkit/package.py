##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCloudkit(PythonPackage):
    version("10.2", sha256="32bd77c2b9109113b2321feb6ed6d754af99df6569d953371f1547123be80467", url="https://pypi.org/packages/80/e3/2030ff7ec63b3d3ba0aa178bc17a902e2e3f51b9b7747660ccd653aec855/pyobjc_framework_CloudKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="ffdedaaa8384a64df6b30d45c834dffa002a63b8e74578012b6261780f31c28c", url="https://pypi.org/packages/9e/5c/5b4c81e2df4d604984cebaf7a0c27b9f0794e94f2899a5c4b683f622b9fd/pyobjc_framework_CloudKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="cf58196fc29c0fec8f5471172d0fc2f4fe03ded5ccb4d4c1075967283164aad3", url="https://pypi.org/packages/c6/88/e8e2e8ea069a67ab082ff9547343c7cfa18bfd0fdde0b91c6699f6db8cea/pyobjc_framework_CloudKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="9292f66e488757646ded43e094fa4b964640b0057308102be274054b954ee537", url="https://pypi.org/packages/79/29/1f2ad207de95f5f0869dbe6d8bd7e95f54c886e95822a551c14c5d49db94/pyobjc_framework_CloudKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b5ef2837d8b56075c523473f74a910e54193fd180d48b4def3abe9227fffe3e9", url="https://pypi.org/packages/47/cb/52e966aedd55404fd50654a1bdb1fab038e96269bdf4738c5af54a984c75/pyobjc_framework_CloudKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="e91f8cde571a56ff9e42d2601e02fdcbfe1fb63a485811735c832eecaeefbba2", url="https://pypi.org/packages/62/d7/006c58c48f66aa1afedc71dca76326602f7d78b305f4f423735890834689/pyobjc_framework_CloudKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="2e92516a4efcbc26968260d23683d7641b08866a881b3d391486c24bf81a757d", url="https://pypi.org/packages/7c/0f/638626ca8b8488cbf6d7a5f1b63ecf57fb2ff84dc9a5685b6a00a9032126/pyobjc_framework_CloudKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="4181b816a3dc174acfcb6488df16478bbcda32ee59e5b705c13849aa74fcf2fa", url="https://pypi.org/packages/a0/7c/38cead66e6a905e50bd5cf6af6e659b7b3d0215b2219eacee6c2dbebc6ca/pyobjc_framework_CloudKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="47a8490ab6ced6891b2dcc1f3b28ae06cf595ff558201747a9464394dea3520b", url="https://pypi.org/packages/85/43/c5f869d3ba6b2c8fce31e2dbc4a1b71561afe33ad15911740a63682780bf/pyobjc_framework_CloudKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="2beb0509ef5b3dc8f6110517939b43317d5011aeda79c134f93b9d84d76f5f43", url="https://pypi.org/packages/72/54/c3d4ddc3e9529a80d25ffdd2ad2ff2e826901a5a9d5a176871529cf48210/pyobjc_framework_CloudKit-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-accounts@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-accounts@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-accounts@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-accounts@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-accounts@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-accounts@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-accounts@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-accounts@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-accounts@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-accounts@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-coredata@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coredata@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coredata@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coredata@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-coredata@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-coredata@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-coredata@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-coredata@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-coredata@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-coredata@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-corelocation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-corelocation@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-corelocation@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-corelocation@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-corelocation@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-corelocation@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-corelocation@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-corelocation@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-corelocation@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-corelocation@8.5:", when="@8.5:8.5.0")
