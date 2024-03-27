##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySoyclustering(PythonPackage):
    version("0.2.0", sha256="e07a9025b85b7d0b6886b64854b57ef3934834756c2bf8a1b6aeff36348a63f1", url="https://pypi.org/packages/56/da/383104eb15776319add42a216f377d76b4a6d0fe4b6b21fce507a8c27607/soyclustering-0.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy@1.3:", when="@0.0.4:")

