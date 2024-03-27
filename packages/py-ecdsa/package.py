##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEcdsa(PythonPackage):
    version("0.18.0", sha256="80600258e7ed2f16b9aa1d7c295bd70194109ad5a30fdee0eaeefef1d4c559dd", url="https://pypi.org/packages/09/d4/4f05f5d16a4863b30ba96c23b23e942da8889abfa1cdbabf2a0df12a4532/ecdsa-0.18.0-py2.py3-none-any.whl")
    version("0.17.0", sha256="5cf31d5b33743abe0dfc28999036c849a69d548f994b535e527ee3cb7f3ef676", url="https://pypi.org/packages/4a/b6/b678b080967b2696e9a201c096dc076ad756fb35c87dca4e1d1a13496ff7/ecdsa-0.17.0-py2.py3-none-any.whl")
    version("0.16.1", sha256="881fa5e12bb992972d3d1b3d4dfbe149ab76a89f13da02daa5ea1ec7dea6e747", url="https://pypi.org/packages/98/16/70be2716e24eaf5d81074bb3c05429d60292c2a96613a78ac3d69526ad2a/ecdsa-0.16.1-py2.py3-none-any.whl")
    version("0.16.0", sha256="ca359c971594dceebf334f3d623dae43163ab161c7d09f28cae70a86df26eb7a", url="https://pypi.org/packages/5d/8b/c6ea939f70b3356e10e771a8d5ef27fd8ecc74d9e49ec8116d94f83b9673/ecdsa-0.16.0-py2.py3-none-any.whl")
    version("0.15", sha256="867ec9cf6df0b03addc8ef66b56359643cb5d0c1dc329df76ba7ecfe256c8061", url="https://pypi.org/packages/b8/11/4b4d30e4746584684c758d8f1ddc1fa5ab1470b6bf70bce4d9b235965e99/ecdsa-0.15-py2.py3-none-any.whl")
    version("0.14.1", sha256="e108a5fe92c67639abae3260e43561af914e7fd0d27bae6d2ec1312ae7934dfe", url="https://pypi.org/packages/a2/25/3bb32da623b39a27a07d194cd58e4540224421d924661de2e694304ae4fa/ecdsa-0.14.1-py2.py3-none-any.whl")
    version("0.14", sha256="da25d37406a664e9e4bcf009834bddfd98ec8d334cf2000621486515c6d1bc58", url="https://pypi.org/packages/f9/67/ee62e7c338e7385bdd04d2702499cb504927d1d6db48aeb2b5e595c42cdf/ecdsa-0.14-py2.py3-none-any.whl")
    version("0.13.3", sha256="9814e700890991abeceeb2242586024d4758c8fc18445b194a49bd62d85861db", url="https://pypi.org/packages/a6/81/2b170b460c84fdc8700cf08aa077ac6a9ff41f4ad3f05d0b3a64ba9f8f2e/ecdsa-0.13.3-py2.py3-none-any.whl")
    version("0.13.2", sha256="20c17e527e75acad8f402290e158a6ac178b91b881f941fc6ea305bfdfb9657c", url="https://pypi.org/packages/23/a8/8aa68e70959e1287da9154e5164bb8bd5dd7025e41ae54e8d177b8d165c9/ecdsa-0.13.2-py2.py3-none-any.whl")
    version("0.13.1", sha256="47d64429e90998846a141f5beadc1e4e8dc1d8a614e321a0609fef5df616a44a", url="https://pypi.org/packages/f9/2a/ed9be4ad09ee37a75d68ee2d7bf535148de4546a875da42e1135bc84d51a/ecdsa-0.13.1-py2.py3-none-any.whl")
    version("0.13", sha256="64cf1ee26d1cde3c73c6d7d107f835fed7c6a2904aef9eac223d57ad800c43fa", url="https://pypi.org/packages/f9/e5/99ebb176e47f150ac115ffeda5fedb6a3dbb3c00c74a59fd84ddf12f5857/ecdsa-0.13.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@0.15:")
        depends_on("py-six", when="@0.14")

