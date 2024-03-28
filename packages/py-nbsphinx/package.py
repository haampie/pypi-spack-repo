# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbsphinx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.3", sha256="6e805e9627f4a358bd5720d5cbf8bf48853989c79af557afd91a5f22e163029f", url="https://pypi.org/packages/a3/a0/ca4aeb2f7f2608a483459a3bb486da250a7eb23eb76c9a0af154395f0cb2/nbsphinx-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="2746680ece5ad3b0e980639d717a5041a1c1aafb416846b72dfaeecc306bc351", url="https://pypi.org/packages/9f/30/ee4dc91710a76c287128f205087544e8adb3a373959e70be6c555ddb40c2/nbsphinx-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="c2991a2c497715f52f6c727f8a633e309f097fe9bb794538011ca1ddb6b698fa", url="https://pypi.org/packages/90/2f/29da1878be332c5f045073761e20a957a6ddef542609640581e620d1e400/nbsphinx-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="09d578cf2dfe38ed8caf680d8b6b66aa2da475f8e2daff3a14757b3df5631752", url="https://pypi.org/packages/23/5c/0a7bd40b1f99a1899a687bf84168dde02beb3601e445f8ecfa42448ccc01/nbsphinx-0.9.0-py3-none-any.whl")
    version("0.8.12", sha256="c15b681c7fce287000856f91fe1edac50d29f7b0c15bbc746fbe55c8eb84750b", url="https://pypi.org/packages/da/38/aff624a3002565c8da13657f11550dbbb65be7401a36656702f2eed4e1b6/nbsphinx-0.8.12-py3-none-any.whl")
    version("0.8.11", sha256="e5c6c76b12fbc425d5538d4b8c0d6fb0c134c28459d4a1b54f41d704b34b4bd1", url="https://pypi.org/packages/f4/f7/a0f94baf48db757c5de1788fcc7e4971e109c1f04ab0331945dbe7cd04fe/nbsphinx-0.8.11-py3-none-any.whl")
    version("0.8.10", sha256="6076fba58020420927899362579f12779a43091eb238f414519ec25b4a8cfc96", url="https://pypi.org/packages/0b/c8/138ec8990f16f765c30a4c350e0fb559eb7698d3ab3b52000773c00ad163/nbsphinx-0.8.10-py3-none-any.whl")
    version("0.8.9", sha256="a7d743762249ee6bac3350a91eb3717a6e1c75f239f2c2a85491f9aca5a63be1", url="https://pypi.org/packages/5b/d1/e18913402619e2673bd29e8e1dc17e0a5e2f2058e8cb0a82e5f86661ea3e/nbsphinx-0.8.9-py3-none-any.whl")
    version("0.8.8", sha256="c6c3875f8735b9ea57d65f81a7e240542daa613cad10661c54e0adee4e77938c", url="https://pypi.org/packages/6d/ec/13038168ecd191aded1de0443817ce6574ec9434d5b7eca7acd16719d610/nbsphinx-0.8.8-py3-none-any.whl")
    version("0.8.7", sha256="8862f291f98c1a163bdb5bac8adf25c61585a81575ac5c613320c6f3fe5c472f", url="https://pypi.org/packages/eb/4d/2c07c13682465e0d2159af292fa20cee26e6a6e322c02764e0ac5d74a824/nbsphinx-0.8.7-py3-none-any.whl")
    version("0.8.6", sha256="133149fd01cbf3c89a2f1a3ca0edfaaddaf55bafbf69b086017df602161b26c8", url="https://pypi.org/packages/ac/ca/35bf177af6ce8afc9db205b00f44fbe16e01193a5fb45b6aa3766ad52d79/nbsphinx-0.8.6-py3-none-any.whl")
    version("0.8.5", sha256="5c8a5731d447653b213ba4429c5b5ee55e0a2e92b5bae3ed931d65bc0ce481ed", url="https://pypi.org/packages/ed/26/2244da6ce9f323747f2512a7201c54c69bc41e59b624159c7e2c8714e07c/nbsphinx-0.8.5-py3-none-any.whl")
    version("0.8.1", sha256="ef75e15047e36faa9741267286b9dc7d5a0d16302f65adee73885e8949ec6f75", url="https://pypi.org/packages/1b/1d/b65dff2f8dc45460e77cef7bb8b761444ecf25759d847c955db02277eb3a/nbsphinx-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="14ccbbd3d5944fd7e14087f67b83ea75cd41c9eb679561258237987d322e9381", url="https://pypi.org/packages/6f/7a/9828e8981e472e717f695da957f52b389e91086532797005999342f487b5/nbsphinx-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils")
        depends_on("py-jinja2@2.11:2", when="@0.8.5")
        depends_on("py-jinja2", when="@:0.8.4,0.8.6:")
        depends_on("py-nbconvert@:5.3,5.4.1:", when="@0.3.5:")
        depends_on("py-nbformat")
        depends_on("py-sphinx@1.8.0:", when="@0.5:")
        depends_on("py-traitlets@5.0.0:", when="@0.8.9:")
        depends_on("py-traitlets", when="@0.2.10:0.8.8")
    # END DEPENDENCIES

