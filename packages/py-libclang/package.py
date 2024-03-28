# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibclang(PythonPackage):
    # BEGIN VERSIONS
    version("15.0.6.1", sha256="a1a8fe038af2962c787c5bac81bfa4b82bb8e279e61e70cc934c10f6e20c73ec", url="https://pypi.org/packages/60/56/7c107ccc000d78c400d083a09f363fe67407048c66eea6c72df1e3303e73/libclang-15.0.6.1.tar.gz")
    version("14.0.6", sha256="9052a8284d8846984f6fa826b1d7460a66d3b23a486d782633b42b6e3b418789", url="https://pypi.org/packages/9d/97/a87a352058772f30c39cace0992c807c1d2a0c3a9fc673434b011ac54538/libclang-14.0.6.tar.gz")
    version("14.0.1", sha256="332e539201b46cd4676bee992bbf4b3e50450fc17f71ff33d4afc9da09cf46cb", url="https://pypi.org/packages/ea/ec/94fefe778caa8f2ecf9bb996917535a49b36580846af908b2f38fe6396c9/libclang-14.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

