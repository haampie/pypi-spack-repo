##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMeautility(PythonPackage):
    version("1.5.1", sha256="93d0ed4fcd9f65fb10376b53c846ac0942332e06c6144e12e5c7a5b1f31accf6", url="https://pypi.org/packages/c6/20/de3443888225574e1e42675e8d740f6cecc5873a6da7640b2c798e22fc81/MEAutility-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="99977208ec465ed7b9789cdccbccb5a8d39c5e3612fd620fe5dcbe8b9dd39846", url="https://pypi.org/packages/fc/fd/5db599ce2694f187f914b02068c7c5df957edbd08b2caa3164f50064a11f/MEAutility-1.5.0-py3-none-any.whl")
    version("1.4.9", sha256="c44089ed35a0a09c65f6f6166c8641c4c8f29a694a5deb2f5a9f61b824b2c765", url="https://pypi.org/packages/3e/92/142b3fd660f141fbd1a0550dc3a367acfc8df39c15ee0e502ce5d74233e7/MEAutility-1.4.9.tar.gz")
    version("1.4.8", sha256="63466aa36d7a5247e2cfa31d0a75e8a5dfab58975f8d18737dac8da1b252a5f5", url="https://pypi.org/packages/f6/f0/4eda4cb3e2b652c178f70aad009ac1a0bb90dc5f15d883c001db3a959a4b/MEAutility-1.4.8.tar.gz")
    version("1.4.7", sha256="d4595e9fc73d4af43bd9819f173f448ad1aa7cacda0a98953045866ec5a9fc89", url="https://pypi.org/packages/39/45/11c61dab738e328d352c97a23177c9a75d89c61fe1e0a4c8d0b526f51fd6/MEAutility-1.4.7.tar.gz")
    version("1.4.6", sha256="464fc5892c052df6ccab01dee679afba0abaccbe840ef0dbcd6eb3f3a32a4543", url="https://pypi.org/packages/68/21/b678ca7a47d4ee0744c09d1ff0e688ccfc0168898c0857e3c2e47cb52a5a/MEAutility-1.4.6.tar.gz")
    version("1.4.5", sha256="3665aee9973d044be9821b594a089022465eff461ebd3ad05b2601bc451dc884", url="https://pypi.org/packages/ea/7b/97008e7e8492d3fdf145e713a1c64491d544b21326bc9a3dbd7b0ea927ad/MEAutility-1.4.5.tar.gz")
    version("1.4.4", sha256="8dad04cfed6fdc8b993a41f8c847905331af7ed3a412d9eda3fca5bc4f88175d", url="https://pypi.org/packages/d7/53/8ebaea57510962928cdfca93e98421173a98d96bb2712328f107d224650a/MEAutility-1.4.4.tar.gz")
    version("1.4.3", sha256="7cd1f723992aa7366f1cbbf8f2843e1f61d8123b459435653860a3b544bc752f", url="https://pypi.org/packages/02/0c/8c5bdfaf8e61e195676d3ded6e6a9a2813609e4121d0b531010b205f56e9/MEAutility-1.4.3.tar.gz")
    version("1.4.2", sha256="3d646997e68b13a21f502242bd38dd3c6c502c04f233e84c6f5a438c2a1b2a0a", url="https://pypi.org/packages/5e/33/a3dc991654645155d0cb8778440fdf3fdd0547dc2af367bfdafd03f6ae1d/MEAutility-1.4.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-matplotlib", when="@1.5:")
        depends_on("py-numpy", when="@1.5:")
        depends_on("py-pyyaml", when="@1.5:")

