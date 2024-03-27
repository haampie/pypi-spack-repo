##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPypdf2(PythonPackage):
    version("2.5.0", sha256="72212067234907341df620e59d6713ec702fa3300cda4559175a71f6fcd12a83", url="https://pypi.org/packages/b2/54/14f9ce3287c995e290206c1a75287aa308e961109fe6a3fb2a91b01a67e3/PyPDF2-2.5.0-py3-none-any.whl")
    version("1.26.0", sha256="e28f902f2f0a1603ea95ebe21dff311ef09be3d0f0ef29a3e44a932729564385", url="https://pypi.org/packages/b4/01/68fcc0d43daf4c6bdbc6b33cc3f77bda531c86b174cac56ef0ffdb96faab/PyPDF2-1.26.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-typing-extensions", when="@2:2.10.3 ^python@:3.9")

