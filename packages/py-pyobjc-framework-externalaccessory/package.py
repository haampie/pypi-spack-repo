# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExternalaccessory(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="e62af0029b2fd7e07c17a4abe52b20495dba05cba45d7e901acbd43ad19c4cc3", url="https://pypi.org/packages/54/fa/c9dcd5b9185eba20d6734e4f993368324122e7fd272e2a35061381f30dd5/pyobjc-framework-ExternalAccessory-10.2.tar.gz")
    version("10.1", sha256="1c206f2e27aedb0258a3cf425ed89cbea0657521829f061362b4fca586e033a8", url="https://pypi.org/packages/61/e5/d0c34dad237b132330fcb3a44db46bf22c647d148feb1f03130cfad4b471/pyobjc-framework-ExternalAccessory-10.1.tar.gz")
    version("10.0", sha256="4b00f07e6ec8e68974d89242789720bfecdc474c26bf0f2b2b2d648e6b6155cc", url="https://pypi.org/packages/91/53/4e210e92d8e1ccb69ad7e19eb285c4c5f90fbdd122d9db9670b0c28fcd67/pyobjc-framework-ExternalAccessory-10.0.tar.gz")
    version("9.2", sha256="3cd681764bc5ba2431309220294d67ef12ec97f57c36c6637e551e5ae0efcc1e", url="https://pypi.org/packages/c6/82/e81fe7a122316263d54b07d173637fabc1daeab5293a8fbde27f75c9e9d0/pyobjc-framework-ExternalAccessory-9.2.tar.gz")
    version("9.1.1", sha256="611ef4af924cf5d39096ebe1d7d67d8361b013bfc1476595c38949302c436b41", url="https://pypi.org/packages/bf/70/c02298c68b4579db37c487ddeb120b7f92f8c83b73ba55f07ff975b0fb1b/pyobjc-framework-ExternalAccessory-9.1.1.tar.gz")
    version("9.1", sha256="ea6ec85d15576a411f48f1e4d2802da54874cd604303622a9ef1791d34c7ddcb", url="https://pypi.org/packages/2a/5f/df638f9e4813317b3a543fc43c0d1e38eb9447f48e32255f4bf2ac5d26e0/pyobjc-framework-ExternalAccessory-9.1.tar.gz")
    version("9.0.1", sha256="533f2a814ab9afcc8594d34f761017d30f0b66518af682fbcafc16b5cd612078", url="https://pypi.org/packages/2e/a5/e31a6d656297221b414ca036c13ff6f5800ab7c3fdfd1f26c06d5d977009/pyobjc-framework-ExternalAccessory-9.0.1.tar.gz")
    version("9.0", sha256="57ca98fdf9cf52033849a10ef52f094c9a5a17d80ccdbb49d4904269b55672c2", url="https://pypi.org/packages/8a/e3/cf748444052811f31aff1fa2d3b96480401adf125a5bfc4b2193b8d87f47/pyobjc-framework-ExternalAccessory-9.0.tar.gz")
    version("8.5.1", sha256="f81fdded05de0a00b41becc0fafb5b30d92da442fc72eb5737f043ab49dfe6da", url="https://pypi.org/packages/f6/35/9d8bf07c210d10ac548def257e168753797b2143849a45176d0a1c73b308/pyobjc-framework-ExternalAccessory-8.5.1.tar.gz")
    version("8.5", sha256="37e8d782fedcedf062140d1c3df6b5e145e1bbe692f3c8db6bc7d736bc6f2c17", url="https://pypi.org/packages/1d/12/e000b6d09132457f0dbaf15f16413866bac48875d5f98c54e6908a658a23/pyobjc-framework-ExternalAccessory-8.5.tar.gz")
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

