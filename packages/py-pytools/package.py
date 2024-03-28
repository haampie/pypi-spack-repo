# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytools(PythonPackage):
    # BEGIN VERSIONS
    version("2022.1.14", sha256="41017371610bb2a03685597c5285205e6597c7f177383d95c8b871244b12c14e", url="https://pypi.org/packages/b5/00/b7350b62803926f1d8fbbcaa50e38bcc93354aa73894c13155825eec897f/pytools-2022.1.14.tar.gz")
    version("2022.1.12", sha256="4d62875e9a2ab2a24e393a9a8b799492f1a721bffa840af3807bfd42871dd1f4", url="https://pypi.org/packages/a1/54/2e20e4a5fd88eec6e1fd65d822e86ab10aec47d9b110c3d4a095bb60768d/pytools-2022.1.12.tar.gz")
    version("2021.2.9", sha256="db6cf83c9ba0a165d545029e2301621486d1e9ef295684072e5cd75316a13755", url="https://pypi.org/packages/46/4b/d0f2b0076f73fc792810cb217a19e24b09a417f261fdb12112859a551076/pytools-2021.2.9.tar.gz")
    version("2019.1.1", sha256="ce2d702ae4ef10a70197b00b93141461140d00578f2a862fa946ca1446a300db", url="https://pypi.org/packages/00/96/00416762a3eda8876a17d007df4a946f46b2e4ee1057e0b9714926472ef8/pytools-2019.1.1.tar.gz")
    version("2016.2.6", sha256="6dd49932b8f81a8b622685cff3dd515e351a9290aef0fd5d020e4df00c06aa95", url="https://pypi.org/packages/68/22/d424bc64595df163da60684396357631ae3d21c44bc9788d2b0f11b3655d/pytools-2016.2.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

