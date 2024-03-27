##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPillow(PythonPackage):
    version("10.2.0", sha256="e87f0b2c78157e12d7686b27d63c070fd65d994e8ddae6f328e0dcf4a0cd007e", url="https://pypi.org/packages/f8/3e/32cbd0129a28686621434cbf17bb64bf1458bfb838f1f668262fefce145c/pillow-10.2.0.tar.gz")
    version("10.1.0", sha256="e6bf8de6c36ed96c86ea3b6e1d5273c53f46ef518a062464cd7ef5dd2cf92e38", url="https://pypi.org/packages/80/d7/c4b258c9098b469c4a4e77b0a99b5f4fd21e359c2e486c977d231f52fc71/Pillow-10.1.0.tar.gz")
    version("10.0.1", sha256="d72967b06be9300fed5cfbc8b5bafceec48bf7cdc7dab66b1d2549035287191d", url="https://pypi.org/packages/64/9e/7e638579cce7dc346632f020914141a164a872be813481f058883ee8d421/Pillow-10.0.1.tar.gz")
    version("10.0.0", sha256="9c82b5b3e043c7af0d95792d0d20ccf68f61a1fec6b3530e718b688422727396", url="https://pypi.org/packages/0f/8b/2ebaf9adcf4260c00f842154865f8730cf745906aa5dd499141fb6063e26/Pillow-10.0.0.tar.gz")
    version("9.5.0", sha256="bf548479d336726d7a0eceb6e767e179fbde37833ae42794602631a070d630f1", url="https://pypi.org/packages/00/d5/4903f310765e0ff2b8e91ffe55031ac6af77d982f0156061e20a4d1a8b2d/Pillow-9.5.0.tar.gz")
    version("9.4.0", sha256="a1c2d7780448eb93fbcc3789bf3916aa5720d942e37945f4056680317f1cd23e", url="https://pypi.org/packages/bc/07/830784e061fb94d67649f3e438ff63cfb902dec6d48ac75aeaaac7c7c30e/Pillow-9.4.0.tar.gz")
    version("9.3.0", sha256="c935a22a557a560108d780f9a0fc426dd7459940dc54faa49d83249c8d3e760f", url="https://pypi.org/packages/16/11/da8d395299ca166aa56d9436e26fe8440e5443471de16ccd9a1d06f5993a/Pillow-9.3.0.tar.gz")
    version("9.2.0", sha256="75e636fd3e0fb872693f23ccb8a5ff2cd578801251f3a4f6854c6a5d437d3c04", url="https://pypi.org/packages/8c/92/2975b464d9926dc667020ed1abfa6276e68c3571dcb77e43347e15ee9eed/Pillow-9.2.0.tar.gz")
    version("9.1.1", sha256="7502539939b53d7565f3d11d87c78e7ec900d3c72945d4ee0e2f250d598309a0", url="https://pypi.org/packages/43/6e/59853546226ee6200f9ba6e574d11604b60ad0754d2cbd1c8f3246b70418/Pillow-9.1.1.tar.gz")
    version("9.1.0", sha256="f401ed2bbb155e1ade150ccc63db1a4f6c1909d3d378f7d1235a44e90d75fb97", url="https://pypi.org/packages/4b/83/090146d7871d90a2643d469c319c1d014e41b315ab5cf0f8b4b6a764ef31/Pillow-9.1.0.tar.gz")
    version("9.0.1", sha256="6c8bc8238a7dfdaf7a75f5ec5a663f4173f8c367e5a39f87e720495e1eed75fa", url="https://pypi.org/packages/03/a3/f61a9a7ff7969cdef2a6e0383a346eb327495d20d25a2de5a088dbb543a6/Pillow-9.0.1.tar.gz")
    version("9.0.0", sha256="ee6e2963e92762923956fe5d3479b1fdc3b76c83f290aad131a2f98c3df0593e", url="https://pypi.org/packages/b0/43/3e286c93b9fa20e233d53532cc419b5aad8a468d91065dbef4c846058834/Pillow-9.0.0.tar.gz")
    version("8.4.0", sha256="b8e2f83c56e141920c39464b852de3719dfbfb6e3c99a2d8da0edf4fb33176ed", url="https://pypi.org/packages/7d/2a/2fc11b54e2742db06297f7fa7f420a0e3069fdcf0e4b57dfec33f0b08622/Pillow-8.4.0.tar.gz")
    version("8.3.2", sha256="dde3f3ed8d00c72631bc19cbfff8ad3b6215062a5eed402381ad365f82f0c18c", url="https://pypi.org/packages/90/d4/a7c9b6c5d176654aa3dbccbfd0be4fd3a263355dc24122a5f1937bdc2689/Pillow-8.3.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-olefile", when="@4:4.0,4.1.1:4")

