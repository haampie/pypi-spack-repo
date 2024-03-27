##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRfc3986(PythonPackage):
    version("2.0.0", sha256="50b1502b60e289cb37883f3dfd34532b8873c7de9f49bb546641ce9cbd256ebd", url="https://pypi.org/packages/ff/9a/9afaade874b2fa6c752c36f1548f718b5b83af81ed9b76628329dab81c1b/rfc3986-2.0.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="a86d6e1f5b1dc238b218b012df0aa79409667bb209e58da56d0b94704e712a97", url="https://pypi.org/packages/c4/e5/63ca2c4edf4e00657584608bee1001302bbf8c5f569340b78304f2f446cb/rfc3986-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="af9147e9aceda37c91a05f4deb128d4b4b49d6b199775fd2d2927768abdc8f50", url="https://pypi.org/packages/78/be/7b8b99fd74ff5684225f50dd0e865393d2265656ef3b4ba9eaaaffe622b8/rfc3986-1.4.0-py2.py3-none-any.whl")
    version("1.3.2", sha256="df4eba676077cefb86450c8f60121b9ae04b94f65f85b69f3f731af0516b7b18", url="https://pypi.org/packages/00/8d/9d56bfe43997f1864fe0891be69bc239ded98e69c9f56eb9eaa5b1789660/rfc3986-1.3.2-py2.py3-none-any.whl")
    version("1.3.1", sha256="a69146f5014a7da1fed9d375c99f5fe2782a27c0e75c778a4083fe954abbde42", url="https://pypi.org/packages/a8/1e/648eed6ea17d1de1585c7a534e765104818eaa16c74ff6cfd3951caeefee/rfc3986-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="5ec984c915ce01ec6c4ebe37ade6a3a8cee6856bfd4facf459799b52142ef978", url="https://pypi.org/packages/71/3e/2171b66145c6a74a94d80e4e6f4dbc5ff08d3add68062a2c426cfbbe402f/rfc3986-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="5ad82677b02b88c8d24f6511b4ee9baa5e7da675599b479fbbc5c9c578b5b737", url="https://pypi.org/packages/e1/59/1d547e9e5e1bf8074951067c3d6b31a2e29fd5b49bd7d32e53ff0da6406c/rfc3986-1.2.0-py2.py3-none-any.whl")

    variant("idna2008", default=False)

    with default_args(type="run"):
        depends_on("py-idna", when="@1.3:+idna2008")

