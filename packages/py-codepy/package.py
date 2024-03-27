##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCodepy(PythonPackage):
    version("2023.1", sha256="bce2e136e9fb3cf59949427d4ef419648778401e6db288596e75b53e144f8b93", url="https://pypi.org/packages/f0/75/6e16a64cb03581c310db65da9dadb2e3e1882251817babf69caf7e98a10a/codepy-2023.1.tar.gz")
    version("2019.1", sha256="384f22c37fe987c0ca71951690c3c2fd14dacdeddbeb0fde4fd01cd84859c94e", url="https://pypi.org/packages/6c/81/338a4d4145af7857f9b6fdf9b4d53c58c7eb4c1d092ff6c010efdb4dfdf3/codepy-2019.1.tar.gz")


