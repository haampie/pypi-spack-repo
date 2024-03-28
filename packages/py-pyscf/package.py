# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyscf(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.0", sha256="9596603c914fb3fba853607e96366fa541012faffd59a4ea052f0122dcea5343", url="https://pypi.org/packages/b4/df/e24bc63a972e8c933ea7857ce49fb1a63c35b6e5d8fa073d1fe3cfcc576f/pyscf-2.5.0.tar.gz")
    version("2.4.0", sha256="af0597c481851b5448e7055c3160aef28dc12a1e0b35dda8279555c0780c0d45", url="https://pypi.org/packages/45/c1/98ec4d58392258addf1e4f66eea1066cd0c213369dec87d4da4e1ad61bdf/pyscf-2.4.0.tar.gz")
    version("2.3.0", sha256="71781de62c25924fd4e93ffeb0451ec0d0b3646fe426c75023f4f519f0f35d85", url="https://pypi.org/packages/5b/57/35c7b9c5b8e42dd1940fc92c6c9b0a4b2d591be128120aa732b0a809503b/pyscf-2.3.0.tar.gz")
    version("2.2.1", sha256="4ff6851351caadc5dfa543b6b2c5fbd926ded87e3cc39faa0054e1e5090ed69a", url="https://pypi.org/packages/57/73/eae6b26c865287aeac6a2bd8e32296f84a289afc04d46c29ee2971b45f71/pyscf-2.2.1.tar.gz")
    version("2.2.0", sha256="8f65042cf7e86aa5088756988eb90418befcd18f07a6b8c597229a5f2ba4f644", url="https://pypi.org/packages/53/09/efb1e3a9e7304e4e58fc70b802b8fe195313b0245d71b50521ed0a1e1843/pyscf-2.2.0.tar.gz")
    version("2.1.1", sha256="608442171f5db106b02a95c878c65798fbbd87dc0ce50551a2e081e7d206adb0", url="https://pypi.org/packages/9b/3c/d62ba6a21c3c2c45a87ad0b66b4a99701a6e524fbc234eacb20fdc5f82ce/pyscf-2.1.1.tar.gz")
    version("2.1.0", sha256="45feecc9c9a0ce18dee73c5b178fb0faa3f0c0d3dd5f98b48dc2370c9e13d05b", url="https://pypi.org/packages/91/85/5c6d31398f224150b73339755d580ccf8c4548da946dfb32dc0844ccec06/pyscf-2.1.0.tar.gz")
    version("2.0.1", sha256="b2f00330f98edf7c5b8272904fc11ca74f4677219ba6468aaa7154580efd9edd", url="https://pypi.org/packages/88/7c/f15820b34db4f1b5d74c257701b76baab92303985dd35a29ddf280d8d106/pyscf-2.0.1.tar.gz")
    version("1.7.5", sha256="52856b39f0ada2f6340757caa65dc5c1d9a3cdfceea2a6615ad8af92664a6c69", url="https://pypi.org/packages/62/be/87e1f4aea51181b25f71cec4c9a60f60cbebf26ca17d17a5b153dd22a8d9/pyscf-1.7.5.tar.gz")
    version("1.7.3", sha256="62a26146a222140395b276ea33182f87809a21989ddcf78e2dcb8e35ebc57af2", url="https://pypi.org/packages/83/81/d7468533be1cf92ebc8fd04f47ef75ccecbcfeec3cdd064a71a5d657c84b/pyscf-1.7.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-h5py", when="@1.4.3:1.4,1.5.3:1.7.3")
        depends_on("py-numpy", when="@1.4.3:1.4,1.5.1:1.7.3")
        depends_on("py-scipy", when="@1.4.3:1.4,1.5.1:1.7.3")
    # END DEPENDENCIES

