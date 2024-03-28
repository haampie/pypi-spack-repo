# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDictionaryservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="39b577b35c52a033cbac030df1fdcd16fb109144e8c59cb2044a13fcd803ab49", url="https://pypi.org/packages/b7/41/d6a796ce075c36770d80cd89c8820fb37f6b84efa214b394a9ad5006c81c/pyobjc_framework_DictionaryServices-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="7ace031cc3df1fa9a4eb663ff55eee0a4c7c8c34653aa1529988d579d273150b", url="https://pypi.org/packages/0a/81/82820ff728c0e66a81dd180fad30a3b97eec9de39fed284257c6b03ad38a/pyobjc_framework_DictionaryServices-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="8bc50b80e8f77e411b707827062609b67695bc5ae619452388eb02bdeea19f05", url="https://pypi.org/packages/5b/96/694d437a3f7fba994f1ae68d37b1eec8c11d033f14f3cd0c7e1e0b7edc7b/pyobjc_framework_DictionaryServices-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="1fd533511698977fd0efc202d99aa02b5a9b3d184c2e10950d7cb1f2b6bf8806", url="https://pypi.org/packages/38/28/dbb2cec2d555a2dfa8c4f280c73f3037413439ca8f0d75641f09946c8305/pyobjc_framework_DictionaryServices-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="d6cc9a76de4a1bda9aca9157ecf0cb7c6356227d95b20b47e0797e2ce15a5287", url="https://pypi.org/packages/44/55/91868d11d9ce9ad7df8c5726dee2c4d39ffe675d53ad356e5ce4ae75bdd7/pyobjc_framework_DictionaryServices-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="d8802690ff7fafe5a405be9cda37b97c36dbaa328966708bc8647e93271aab99", url="https://pypi.org/packages/2a/61/613dfa0f080f492c49d75e5746038cd0496652c4a82ed4409b7a3bc1400a/pyobjc_framework_DictionaryServices-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="e2f2fd8d0d833d2a211c0aea601d6291e118ac0e2c5da6445db9903b63f6d197", url="https://pypi.org/packages/78/03/e36883f34db74680150c5dc779680c82aa88cbbd2409a7841a89c86dcec4/pyobjc_framework_DictionaryServices-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="5396744d147524f604d8bc0018739dd1811886848c95f0851c6ed71000588012", url="https://pypi.org/packages/c4/20/75c8ca84446a6e07c9146ea67aeb7a645d2f644e73d9c649c84771cf4dcd/pyobjc_framework_DictionaryServices-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="a331b43f9349708c7cc44e82d778cb99539381666accbd1b19b73d43f36def3e", url="https://pypi.org/packages/4b/8b/d1b84ac20fd509f7503b8f6c2226b6d1be8b61414407fd374ef8601283c1/pyobjc_framework_DictionaryServices-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="1df49a178970711a2b5fa7c4a4bf7bccd806c21c855ef6da41a1b303a80fde29", url="https://pypi.org/packages/25/9c/907ace66857704f04c94c1f857c480340b4bab7c6b8166fa545f82e7b3af/pyobjc_framework_DictionaryServices-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coreservices@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coreservices@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-coreservices@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-coreservices@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-coreservices@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-coreservices@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-coreservices@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-coreservices@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

