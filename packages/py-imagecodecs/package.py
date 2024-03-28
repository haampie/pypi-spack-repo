# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImagecodecs(PythonPackage):
    # BEGIN VERSIONS
    version("2024.1.1", sha256="fde46bd698d008255deef5411c59b35c0e875295e835bf6079f7e2ab22f216eb", url="https://pypi.org/packages/92/e3/e17c8b9703dc467041ac76d41fe18f67d877ea0ab35d8fac2046e3873945/imagecodecs-2024.1.1.tar.gz")
    version("2023.9.18", sha256="bf4b4be4759fc3b27b5022228aada83e735744e4b7c204bcdccaa961c3f79d4d", url="https://pypi.org/packages/5e/a7/394dd3fe67042c4234a74c47d4bf0b3f436d9af6c7fb5c889c3fd55f687a/imagecodecs-2023.9.18.tar.gz")
    version("2023.9.4", sha256="1f09a2f9df6f6e29abbe2a20a1e7f5990edd1bd2c02dcb0611c841ffc5b8b178", url="https://pypi.org/packages/dc/e5/4f8a026d95b5973bcca7640a0448e7d7df7ed0f54ee89bbba74945789936/imagecodecs-2023.9.4.tar.gz")
    version("2023.8.12", sha256="5410ccd1e6f46289c10c076579d38f621b4aaa207d54d93aeb338c5fbcdea709", url="https://pypi.org/packages/15/15/5a860abd98ad629ef4967e6aa377e91946fd79661a003752e850735e99af/imagecodecs-2023.8.12.tar.gz")
    version("2023.7.10", sha256="cce1b815e55c4cda67582b87fbf4e2b3caa2dd447b1cdb33fa4f8ccafea8064a", url="https://pypi.org/packages/a6/a7/259d654b464f55c3d345a5f489e97bab75942b3b57a331f4332f39bff18f/imagecodecs-2023.7.10.tar.gz")
    version("2023.7.4", sha256="8c45a63d2dea712b5bc3c763771540510303018168531c01e0d89573b6d1043a", url="https://pypi.org/packages/43/f2/559721c2957d1873e1471b1b31699ed3f6eaa6df168e5cc03242764cbaa5/imagecodecs-2023.7.4.tar.gz")
    version("2023.3.16", sha256="e39c2a63f7f5b9bee0ba4961db8c1e7f2518ce07d2fd10a56624d17f1407efc1", url="https://pypi.org/packages/0a/63/c29f3e6677883f97a9988a31f61523b9a40b9fb00c10f1a99935403d3a32/imagecodecs-2023.3.16.tar.gz")
    version("2023.1.23", sha256="1b4591839a2f5c90467e50ebe54117cbd9be42c18864abdf85fc7743223ac5b2", url="https://pypi.org/packages/fa/81/2ac000a536323e9ac0ae785be8f16eeaf6cb95c33d024d5483fa7161291f/imagecodecs-2023.1.23.tar.gz")
    version("2022.12.24", sha256="c5282a808786dadb8e3ee238bb213b2e065574f1bb0f4b51e8bf93747e0babb3", url="https://pypi.org/packages/ed/bb/34abf4c2c9aaac8a449696872eed1202df7dc68a5f43f7ff43528208d8b1/imagecodecs-2022.12.24.tar.gz")
    version("2022.12.22", sha256="c685eb1fbd004918980aa3314e4c2ac22e931130943a83a55912020d720cd731", url="https://pypi.org/packages/58/fa/31fa49734b05d770c9ed14df9a5105999804bc91e979af142bdf27daa818/imagecodecs-2022.12.22.tar.gz")
    version("2022.2.22", sha256="062bef6b003290a8163abed2744b406854238208dfdd41cf7165253c6e01c0bd", url="https://pypi.org/packages/59/2d/344eaece340a87945b22dff57afb954487772394b801486c01184c4684ce/imagecodecs-2022.2.22.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.7:")
        depends_on("py-numpy", when="@2023.9.18:")
    # END DEPENDENCIES

