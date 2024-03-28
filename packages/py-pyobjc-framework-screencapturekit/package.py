# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScreencapturekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="86f64377be94db1b95e77ca53301ed94c0a7a82c0251c9e960bcae24b6a5841b", url="https://pypi.org/packages/ea/5b/7a4dab5183278819464b6f698b352428235ab1c6618e06f1a64100db290f/pyobjc-framework-ScreenCaptureKit-10.2.tar.gz")
    version("10.1", sha256="a00d85c97bf0cdd454d57181c371f372b8549c4edd949e2b66f42782f426f855", url="https://pypi.org/packages/c7/d9/ebfde62b49d657d16245628fab96d05b2bc4e9f160dae53d625ad7cb259e/pyobjc-framework-ScreenCaptureKit-10.1.tar.gz")
    version("10.0", sha256="d6abaccf2620d01af9bcb408fc47713f813839a35899caea8fa0a96a147597b9", url="https://pypi.org/packages/b8/2d/f38bccfb13480be7b199660db08172208a2bb62e8a85f6402c43aa7d6fb6/pyobjc-framework-ScreenCaptureKit-10.0.tar.gz")
    version("9.2", sha256="e714c9b8bf543321c479168ee27e2d647ebbea977621de37dda0475429738859", url="https://pypi.org/packages/ba/f0/38ef0c8ecde76844edd07b6f2f2ea60a0f648f39045db3dd420dc283c76b/pyobjc-framework-ScreenCaptureKit-9.2.tar.gz")
    version("9.1.1", sha256="80d3aff6cd58231e15cc81bee4d106ee030e3beafcf88db8ae6a872c2c808b12", url="https://pypi.org/packages/5a/6d/276fab28edf76ca406d94ea5b7ca16a8d88ad2db8cbbe7e8a7890b9daa6b/pyobjc-framework-ScreenCaptureKit-9.1.1.tar.gz")
    version("9.1", sha256="f0d999f4e3b1bf8a448334eaf82e0a5462b6e5ef46bba715f42eaf14bed7799d", url="https://pypi.org/packages/0c/08/e67c67ed6a335912d125aa4aa117417a1fc182cddbe2aa1b2c44808979e3/pyobjc-framework-ScreenCaptureKit-9.1.tar.gz")
    version("9.0.1", sha256="4fc0b5701b69ce218a574749df561e091b3a36f53450ed66386c6eac2c8d1c7b", url="https://pypi.org/packages/ba/aa/e13d563d5939bf35d240882bcc3c15ffdbae9171911f0619b75b0498997e/pyobjc-framework-ScreenCaptureKit-9.0.1.tar.gz")
    version("9.0", sha256="97cadd42e78cf0e9cb14b300f9839911b9484be877344d13eb0b198c7c58619f", url="https://pypi.org/packages/41/3e/194817a6948ece112a26dd0a9bb2153ffbe1bd7c103464cd59e5107c7904/pyobjc-framework-ScreenCaptureKit-9.0.tar.gz")
    version("8.5.1", sha256="a52e0e66142177ce2720fb90f5b49b8bcb2f2b991694a19a5a8c7a2af8c73e07", url="https://pypi.org/packages/cf/5d/01bb64b316a50db8be475e5b95e15ca7563527ed59356ffc8f68ed78e08d/pyobjc-framework-ScreenCaptureKit-8.5.1.tar.gz")
    version("8.5", sha256="25a995ba1d6a19a0eb9f4982052f94b6cfc23cdfd805f1ef1b5d8aec0e8800a7", url="https://pypi.org/packages/0e/08/a5addc82b082cb88808cf99c19c30ecf059ced804fa361924eb5a14e5715/pyobjc-framework-ScreenCaptureKit-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coremedia@10:", when="@10:10.0")
    # END DEPENDENCIES

