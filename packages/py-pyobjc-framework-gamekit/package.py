# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="0ef877db88e8888ecf682b09b9fb1ee6b879f23d521ce3a738a1b0fb2b885974", url="https://pypi.org/packages/0c/e0/89bec2f22f568644254db7f5469f2cc6cf1a2ba3ff3dbcb8a354300359cc/pyobjc-framework-GameKit-10.2.tar.gz")
    version("10.1", sha256="6fa87a29556cdaf78c86851fc61edb6d384f1a7370a75a66bdd208ed1250899f", url="https://pypi.org/packages/81/5a/6f8102707f5b7a366289551f461dfc204f3cc2bd4928a1ee14f8107d24e6/pyobjc-framework-GameKit-10.1.tar.gz")
    version("10.0", sha256="6febacef9b003b58eeb6ca936cd83825bd22fe55475b965e0deb29b48d5912c5", url="https://pypi.org/packages/61/f6/07abe9ef376412045c066aa4470d2b3f8bfdad89a5c97177b3fa8ddc4c5e/pyobjc-framework-GameKit-10.0.tar.gz")
    version("9.2", sha256="25c9161d6561fa2a7822936a03e796e0022a5293ab672b2429429f7b03f3e9e2", url="https://pypi.org/packages/c8/13/78e4ebe174af99fb02395253f8bba10c9a6f154866cf497443b858cf2b1b/pyobjc-framework-GameKit-9.2.tar.gz")
    version("9.1.1", sha256="f07d71187d66757666908525211e73da13774c99209a5b92ee884a3cb1097edd", url="https://pypi.org/packages/0f/78/0b3eddcadc0ab68411bcd421a4d9fd3ad82812f4f33a331f2533413f6ac5/pyobjc-framework-GameKit-9.1.1.tar.gz")
    version("9.1", sha256="29754103d7e65b7f796436caaa7ef787d390db1db6258ed27f2c747f2d8108a2", url="https://pypi.org/packages/04/8d/4c6bd334e1d60c26c8fa4e2df92324cc7f63ef113c31892bf0743e247657/pyobjc-framework-GameKit-9.1.tar.gz")
    version("9.0.1", sha256="dba15ad934f048950fb4b8aeaeb79b9c11575970a5ab696d2f37ccce952f669d", url="https://pypi.org/packages/69/b2/bf6fcb7db1a8ad801e7ad0483bedc12d26e6b351020ef24fb5b7ff2125e9/pyobjc-framework-GameKit-9.0.1.tar.gz")
    version("9.0", sha256="2c9e404a124513da6e5e286cc59a519648fd923847aba616125aab046297b3a6", url="https://pypi.org/packages/17/09/58eb523868fff94982427dd648588f40b356d6a8432aac2c703998ec66d1/pyobjc-framework-GameKit-9.0.tar.gz")
    version("8.5.1", sha256="3de0782b3ec865a58ba08faaa726a8106b4ddf50ab5947f50ff8aaab7c656f0e", url="https://pypi.org/packages/a5/a2/7079a838629e198f9e136e568fa96b0914a714fa5fe5fa4a3ceb27f54688/pyobjc-framework-GameKit-8.5.1.tar.gz")
    version("8.5", sha256="612284664ff2234f2d36fa8d928a65160a7dd40c90c5044e6155db652926fae2", url="https://pypi.org/packages/4f/aa/4f74c91149dd210ba62f5bdc812abc3b1c641abcd97ced7cabc49f9f7dd2/pyobjc-framework-GameKit-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
    # END DEPENDENCIES

