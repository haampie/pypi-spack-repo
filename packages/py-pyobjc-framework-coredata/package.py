# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoredata(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="0260bbf8f4ce6071749686fdc079618b3bd2b07976db7db4c864ecc62316bb3b", url="https://pypi.org/packages/f5/d6/638692afd0dcfd8f5837ac9868159ea945533c789003389ab596dd3e3bae/pyobjc-framework-CoreData-10.2.tar.gz")
    version("10.1", sha256="01dfbf2bfdaa4e0aa3e636025dc868ddb62aedf710890e6af94106278f1659aa", url="https://pypi.org/packages/39/c8/d96818138a5580a69bea8830cb9962c6f5f199ed09125b73fa7785f39ff0/pyobjc-framework-CoreData-10.1.tar.gz")
    version("10.0", sha256="6799c3ab2ad5d609df8d8801d19740abdbe8ea70851abfe8a660bcb91818238d", url="https://pypi.org/packages/4f/52/9355a5155b72154883e8b3fd93ae7155e825f4e8385555f6b2a241ad3629/pyobjc-framework-CoreData-10.0.tar.gz")
    version("9.2", sha256="5663b96a7ac385c6607fb3b9a1011ebd6d8de10968ef77882ffe21a2992f74da", url="https://pypi.org/packages/69/eb/f53d3f9e08ded40b8e4171dcb0be06ae6d210c843d68455a304dd1051ba7/pyobjc-framework-CoreData-9.2.tar.gz")
    version("9.1.1", sha256="bee412788a355be20189573be0b08225a0eae38c302c50e85496900d7740a933", url="https://pypi.org/packages/b8/d5/4cc1f9ba2783b24973c97f8e2c18ae5c570e76e054e7984b5366b18bef6a/pyobjc-framework-CoreData-9.1.1.tar.gz")
    version("9.1", sha256="3eb033299fbc39dff7c807890c6fb538743aefc8934e3a7971c11615c5b437bf", url="https://pypi.org/packages/72/1a/d6f92713541a4bfb7962c9f5ac7152a96e9e8886bec10dac22d271656bbc/pyobjc-framework-CoreData-9.1.tar.gz")
    version("9.1-beta1", sha256="a35912f7b356ea145aa5baf293075f57964b8e19997b5042ba151706561adff8", url="https://pypi.org/packages/8a/f3/5271019b3c24cefa0b6e7995f27dcf9c6d1e7e65ac729d1b35467dec1983/pyobjc-framework-CoreData-9.1b1.tar.gz")
    version("9.0.1", sha256="aca27739366621c6986651f0ea68d47341b1e9b2bf0f118b6972a68ebdab7abd", url="https://pypi.org/packages/fe/9f/44a3b70fc84812cea45a26c4129440d19da4dd8453ed47134f5c340e0b29/pyobjc-framework-CoreData-9.0.1.tar.gz")
    version("9.0", sha256="cf364f13802b3cdba09aaa5a52192803bf2d7b7fe90f357a576082448210efbb", url="https://pypi.org/packages/a5/d3/4e55af5ad4ae428d2ff9727ef883c5c1865ea8ef02dc1a4f21c1c0e4eb7f/pyobjc-framework-CoreData-9.0.tar.gz")
    version("8.5.1", sha256="03c49c4081ee996d91a6682960205086295c78fbed23ec74311229be6005b35e", url="https://pypi.org/packages/8f/4c/35cccae0d449f0ef925990e1a99110ca088cef04160532162f1bea227dbd/pyobjc-framework-CoreData-8.5.1.tar.gz")
    version("8.5", sha256="a4f0c3fdb69112a337f8262cdf65f6813b343cec88fd459a532f472f2fc20ae4", url="https://pypi.org/packages/0f/26/0df813b45b41aba52b8878ec4ca5f9d77eebbc63df335fa52e01dbe399b0/pyobjc-framework-CoreData-8.5.tar.gz")
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

