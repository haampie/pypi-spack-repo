##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIsodate(PythonPackage):
    version("0.6.1", sha256="0751eece944162659049d35f4f549ed815792b38793f07cf73381c1c87cbed96", url="https://pypi.org/packages/b6/85/7882d311924cbcfc70b1890780763e36ff0b140c7e51c110fc59a532f087/isodate-0.6.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="2e364a3d5759479cdb2d37cce6b9376ea504db2ff90252a2e5b7cc89cc9ff2d8", url="https://pypi.org/packages/b1/80/fb8c13a4cd38eb5021dc3741a9e588e4d1de88d895c1910c6fc8a08b7a70/isodate-0.6.0.tar.gz")
    version("0.5.4", sha256="42105c41d037246dc1987e36d96f3752ffd5c0c24834dd12e4fdbe1e79544e31", url="https://pypi.org/packages/f4/5b/fe03d46ced80639b7be9285492dc8ce069b841c0cebe5baacdd9b090b164/isodate-0.5.4.tar.gz")
    version("0.5.1", sha256="b12aed31c0e834543497e24d609a41531a800d8304c39e6665c45ca023b012fb", url="https://pypi.org/packages/4a/98/07f5bb685219005c3a5788ebe492561c44a75d6b690446667ab508ef070d/isodate-0.5.1.tar.gz")
    version("0.5.0", sha256="f3e436a9c321882942a6c62e9d8ea49787b4c0ea7f7bb3cbd047bcf76bd0dfbe", url="https://pypi.org/packages/25/5e/3b2c00046b65604520fb0aaf1bf1ee989010102446131c083b73771d7107/isodate-0.5.0.tar.gz")
    version("0.4.9", sha256="4e13c0b5824e9af40d99ad1d3969c880e49b6b09e4de138aa08db3d571b2190d", url="https://pypi.org/packages/bb/b2/282b0415c36cd9dc6bb64071ce0a13e1426097654b45eebdccebcd827d49/isodate-0.4.9.tar.gz")
    version("0.4.8", sha256="45b84949e4d1ef4c9e55e4516bf7c33707e8007b80bf62fc887d3c7320ab400b", url="https://pypi.org/packages/7b/5c/a1702a66eb07cf9b22f335215ee6d93d3bf3ed51f11459202f484773f907/isodate-0.4.8.tar.gz")
    version("0.4.7", sha256="62319ac34b2180d450a4d927873cb2600f3c13bce6b2077cdd770c77b3a987e1", url="https://pypi.org/packages/f2/59/d058a2caabe83e2ff2006877f1bb788ca8c58879794bcf30a79e2ca861dc/isodate-0.4.7.tar.gz")
    version("0.4.6", sha256="3a8463021311a7cb7b804106576f16357f251a372f70a4302c15425c0c4c06a8", url="https://pypi.org/packages/e9/7c/11bf76137474ac86c04ae4e295a50104cad55b834134ffa68695ed0109ea/isodate-0.4.6.tar.gz")
    version("0.4.5", sha256="d0b9bcccfd51b99193073cf4ed9cebd06d5cab1cbcd96510ccfcccaf155eeb5f", url="https://pypi.org/packages/f7/43/c4c954c6771c2180da046113e2a56f86db29e09347ffc86be983a81b0743/isodate-0.4.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@0.6.1:")
