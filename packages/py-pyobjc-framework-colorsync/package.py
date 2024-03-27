##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkColorsync(PythonPackage):
    version("10.2", sha256="2fcc68eb6fa6300d34b95b1da1cc8d244f6999aed4b83099a3323d32e0349f98", url="https://pypi.org/packages/1b/4e/26ac61866995cc31995516f3cf6c203257706f64c0d352bfa866f5d30498/pyobjc_framework_ColorSync-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="58596365b270453c3ce10bb168383c615321fa377a983eba3021f664c98f852a", url="https://pypi.org/packages/c0/3c/02627078ce8af21eef0628a1f21d20a714576afc9c7a2782c09b655466ff/pyobjc_framework_ColorSync-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="5c5d361ebdcf72f4a2665cf0c68adc153b6621ea7ea0df6bbc60a4a69ec1e2b0", url="https://pypi.org/packages/06/90/2eb5bff8a7867a2001b7f4280ede93a64e56320c32597e5d1d239dbec62c/pyobjc_framework_ColorSync-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="fe7b2364f29fe8e43e3a65312c5b2bd60884b3e78ec4f70e45b4e1003cd12ffb", url="https://pypi.org/packages/21/2a/c657f955920adbcdb74c6fce7b9c66d04694a64451e4e2431e17fc0df68a/pyobjc_framework_ColorSync-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="40b10afa8922f07bf8391a7bfe37c419b9bb9474261999e01d8a4a7949b5f792", url="https://pypi.org/packages/88/e4/6fb296f4d204c06d652c90aecb1dca91b7f61d7e57767976e1a3c2f13880/pyobjc_framework_ColorSync-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="5e49e4d4f6f34306cdbeb8a5d158d97b617e91619abf8705c2f49b9676e74996", url="https://pypi.org/packages/47/91/ed5e196f43e650ed462f7055d197a2b1f504e9ca69f0da82e2639d190682/pyobjc_framework_ColorSync-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="ca3ff3558febd237c4bf4db36b0e417540569ec7b05af17c3805012bb3a438c0", url="https://pypi.org/packages/9f/cf/f25a97e0d0f76c291dcdc1d3b24af731e745637540d61868b40f6ff5cdca/pyobjc_framework_ColorSync-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="0209ec98dd2e20786f2c0c0eba7310073295a68593e1695c1b7c38b1ca835dc7", url="https://pypi.org/packages/cb/ec/7fd38045e64e1ee8ce0c5a3d06517b36647ab69e0fee74322165f7eb2912/pyobjc_framework_ColorSync-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="487c3926f602e344e4823c7043a715134ef17a07c21ae37906fb7806437fa5ad", url="https://pypi.org/packages/21/74/85dbc97c5b94180d2d41e0aeba84500f01c178d36148b9a72c26db94aa69/pyobjc_framework_ColorSync-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="9cbf45dee34e97ad4807c303095b8e97fd601f1c442dfb18f4c84351807d3f8b", url="https://pypi.org/packages/d4/11/f4be1d531c94bc522f3acb27d5e006c63ec3ceb4040c42241d35410dfdf5/pyobjc_framework_ColorSync-8.5-py2.py3-none-any.whl")

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

