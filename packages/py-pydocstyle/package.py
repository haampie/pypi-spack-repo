# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydocstyle(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.3.0", sha256="118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019", url="https://pypi.org/packages/36/ea/99ddefac41971acad68f14114f38261c1f27dac0b3ec529824ebc739bdaa/pydocstyle-6.3.0-py3-none-any.whl")
    version("6.2.3", sha256="a04ed1e6fe0be0970eddbb1681a7ab59b11eb92729fdb4b9b24f0eb11a25629e", url="https://pypi.org/packages/2f/47/25f4c4e1b7bfe1d254ab94a256607fac14185b5c2e7521beb50b90e3ed58/pydocstyle-6.2.3-py3-none-any.whl")
    version("6.2.2", sha256="021b33525927b43b4469c2715694c38082cb98146b52342df652b30806e3cb61", url="https://pypi.org/packages/96/ac/b1c2fd6df55ef83435a1dd31530a918faa2b4cf7f38f0cdb10a084929301/pydocstyle-6.2.2-py3-none-any.whl")
    version("6.2.1", sha256="e034023706489a5786778d21bd25e951052616b260d83e163f09d559dcd647b9", url="https://pypi.org/packages/1e/4a/70a55fe6dada5acf640b202a4c2cda39a74cc51222edd44154c914600e9d/pydocstyle-6.2.1-py3-none-any.whl")
    version("6.2.0", sha256="39573fa08919ac492b063724af39a1afdcfea8cdaa2c7b8018ca0dfff5d7e36f", url="https://pypi.org/packages/90/10/f24113b83880421f62b9d721c4a9f23aca13c0e775d0fdf616927bea813c/pydocstyle-6.2.0-py3-none-any.whl")
    version("6.1.1", sha256="6987826d6775056839940041beef5c08cc7e3d71d63149b48e36727f70144dc4", url="https://pypi.org/packages/87/67/4df10786068766000518c6ad9c4a614e77585a12ab8f0654c776757ac9dc/pydocstyle-6.1.1-py3-none-any.whl")
    version("6.1.0", sha256="f598604f0ac0e2673686770487179d83c515b8d1c765a177968a863994c3c156", url="https://pypi.org/packages/c4/e5/8dd392ce56490aadcab870fd3fa310a3e53122fa267dd2da7256536c7a7e/pydocstyle-6.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("toml", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-snowballstemmer@2.2:", when="@6.2:")
        depends_on("py-snowballstemmer", when="@4:6.1")
        depends_on("py-toml@0.10.2:", when="@6.2:6.2.0+toml")
        depends_on("py-toml", when="@6.1+toml")
        depends_on("py-tomli@1.2.3:", when="@6.2.1:+toml ^python@:3.10")
    # END DEPENDENCIES

