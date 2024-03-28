# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMedialibrary(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="98b9687f1399365889529c337d99d7f19edf3a94beb05884cf15a29f4fc178af", url="https://pypi.org/packages/52/a6/7ae38a5a4b80327857bd539ee0ffb6899f543c32cf0ca6ff9ecdd1ef5481/pyobjc_framework_MediaLibrary-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="420d5006c624aaaf583058666fd5900a5619ff1f230e99cdd3acb76c12351a37", url="https://pypi.org/packages/8e/97/6ac111133068112e72028d87cbc9bc94507e2b355f85f5f4052e77603eea/pyobjc_framework_MediaLibrary-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="e7d0f3353a954abc801bcdb7c02713f38d76835eb8ff4912fab5d005b95d5459", url="https://pypi.org/packages/d6/73/3f07536b404a0a0693fb0b0d394edc1092e9f16bb0c4d15766b128a51396/pyobjc_framework_MediaLibrary-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="caea22f65679a9ae6ce5dff61ae1dbd681ce240b1693de94bc1421dd5cfb49a3", url="https://pypi.org/packages/f2/10/64c80fba675d0219bb1879e5522723663cc356a57c997e990c23acf0fa06/pyobjc_framework_MediaLibrary-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="35537f04d731c1eca707f183a48b1e8e8d776c3ababb5b0ff2a59e96e828fc8b", url="https://pypi.org/packages/fa/a4/1e593af5a51a3a378c89914960f763d35b830bb927da5ad72f2cbcd8f072/pyobjc_framework_MediaLibrary-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="197563f9c443c616e125e6bf2f5ad0966376099c8b5bbe713ff68139b17941dc", url="https://pypi.org/packages/5a/59/a6c404af6d6bc267c21339dfe2e3f6158bb3d1d99e73ad8d47647366dfe0/pyobjc_framework_MediaLibrary-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="4a13451b9ba84dda47d98724765147d616eb66f02649074dcae8cd8392c9ee35", url="https://pypi.org/packages/3b/54/9569708caeb226a3418e8aff7a02156f9aa6d0ad9d8989766e60b611f468/pyobjc_framework_MediaLibrary-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="0530fcef36518e6a835561dc33ce6ff547b751c308a38deaa0b37db282237fc5", url="https://pypi.org/packages/6d/5e/ad201e6721160306c203df9f0446088812f11c29819a2ff01e2bbe48b97f/pyobjc_framework_MediaLibrary-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="8a96d2cdf6a55dac23065ddc8318f26df729d2cf0c8f1cba2acfc33a38f41998", url="https://pypi.org/packages/29/62/998ec372e2796c2e6a28ded93c078bde84af979c135a7ce6a82fecbe87d9/pyobjc_framework_MediaLibrary-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="90e9db486c23f2346eb6a7f2fc0abb1e1cfa0a172d93373070413b685ee592e5", url="https://pypi.org/packages/76/e5/d0f16c7981d04d020c8b6d49ea0c373bf52707ed581b13237f699d124285/pyobjc_framework_MediaLibrary-8.5-py2.py3-none-any.whl")
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
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-quartz@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-quartz@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-quartz@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-quartz@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-quartz@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-quartz@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

