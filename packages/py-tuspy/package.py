# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTuspy(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.3", sha256="024d3d1745120098a85635e42242039ca6b1bc787f561ec974fffb45fc775c1b", url="https://pypi.org/packages/52/81/ec2c616fc39202911d14e3adc4b2681e8c052a8981574a9f988cdd6b9212/tuspy-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="ca2b0d3e4c6ed0020761e449c61ac93d48cafe2f5384c390cacb27f36c279ef1", url="https://pypi.org/packages/ef/e4/d9d439bb08ba19dfeeb61cb54cc91a2257406a173e92a0b9305059ffb13c/tuspy-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="4c136bb97593367376e77f1d9580c1990bd535698f86765c80db9b9d3864f35f", url="https://pypi.org/packages/dd/51/266478fe39493b0251ba1a29d0ae5f695c62f7b935283d45f788889cea6a/tuspy-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="09a81eba7b0ce4da7870961721892c62f1d62570913bcef6727ef5599e3f4181", url="https://pypi.org/packages/aa/3d/785bacd0653732f1cfc3a1331e062924fde72e507b31eddb5b4dcdfec00c/tuspy-1.0.0.tar.gz")
    version("0.2.5", sha256="8ce106dd139ac77a097e8728f15f90d99df7408d9e67ac780ce44aefb9b5dd8d", url="https://pypi.org/packages/03/13/a5d87dc357f7146d54cd9c46d0fa7e9c80357e4fab7cdbf8fda14b727ec0/tuspy-0.2.5-py3-none-any.whl")
    version("0.2.4", sha256="49b674003bbdb0e2ee3fc949490f85ca381929f712f17a7a56404ff6217e96e8", url="https://pypi.org/packages/68/9c/21dedeb7e98a1d905a529a1ba044482510e5954bb70bd4392984e44b5785/tuspy-0.2.4.tar.gz")
    version("0.2.3", sha256="c3780833bcb1e9c4efa22a432221cb9850a298235ab12338ecfe2ac9f04e734d", url="https://pypi.org/packages/d9/45/e1a842e9d0994830eca1688ae235978668ea19fd9a0a79720b2d3be1b248/tuspy-0.2.3.tar.gz")
    version("0.2.2", sha256="cf55b742cf6e662db59ffd9a84aa6813eefd922396dc0d6e2928352e244a04d9", url="https://pypi.org/packages/3c/66/6767d11ba9173c055d4fbaed3c2de6693b31d765096198e683118602e283/tuspy-0.2.2.tar.gz")
    version("0.2.1", sha256="fd51ceeddaf35db176d27bce5e1958f93edcf12fbed0473f3bf8132e8e19d906", url="https://pypi.org/packages/ce/23/f8cdb6ec7a3c43b8913843279bc4a61736578a1d0f950c3dd6a94f13fc0e/tuspy-0.2.1.tar.gz")
    version("0.2", sha256="7ba90747e48522f6d48cce0e822eb95779b110e78fb2b8c8fe1967381d53030b", url="https://pypi.org/packages/7f/81/c7dd84abfd525fdf0d5f8c0a9130944a9fe20c547bf116efe5208561011a/tuspy-0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@3.6.2:", when="@1.0.1:")
        depends_on("py-certifi@2018:", when="@0.2.5:0")
        depends_on("py-future@0.16:", when="@0.2.5:0,1.0.1")
        depends_on("py-requests@2.18.4:", when="@0.2.5:0,1.0.1:")
        depends_on("py-six@1.11:", when="@0.2.5:0,1.0.1:1.0.2")
        depends_on("py-tinydb@3.5:", when="@0.2.5:0,1.0.1:")
    # END DEPENDENCIES

