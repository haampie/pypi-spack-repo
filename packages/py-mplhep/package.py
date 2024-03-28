# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMplhep(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.43", sha256="db055a4d6cba78be3a840a2895cae78c6e615a144c951bfbf7d16ac4bfc5275d", url="https://pypi.org/packages/27/25/870f324ab83804c2e70403d569f091f21589cb6eed2f9cfe6f4ce579c0d7/mplhep-0.3.43-py3-none-any.whl")
    version("0.3.42", sha256="a3b5c6ab12ddbcd0382ec4c1d7e46323cb6f7010c6e987bb9eb6c2addfc5171a", url="https://pypi.org/packages/4c/0e/2c797edf8c7859fe6eeb54d3e467bf588febea0922a548b3620fc8c28b18/mplhep-0.3.42-py3-none-any.whl")
    version("0.3.41", sha256="36b6fe89a3990ef8578b2035f2b0764d1243fc8fdd76ebcdc74159ed4b8a3178", url="https://pypi.org/packages/1e/0b/0a8a580d20c23a2b58c6d18128798eb1d7102acfc45d13f7f0fa81948363/mplhep-0.3.41-py3-none-any.whl")
    version("0.3.40", sha256="c8ea2a16bf466a64a5f3063a52993687abecc00ef4b595604bb397b9548df226", url="https://pypi.org/packages/7a/8d/9c16a7bcef0a72367da6ef302ce3f3536e0e63482ede9f7717eaf0983b45/mplhep-0.3.40-py3-none-any.whl")
    version("0.3.35", sha256="5748795a8ad576e4a1bc2eba0f5155d572333013f1bbf8e729eb36cde44a7cba", url="https://pypi.org/packages/1d/44/8548ab486b9b6cb6449f2e03840f1fc43d349777e3b88553c14be29dec47/mplhep-0.3.35-py3-none-any.whl")
    version("0.3.34", sha256="46563b0d9b2f115142b326966f448500f343269610a00169b0c508bce3fb9a74", url="https://pypi.org/packages/67/e3/4a824cb3f47b0b35732b672f43cf95f4f49fb7b427276cad696f87d56d77/mplhep-0.3.34-py3-none-any.whl")
    version("0.3.33", sha256="67a13b209919b8e9ce19b96cbb57e4e83538cdc3a0bd907c0b0d44e0d17aeb23", url="https://pypi.org/packages/34/76/dd77a18f5a6f427c89d8aed3b5bf8bbaf4a08cd9ae909cc4b004bdf8d23b/mplhep-0.3.33-py3-none-any.whl")
    version("0.3.32", sha256="c9e123721192481b10def37926d6dee666949b3f6b2ba9961b3beb0c30a1f81c", url="https://pypi.org/packages/30/a3/2c7f322e7c7c369edd5a895c59428b25274b0c7a43992d44033d0aca8f55/mplhep-0.3.32-py3-none-any.whl")
    version("0.3.31", sha256="60511b210051d389fbce47ecb10737f09d4c5ba1deb588366c440e536240b74c", url="https://pypi.org/packages/96/27/ae5b9cd87516763a8dac539911d160cc7a45f91f28b8010b026578a17960/mplhep-0.3.31-py3-none-any.whl")
    version("0.3.30", sha256="390c6d4b9964dce68125e110245db6386e60f642d00cc28bf87116c26ba066e8", url="https://pypi.org/packages/2e/bd/17d6262a0586317531a28d30a4100c8d148047cd2033d7def20ce495aca8/mplhep-0.3.30-py3-none-any.whl")
    version("0.3.26", sha256="1490d127e37f843579d0d5b643f053e6cf54d6966831211cd87246e3c532d70f", url="https://pypi.org/packages/94/08/99ac2ed8e6be593f8c3f2c593ed36db5c0f5acd27af2601f21fb7f309eb5/mplhep-0.3.26-py3-none-any.whl")
    version("0.3.15", sha256="d5719d19d247caa18916b93e4484cb1c519d8528fb09e1671094f947eaa407ab", url="https://pypi.org/packages/33/80/4888aa2686b6ef6de6b1275f442fd88f3ef2f6dba0cb21f452e605cb2f29/mplhep-0.3.15-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib@3.4.0:", when="@0.3:")
        depends_on("py-mplhep-data", when="@0.3:")
        depends_on("py-numpy@1.16.0:", when="@0.0.26:")
        depends_on("py-packaging", when="@0.0.26:")
        depends_on("py-scipy@1.1.0:", when="@0.0.26:0.2")
        depends_on("py-uhi@0.2:", when="@0.3:")
    # END DEPENDENCIES

