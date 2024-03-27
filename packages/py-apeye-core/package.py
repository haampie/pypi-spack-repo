##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApeyeCore(PythonPackage):
    version("1.1.5", sha256="dc27a93f8c9e246b3b238c5ea51edf6115ab2618ef029b9f2d9a190ec8228fbf", url="https://pypi.org/packages/77/9f/fa9971d2a0c6fef64c87ba362a493a4f230eff4ea8dfb9f4c7cbdf71892e/apeye_core-1.1.5-py3-none-any.whl")
    version("1.1.4", sha256="084bc696448d3ac428fece41c1f2eb08fa9d9ce1d1b2f4d43187e3def4528a60", url="https://pypi.org/packages/f4/af/7cfe2c5e01d70848ac1731c8ab37e0e49ab39cf18e595446c192349639c0/apeye_core-1.1.4-py3-none-any.whl")
    version("1.1.3", sha256="c9210d7701f62a8a42f44007fafb0d20acc397284d24790f877ee89f0d6325e7", url="https://pypi.org/packages/46/b8/2c0863c670cd4d5be636a3123e365b2f102dbbbfe6aeac3af0c4ae47e57d/apeye_core-1.1.3-py3-none-any.whl")
    version("1.1.2", sha256="7c38930ecc9a9bf002187a7d59fedd7442f995013fa1cd9501e4564d600886f6", url="https://pypi.org/packages/a8/63/dc06f9f7ecb82f42a900b9961a06284428fd265be8390efdb7f7566e1d25/apeye_core-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="3a5d61889a40a8b71394cd7d15ece7e6af3ec2f8450c3f5c2d5c4881fcae8743", url="https://pypi.org/packages/f2/c8/af7592f7ed0a2163e95c3020320851de407f4b9eb5477526f7c3ff54d9c4/apeye_core-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="b711fa1f2df30ec39f4e555cfca9c76120a643b8274397bf67dd6904066a4ae2", url="https://pypi.org/packages/21/f3/f0fceb16d02b9d27c75baebc4f8eacf8d5c61f4765d580965a746ae267a7/apeye_core-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="11e7c51e8ebb71524d24e72e3122f7f625e31b0a759cd554ce2a6b166fceec86", url="https://pypi.org/packages/be/cb/3c60baa0d4fe09025c07bb68c29f1c0566faa954cf86e11ffc5e989f558c/apeye_core-1.0.0-py3-none-any.whl")
    version("1.0.0-beta2", sha256="80ee0c4421bfbb8bd8cec191b9d27f21f504b0a72594da7493ed4bc16df81f4c", url="https://pypi.org/packages/03/3c/fe632ec446e2834e1b687ff6dc729d20860c608935b10ecae645279a3747/apeye_core-1.0.0b2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-domdf-python-tools@2.6:")
        depends_on("py-idna@2.5:")

