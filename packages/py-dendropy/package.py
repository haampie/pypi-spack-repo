# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDendropy(PythonPackage):
    # BEGIN VERSIONS
    version("4.6.1", sha256="8527a208482302642e7e38229a2369d01a51d05011e9a68067d92be5fbbf6b58", url="https://pypi.org/packages/7c/3b/f880fd07cb79a46ca838e46ba021fcdaa464bb21e2a9264a7afe77046a88/DendroPy-4.6.1-py3-none-any.whl")
    version("4.6.0", sha256="c4361b8348ca7d787e827f544888bf5ed034d62a4ea4473e40f0a9ad67039964", url="https://pypi.org/packages/b0/c0/841e46da39a4dae07a5cd4e7a1c9472acbdd623f820b125b5995dd342c9a/DendroPy-4.6.0-py3-none-any.whl")
    version("4.5.2", sha256="3e5d2522170058ebc8d1ee63a7f2d25b915e34957dc02693ebfdc15f347a0101", url="https://pypi.org/packages/f9/10/125c181b1d97ffc4661a60ec897cfe058dc46cb53900d807819464c3510f/DendroPy-4.5.2.tar.gz")
    version("4.5.1", sha256="3503b170ba4830239dfa93371d210367a3be5825c3cb23ad7504a0feb3be7dbe", url="https://pypi.org/packages/e0/f3/222e939e250e71234031d182e58704fff1c3296140f91f70d7ef8b3e17a6/DendroPy-4.5.1.tar.gz")
    version("4.4.0", sha256="f0a0e2ce78b3ed213d6c1791332d57778b7f63d602430c1548a5d822acf2799c", url="https://pypi.org/packages/f5/21/17e4fbb1c2a68421eec43930b1e118660c7483229f1b28ba4402e8856884/DendroPy-4.4.0.tar.gz")
    version("4.3.0", sha256="bd5b35ce1a1c9253209b7b5f3939ac22beaa70e787f8129149b4f7ffe865d510", url="https://pypi.org/packages/58/14/d4559893d72675b322c1d60229ef3490bc5c2f5b28c5cc339956aaf8f507/DendroPy-4.3.0.tar.gz")
    version("4.2.0", sha256="f790bb3d63b0a0573ff4b2657e4f745c94a3d46eaae0ddb5a429b857dad08795", url="https://pypi.org/packages/e6/5a/d48c8d3f8100efd5eb6e6142f28bf1c13200e08882e59596369035ebc138/DendroPy-4.2.0.tar.gz")
    version("4.1.0", sha256="c3d4b2780b84fb6ad64a8350855b2d762cabe45ecffbc04318f07214ee3bdfc9", url="https://pypi.org/packages/65/3a/19556a58c560de488dffbf3c7fe7c9ed34c1a6223f0dfe971224a42aaf39/DendroPy-4.1.0.tar.gz")
    version("4.0.3", sha256="a2c074eb91e2866120521c076587983900c5b312879832c3559effb730bd4465", url="https://pypi.org/packages/66/0b/72ca62a6e87ddb9b70cac2cf1fc199ca00127fc168c52bcbcbf30cfb5947/DendroPy-4.0.3.tar.gz")
    version("4.0.2", sha256="b118c9e3e9408f2727e374032f6743a630e8a9239d84f898ed08cd5e68c5238d", url="https://pypi.org/packages/62/10/117c87b76f5f84d4559bd7ad25af04f11369ef8267f3c8e7d62769efc85d/DendroPy-4.0.2.tar.gz")
    version("3.12.0", sha256="38a0f36f2f7aae43ec5599408b0d0a4c80996b749589f025940d955a70fc82d4", url="https://pypi.org/packages/43/22/69b7713b094697f8a432abe96c44a155519ef67b3c31221de32f4c3d5fa5/DendroPy-3.12.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@4.6:")
    # END DEPENDENCIES

