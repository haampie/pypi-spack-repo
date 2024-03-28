# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytools(PythonPackage):
    # BEGIN VERSIONS
    version("2024.1.1", sha256="9f1d03040d78d9d2a607d08de64ec4e350aecdf4ee019f627ce1f1f0c2a4400d", url="https://pypi.org/packages/2f/64/65825bb59ae728584ef9ea2d5998f1d2737a2ec720af113a886ca3db8640/pytools-2024.1.1-py2.py3-none-any.whl")
    version("2024.1", sha256="6ebc59a8638cef1e40558ead077cd382b8029fe54d4a3922a7520d4bb5541740", url="https://pypi.org/packages/40/6b/e07180e8997c160c902c3f5bc6fff794a325914968381c0a256d0827db79/pytools-2024.1-py2.py3-none-any.whl")
    version("2023.1.1", sha256="53b98e5d6c01a90e343f8be2f5271e94204a210ef3e74fbefa3d47ec7480f150", url="https://pypi.org/packages/3d/4b/4cbe808b38ee25d3c3f1b1b99bde39cef43c30df64416b62e28079404d1b/pytools-2023.1.1-py2.py3-none-any.whl")
    version("2023.1", sha256="7818a7ca089e51dbd5405681522bb404de21eca43ee69b6348a8095900909ef2", url="https://pypi.org/packages/d4/3d/fdba05f97e9356b6a8ea8949fc1fab385ee0de5e989f0a5d9958710721bd/pytools-2023.1-py2.py3-none-any.whl")
    version("2022.1.14", sha256="41017371610bb2a03685597c5285205e6597c7f177383d95c8b871244b12c14e", url="https://pypi.org/packages/b5/00/b7350b62803926f1d8fbbcaa50e38bcc93354aa73894c13155825eec897f/pytools-2022.1.14.tar.gz")
    version("2022.1.13", sha256="c2f98359f6f281fb9d06136cdfb825a1984571598c8b437f8d6815ab80a04149", url="https://pypi.org/packages/48/d8/93d4dc493e5ee107ae181a918a8f5e8f117a1bcdafc6aa70eadb6be49cd5/pytools-2022.1.13.tar.gz")
    version("2022.1.12", sha256="4d62875e9a2ab2a24e393a9a8b799492f1a721bffa840af3807bfd42871dd1f4", url="https://pypi.org/packages/a1/54/2e20e4a5fd88eec6e1fd65d822e86ab10aec47d9b110c3d4a095bb60768d/pytools-2022.1.12.tar.gz")
    version("2022.1.11", sha256="810173d62d5d6c391b137a6666be4a1616eae05df24d5ddbc0eada684a0180a2", url="https://pypi.org/packages/dc/03/266c1815b917adf6edb438f8f56bd19565cb681b5f446b6b2bf89426d403/pytools-2022.1.11.tar.gz")
    version("2022.1.10", sha256="7c949e6838f90ee4931e5b868c6998782c129c0d9409cedb94f499bab400331e", url="https://pypi.org/packages/0e/d3/81b179d54afba4050359863da33a9f1225019940231f5ac4900d476ebaff/pytools-2022.1.10.tar.gz")
    version("2022.1.9", sha256="3393d25029982080e3fb94c47bf627a1e553ccd174fe2edef6c1c5ec723918ff", url="https://pypi.org/packages/f5/e4/8fd397090b3810d8332af54e91171cdf9360e18b66cc2c5975a33c89726f/pytools-2022.1.9.tar.gz")
    version("2021.2.9", sha256="db6cf83c9ba0a165d545029e2301621486d1e9ef295684072e5cd75316a13755", url="https://pypi.org/packages/46/4b/d0f2b0076f73fc792810cb217a19e24b09a417f261fdb12112859a551076/pytools-2021.2.9.tar.gz")
    version("2019.1.1", sha256="ce2d702ae4ef10a70197b00b93141461140d00578f2a862fa946ca1446a300db", url="https://pypi.org/packages/00/96/00416762a3eda8876a17d007df4a946f46b2e4ee1057e0b9714926472ef8/pytools-2019.1.1.tar.gz")
    version("2016.2.6", sha256="6dd49932b8f81a8b622685cff3dd515e351a9290aef0fd5d020e4df00c06aa95", url="https://pypi.org/packages/68/22/d424bc64595df163da60684396357631ae3d21c44bc9788d2b0f11b3655d/pytools-2016.2.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.6:", when="@2023:+numpy")
        depends_on("py-platformdirs@2.2:", when="@2023:")
        depends_on("py-typing-extensions@4:", when="@2023: ^python@:3.10")
    # END DEPENDENCIES

