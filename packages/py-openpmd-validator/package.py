##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenpmdValidator(PythonPackage):
    version("1.1.0.3", sha256="8f55d04acd135d0afa67b4224912b2a009e660c8bbc9e94c49b79554fd3e6192", url="https://pypi.org/packages/68/b0/7aa658cc495b058f49af93afe2db01170e3e4a80c3a3404bcbae4b63633a/openPMD_validator-1.1.0.3-py3-none-any.whl")
    version("1.1.0.2", sha256="754c0a8c3ae1a13079e5c535d50ab1074537fd2a29814193298c1c3c8cf2129c", url="https://pypi.org/packages/81/86/c939f7bd14de85a97ee658def8491e2430be366d49ec601ec0b7a30f3d72/openPMD_validator-1.1.0.2-py3-none-any.whl")
    version("1.1.0.1", sha256="7585abbd32523ae6b8065772e1cc27a45e232c526a9fc0bd8ce85182d1b4b325", url="https://pypi.org/packages/11/db/589cd5ddcc8d60a74e8ffaaf43e19af3b1bb91e6ef8996bd0531bfdb470c/openPMD-validator-1.1.0.1.tar.gz")
    version("1.0.0.2", sha256="9610b552aef48baf37e1ce3fe1372b5a2a2f358ff50e23283e79fdfb6fee5366", url="https://pypi.org/packages/6f/6e/0b78f7225cffe8098d48b7fbeab8fe350b970368daef4d62a0c7baf4a315/openPMD-validator-1.0.0.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-h5py")
        depends_on("py-numpy@1.6.1:")
        depends_on("py-python-dateutil@2.3:")

