# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoretext(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="59ef8ca8d88bb53ce9980dda0b8094daa3e2dabe355847365ba965ff0b49f961", url="https://pypi.org/packages/51/51/17409f0a85753e780893515d9a525eb291852428cac18839601161535553/pyobjc-framework-CoreText-10.2.tar.gz")
    version("10.1", sha256="b6a112e2ae8720be42af19e0fe9b866b43d7e9196726caa366d61d18294e6248", url="https://pypi.org/packages/3b/9c/77d12eb9ff0740a94677d719476c9cf7a482a62e4dfd78d91f58507c9ed1/pyobjc-framework-CoreText-10.1.tar.gz")
    version("10.0", sha256="2c157d82373b8128afb9a61df26cbf029896adf86bf86876ce3f8cc3c3f3cb1b", url="https://pypi.org/packages/b3/bd/4da5277e3fcfa374d0039fc4361e1a2e8d87332a6c5a195c3d0e0744f657/pyobjc-framework-CoreText-10.0.tar.gz")
    version("9.2", sha256="24a2aba7419e9955f8f83cd85378743a14f29011e671c168d54d4a92ca06c9a4", url="https://pypi.org/packages/d4/ca/452214e5d14a158c4b594a6de949197489d67c1d23bff5ad253ce9c667dc/pyobjc-framework-CoreText-9.2.tar.gz")
    version("9.1.1", sha256="65023e4fd5bb91949eb324b6baa45a9f2ff69c344f77084d63a8b0ec1fae0fa1", url="https://pypi.org/packages/c0/06/cb094ea46111e82ddf2e1247cb7b92766111571727e94025a33233c79795/pyobjc-framework-CoreText-9.1.1.tar.gz")
    version("9.1", sha256="84f53c8b89f3852d117287528062bbad4d886ff92546b3fc1a0ebb6a63c77bf3", url="https://pypi.org/packages/9e/11/a299a523f3650cf24cdef7aab4c703237506784baaaab7e2951107728e2c/pyobjc-framework-CoreText-9.1.tar.gz")
    version("9.0.1", sha256="0128b6360a492a2a6560f36ae4fb721991b545faed4da1dab3664d8ed2083676", url="https://pypi.org/packages/ec/ca/a6c197e826ee2aa5ceaa52579ce8cc316ad7e4a2a2c7f7f8742cb186e47a/pyobjc-framework-CoreText-9.0.1.tar.gz")
    version("9.0", sha256="ac72b8bef194399e6d991938ee98b36892c944eedb0c085ae17b9b3a2081d80c", url="https://pypi.org/packages/09/f6/c65c6c475c31ec61edd87e414a6bb20ff65bf3c1dd7dd6d9254f8c93bd11/pyobjc-framework-CoreText-9.0.tar.gz")
    version("8.5.1", sha256="3c90ee9d10314372a2844ca6ba0e4749a73b96d168d38ba410dd2cfe4bf3911c", url="https://pypi.org/packages/2b/30/ae8478aff5514d971a1d86e2e376fa1945f6c60db7dffeb4a2133285a5b8/pyobjc-framework-CoreText-8.5.1.tar.gz")
    version("8.5", sha256="541b662897cb97ac770a0467bf50707030f8b31f70e3ba5a957fff5d4e916f78", url="https://pypi.org/packages/eb/51/9a5dc46afe1486c715c640186f2bf1a3b2d8ee57a3473d3273ab63c16742/pyobjc-framework-CoreText-8.5.tar.gz")
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

