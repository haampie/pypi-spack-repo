# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAse(PythonPackage):
    # BEGIN VERSIONS
    version("3.21.1", sha256="627deb46528efe1bac2bf873d1f0ca029943062960dff02cf3a05062964dfe5e", url="https://pypi.org/packages/a5/36/de17e79f29e06d9a92746d0dd9ec4636487ab03f6af10e78586aae533f7a/ase-3.21.1-py3-none-any.whl")
    version("3.21.0", sha256="7a756aba07c8e7c055bd3ba079facfc7f753c2c6e712a92b939dd1f1246ab74a", url="https://pypi.org/packages/f6/ad/5de9c50e7e4346f18f9020b6a5cf3ed3d4a47520a3bf6a6b0e5ae6b7d315/ase-3.21.0-py3-none-any.whl")
    version("3.20.1", sha256="107f504923f21908fe4c153b9a5ea2bf2984bd91866530172d958df91750599d", url="https://pypi.org/packages/51/78/edadb45c7f26f8fbb99da81feadb561c26bb0393b6c5d1ac200ecdc12d61/ase-3.20.1-py3-none-any.whl")
    version("3.19.3", sha256="4cb2dc9c9c7a2724d17e0da09d3e02defb42214ff11952a243b3dcf3875dafdf", url="https://pypi.org/packages/12/c2/7d91eccb0f4ab6f53b014b766bf4761afb69d19066b4f6b1dcc49c31eba7/ase-3.19.3-py3-none-any.whl")
    version("3.19.2", sha256="ca7fd385d6f3cd26cf43cf24709c423715565f9179327e7fef118f7128f32b56", url="https://pypi.org/packages/3c/46/62799e6924b21e7969508d17f34e841330dacdbe9a7320b1ce680f676397/ase-3.19.2-py3-none-any.whl")
    version("3.19.1", sha256="c27eac75027747131fb356aa6b94c95817d4c25f8e086f12773895aad86fccc2", url="https://pypi.org/packages/d0/70/a8b1a7831193aa228defd805891c534d3e4717c8988147522e673458ddce/ase-3.19.1-py3-none-any.whl")
    version("3.19.0", sha256="0c1d31802af129462e621a0714d6227eb9a31bcd11787821d88d481d47805baf", url="https://pypi.org/packages/5a/2f/b1f08bea98e5139a3e44029998c68c6e44f20a0504fc56ca6549e408e5f0/ase-3.19.0-py3-none-any.whl")
    version("3.18.2", sha256="4c6eb37027d53df623437ebbd082d1b476975b72e9e079ed92e3066f78196399", url="https://pypi.org/packages/6b/4c/744a93b4e58bb670aa492f294ea80f1b36bcee88a1150d26a7a20225a253/ase-3.18.2-py3-none-any.whl")
    version("3.18.1", sha256="e2cb7d80aa03c1eadbc2e181376b954dab03cf36b069caa6e6566463664fb973", url="https://pypi.org/packages/fc/cb/314601dc48d55c7c9c4f481f3099669c0f496da7c9fdddecfe74b2fdc6b2/ase-3.18.1-py3-none-any.whl")
    version("3.18.0", sha256="c5a5295788050ff679c6d316ad5358753bb07ecdc5714139661c29379571a372", url="https://pypi.org/packages/c6/06/ccbdfa2a7ba6b12e1225d98efc930cc244d8673885c00dab89e8bed79037/ase-3.18.0-py3-none-any.whl")
    version("3.15.0", sha256="9c3a01eecf8a827583e8d789df6237e1f943246a7ba679a7a1fd40582bd298c9", url="https://pypi.org/packages/d2/d0/d819b98529a190f2b34a90e8081628de2cb3432660a4025f11471e9a0ec6/ase-3.15.0-py3-none-any.whl")
    version("3.13.0", sha256="c4046c50debac28415b36616d79aa28e68ae2cd03c013c2aed6a1e3d465c0ee1", url="https://pypi.org/packages/84/a8/664c99fc94510163b5289c8e475660182f0f6ba098c549879bc5d36c17fd/ase-3.13.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flask", when="@3.14:3.18.0")
        depends_on("py-matplotlib@2.0.0:", when="@3.20:3.21")
        depends_on("py-matplotlib", when="@3.14:3.19")
        depends_on("py-numpy@1.11.3:", when="@3.20:3.21")
        depends_on("py-numpy", when="@3.14:3.19")
        depends_on("py-scipy@0.18.1:", when="@3.20:3.21")
        depends_on("py-scipy", when="@3.14:3.19")
    # END DEPENDENCIES

