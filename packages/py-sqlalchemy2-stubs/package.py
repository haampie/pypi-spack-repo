# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlalchemy2Stubs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.2-alpha38", sha256="b62aa46943807287550e2033dafe07564b33b6a815fbaa3c144e396f9cc53bcb", url="https://pypi.org/packages/ee/ea/6eff437d0a26c894da2982429ed2c148ecaf0526349ddc8cda1e7151c171/sqlalchemy2_stubs-0.0.2a38-py3-none-any.whl")
    version("0.0.2-alpha37", sha256="43067e3f67bd16a7fb2b574ee696f7ed53bf60f3e73329cf234a7b4dd4d3816a", url="https://pypi.org/packages/28/1d/8f4bd7fcd5a8d285f7eb089fe1a921564f910391c66ed7a6e874af25a727/sqlalchemy2_stubs-0.0.2a37-py3-none-any.whl")
    version("0.0.2-alpha36", sha256="9b5b3eb263cdc649b6a5619d2c089b98290406027a01e1de171eeb98c38ce678", url="https://pypi.org/packages/12/fe/5532e641673ceaec4f31bce655671ced7827d0ec89a149e6f770bda8480d/sqlalchemy2_stubs-0.0.2a36-py3-none-any.whl")
    version("0.0.2-alpha35", sha256="593784ff9fc0dc2ded1895e3322591689db3be06f3ca006e3ef47640baf2d38a", url="https://pypi.org/packages/bd/a6/289f42af833bf4e6d14e416f79cdeada07d2e5a37fcdd8e469b535fd8fd6/sqlalchemy2_stubs-0.0.2a35-py3-none-any.whl")
    version("0.0.2-alpha34", sha256="a313220ac793404349899faf1272e821a62dbe1d3a029bd444faa8d3e966cd07", url="https://pypi.org/packages/32/12/ecfcbe41207a2c6d8b9a9cbb62f80f398de3a2d426355fc568665c8ae2d3/sqlalchemy2_stubs-0.0.2a34-py3-none-any.whl")
    version("0.0.2-alpha33", sha256="9809e7d8ea72cd92ac35aca4b43f588ae24b20376c55a0ef0112a08a6b537180", url="https://pypi.org/packages/b6/be/a402ba6f56b5d02afbad426067f8ef248d100787c4cc5db9f4632477e69b/sqlalchemy2_stubs-0.0.2a33-py3-none-any.whl")
    version("0.0.2-alpha32", sha256="7f5fb30b0cf7c6b74c50c1d94df77ff32007afee8d80499752eb3fedffdbdfb8", url="https://pypi.org/packages/e0/1c/ac744b3e7d78902e5b8525270a3c09f37edd56ffab7da8b3a20e9d596604/sqlalchemy2_stubs-0.0.2a32-py3-none-any.whl")
    version("0.0.2-alpha31", sha256="515a97fbe4b7cd299b43166c51ce6f356f1222128bf2ba57b0619ce8d89dfab4", url="https://pypi.org/packages/5b/94/af629003deb36b75dc094521c2e857aa71042593ac03b96e720f2df533e8/sqlalchemy2_stubs-0.0.2a31-py3-none-any.whl")
    version("0.0.2-alpha30", sha256="44fa604e4bf8108e931a629fc72df2a95dbe0b2c1bd16f3f4f735c7aabc2f9e3", url="https://pypi.org/packages/c2/34/91d4788e80b8ef99aaded1aa1791340303e4f328e32854be5c96b86e354b/sqlalchemy2_stubs-0.0.2a30-py3-none-any.whl")
    version("0.0.2-alpha29", sha256="ece266cdabf3797b13ddddba27561b67ae7dedc038942bf66e045e978a5e3a66", url="https://pypi.org/packages/15/e1/1c98bb2d4938656d3530269f203eb4b9c221231643d2d9922018346f6972/sqlalchemy2_stubs-0.0.2a29-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@3.7.4:", when="@0.0.1-alpha4:")
    # END DEPENDENCIES

