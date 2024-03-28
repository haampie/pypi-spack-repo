# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAioftp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.22.3", sha256="93d17d5d3b8033570f2dfee013172d49e52323437925120ec87190539113ebd0", url="https://pypi.org/packages/0f/5f/81bb77d4e2e5569106f2b9420d126d3c5531f4dc33a772ddd9eea57e03aa/aioftp-0.22.3-py3-none-any.whl")
    version("0.22.2", sha256="0764933053f6652d27504917824bbf4f41445e99b78b52f44f36f34bf80f3740", url="https://pypi.org/packages/f4/0c/291e0ab27392f380bdfc8fab3180da7b5365dcff3b76c614cee87ca30c36/aioftp-0.22.2-py3-none-any.whl")
    version("0.21.4", sha256="ad7c1136754799808fca890ea41ea7ec8fcd1bb5167a1f46e04db15267242324", url="https://pypi.org/packages/90/d3/211850ff64f9035e27eeb8aaffc37ed66e12870949c5aee0f2414d704749/aioftp-0.21.4-py3-none-any.whl")
    version("0.21.3", sha256="7c07ddc959e3ed30bdf5d5373da9d5ee9b7871e2d81835073132acd472b84b01", url="https://pypi.org/packages/26/96/0533c7f3520fb82bd39cfb343a7b3d23a566066de68c3886c0572b686ea6/aioftp-0.21.3-py3-none-any.whl")
    version("0.21.2", sha256="2f07cba5923e40427100bd7ea7913900b346d5b3c58f6f11dbfa227418bbd406", url="https://pypi.org/packages/2f/dc/23a08166993b6e6d4592b8354e882dd9d4923fa9808e96a7cdac1d301ed3/aioftp-0.21.2-py3-none-any.whl")
    version("0.21.1", sha256="c4c4dd6e3673f4c7d350505905cacb7bba15e99091901e5d512be79f87e29f2e", url="https://pypi.org/packages/db/9d/6ef461dcec42bc0f0193f1cd526ad0251e829ed512c390dca0762c075dd5/aioftp-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="b0e2bc1da5df2ae4ad469db58681d34904047ba8a5f36e9980e6649371c9a824", url="https://pypi.org/packages/7a/35/ed6c209cce24387445f258c369f73bbcc17c462ac26a643aaae2b0ce3fc6/aioftp-0.21.0-py3-none-any.whl")
    version("0.20.1", sha256="70eb8f12eb0ac43afa5ba313261efe7e5a70df9b92c18fae00192e08be1923d6", url="https://pypi.org/packages/5d/f8/6f8153ec5cb9a5128d365ee0dde79bc542470d2064e592c9a680a49a2877/aioftp-0.20.1-py3-none-any.whl")
    version("0.20.0", sha256="3414f263a5fe2dd7619c60410a958d097a1ab6ba2b50db8d9618f321e3a928e5", url="https://pypi.org/packages/52/77/34d3abb5d248746e3f6e4dec1540bf649ccde1b8e3c4ee8a9b188219c23c/aioftp-0.20.0-py3-none-any.whl")
    version("0.19.0", sha256="9d736502735999581f6cb4caaed0fa5ec4e138a1b8b039ca1c711659ea0be5c5", url="https://pypi.org/packages/26/15/dc740c10c1c8d9f0fa2f982cb666e4ec759d1cde24a99ade7c4386aadaca/aioftp-0.19.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@0.22:0.22.2")
    # END DEPENDENCIES

