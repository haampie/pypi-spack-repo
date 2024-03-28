# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPubchempy(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.4", sha256="24e9dc2fc90ab153b2764bf805e510b1410700884faf0510a9e7cf0d61d8ed0e", url="https://pypi.org/packages/aa/fb/8de3aa9804b614dbc8dc5c16ed061d819cc360e0ddecda3dcd01c1552339/PubChemPy-1.0.4.tar.gz")
    version("1.0.3", sha256="a621c6888c537555ff7effe51c3018d02f586e5677fde0437cf7fd4cda208630", url="https://pypi.org/packages/29/6a/6c7be1445b93a87b1870bcd0b82d0d89c16ea6370caf29618d944fb50aa1/PubChemPy-1.0.3.tar.gz")
    version("1.0.2", sha256="a46fac98e137f207162f7ac8915d9c42db1b8996e451d4a603169ea1d582d459", url="https://pypi.org/packages/64/c4/a48c7b8716c1a2863c962adad4baae63a8050d6cd95597641479d16631c3/PubChemPy-1.0.2.tar.gz")
    version("1.0.1", sha256="8c7eb92739a72ed9e5c0dad13cdc47afbe6f609479b54a0949023a1dde161918", url="https://pypi.org/packages/69/6d/18d23f8cd2da97ca0e4cb72bd87804dcd171f3fec3f50f56599f11c57512/PubChemPy-1.0.1.tar.gz")
    version("1.0", sha256="9bbbeab7dc52390a2f19d61a6ae8fbdd32f388bb35a8a550f4e6f97cea3132c3", url="https://pypi.org/packages/c3/1b/9b0b317c0746dd21e7db868981be3a7d4989a1cc9e82af254690125875e9/PubChemPy-1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("pandas", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

