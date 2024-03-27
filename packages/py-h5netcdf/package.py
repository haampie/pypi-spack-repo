##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH5netcdf(PythonPackage):
    version("1.3.0", sha256="f2df69dcd3665dc9c4d43eb6529dedd113b2508090d12ac973573305a8406465", url="https://pypi.org/packages/68/2d/63851081b19d1ccf245091255797cb358c53c886609b5056da5457f7dbbf/h5netcdf-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="aa53c39b94bcd4595a2e5a2f62f3fb4fb8a723b5ca0a05f2db352f014bcfe72c", url="https://pypi.org/packages/d1/11/8116d6f209c8588ceb1382fddb8820fc720330373d9bd1a09434d684dbde/h5netcdf-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="338e65212cee129e4508a49994f230a3083910fbf20454bb57aa1ca99687ad34", url="https://pypi.org/packages/e2/7a/709f1d5eaabeb64948ff11cf840d1cb5ae2797ddcd10c9f725e40fd74691/h5netcdf-1.1.0-py2.py3-none-any.whl")
    version("1.0.2", sha256="4a4c277e18a906ab66e78ae2d95d27de4eec3519b87871adfd137974265bc250", url="https://pypi.org/packages/fb/81/569ab60d33e51482192a278ee3457704805470d8fe0d757237cf02f01c53/h5netcdf-1.0.2-py2.py3-none-any.whl")
    version("0.10.0", sha256="2c526715f9010f403b7f667a146950515e44b17068196c3f004ee5c6c7563e18", url="https://pypi.org/packages/41/d4/ba3923cc4875e693d060b13ae53a8b3fee1588b11ddfb5b9247efaac2c97/h5netcdf-0.10.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2:")
        depends_on("py-h5py", when="@0.3:")
        depends_on("py-packaging", when="@0.13.1:")

