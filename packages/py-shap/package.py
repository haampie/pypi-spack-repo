# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyShap(PythonPackage):
    # BEGIN VERSIONS
    version("0.45.0", sha256="be8ffc213ba3da1ce7950784571356e6ca77bee94446ddfa9c63eb2c72f7ce9e", url="https://pypi.org/packages/dc/6b/1b485a78385f9f682f3f53d704d10087f80fc74ad2e3ebe4adc91b6ee1dd/shap-0.45.0.tar.gz")
    version("0.44.1", sha256="a21d5a622e12e7c3b4a58d6e93b70133b7e09b6342b19746071a0dc2d190b432", url="https://pypi.org/packages/ec/e0/85a34a7ec70b4f85e9b20b9e4234441b7cf4f8f24b2c59cf231115325a84/shap-0.44.1.tar.gz")
    version("0.44.0", sha256="8f5f0401df83c8b2b566f41872f1bd8bc05bba43aab9e82bfb2047e9b2a0471c", url="https://pypi.org/packages/d2/24/b701ec8ca1fa01b8e1998147462734cae7e613ed4f1ed789239108c9fcd3/shap-0.44.0.tar.gz")
    version("0.43.0", sha256="1eabe01444a24e181ef6a7c9593b4d7c7143eefaeb1fa4d97bd5d9fdc96c4c1e", url="https://pypi.org/packages/65/33/4e8c9c800a10bb428787339a07fb05a8ccbfa6015f5423a849e6d2f8bacd/shap-0.43.0.tar.gz")
    version("0.42.1", sha256="64403915e4a07d2951e7eee4af0e835b1b519367b11806fe1aa4bd6d81adb626", url="https://pypi.org/packages/b3/5c/087c301fcbd2164c097b87ca16e8e94ec06b28006b6e5d8ac8bfad4bea33/shap-0.42.1.tar.gz")
    version("0.42.0", sha256="3ad942256d8f1d510eeb8cd8a98352cec08232052674b678718b57e30651abea", url="https://pypi.org/packages/65/00/2d00b3f5b6250af7f68bcdde35d872c661ddc7f9e45e927295893047ef05/shap-0.42.0.tar.gz")
    version("0.41.0", sha256="a49ea4d65aadbc845a695fa3d7ea0bdfc8c928b8e213b0feedf5868ade4b3ca5", url="https://pypi.org/packages/ed/bb/b48bb3fe1b47e7673b037ed9627746eb1bf9f3ee5b45289f5ab6a26089ef/shap-0.41.0.tar.gz")
    version("0.40.0", sha256="add0a27bb4eb57f0a363c2c4265b1a1328a8c15b01c14c7d432d9cc387dd8579", url="https://pypi.org/packages/cc/55/3713d33d56fdb77916f80f635a9d02e2f24ddb8dc26f278ff759fc088b08/shap-0.40.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.45:")
        depends_on("py-cloudpickle", when="@0.43:")
        depends_on("py-numba", when="@0.43:")
        depends_on("py-numpy", when="@0.43:")
        depends_on("py-packaging@21:", when="@0.43:")
        depends_on("py-pandas", when="@0.43:")
        depends_on("py-scikit-learn", when="@0.43:")
        depends_on("py-scipy", when="@0.43:")
        depends_on("py-slicer@0.0.7", when="@0.43:")
        depends_on("py-tqdm@4.27:", when="@0.43:")
    # END DEPENDENCIES

