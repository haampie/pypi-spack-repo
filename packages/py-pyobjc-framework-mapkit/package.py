# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMapkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="35dfe7aa5ec9e51abc47d6ceb0f83d3c2b5876258591a568e85e2db8218427c4", url="https://pypi.org/packages/33/2b/e30a760dd6c6b7a123f5182ef52a2220dc06daf207ca5bf9963b755cf07f/pyobjc-framework-MapKit-10.2.tar.gz")
    version("10.1", sha256="4e5b295ce1e94ed38888a0c4e3a5a92004e63e6d2ba9a86b5a277bbe658ddf05", url="https://pypi.org/packages/1b/c1/505e60370bd3de4a2b6ad107626d6c54fd42bf57c70d22f9d9e5bed0a1a1/pyobjc-framework-MapKit-10.1.tar.gz")
    version("10.0", sha256="35a4ac2a9ae3b13699290a6fb592d1914498e4de1b90a2b60394069cd0a02c5b", url="https://pypi.org/packages/f5/9c/f5c3a5dd730686467756523ca8b5f87b31b4c8df281ad485a44febde7ae8/pyobjc-framework-MapKit-10.0.tar.gz")
    version("9.2", sha256="bf6b171179c13060a34cd3739b339059082385230330a00041519367f282beae", url="https://pypi.org/packages/71/79/d03f7c3427a68d323a354adc2592849138e302112c34a7a37def9feaa279/pyobjc-framework-MapKit-9.2.tar.gz")
    version("9.1.1", sha256="9010759a325f096b5289e9dd8f85bee942ea1011eb9e86f23e96eb9cd7b5a460", url="https://pypi.org/packages/e7/bd/5ea81d4e78f51c9f40d0b28eeb4e92aae9df2ed76ebeb1b12f2669b678d0/pyobjc-framework-MapKit-9.1.1.tar.gz")
    version("9.1", sha256="b37627364c4de5d59583ba2a7a9316e2e0881e50c53ea328050003c2863f09f1", url="https://pypi.org/packages/d8/61/b4899e3c285c50bfd677a667470fa17721c33bcfb56990e54e1bfeec23c6/pyobjc-framework-MapKit-9.1.tar.gz")
    version("9.0.1", sha256="70a0f31276ff51e5ff2d6657681b38121ad5e893db3bb170a2f4d7a22458622b", url="https://pypi.org/packages/9f/51/ffdb41c036fe6b938f0f2a76ba69bd07f821b87a15ea9934e93a5af8587f/pyobjc-framework-MapKit-9.0.1.tar.gz")
    version("9.0", sha256="9710f9cf2adede1b7df15b3186c6505402b5f1dcdc1c3a760df95fe57894fd5b", url="https://pypi.org/packages/39/71/9039b16c509cce0db7c1274abeb24bebb91c6efb8632faca9bc19e525a92/pyobjc-framework-MapKit-9.0.tar.gz")
    version("8.5.1", sha256="77d4a0093b3c2882699c8786e5a093fc3a7c4ecd52bd07dc58dba99248c06c70", url="https://pypi.org/packages/cc/52/b5523c8e6d59ead860616512bfb2f0390144347d8c187a7b6a6441ecc6db/pyobjc-framework-MapKit-8.5.1.tar.gz")
    version("8.5", sha256="fb9060ad279dd9253caaf1c8e31940678799f5b8ee6d74bc5de6507715e3f4c9", url="https://pypi.org/packages/15/7a/898c31e764d5eedd64e40095bcae623c8740dbd93fb2926935ce255215f1/pyobjc-framework-MapKit-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-corelocation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-corelocation@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-corelocation@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
    # END DEPENDENCIES

