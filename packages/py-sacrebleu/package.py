# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySacrebleu(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.1", sha256="d24a783598ea5cfa2bb461cd377a5e3f76fa38a7df170bf99069fbd4c8157d25", url="https://pypi.org/packages/de/a5/bf9eddf90deeb7833bbb1ecd7cd4515245cc54c330b936d502ac531f9412/sacrebleu-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="fc7c34464a56d691bf5e37c4b5292142d2273b02516ac61e264cd19035fff981", url="https://pypi.org/packages/de/ea/025db0a39337b63d4728a900d262c39c3029b0fe76a9876ce6297b1aa6a0/sacrebleu-2.4.0-py3-none-any.whl")
    version("2.3.3", sha256="215422e29c615823281d7aa1c85c2955b9a810eee7c59909c605e8e62ee63478", url="https://pypi.org/packages/0a/a6/2ac47e71e526bbcd97ea08f20d9ef7d3852e2594ec7b2d55f5d2bbfd7aae/sacrebleu-2.3.3-py3-none-any.whl")
    version("2.3.2", sha256="ee8891d790cafbc8d3fe2a2ab2672b705fd856d287160040206785ded93a6e01", url="https://pypi.org/packages/df/c0/ff53cb76c1b050ad25d056877ba6d3f6fa964134370c4ccf57ad933d6f72/sacrebleu-2.3.2-py3-none-any.whl")
    version("2.3.1", sha256="352227b8ca9e04ed509266d1fee6c8cff0ea1417c429f8c684645ad2db8b02e7", url="https://pypi.org/packages/30/09/986d4df9ab18e7b12c145851491c89df4ef90f0d380f62bf4490aeb642a4/sacrebleu-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="e34ad8b8706be02b21e1a76974afbc66aa64a34933d708b0441b7d546efd4773", url="https://pypi.org/packages/46/7d/a187def38be97d0ed1399194b22af3617893fe41178eea4d7cda3fca523e/sacrebleu-2.3.0-py3-none-any.whl")
    version("2.2.1", sha256="3e73d81fe92fbb07a19447634898bc77501af060fa4d69e3fcd139db00e6e060", url="https://pypi.org/packages/6c/c4/fe3092828e1a6c4926823bbae31d9e671c1d7453171feda0b124f476126f/sacrebleu-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="2f9091da6639bff1b793b8dd0ec942aa30df08fa97d18697244b902e7eec6b5d", url="https://pypi.org/packages/f7/7e/fcf46053f73ab00ed4d9cf04433344def0d7e8d4ff3e2d5b8c480b6e1052/sacrebleu-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="0060b8df217d3c590d7f50b1813b5aeb766a7c9be1e939905ce6d25e6b663966", url="https://pypi.org/packages/65/35/4a31dd2fd8fe5ed780a086e7ac46d830ee9bd3fe34756b93175b2e0e3d76/sacrebleu-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="1acae0221e27c23c4987834fd17b284b4addc6556941c2097c4d618baa2d67af", url="https://pypi.org/packages/fa/63/b3c11f951eafa2dc296862431f29fb12dbe191cb72217cf88ed04c32086b/sacrebleu-2.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama", when="@2:")
        depends_on("py-lxml", when="@2.2:")
        depends_on("py-numpy@1.17.0:", when="@2:")
        depends_on("py-portalocker", when="@1.4:1.5.0,2:")
        depends_on("py-regex", when="@2:")
        depends_on("py-tabulate@0.8.9:", when="@2:")
    # END DEPENDENCIES

