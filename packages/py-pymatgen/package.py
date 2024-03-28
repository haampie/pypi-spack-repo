# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymatgen(PythonPackage):
    # BEGIN VERSIONS
    version("2024.3.1", sha256="798937cf2c33d8469ea1347607e22fbca6c94528b4b1343057b63e94892653a3", url="https://pypi.org/packages/c5/c8/37069017466f04bdfd321f36795762b72ccb776bff110d327faf950f2748/pymatgen-2024.3.1.tar.gz")
    version("2024.2.23", sha256="48764e1bdf8d6b0209b650a96c86947b73d41bc7d2cc4ff13b2ac54dd1c308eb", url="https://pypi.org/packages/4d/a0/903a79eeddd76e1913af8d7911dc7edc4b6898cc616642a8229124a1d21a/pymatgen-2024.2.23.tar.gz")
    version("2024.2.20", sha256="76645ade67f00a60fa14f954a191716bb3021b7482d8d76ca4407d2b051a22d4", url="https://pypi.org/packages/df/f0/a2c60b88bc8c28a385f9b74310c236b39f0a9d51a1508a99d01abead75d1/pymatgen-2024.2.20.tar.gz")
    version("2024.2.8", sha256="1ed429c6c5eff9f0156a921ca9f8513623c37665d23a4bc882dd11cd88ff1bec", url="https://pypi.org/packages/10/0d/008bfb60f9ec80fa3c749dec7b800bbbfcc7a869a4cb37b1b905e6ff2660/pymatgen-2024.2.8.tar.gz")
    version("2024.1.27", sha256="58312100ab88f861847886052275025daaecc95733b53808456642c2a2c431ce", url="https://pypi.org/packages/4f/68/1039e53ed3f544772bd24b1402fdd0a4f340b797718c160672f18e9eb3d0/pymatgen-2024.1.27.tar.gz")
    version("2024.1.26", sha256="73c020fd4375a9c5372892e531e84c7a9c4deb2eb21cd4063e0e8ef1ea727f77", url="https://pypi.org/packages/ce/f8/7ad8ed6b7ada10951b2c53bcc206d5abb0d9c8ace9fa8c307706bfe713eb/pymatgen-2024.1.26.tar.gz")
    version("2023.12.18", sha256="56c0041fe5431ac1b8f8c0c17d06091c4d61082c3a99924f3940d73ebb6656eb", url="https://pypi.org/packages/67/f6/31cfbcf941391f5165085643e134d2bb3b8a61967035a2abd522ef0f4fe7/pymatgen-2023.12.18.tar.gz")
    version("2023.11.12", sha256="6746cc222e033ec4182596b91004599845a4bfc1bbc4d0b0f0d88f60d3d650a4", url="https://pypi.org/packages/49/db/1db7e2f1ee9d95bd085883d76fa375bef2d7c179c4adaf568c870ff34577/pymatgen-2023.11.12.tar.gz")
    version("2023.11.10", sha256="318360e641a4d8f931dcb3c3b9317d1c066742ad3dcf9f143bac615f6dafd02e", url="https://pypi.org/packages/3c/ba/aafdc45ab74537b2037bf9a193ca3b14fbfb2b097f1d7a5395089341ee27/pymatgen-2023.11.10.tar.gz")
    version("2023.10.11", sha256="2b6c0012ffd942f6aef89a63c7e20297cf5c4e0533d5f7604110d4485b5176b6", url="https://pypi.org/packages/f2/74/d184c44c5999427956e418a1b41cd681fa1c6472692328e864ab3f902ddf/pymatgen-2023.10.11.tar.gz")
    version("2022.9.8", sha256="2250e05b81af3313bc0fc70cb558c2f528ed4eefb32d943ed9bd7a9756f03652", url="https://pypi.org/packages/92/f5/f85118b4ca8af05b147fda11dda53a699f5932293fd78268e3c5438b1d31/pymatgen-2022.9.8.tar.gz")
    version("2021.3.9", sha256="a6f22d69133a48b7801bfd5e6a2878b47b4b4b2ef1a377b87c6c573be14cbf16", url="https://pypi.org/packages/18/06/8f4a5288ea5d940773d9c8651aee59535006353b1b592ac1e61802b0749f/pymatgen-2021.3.9.tar.gz")
    version("2020.12.31", sha256="5002490facd47c55d2dae42c35712e061c1f5d881180485c0543a899589856d6", url="https://pypi.org/packages/e1/18/274b40cff34257a728071199d21105ced3116b42dd60793113eee7b1b5ca/pymatgen-2020.12.31.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.9:")
        depends_on("py-joblib", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-matplotlib@1.5:", when="@2017.8.14:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-monty@2024.2:", when="@2024.2:")
        depends_on("py-monty@3.0.2:", when="@2019.10.3:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:2024.1")
        depends_on("py-networkx@2.2:", when="@2019.7.21:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-numpy@1.25.0:", when="@2023.10:2023.10.3,2023.10.11:")
        depends_on("py-palettable@3.1.1:", when="@2019.7.21:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-pandas", when="@2017.12:2020.1,2020.3.13:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-plotly@4.5.0:", when="@2020.4:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-pybtex", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-requests", when="@2017.8.14:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-ruamel-yaml@0.17:", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-scipy@1.5.0:", when="@2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-spglib@2.0.2:", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-sympy", when="@2017.8.14:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-tabulate", when="@2017.8.14:2020.7,2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-tqdm", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
        depends_on("py-uncertainties@3.1.4:", when="@2023.9.10,2023.10:2023.10.3,2023.10.11:")
    # END DEPENDENCIES

