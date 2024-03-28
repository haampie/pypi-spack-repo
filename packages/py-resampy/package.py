# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyResampy(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.3", sha256="ad2ed64516b140a122d96704e32bc0f92b23f45419e8b8f478e5a05f83edcebd", url="https://pypi.org/packages/4d/b9/3b00ac340a1aab3389ebcc52c779914a44aadf7b0cb7a3bf053195735607/resampy-0.4.3-py3-none-any.whl")
    version("0.4.2", sha256="4340b6c4e685a865621dfcf016e2a3dd49d865446b6025e30fe88567f22e052e", url="https://pypi.org/packages/f2/d3/5209fd2132452f199b1ddf0d084f9fd5f5f910840e3b282f005b48a503e1/resampy-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="11f3cb4ebcaa4d4bf2ef803350d0887ecbfa10962d5850839f54cf5db31beca0", url="https://pypi.org/packages/96/f6/819514dd8be3681fdd1dc81a94f5e1d51019c18e9e7b351c8e097a86e77f/resampy-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="a2fca38a7a1b0851d7ac66535c8ee42fc778953005810f8d4dc80c46a1f9c3d7", url="https://pypi.org/packages/52/85/488fad73a9db1ae096f59c6927ba07e0d74f2ef30716b3de320431cd4929/resampy-0.4.0-py3-none-any.whl")
    version("0.3.1", sha256="b09066c8f0eb0418d59963aca23b79b52d0ace0b8a6de0fce082e6771f7c3f68", url="https://pypi.org/packages/51/7e/7aec4c54c4b11ac8333dc01d0e910e692be7da944769e37f9e248537a3f1/resampy-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="19aab417ac8c7dee0050def09e0ac8d098a6afa910603e9cae25bd0ef8b805a4", url="https://pypi.org/packages/59/00/2aba99630a823efa086b65f04b7025264b0dc924cae664dd897e6ba1f3d6/resampy-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="62af020d8a6674d8117f62320ce9470437bb1d738a5d06cd55591b69b463929e", url="https://pypi.org/packages/79/75/e22272b9c2185fc8f3af6ce37229708b45e8b855fd4bc38b4d6b040fff65/resampy-0.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-resources", when="@0.4.3: ^python@:3.8")
        depends_on("py-numba@0.53.0:", when="@0.4:")
        depends_on("py-numba@0.47:", when="@0.3")
        depends_on("py-numpy@1.17.0:", when="@0.3:")
    # END DEPENDENCIES

