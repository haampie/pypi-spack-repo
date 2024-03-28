# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH5netcdf(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.0", sha256="f2df69dcd3665dc9c4d43eb6529dedd113b2508090d12ac973573305a8406465", url="https://pypi.org/packages/68/2d/63851081b19d1ccf245091255797cb358c53c886609b5056da5457f7dbbf/h5netcdf-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="aa53c39b94bcd4595a2e5a2f62f3fb4fb8a723b5ca0a05f2db352f014bcfe72c", url="https://pypi.org/packages/d1/11/8116d6f209c8588ceb1382fddb8820fc720330373d9bd1a09434d684dbde/h5netcdf-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="338e65212cee129e4508a49994f230a3083910fbf20454bb57aa1ca99687ad34", url="https://pypi.org/packages/e2/7a/709f1d5eaabeb64948ff11cf840d1cb5ae2797ddcd10c9f725e40fd74691/h5netcdf-1.1.0-py2.py3-none-any.whl")
    version("1.0.2", sha256="4a4c277e18a906ab66e78ae2d95d27de4eec3519b87871adfd137974265bc250", url="https://pypi.org/packages/fb/81/569ab60d33e51482192a278ee3457704805470d8fe0d757237cf02f01c53/h5netcdf-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="4a4762dbfcec871c43455e3b3ae599d2ecbf7a3698069fd73f511d0038676ccc", url="https://pypi.org/packages/43/5e/a4f8ab46b9440ad351d486070cb7940e35bd37a4182a31b40298ae499694/h5netcdf-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="97c619b3e199d2b799bbf97e03387c68787ffbdef910c924d0fd36037680108f", url="https://pypi.org/packages/fc/ea/753d7614168845e1ac5a088ad7f939af412afaf06cb2e4e7df7d4a357109/h5netcdf-1.0.0-py2.py3-none-any.whl")
    version("0.15.0", sha256="62abc9e4b25daff1f49f5f0734e98ca8b2189672e35f9a5bef42b4217c5abbdf", url="https://pypi.org/packages/2e/0c/622224650b0575a4024bb3baf0bee896f195cb235b297f95e867a432e4dc/h5netcdf-0.15.0-py2.py3-none-any.whl")
    version("0.14.1", sha256="161ccdb511f36efe1cdbab2d973f41e85e86f5ef727d836ea0ead261b6eea130", url="https://pypi.org/packages/36/65/4c633f639273ec00a3c8a980aff3b8391d84e16f311abce28a772797f6e6/h5netcdf-0.14.1-py2.py3-none-any.whl")
    version("0.14.0", sha256="a423364576f431c5adb3e313c320c246cf0e441c1e5d9621b7a4ef75fd0500ea", url="https://pypi.org/packages/48/b8/0f1df4368f71cc215e6e207dd463f608b56e5cc44033685e281c3590f834/h5netcdf-0.14.0-py2.py3-none-any.whl")
    version("0.13.1", sha256="b7efb5debae8054e303fc4f8f56bba47377bbe06c581584741e6b69fcfb50989", url="https://pypi.org/packages/d1/d1/ea0b8866990d6c541e7af47bafe65bac43ebead7a6eb7748435ffc86d578/h5netcdf-0.13.1-py2.py3-none-any.whl")
    version("0.10.0", sha256="2c526715f9010f403b7f667a146950515e44b17068196c3f004ee5c6c7563e18", url="https://pypi.org/packages/41/d4/ba3923cc4875e693d060b13ae53a8b3fee1588b11ddfb5b9247efaac2c97/h5netcdf-0.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2:")
        depends_on("py-h5py", when="@0.3:")
        depends_on("py-packaging", when="@0.13.1:")
    # END DEPENDENCIES

