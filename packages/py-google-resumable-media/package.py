##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleResumableMedia(PythonPackage):
    version("2.7.0", sha256="79543cfe433b63fd81c0844b7803aba1bb8950b47bedf7d980c38fa123937e08", url="https://pypi.org/packages/b2/c6/1202ef64a9336d846f713107dac1c7a0b016cb3840ca3d5615c7005a23d1/google_resumable_media-2.7.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="fc03d344381970f79eebb632a3c18bb1828593a2dc5572b5f90115ef7d11e81b", url="https://pypi.org/packages/c7/4f/b8e5e22406e5aeafa46df8799939d5eeee52f18eeed339675167fac6603a/google_resumable_media-2.6.0-py2.py3-none-any.whl")
    version("2.5.0", sha256="da1bd943e2e114a56d85d6848497ebf9be6a14d3db23e9fc57581e7c3e8170ec", url="https://pypi.org/packages/a8/84/b8c526864e53ee265516453015f707432448546c525dcf2b89bfd6c67245/google_resumable_media-2.5.0-py2.py3-none-any.whl")
    version("2.4.1", sha256="831e86fd78d302c1a034730a0c6e5369dd11d37bad73fa69ca8998460d5bae8d", url="https://pypi.org/packages/0b/d8/9a46125189d955ff50228351848019aef51775787db59373fefb20b09b3b/google_resumable_media-2.4.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="2aa004c16d295c8f6c33b2b4788ba59d366677c0a25ae7382436cb30f776deaa", url="https://pypi.org/packages/4f/8e/5f42ac809ad8bccca7060132a274d714fbf4e2ef8f2424ef2301a2dbc4fb/google_resumable_media-2.4.0-py2.py3-none-any.whl")
    version("2.3.3", sha256="5b52774ea7a829a8cdaa8bd2d4c3d4bc660c91b30857ab2668d0eb830f4ea8c5", url="https://pypi.org/packages/02/a3/19447ef22fdaccf773c395add9d200a6dacba3d39742d9ede0cc67c51874/google_resumable_media-2.3.3-py2.py3-none-any.whl")
    version("2.3.2", sha256="3c13f84813861ac8f5b6371254bdd437076bf1f3bac527a9f3fd123a70166f52", url="https://pypi.org/packages/b5/70/92b07646d384f1de8544b9bee7ecc19ca567c3813e458b7fcc6a4b8168b1/google_resumable_media-2.3.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="7465f228b1d4b79f6048403b7873e1167d2ee31ae3e552fc0698a9a8789e594c", url="https://pypi.org/packages/c3/35/a4df0c4a8ddc4117ef1329685a898756c3f9d91d1555627d9593c63783bd/google_resumable_media-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="36dc2f7201ee1cb360ef502187aa4e1f2b6ec4467fcee92e08a8cf165e36f587", url="https://pypi.org/packages/b4/fa/9a731d420f68d883e3103c2d47874cf620409561db4b218729935ba3c3b4/google_resumable_media-2.3.0-py2.py3-none-any.whl")
    version("2.2.1", sha256="fd616af31b83d48da040c8c09b6994606e1734efb8af9acc97cf5d6070e9ba72", url="https://pypi.org/packages/00/b1/e3cbb920c46a838d67915e65fcb40b83aa70c0a2da0b6812b5f534234529/google_resumable_media-2.2.1-py2.py3-none-any.whl")
    version("0.3.2", sha256="2dae98ee716efe799db3578a7b902fbf5592fc5c77d3c0906fc4ef9b1b930861", url="https://pypi.org/packages/e2/5d/4bc5c28c252a62efe69ed1a1561da92bd5af8eca0cdcdf8e60354fae9b29/google_resumable_media-0.3.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-crc32c@1:", when="@1:2.0.1,2.0.3:")
        depends_on("py-six", when="@:1.3.0")

