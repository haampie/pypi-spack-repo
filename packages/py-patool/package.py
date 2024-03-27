##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPatool(PythonPackage):
    version("2.2.0", sha256="21db6cc2fcd77acd37768258d1ad5aa3df0f676331fd80dfb1eb628626bc9155", url="https://pypi.org/packages/e6/64/e9dd887985305d4cc88b09bcaaaafe5053197e5ebbeba62473f8c3cf6d80/patool-2.2.0-py2.py3-none-any.whl")
    version("2.1.1", sha256="85a90896896fd28a6c2ac748b10abffe52858fa5a2a33d1ed364955e12ec62c0", url="https://pypi.org/packages/a4/1e/440d6f0de850771c05773958546485f74cfa9c72ff7926d0af5ab256c2e7/patool-2.1.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="046db47d262c44cc7991e8c41dbfa81d9dbe6a5dbfc09b1636670364a260f539", url="https://pypi.org/packages/cf/80/1476f3522dc9ef5752facada4188efd6f45f1b30ef25d4524c2ba7940026/patool-2.1.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="417d136d75eb55c1649c83a0299b52a3b0a852134afd8a74d12b9bdbf4072ec4", url="https://pypi.org/packages/ae/2d/7780e97ca4b9c6309f0df70a8c5ae93d894e8e233421e9268a17e11f19e6/patool-2.0.0-py2.py3-none-any.whl")
    version("1.15.0", sha256="b14fd047571f71220de5d220bac9974fa2f423cce3c42cf0a85f54f155c30f09", url="https://pypi.org/packages/f4/f0/cee07d9fee3ac4b846fb44eca856142a7bcf44be83e221c4d698fec449d9/patool-1.15.0-py2.py3-none-any.whl")
    version("1.14.1", sha256="01809f699bb9afeef612eff2ad564336af1108f1eb2b39fa6d678a4dcc0a8689", url="https://pypi.org/packages/34/69/a1108830707190ecd788396c3bbdad55bb4725af82d771d60a8c473653c1/patool-1.14.1-py2.py3-none-any.whl")
    version("1.14.0", sha256="14e695ef85f5b1bc7227140effd35f0461dc7b86c7dcab692941cb78c8792bca", url="https://pypi.org/packages/75/ae/ab05ec55b96b18e6d47e0208a8f836f1930437930c950c1b957da1adc2d7/patool-1.14.0-py2.py3-none-any.whl")
    version("1.13", sha256="224dd373ed8ee52aca908f8123b52c02539ee88e10770b884284eb737b3b755f", url="https://pypi.org/packages/f4/e7/6a0f9f24af5f1361ef42d7d997e5ae1e8b6046483830ccc2568a4174a2ea/patool-1.13-py2.py3-none-any.whl")
    version("1.12", sha256="3f642549c9a78f5b8bef1af92df385b521d360520d1f34e4dba3fd1dee2a21bc", url="https://pypi.org/packages/43/94/52243ddff508780dd2d8110964320ab4851134a55ab102285b46e740f76a/patool-1.12-py2.py3-none-any.whl")
    version("1.11", sha256="1217e1ffc38c69da9a11cecdd2640e376ccd1f05d880da5d1faea14a92fcf275", url="https://pypi.org/packages/53/c2/b1152511a1bd113ca07392f12e096c656c5a079962b28e5388711650e683/patool-1.11-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.10:", when="@2:")
        depends_on("python@3.9:", when="@1.13:1")

