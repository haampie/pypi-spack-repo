##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGooglePasta(PythonPackage):
    version("0.2.0", sha256="c9f2c8dfc8f96d0d5808299920721be30c9eec37f2389f28904f454565c8a16e", url="https://pypi.org/packages/35/4a/0bd53b36ff0323d10d5f24ebd67af2de10a1117f5cf4d7add90df92756f1/google-pasta-0.2.0.tar.gz")
    version("0.1.8", sha256="713813a9f7d6589e5defdaf21e80e4392eb124662f8bd829acd51a4f8735c0cb", url="https://pypi.org/packages/57/ac/aebe06c6a3154ce21fe82d42f31511ababe87dc30c1b041716493e061633/google-pasta-0.1.8.tar.gz")
    version("0.1.7", sha256="79d1ce28b381d68e98ef7707d19909adb58912f8dae8734402454424fc76b8fe", url="https://pypi.org/packages/7a/4e/c3e35716d57eba02e49b8ad72a744435df1935f189fbc5f47edafb6d4f00/google-pasta-0.1.7.tar.gz")
    version("0.1.6", sha256="445b38ff8aeb8e140aaefc9b18e7766b9170efe8f3ca8632cc5e3ed9b2546f53", url="https://pypi.org/packages/32/61/bb45132e517e06c3c5a11cc39fd9325a6bb743d546efb5289604834aa68b/google-pasta-0.1.6.tar.gz")
    version("0.1.5", sha256="2add9541d443d03e57c7841b5c35815779711b23ea1418bd4bc981d0373467d3", url="https://pypi.org/packages/b2/86/c3655f1c7c8bf42e84c0f9cb9ea13e7528c92cc3b08320c3cd911095eacb/google-pasta-0.1.5.tar.gz")
    version("0.1.4", sha256="670eb10b52ad5febaf1b351f634478f9bcac0b0e52146e8a9efd4a1783a2c05c", url="https://pypi.org/packages/4b/74/b77ad523562fd532b48b3e9d3c9e587a3b68cdf1a7997fc7566eae88f296/google-pasta-0.1.4.tar.gz")
    version("0.1.3", sha256="36bf8616c17cbb93d91572b5812dcd5aef4b7d8f3f3582e67a087363c4de9fb1", url="https://pypi.org/packages/32/e4/07c122bb7946bcafa418e1af6601e5fe24a00e5fc38e956d85d3a70378f8/google-pasta-0.1.3.tar.gz")
    version("0.1.2", sha256="b8e7d4f557c855629cfa2da9a1779e8206a494b52e520ea1cac0971bf7434004", url="https://pypi.org/packages/72/d6/5a91414e76220dbca90f5b455a7c6d85b0bff2baba266e86a8513c3fb966/google-pasta-0.1.2.tar.gz")
    version("0.1.1", sha256="cadf1c869bd78fbf8ff2b89aaad05b2a79d8ccf48f7dd84cb0bf4ad8e917b6a3", url="https://pypi.org/packages/90/7c/57de8b68f3c77f785f02ba0921746af8aefd3206021f29194e19bf8dc6c5/google-pasta-0.1.1.tar.gz")
    version("0.1", sha256="5a65ad5977a074e4aa2be28e8f8dd2afc6c5520bae08e3e0bc4bbc6902fb41d8", url="https://pypi.org/packages/9e/50/1ef3b6b3ef4405135c7e76041a699194000d8c9e878a1a50462d4d66437d/google-pasta-0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@0.1.8:")

