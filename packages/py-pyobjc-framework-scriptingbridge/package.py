# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScriptingbridge(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="c02d88b4a4d48d54ce2260f5c7e1757e74cd91281352cdd32492a4c7ee4b0e7c", url="https://pypi.org/packages/7a/b5/12685787d801a53cdd535ef71487b0b0bd9dca937a6a106f0e8a3a908b66/pyobjc-framework-ScriptingBridge-10.2.tar.gz")
    version("10.1", sha256="7dce35a25d1f3b125e4b68a07c7f9eaa33fc9f00dde32356d0f7f73eb09429a3", url="https://pypi.org/packages/cb/95/3e526bb4724aaba185036d81165bee2500f22783559db552c4d7135bc434/pyobjc-framework-ScriptingBridge-10.1.tar.gz")
    version("10.0", sha256="dc8ee394c84caabef9512eaf784ba91459b9560556da5fd5762aa7a6ef5e4612", url="https://pypi.org/packages/b2/6e/c35a507c0d37be5ef768f9cb5a3a5ff150bc8014b12c3ad87847df8b7d90/pyobjc-framework-ScriptingBridge-10.0.tar.gz")
    version("9.2", sha256="48adc2a2b27f8f699f8d9e849c04b0a05afae8044d0435bc0765cdb79f42c051", url="https://pypi.org/packages/bc/20/3fa0549df9ec90015d2f666438f51454aa309e935707ac6f7d90ccac3eaa/pyobjc-framework-ScriptingBridge-9.2.tar.gz")
    version("9.1.1", sha256="63d9282f7e409f3b7099b943fc7df1e5184dd2722d7fa994511387a06f7d08ce", url="https://pypi.org/packages/1c/b4/20743fb4cb33d24b154bfdd2ce58674d75d6f973ea6fd59008cf861da874/pyobjc-framework-ScriptingBridge-9.1.1.tar.gz")
    version("9.1", sha256="a8d5b71d12672e1c25f81235d8773f614e29cb1bfcbe9578ee0a2a4fd67deaef", url="https://pypi.org/packages/dd/ed/f542f481cc2cb982c327ae4b3facf460631a509ed4208c0ab5b42f3136df/pyobjc-framework-ScriptingBridge-9.1.tar.gz")
    version("9.0.1", sha256="2ae301056dfe2e6d338da2523d29a08a4b0edb0bf547efa94e283b2022a8e5d8", url="https://pypi.org/packages/e5/8d/1377c9c9f8f6da59c0a7f7344583c8c5fa3778f78760ea3275f0719553b6/pyobjc-framework-ScriptingBridge-9.0.1.tar.gz")
    version("9.0", sha256="3197ad41da21784518547c783426c8ce1cee34e5bb5f6029c3f3c3b68aa6737e", url="https://pypi.org/packages/b5/b7/75a2017b99659f3c1988dce2cd0601d6c429fe01ab477df9da615ded4a59/pyobjc-framework-ScriptingBridge-9.0.tar.gz")
    version("8.5.1", sha256="51b2da03b4c7d12ac814e953bfa897d1763683d4f9293f76a0ecc54745cc64d6", url="https://pypi.org/packages/f2/2b/b845426547a32b709f8d960a8c891865fb19f4c277b47887924817c27b8e/pyobjc-framework-ScriptingBridge-8.5.1.tar.gz")
    version("8.5", sha256="20df11bd2f57e8105d42b9bcde84881dc2fc6119727fd5d501fac50666f3fb00", url="https://pypi.org/packages/c2/68/770d217e3c51b9bbd2c06eaa783097e506b0f8bdd8b0b33b81717760616a/pyobjc-framework-ScriptingBridge-8.5.tar.gz")
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

