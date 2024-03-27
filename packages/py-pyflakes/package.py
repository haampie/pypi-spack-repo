##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyflakes(PythonPackage):
    version("3.2.0", sha256="84b5be138a2dfbb40689ca07e2152deb896a65c3a3e24c251c5c62489568074a", url="https://pypi.org/packages/d4/d7/f1b7db88d8e4417c5d47adad627a93547f44bdc9028372dbd2313f34a855/pyflakes-3.2.0-py2.py3-none-any.whl")
    version("3.1.0", sha256="4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774", url="https://pypi.org/packages/00/e9/1e1fd7fae559bfd07704991e9a59dd1349b72423c904256c073ce88a9940/pyflakes-3.1.0-py2.py3-none-any.whl")
    version("3.0.1", sha256="ec55bf7fe21fff7f1ad2f7da62363d749e2a470500eab1b555334b67aa1ef8cf", url="https://pypi.org/packages/af/4c/b1c7008aa7788b3e26c06c60aa18da7d3aa1f00e344aa3f18ac92768854b/pyflakes-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="e38cbaa285564388a9622d7e440445d40c508d8fbf96e0c0f3ef28e47d8ba8a2", url="https://pypi.org/packages/ad/71/aec2836649684d1cb1066a30a7d44bbe333da62621c79e091805f9d010fa/pyflakes-3.0.0-py2.py3-none-any.whl")
    version("2.5.0", sha256="4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2", url="https://pypi.org/packages/dc/13/63178f59f74e53acc2165aee4b002619a3cfa7eeaeac989a9eb41edf364e/pyflakes-2.5.0-py2.py3-none-any.whl")
    version("2.4.0", sha256="3bb3a3f256f4b7968c9c788781e4ff07dce46bdf12339dcda61053375426ee2e", url="https://pypi.org/packages/43/fb/38848eb494af7df9aeb2d7673ace8b213313eb7e391691a79dbaeb6a838f/pyflakes-2.4.0-py2.py3-none-any.whl")
    version("2.3.1", sha256="7893783d01b8a89811dd72d7dfd4d84ff098e5eed95cfa8905b22bbffe52efc3", url="https://pypi.org/packages/6c/11/2a745612f1d3cbbd9c69ba14b1b43a35a2f5c3c81cd0124508c52c64307f/pyflakes-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="910208209dcea632721cb58363d0f72913d9e8cf64dc6f8ae2e02a3609aba40d", url="https://pypi.org/packages/57/7e/188ea51830ff05ecf6154b849cd420cf581c0deb60c173215d326e8af197/pyflakes-2.3.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="0d94e0e05a19e57a99444b6ddcf9a6eb2e5c68d3ca1e98e90707af8152c90a92", url="https://pypi.org/packages/69/5b/fd01b0c696f2f9a6d2c839883b642493b431f28fa32b29abc465ef675473/pyflakes-2.2.0-py2.py3-none-any.whl")
    version("2.1.1", sha256="17dbeb2e3f4d772725c777fabc446d5634d1038f234e77343108ce445ea69ce0", url="https://pypi.org/packages/84/f2/ed0ffb887f8138a8fe5a621b8c0bb9598bfb3989e029f6c6a85ee66628ee/pyflakes-2.1.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="5e8c00e30c464c99e0b501dc160b13a14af7f27d4dffb529c556e30a159e231d", url="https://pypi.org/packages/48/6d/7bfd617b21292397e10e24af4cf42947a359b0c425b66f194cf5d14b1444/pyflakes-2.1.0.tar.gz")
    version("1.6.0", sha256="8d616a382f243dbf19b54743f280b80198be0bca3a5396f1d2e1fca6223e8805", url="https://pypi.org/packages/26/85/f6a315cd3c1aa597fb3a04cc7d7dbea5b3cc66ea6bd13dfa0478bf4876e6/pyflakes-1.6.0.tar.gz")
    version("1.5.0", sha256="aa0d4dff45c0cc2214ba158d29280f8fa1129f3e87858ef825930845146337f4", url="https://pypi.org/packages/5b/b7/dcd6ebc826065ca4ccd2406aac4378e1df6eb91124625d45d520219932a1/pyflakes-1.5.0.tar.gz")
    version("1.4.0", sha256="05c8a1702088e9b54acb422f78210afc6074b3472afa7a0a77f0b8aa3f5db605", url="https://pypi.org/packages/74/b6/80853b2c3cec3cf1c85b4205ed0685b9ea6c25607554dbd5cb1b214af536/pyflakes-1.4.0.tar.gz")
    version("1.3.0", sha256="a4f93317c97a9d9ed71d6ecfe08b68e3de9fea3f4d94dcd1d9d83ccbf929bc31", url="https://pypi.org/packages/9f/48/927b1bf3e15d3dadfcfafb505177a62cdabcb78cf7eac4f31f180d5b1e26/pyflakes-1.3.0.tar.gz")
    version("1.2.3", sha256="2e4a1b636d8809d8f0a69f341acf15b2e401a3221ede11be439911d23ce2139e", url="https://pypi.org/packages/54/80/6a641f832eb6c6a8f7e151e7087aff7a7c04dd8b4aa6134817942cdda1b6/pyflakes-1.2.3.tar.gz")
    version("1.2.2", sha256="58741f9d3bffeba8f88452c1eddcf1b3eee464560e4589e4b81de8b3c9e42e4d", url="https://pypi.org/packages/af/6e/6f8cb1d6dfb08b08c2f4c11fdb478b8d63f51f03d1d1bd61d4e154922cc2/pyflakes-1.2.2.tar.gz")
    version("1.2.1", sha256="7e5e3a5e7ce8d1afb9cbcff2bb10cffaf83e1d94ab7c78eb86a715a88c32e22f", url="https://pypi.org/packages/c8/9c/8db4fc4986466ab7df13835a0653e358305622c96f90807964f73161f7f6/pyflakes-1.2.1.tar.gz")
    version("1.2.0", sha256="3633e000ffdc307ff1a7d7450e895ff8813e20b084ef263b5669eef9bc4c7a52", url="https://pypi.org/packages/34/20/c1c6eb3977d4f4d8ac136c5969bf642273e44c6ac93a22b6a26e8bed32bd/pyflakes-1.2.0.tar.gz")
    version("1.1.0", sha256="e5f959931987e2be178781554b485d52342ec9f1b43f891d2dad07a691c7a89a", url="https://pypi.org/packages/3b/c0/babde99e111ebbbe8864c452db9132069a51c63f60e1cdfa49f00a229fca/pyflakes-1.1.0.tar.gz")
    version("1.0.0", sha256="f39e33a4c03beead8774f005bd3ecf0c3f2f264fa0201de965fce0aff1d34263", url="https://pypi.org/packages/45/24/6bc038f3422bab08c24173c1990a56e9eb0c4582a9b202858a33f8aefeb8/pyflakes-1.0.0.tar.gz")
    version("0.9.2", sha256="05df584a29eeea9a2a2110dd362e53d04e0c4bb1754b4d71234f651917f3c2f0", url="https://pypi.org/packages/59/70/6fbc74a5554fd6f0230f6cc298c9e74847cc727bdbf07c9f9d01ad8c0dc3/pyflakes-0.9.2-py2.py3-none-any.whl")
    version("0.9.1", sha256="0aaa2e555db3fc5084a1e6143cb54b787e8d5dbfb436d616ba3cb2d634f02923", url="https://pypi.org/packages/f2/56/7ddb2c7ba7c6c6583784043d9408a8f165b9fd0a319400ceae0043dea892/pyflakes-0.9.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="763e6dc73539e90badfdb6f476d71fc68abc8ef572b3ef2022ddc9cc6baec4c3", url="https://pypi.org/packages/aa/72/c2cc75d9eb4da5edb6ad23955df0b52048cdada68eb569d4177955f7c6e0/pyflakes-0.9.0-py2.py3-none-any.whl")
    version("0.8.1", sha256="3fa80a10b36d51686bf7744f5dc99622cd5c98ce8ed64022e629868aafc17769", url="https://pypi.org/packages/75/22/a90ec0252f4f87f3ffb6336504de71fe16a49d69c4538dae2f12b9360a38/pyflakes-0.8.1.tar.gz")


