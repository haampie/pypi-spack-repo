##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGunicorn(PythonPackage):
    version("21.2.0", sha256="3213aa5e8c24949e792bcacfc176fef362e7aac80b76c56f6b5122bf350722f0", url="https://pypi.org/packages/0e/2a/c3a878eccb100ccddf45c50b6b8db8cf3301a6adede6e31d48e8531cab13/gunicorn-21.2.0-py3-none-any.whl")
    version("21.1.0", sha256="11fc98ea214a5845f614891e8c90b0211fbe595e677d204d7cd7d80f6f348891", url="https://pypi.org/packages/ba/d6/5ec4f4cab2caf886b6b434d6aaa47d25a1bd69b8b7ef44a0d05d840a9e0e/gunicorn-21.1.0-py3-none-any.whl")
    version("21.0.1", sha256="949880781d74f55eda34eb1a552f9c83db6edb42f2bd4f87c09e2a66b13922ea", url="https://pypi.org/packages/a8/91/3f96a766e0c4d6fc55b522a6fab2ba6da13e4e22f1b2b3730b241bedc141/gunicorn-21.0.1-py3-none-any.whl")
    version("21.0.0", sha256="f3a52f282306059b3a39761559c086d326449a2d67eb8ab224f057caa7cd1cff", url="https://pypi.org/packages/e3/02/f669a0ebb42992eff6c581710a43d8e612803a6ad7aa992c71910324c523/gunicorn-21.0.0-py3-none-any.whl")
    version("20.1.0", sha256="9dcc4547dbb1cb284accfb15ab5667a0e5d1881cc443e0677b4882a4067a807e", url="https://pypi.org/packages/e4/dd/5b190393e6066286773a67dfcc2f9492058e9b57c4867a95f1ba5caf0a83/gunicorn-20.1.0-py3-none-any.whl")
    version("20.0.4", sha256="cd4a810dd51bf497552cf3f863b575dabd73d6ad6a91075b65936b151cbf4f9c", url="https://pypi.org/packages/69/ca/926f7cd3a2014b16870086b2d0fdc84a9e49473c68a8dff8b57f7c156f43/gunicorn-20.0.4-py2.py3-none-any.whl")
    version("20.0.3", sha256="1d8012b859f4cd9e45753f1ccb33a94df1ab9e1b7af4f81ac871680b4042b08b", url="https://pypi.org/packages/e4/cc/e29ede47f5591245e7a343ffa541d250ae51ba136bb9a7e8fe6d1bb24803/gunicorn-20.0.3-py2.py3-none-any.whl")
    version("20.0.2", sha256="fe457b7093b353cefcb2ebc40d192fc7c8a62bba49da648c9e1fa0671fa654d1", url="https://pypi.org/packages/4c/f4/1fff9549bda65801f34bd02a86bde95c945401bfc21cc9cb9e35ec790ba5/gunicorn-20.0.2-py2.py3-none-any.whl")
    version("20.0.0", sha256="0806b5e8a2eb8ba9ac1be65d7b743ec896fc25f5d6cb16c5e051540157b315bb", url="https://pypi.org/packages/60/0d/3dbda0324f5bf007f3274e5ea09f0f3bcbf0ca01a75b80ff4f1ff9f8ecfd/gunicorn-20.0.0-py2.py3-none-any.whl")
    version("19.10.0", sha256="c3930fe8de6778ab5ea716cab432ae6335fa9f03b3f2c3e02529214c476f4bcb", url="https://pypi.org/packages/5f/54/c15f2c243c19074cbf06ce6c48732d99aec825487f87e57e86e9a22990f2/gunicorn-19.10.0-py2.py3-none-any.whl")
    version("19.9.0", sha256="aa8e0b40b4157b36a5df5e599f45c9c76d6af43845ba3b3b0efe2c70473c2471", url="https://pypi.org/packages/8c/da/b8dd8deb741bff556db53902d4706774c8e1e67265f69528c14c003644e6/gunicorn-19.9.0-py2.py3-none-any.whl")
    version("19.8.1", sha256="7ef2b828b335ed58e3b64ffa84caceb0a7dd7c5ca12f217241350dec36a1d5dc", url="https://pypi.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl")
    version("19.8.0", sha256="f5ca088d029fe3cea166c59bb43b7ccc9c850fe25af3da61350fe712c5cc5aa2", url="https://pypi.org/packages/ba/a9/67db283e31084925e5b1943a724965f0320577bfdc5144175b64d4328df0/gunicorn-19.8.0-py2.py3-none-any.whl")
    version("19.7.1", sha256="eee1169f0ca667be05db3351a0960765620dad53f53434262ff8901b68a1b622", url="https://pypi.org/packages/30/3a/10bb213cede0cc4d13ac2263316c872a64bf4c819000c8ccd801f1d5f822/gunicorn-19.7.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-packaging", when="@21:")
        depends_on("py-setuptools@3:", when="@20")

