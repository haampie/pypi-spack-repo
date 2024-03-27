##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyroPpl(PythonPackage):
    version("1.9.0", sha256="33e63fcd4df7a81aa295b6d9ce572751921b5ad2803f5c2b30692c824d2cc90d", url="https://pypi.org/packages/23/2c/8e5a735ac4e6ea43af20d90d18668674831cabec25d5109f569bafb062e2/pyro_ppl-1.9.0-py3-none-any.whl")
    version("1.8.6", sha256="18a28febe1be9c42af94a684c2971a798f2acb51f77b07e8430f146eafe11fed", url="https://pypi.org/packages/f2/93/59bced321ede6eeb60061f156df8aae3f4832127fe97f4e86c567ad3b9cc/pyro_ppl-1.8.6-py3-none-any.whl")
    version("1.8.5", sha256="09616269053f45b9c230ed6bcfbde199b9c308780d972b863ef7bdb707a1c346", url="https://pypi.org/packages/1e/59/cbfb15b4d9b3b04fe05e33d3b9b9662ef3e324225d528a538cc1bc1db28b/pyro_ppl-1.8.5-py3-none-any.whl")
    version("1.8.4", sha256="294f78f28f2fe7bbea2792bd6bd8c69b7cfe493cf8940cac97a9b5d0e7f194cd", url="https://pypi.org/packages/b5/b1/ccceeae368b7e2b5504229e74ad584e4b8071faeef23b0e888d1c9d8ef3d/pyro_ppl-1.8.4-py3-none-any.whl")
    version("1.8.3", sha256="cf642cb8bd1a54ad9c69960a5910e423b33f5de3480589b5dcc5f11236b403fb", url="https://pypi.org/packages/21/71/aa3bad6429b9e3a1c78e64539cc8d7a1e0437f4298c68b1535b010abe77b/pyro_ppl-1.8.3-py3-none-any.whl")
    version("1.8.2", sha256="246f580fca1f0ae5b1453b319a4ee932048dbbfadaf23673c7ea1c0966daec78", url="https://pypi.org/packages/f5/6a/158c1394809eb09316e14ffe8b63c0eec21cedcfcbc67f99c3428b86bb2d/pyro_ppl-1.8.2-py3-none-any.whl")
    version("1.8.1", sha256="ca01ab4565eb9a1af4a60dbc481da5cb6f5fe5a72efa19e83638e03683efbca6", url="https://pypi.org/packages/68/01/507d1b150701800d90d45f3ba06c296a0e1eaa7f3caba4db15d7495ff6bb/pyro_ppl-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="69e234faf37b9752eef7f780cb6e2b2489e88abc34dfa4706eb92c8f6b811cf6", url="https://pypi.org/packages/aa/a0/c94b31968713f1bbb8978094cb65ef992ac09e6637f905d7062467bceba8/pyro_ppl-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="de5fb8cd4691c260f8dd9fb36e666b23b926b460552c09c2860f1d26c8bd280a", url="https://pypi.org/packages/df/fa/19121468eacf215d15192305a31c40633d4c83231ef9a87b5ef78e992984/pyro_ppl-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="0cc15c4bae3b25d6b3b3b674de6721e5572db6f0805bb2cdb766a53aa2ab3221", url="https://pypi.org/packages/aa/7a/fbab572fd385154a0c07b0fa138683aa52e14603bb83d37b198e5f9269b1/pyro_ppl-1.6.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-graphviz@0.8:", when="@0.5.1:1.0")
        depends_on("py-numpy@1.7:", when="@0.5.1:")
        depends_on("py-opt-einsum@2.3.2:", when="@0.5.1:")
        depends_on("py-pyro-api@0.1.1:", when="@0.5.1:")
        depends_on("py-torch@2:", when="@1.9:")
        depends_on("py-torch@2.0.1:", when="@1.8.5")
        depends_on("py-torch@1.11:", when="@1.8.1:1.8.4,1.8.6:1.8")
        depends_on("py-torch@1.9:", when="@1.7:1.8.0")
        depends_on("py-torch@1.8:", when="@1.6")
        depends_on("py-tqdm@4.36:", when="@0.5.1:")

