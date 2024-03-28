# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydicom(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.4", sha256="f9f8e19b78525be57aa6384484298833e4d06ac1d6226c79459131ddb0bd7c42", url="https://pypi.org/packages/35/2a/8c0f6fe243e6b6793868c6834203a44cc8f3f25abad780e1c7b21e15594d/pydicom-2.4.4-py3-none-any.whl")
    version("2.4.3", sha256="797e84f7b22e5f8bce403da505935b0787dca33550891f06495d14b3f6c70504", url="https://pypi.org/packages/24/fe/d74445ca70ca30328a0c07ba50d9558741882a524ae92a7b482cce7ec6bf/pydicom-2.4.3-py3-none-any.whl")
    version("2.4.2", sha256="d2801c234a2f99ac97c6c0b5e50a908ed16d2fef905a2fda49fecd311cd88802", url="https://pypi.org/packages/a7/77/bbe5dc1b3c23854cbab5db1e1106d82896e1315acfc2d1acdca2f881ebef/pydicom-2.4.2-py3-none-any.whl")
    version("2.4.1", sha256="301cbf8bf2cca95643ccf678f5b0cfecfd15974cd27e199f0856c44694852c0e", url="https://pypi.org/packages/76/ce/a941758893f96197d5c96c1f733883a6917d377d3e136a5b65c73a64b03d/pydicom-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="bfb588716e5c86392c9d041addbca422a9d795bba984f9c75711490f4c8fc939", url="https://pypi.org/packages/92/26/554860de3197279869a3271f6440497c8bd720171d339021c99717c48e11/pydicom-2.4.0-py3-none-any.whl")
    version("2.3.1", sha256="b00bacdabc1f8a18b61a08bb6cd0f41c419446531638c895a708c22a35d69cfe", url="https://pypi.org/packages/bc/72/8342fdbd09a169c8552d1df40b3679776c45cabb47c667022afae50aecd4/pydicom-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="8ff31e077cc51d19ac3b8ca988ac486099cdebfaf885989079fdc7c75068cdd8", url="https://pypi.org/packages/5f/45/97660cc1ec770e2e82fd5d704c1d6ff9c308ecfcbbf07c2b2f92ca755b70/pydicom-2.3.0-py3-none-any.whl")
    version("2.2.2", sha256="6ecb9c6d56a20b2104099b8ef8fe0f3664d797b08a0e0548fe0311b515b32308", url="https://pypi.org/packages/53/9a/98df4fb41e7905b587be2ee9ce38bab8a092990bd174f46fd915a23ec0ea/pydicom-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="444b5b7289135ff5ea76dfc69d3597dcfde1cd050ca387f709d777f35701242d", url="https://pypi.org/packages/f5/05/6228a7ecb8bbd4b6c334dde2cc6e61d21db918ce5288e2d113dca8a46776/pydicom-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="f55f236069d7f0445b5d0dcca7e8733ef17c39e87d6e06e0fac7b9a91442e8a9", url="https://pypi.org/packages/a3/4f/a96cd1bf529854b67e05f77f41b8600164ad5bc76e47bf7f37e9fd1c0f46/pydicom-2.2.0-py3-none-any.whl")
    version("2.1.2", sha256="d97f53a7b269dbd7414d18342f1b70f80d7d35dc4e479316bab146daac0e0c15", url="https://pypi.org/packages/f4/15/df16546bc59bfca390cf072d473fb2c8acd4231636f64356593a63137e55/pydicom-2.1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

