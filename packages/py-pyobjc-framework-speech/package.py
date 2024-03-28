# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSpeech(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4cb3445ff31a3f8d50492d420941723e07967b4fc4fc46c336403d8ca245c086", url="https://pypi.org/packages/a4/b4/95857748e26fe65c52c4e1544335cc9b3af831f0b8bd7c76e501b12c711a/pyobjc-framework-Speech-10.2.tar.gz")
    version("10.1", sha256="a9eddebd4e4bcdb9c165129bea510c5e9f1353528a8211cc38c22711792bf30d", url="https://pypi.org/packages/9a/5b/1f6c591fac57f9114a6607c1aad89daab762379485d580cf4d7d9a5a7a7f/pyobjc-framework-Speech-10.1.tar.gz")
    version("10.0", sha256="ffcd35855246432f02ebd96e6eb97da319f3ff108d8b62266e83da9c5eec8497", url="https://pypi.org/packages/66/31/04456b6bba46d2ba400fd8292fc04803c80c56cb09b1bf9854c031533c41/pyobjc-framework-Speech-10.0.tar.gz")
    version("9.2", sha256="d2fe99a42b31e33f4284821e1a272800d801a37de1cb6f1e901891d5a2f538e5", url="https://pypi.org/packages/51/d1/c1f553af049aa885999c97ab3983b9cfec967f332191f572268592c192c9/pyobjc-framework-Speech-9.2.tar.gz")
    version("9.1.1", sha256="d341ce6dd03885e07a6bae4e88e2949999cff8d6c21e420e8e41c08b968298f8", url="https://pypi.org/packages/45/3c/6ef785e2fe1bac0fb9907364dbfa32b59c72f8656bce5b03f9d8ac5f7baa/pyobjc-framework-Speech-9.1.1.tar.gz")
    version("9.1", sha256="efbb7ad25827638c95d971d5e8eba8442a68c6c456eb0faee3808976dee9371c", url="https://pypi.org/packages/34/5c/c29516180d2a01799bd2b3e567cd0050056f20de80bcfdf3eebc7b149731/pyobjc-framework-Speech-9.1.tar.gz")
    version("9.0.1", sha256="ec85948f88cc4a1f77c0cddca93046c0d0b4af526e3bc2aa90f77bdea916f288", url="https://pypi.org/packages/f8/d6/801b18ffcf806a1734eaa93026e94859b2fd45d20dd1b3f921691fcd45d4/pyobjc-framework-Speech-9.0.1.tar.gz")
    version("9.0", sha256="def1c54bbf72686e0bbab384e91d6ca0d0b36b554c70a69188150f7ef05f6277", url="https://pypi.org/packages/69/ed/09ea05028eed4668239c98d1b8547ea071341cd54f620c8c5fa122d03300/pyobjc-framework-Speech-9.0.tar.gz")
    version("8.5.1", sha256="eebaf4c0b2328edca89782c831c478d707bd03c97a6043330c701d10bcc5ca9f", url="https://pypi.org/packages/db/c2/f4675ece68c47b77e6ec68ccca50a8ce6b93e80555655be17316649340f4/pyobjc-framework-Speech-8.5.1.tar.gz")
    version("8.5", sha256="09a42fe7225c1baf19fb48e89853ba58b758e0796698105ce1dc4c2bdfd82522", url="https://pypi.org/packages/f7/b3/e04e7d3f13748984dc9deceb00e13f939dd9e85631871c30af4b290892f9/pyobjc-framework-Speech-8.5.tar.gz")
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

