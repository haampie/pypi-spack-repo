##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkdocsMaterial(PythonPackage):
    version("8.5.11", sha256="c907b4b052240a5778074a30a78f31a1f8ff82d7012356dc26898b97559f082e", url="https://pypi.org/packages/34/aa/62e1d18c61c278ef7afceb4762e442fb0487e12d53ab700f620fb0cfc99a/mkdocs_material-8.5.11-py3-none-any.whl")
    version("8.5.10", sha256="51760fa4c9ee3ca0b3a661ec9f9817ec312961bb84ff19e5b523fdc5256e1d6c", url="https://pypi.org/packages/6e/cb/efb4e8137a8af504b4e14f473bf1249756f585ddffd9c913448154867e1e/mkdocs_material-8.5.10-py3-none-any.whl")
    version("8.5.9", sha256="143ea55843b3747b640e1110824d91e8a4c670352380e166e64959f9abe98862", url="https://pypi.org/packages/37/76/4116fa40257d8df4550e5aefee7b46cdb2e549a238dd3c050c2188ee639c/mkdocs_material-8.5.9-py3-none-any.whl")
    version("8.5.8", sha256="7ff092299e3a63cef99cd87e4a6cc7e7d9ec31fd190d766fd147c35572e6d593", url="https://pypi.org/packages/b7/df/beb5ce65ff31210f4b7637e93c9bc115f5531056964a7f275c619e6c39bf/mkdocs_material-8.5.8-py3-none-any.whl")
    version("8.5.7", sha256="07fc70dfa325a8019b99a124751c43e4c1c2a739ed1b0b82c00f823f31c9a1e2", url="https://pypi.org/packages/9e/c3/5c15521fe72120cdfbde99da3650bc83419f9caf5af4794a83420c2c00f6/mkdocs_material-8.5.7-py3-none-any.whl")
    version("8.5.6", sha256="b473162c800321b9760453f301a91f7cb40a120a85a9d0464e1e484e74b76bb2", url="https://pypi.org/packages/c4/72/cfdc88993d73c3f3b9b3db5675c63af1e0e30327c498378b3b67dd6a6157/mkdocs_material-8.5.6-py3-none-any.whl")
    version("8.5.5", sha256="0a95965db858cae5c75201726ffc871b8ba54b1ef70b237ca63fd150cfee9f39", url="https://pypi.org/packages/d0/2b/a10186738708ffb7cc97d6ce52fcb8eacb7ac2c1aaf18d7c29c7ca1db2e7/mkdocs_material-8.5.5-py3-none-any.whl")
    version("8.5.4", sha256="aec2f0f2143109f8388aadf76e6fff749a2b74ebe730d0f674c65b53da89d19d", url="https://pypi.org/packages/72/13/ee77fa6a419385393a89cb885a46c76f09fa26392a1225dcb32ce540e687/mkdocs_material-8.5.4-py3-none-any.whl")
    version("8.5.3", sha256="d194c38041d1e83560221022b3f85eec4604b35e44f5c3a488c24b88542074ed", url="https://pypi.org/packages/42/c1/a7b819a4a92cfd4b2e429f15ac3d163b68be0589005f93a0a92df34b8d98/mkdocs_material-8.5.3-py3-none-any.whl")
    version("8.5.2", sha256="1962099d8c6eb7571896a0e7fdc52ff4fda1e906969d0e42ae3537418e807868", url="https://pypi.org/packages/4b/9d/2d9176945c1c211138c22c98f74f1eb8aea8361bd65fcd7da94eb57e5368/mkdocs_material-8.5.2-py2.py3-none-any.whl")
    version("8.4.0", sha256="ef6641e1910d4f217873ac376b4594f3157dca3949901b88b4991ba8e5477577", url="https://pypi.org/packages/b8/be/e2f9f868d64d2147dd641eda9216e0f86ce5b3111a2be63a07cc1bc55520/mkdocs_material-8.4.0-py2.py3-none-any.whl")
    version("8.3.6", sha256="01f3fbab055751b3b75a64b538e86b9ce0c6a0f8d43620f6287dfa16534443e5", url="https://pypi.org/packages/cb/bf/501a3aa2e67f9d35dfd6c1882dc62c53b6bb4dc2110f7d49c1df45d40b92/mkdocs_material-8.3.6-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jinja2@3.0.2:", when="@8.3.1:9.0.0-beta4")
        depends_on("py-markdown@3.2:", when="@4.6.1:6.1,6.2.2:9.2.6")
        depends_on("py-mkdocs@1.4:", when="@8.5.5:8")
        depends_on("py-mkdocs@1.3:", when="@8.2.8:8.5.4")
        depends_on("py-mkdocs-material-extensions@1.1:", when="@8.5.8:9.2.6")
        depends_on("py-mkdocs-material-extensions@1.0.3:", when="@8.2.8:8.5.7")
        depends_on("py-pygments@2.12:", when="@8.2.12:9.0.0-beta4")
        depends_on("py-pymdown-extensions@9.4:", when="@8.2.12:8")
        depends_on("py-requests@2.26:", when="@8.5:9.2.6")

