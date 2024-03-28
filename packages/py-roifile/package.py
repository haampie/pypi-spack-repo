# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRoifile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2024.3.20", sha256="84b0af1394d0f0e50d04a5b107e64bf90f9712c1102ee397103f6a71917b974d", url="https://pypi.org/packages/b8/0d/c8881882852416d0d9bcd96bc6a1a54e80f6bae0eeba5c96c7b39f1e0403/roifile-2024.3.20-py3-none-any.whl")
    version("2024.1.10", sha256="0dde8f4d0971439cc373250b8a312c0acf662249560161d61a191d0d09af1aa1", url="https://pypi.org/packages/d2/9a/edfa8073b0e656d358f0ca66bd09cc1caaafc1208b6004a39053883f4674/roifile-2024.1.10-py3-none-any.whl")
    version("2023.8.30", sha256="14d04b2d4b46b8d326ec18e0fe5e4e9448cb6d6731efb6953eac969aef091277", url="https://pypi.org/packages/fd/15/6918cb0d6a3938602dc1fd116a93330e3c49a2e9f12891228ab2f990e20d/roifile-2023.8.30-py3-none-any.whl")
    version("2023.5.12", sha256="bc8d08b4ace913d4d8128083b5337fa5be7b1997dd1b061fe1df151c2d360242", url="https://pypi.org/packages/86/d3/8d8025b959e53bf040ec397674e1aa20e7270fbcc50619a07aef5099debd/roifile-2023.5.12-py3-none-any.whl")
    version("2023.2.12", sha256="3b8b99fee19cde4506ab30d3b7dda68a066ae132aa191edbafc1b6b3606d4393", url="https://pypi.org/packages/21/af/2b3327426a244bf3ab0606f5728d30d8a276ba4bf24a1e83469db20935cc/roifile-2023.2.12-py3-none-any.whl")
    version("2022.9.19", sha256="0ea5147aee645dcb24764b02f258ffb49acae45a3c834f335965363d214230a8", url="https://pypi.org/packages/be/a6/ee05ecd329a8dff2e0a31d4e1fc5959b93d9f0e9edce75d679d4e5a4c113/roifile-2022.9.19-py3-none-any.whl")
    version("2022.7.29", sha256="13c59540286c46a115e63e86596755d8b5f2b08b7e0642117592b03be7b2b863", url="https://pypi.org/packages/54/cc/804d335b8e8909c60508d857db1d5a59b14afc58419c319ad54783d484b8/roifile-2022.7.29-py3-none-any.whl")
    version("2022.3.18", sha256="d27cb94daeda42a5d81d1365c2f043e73cdf344db25f4d247b06c0dd3c14a2ca", url="https://pypi.org/packages/df/40/d4dead60aa88f0bebbc5934dd62995fc0c0d3a665c93842fe4f50d27f9eb/roifile-2022.3.18-py3-none-any.whl")
    version("2022.2.2", sha256="f606541901bddcbbe3932036cf7ca0f78deaec26c98e3c8835cb25c8cca69755", url="https://pypi.org/packages/cd/44/627d82a1f72d86d4a3e51a3b80cf7a392d497a633f06448b64a6d07f6b46/roifile-2022.2.2-py3-none-any.whl")
    version("2021.6.6", sha256="f5c8878d63b660aaa80176b19d3fb451f6c403802e916e93fd1be171a0d402c3", url="https://pypi.org/packages/87/67/fc55adb049a2697fbcd4b9091ab11f4dba28bb8ce94a1445782e0813e448/roifile-2021.6.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("all", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.8:")
        depends_on("py-matplotlib", when="@2023.5:+all")
        depends_on("py-matplotlib@3.3.0:", when="@2022:2023.2+all")
        depends_on("py-matplotlib@3.2.0:", when="@2020.11:2021+all")
        depends_on("py-numpy", when="@2023.5:")
        depends_on("py-numpy@1.19.2:", when="@2022:2023.2")
        depends_on("py-numpy@1.15.1:", when="@2020.5:2021")
        depends_on("py-tifffile", when="@2023.5:+all")
        depends_on("py-tifffile@2021.11:", when="@2022:2023.2+all")
        depends_on("py-tifffile@2020.6:", when="@2020.8:2021+all")
    # END DEPENDENCIES

