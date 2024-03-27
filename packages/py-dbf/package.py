##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDbf(PythonPackage):
    version("0.99.3", sha256="940272a72ac27d16a1db69aafef820684012cc3553ffe9875d5cd2e3a9cb69dc", url="https://pypi.org/packages/2a/52/3d56dac7bdf8ef55b9f554e49bba34448dee20ba84335c3d2250f46884e2/dbf-0.99.3.tar.gz")
    version("0.97.11", sha256="8aa5a73d8b140aa3c511a3b5b204a67d391962e90c66b380dd048fcae6ddbb68", url="https://pypi.org/packages/91/d7/1217ff1f2b4f2b7e39d7a30a377f7c8ce39299b12284e60040d6e6fd3b92/dbf-0.97.11.tar.gz")
    version("0.96.5", sha256="5a4b54157bcd40cd9149155c21b71073570f4bb83ad495f3a88b23c463bd4f98", url="https://pypi.org/packages/22/fd/2819d7907074f097098be527471e03144520fcef968939e0c1e7a33ec2b4/dbf-0.96.005.zip")
    version("0.94.3", sha256="c95b688d2f28944004368799cc6e2999d78af930a69bb2643ae098c721294444", url="https://pypi.org/packages/7c/ef/79873517838910e8f1bd5610ab3de380a3886675103072727266eec91bbc/dbf-0.94.003.tar.gz")

    with default_args(type="run"):
        depends_on("py-aenum", when="@0.96.8:0.97.2,0.97.4:0.97.5,0.97.8:0.98.3")

