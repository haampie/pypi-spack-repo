# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMatplotlibInline(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.6", sha256="f1f41aab5328aa5aaea9b16d083b128102f8712542f819fe7e6a420ff581b311", url="https://pypi.org/packages/f2/51/c34d7a1d528efaae3d8ddb18ef45a41f284eacf9e514523b191b7d0872cc/matplotlib_inline-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="a68624e181d5b272bbfbaadb44412c9d3c9ebbcb703404502b9c937afc377ff5", url="https://pypi.org/packages/82/91/e6a5eb59cb0b37c97db24f01144709be49e1c1be83ae7d463cde14914ad5/matplotlib_inline-0.1.5-py3-none-any.whl")
    version("0.1.4", sha256="d005283ebadff51fe2b84ebdb211f50d45b910fba3a473c39c8fca172a750860", url="https://pypi.org/packages/ed/57/ec973a6615e7a863b371ed084fa78b5999a6cc38cc0b4916813549cef087/matplotlib_inline-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="aed605ba3b72462d64d475a21a9296f400a19c4f74a31b59103d2a99ffd5aa5c", url="https://pypi.org/packages/a6/2d/2230afd570c70074e80fd06857ba2bdc5f10c055bd9125665fe276fadb67/matplotlib_inline-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="5cf1176f554abb4fa98cb362aa2b55c500147e4bdbb07e3fda359143e1da0811", url="https://pypi.org/packages/7f/de/6c111d687335729cf8c156394c8d119b0dc3c34b6966ff2a2f7fe4aa79cf/matplotlib_inline-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="82e6dfdd8dd60617572d272ddbdcaeb504b8507ae640d63af6d52539cabc2bdc", url="https://pypi.org/packages/9b/d6/4eac213bd86ac1b82564c78df57e4b05b709e3a4f5e85ef805a6a4722e08/matplotlib_inline-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="760376455eae04c47ee343d02430c434ef583667d2b3a2703c31f093baac2173", url="https://pypi.org/packages/2a/4b/12160555fbf82de281a3edc9d31744b667bfb5ad33bdfa5841f75306778c/matplotlib_inline-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipython", when="@:0.1.1")
        depends_on("py-matplotlib", when="@:0.1.0")
        depends_on("py-traitlets")
    # END DEPENDENCIES

