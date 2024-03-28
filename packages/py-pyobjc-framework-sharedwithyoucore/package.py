# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSharedwithyoucore(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="cc8faa9f549f6c931be33cf99f49b8cde11db52cb542e3797c3a27f98e5e9a2a", url="https://pypi.org/packages/43/b0/172f68ec7fe267e8ffae2c294c2be748ca9a0e993ceb55fd896d02d3882a/pyobjc-framework-SharedWithYouCore-10.2.tar.gz")
    version("10.1", sha256="2b4f62b0df4bd44198f6d3a3aae4d054592261d36fc2af71f9dd81744aa99815", url="https://pypi.org/packages/a6/62/d5040cd9942bab1fdbbe1bc895b95ae70b704b65b6c549f63a186343a57b/pyobjc-framework-SharedWithYouCore-10.1.tar.gz")
    version("10.0", sha256="b07e79716e496270a4a84bd2645c1a1dc48b557ff3faaf268c8d5d4c79de9ede", url="https://pypi.org/packages/4c/14/a74bfc4ec6eea6112933fd8ace1b9440e677f2960e74fb8821f4fd519a20/pyobjc-framework-SharedWithYouCore-10.0.tar.gz")
    version("9.2", sha256="ddc00f4a40c0e81e68cf0bc4ff15f4980ab7367aca90c3c2f592762d081169e7", url="https://pypi.org/packages/84/e4/b8f0a658f776a971b097d937b223c093fbaa832c6bc2988e97b85dbed905/pyobjc-framework-SharedWithYouCore-9.2.tar.gz")
    version("9.1.1", sha256="40748793da368235379d2ce1e6abf6861e233048e215fedc3064e7f19a2f991a", url="https://pypi.org/packages/00/be/a8f51366709041b8d03fb2412096c848f74ec45f50b28c56ad28bc6c503b/pyobjc-framework-SharedWithYouCore-9.1.1.tar.gz")
    version("9.1", sha256="ef0cb74a7330d33513510adfbbead97a2bc4fa5f27f25947445ccea866aa7408", url="https://pypi.org/packages/58/fb/de5fb49de1ecd7cbd9ca03abc11cb3a914b0b1184587a291a7534d4b1a74/pyobjc-framework-SharedWithYouCore-9.1.tar.gz")
    version("9.0.1", sha256="715f4dc0295182cb6164f508163b094c0edb8b5bdb846cd3bda979535cfdbb9a", url="https://pypi.org/packages/e8/87/15e6c49e9284341679b70bc7f7d22367572ecb469dfe80d71e4e668ef028/pyobjc-framework-SharedWithYouCore-9.0.1.tar.gz")
    version("9.0", sha256="0f2e567067507cab77524027022e5ce51e5b0b2e556c90d4e8050bfb07f9b61e", url="https://pypi.org/packages/70/40/98ca5103db5da1b594acf77d10937dc7b57f2acb8ff373272b0d3f066c8b/pyobjc-framework-SharedWithYouCore-9.0.tar.gz")
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

