# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFileproviderui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="5fac2067c09a23a436708e05d71faf65d64f4c36b45ad254617720b1a682aad6", url="https://pypi.org/packages/b3/a4/be98b494eab0288487110cf1be54b379d883b834926e7fd44bf57d6e4027/pyobjc_framework_FileProviderUI-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="ef85cead617c3e9b851589505503d201197bbc0ee27117a77243a1a4e99fad7d", url="https://pypi.org/packages/d0/3f/47fe13a063476cbcbdb91bd3a05116e141d9485c5f292b2faa2efd83bc58/pyobjc_framework_FileProviderUI-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="bca5613525ffb757e033803060d63f592612820fbe7ff024e931a5e3745ec08b", url="https://pypi.org/packages/36/5b/c7639f89b9a1c65ad9df410a1663e484d4efd58b8724f4c8ef364f301b3e/pyobjc_framework_FileProviderUI-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="704b52da8e37124575f40f33c0869b6ec561918dda9b6f69327238a46b865df0", url="https://pypi.org/packages/17/af/670aa3c84665ad6dfffaddbd90115808f9a0543e21db9f742e8c6931294a/pyobjc_framework_FileProviderUI-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="af1461628e8208c2f9b49f5da972fff7ed7f9fe1cc95cbaa49743a2c0fe31699", url="https://pypi.org/packages/ee/cf/c6b618b1d191bbc3b45c6e9a536fcb2f6f2264b8a2298d2c7210ced570e7/pyobjc_framework_FileProviderUI-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="5a41be6058955f374ab1b8bdfe1f9a4ebcaf2499cc0be897c67144a9c1be80dd", url="https://pypi.org/packages/cd/f9/61307bf96ce5858c51f7ee82b5f3ca1d233efa3d68d02463d1ea0f65f179/pyobjc_framework_FileProviderUI-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="70bddbaa5b81d113b2868c1ef4c0a07e5b37c4da134cf864d4e0c0577df3b9c8", url="https://pypi.org/packages/8e/d0/bcfccf078c486f91ba2b9d474274bf98f388966eacd9cce089c9e436d5ed/pyobjc_framework_FileProviderUI-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="7c599e63325bbaae24a7a57b74a2da2a8b47718e2d480be28342d2233db48404", url="https://pypi.org/packages/1c/6d/c4fc8b966800f2ef7a748ddbf30b2881dc916af6b48b019e70ab07bf3c7a/pyobjc_framework_FileProviderUI-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="29a2de4984a7980d5f6741f66b49b62eec060841c684fa7fa62c7d1e2bb0cc36", url="https://pypi.org/packages/2b/a8/dea6c6eead60d9589428769a44c55ae4861f5e7da8833bfb9a6ee36a1a16/pyobjc_framework_FileProviderUI-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="f650a75374e2795800ca0b8efb5e5d0a78ac3cacaadf46c86af5d85aafdd66b0", url="https://pypi.org/packages/6e/50/27d51ad77a5ad10ec579f68c6d9288ecddf0be4737341b889a0d8f87a9a0/pyobjc_framework_FileProviderUI-8.5-py2.py3-none-any.whl")
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
        depends_on("py-pyobjc-framework-fileprovider@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-fileprovider@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-fileprovider@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-fileprovider@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-fileprovider@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-fileprovider@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-fileprovider@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-fileprovider@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-fileprovider@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-fileprovider@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

