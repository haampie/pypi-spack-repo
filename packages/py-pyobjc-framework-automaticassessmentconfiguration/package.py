##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAutomaticassessmentconfiguration(PythonPackage):
    version("10.2", sha256="ead3f75200ad74dd013b4a6372054b84b2adeacdac656ca31e763e42fb76cf7b", url="https://pypi.org/packages/f2/f4/1690886940bd04ca5a2ca16a48f52494d13f522a90d17802d726172df26d/pyobjc-framework-AutomaticAssessmentConfiguration-10.2.tar.gz")
    version("10.1", sha256="c8f32f5586f7d7f9fd12343714c7439a1dfad5b5393f403aee440b5f91ef9f7d", url="https://pypi.org/packages/86/73/85ddd9e506536a10bf97487d0e8529045d29b63f12311bd8fec8dcec080c/pyobjc-framework-AutomaticAssessmentConfiguration-10.1.tar.gz")
    version("10.0", sha256="008599dc2b2af1175e574ebce2be950c5bb67a2c9eb7391535dac4f514e158a2", url="https://pypi.org/packages/90/54/20b9e31239c834bfd7d86391c89728c68aa6dc0a04806f41fbe962a9c71c/pyobjc-framework-AutomaticAssessmentConfiguration-10.0.tar.gz")
    version("9.2", sha256="6617978c2f0618a9df4c8fefb2e3d6a00ca8580e36baa4a95145f749375f23d1", url="https://pypi.org/packages/06/19/4f0323f4dd31a469727fe69c4e085f3f7c49bdaf929d3a9cee190441acfb/pyobjc-framework-AutomaticAssessmentConfiguration-9.2.tar.gz")
    version("9.1.1", sha256="9b936e29c2585ebfe243c0cc3e762d432d32224100add996aa86ff3e14de594e", url="https://pypi.org/packages/61/19/04abcb991eba3b630146ac67fd094c9e341be2223780ad390f4dd931cd63/pyobjc-framework-AutomaticAssessmentConfiguration-9.1.1.tar.gz")
    version("9.1", sha256="6a2a42219c5e083f6d82bf3a7d968d0adba649ad08a175f79a3fe575c81e2001", url="https://pypi.org/packages/b0/5e/c7a4b37847973875242b40f7615b1aafcbed2dcf4c76483178ce90aa9a82/pyobjc-framework-AutomaticAssessmentConfiguration-9.1.tar.gz")
    version("9.0.1", sha256="2f79daec218f27f0941253238d8ea22d17bf37f9cc3af8ab0ef264c27575a9aa", url="https://pypi.org/packages/c9/81/869527b2b3f7d9dd766d77cedbc43d4364986cb956ac181f91e12fd1f9c3/pyobjc-framework-AutomaticAssessmentConfiguration-9.0.1.tar.gz")
    version("9.0", sha256="1f86891b529a198544865fa393836cf898dc770e98e5e4eb8ec9dbe8f0aaf91c", url="https://pypi.org/packages/69/75/9720bf90f88b71212dae7edb6b60f804ea2c77e4898f37e4172d24a2ef1d/pyobjc-framework-AutomaticAssessmentConfiguration-9.0.tar.gz")
    version("8.5.1", sha256="a777b6fca1ce8953195ec68adfed8103646f72a1be32c4e6cd740f06280346aa", url="https://pypi.org/packages/74/f5/c291f614acc784a00e2347afb76ee8083817b03b8c66d8b5ec875f9d0b72/pyobjc-framework-AutomaticAssessmentConfiguration-8.5.1.tar.gz")
    version("8.5", sha256="ce67b419fa5adf994f6fc4d2a3dacf48e8b433ba09ce22af9b617d4bd97e4ebd", url="https://pypi.org/packages/dc/9f/1a599ba49c05e952022330f7a8f041a92f1ab6880d9e6ebe96a545e270f4/pyobjc-framework-AutomaticAssessmentConfiguration-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

