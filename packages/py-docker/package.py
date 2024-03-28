# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDocker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.0.0", sha256="12ba681f2777a0ad28ffbcc846a69c31b4dfd9752b47eb425a274ee269c5e14b", url="https://pypi.org/packages/18/bd/9706c10bb12e05043ef138dc8d412cfd17f29c8df0fb28ad71c96a98785d/docker-7.0.0-py3-none-any.whl")
    version("6.1.3", sha256="aecd2277b8bf8e506e484f6ab7aec39abe0038e29fa4a6d3ba86c3fe01844ed9", url="https://pypi.org/packages/db/be/3032490fa33b36ddc8c4b1da3252c6f974e7133f1a50de00c6b85cca203a/docker-6.1.3-py3-none-any.whl")
    version("6.1.2", sha256="134cd828f84543cbf8e594ff81ca90c38288df3c0a559794c12f2e4b634ea19e", url="https://pypi.org/packages/32/a3/9ae84296a1a66fd62d120105edd515796369dfc30dd92eeae00fb1b2f54c/docker-6.1.2-py3-none-any.whl")
    version("6.1.1", sha256="8308b23d3d0982c74f7aa0a3abd774898c0c4fba006e9c3bde4f68354e470fe2", url="https://pypi.org/packages/b6/21/6b7450980b84c435ac4b58ad6b291c99b506d07a261bafe2bd96ecbc68bd/docker-6.1.1-py3-none-any.whl")
    version("6.1.0", sha256="b65c999f87cb5c31700b6944dc17a631071170d1aab3ad6e23506068579f885d", url="https://pypi.org/packages/bc/dc/37798b48dafda361f3006244f8fd0cc403e75bd7af071f7a65a2f68b72bd/docker-6.1.0-py3-none-any.whl")
    version("6.0.1", sha256="dbcb3bd2fa80dca0788ed908218bf43972772009b881ed1e20dfc29a65e49782", url="https://pypi.org/packages/d5/b3/a5e41798a6d4b92880998e0d9e6980e57c5d039f7f7144f87627a6b19084/docker-6.0.1-py3-none-any.whl")
    version("6.0.0", sha256="6e06ee8eca46cd88733df09b6b80c24a1a556bc5cb1e1ae54b2c239886d245cf", url="https://pypi.org/packages/57/16/71275ff97da8d2b3b1895655182eb18692d234860bfb42366aaf511389af/docker-6.0.0-py3-none-any.whl")
    version("5.0.3", sha256="7a79bb439e3df59d0a72621775d600bc8bc8b422d285824cb37103eab91d1ce0", url="https://pypi.org/packages/54/f3/7af47ead249fbb798d64a0438bad5c26f17ef6ac5cd324d802038eb10d90/docker-5.0.3-py2.py3-none-any.whl")
    version("5.0.2", sha256="9b17f0723d83c1f3418d2aa17bf90b24dbe97deda06208dd4262fa30a6ee87eb", url="https://pypi.org/packages/59/86/b2430d652d082a2132bbd6023b3f298d0582977c27f125c7e3875c65e178/docker-5.0.2-py2.py3-none-any.whl")
    version("5.0.1", sha256="b88eef725b33c0ed59c67506631bbb09b480b7ca5a739bbbb948b446443fe914", url="https://pypi.org/packages/0f/f6/7bffaae55542f5317d292f95171a65d535ac26eaf4de65f2c539d680a93d/docker-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="fc961d622160e8021c10d1bcabc388c57d55fb1f917175afbe24af442e6879bd", url="https://pypi.org/packages/b2/5a/f988909dfed18c1ac42ad8d9e611e6c5657e270aa6eb68559985dbb69c13/docker-5.0.0-py2.py3-none-any.whl")
    version("4.2.1", sha256="672f51aead26d90d1cfce84a87e6f71fca401bbc2a6287be18603583620a28ba", url="https://pypi.org/packages/2b/80/4eab8a38ff62c31716d07753980a7c5e6550b61096926384f01e742b4a4b/docker-4.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ssh", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@6:")
        depends_on("py-paramiko@2.4.3:", when="@6:+ssh")
        depends_on("py-paramiko@2.4.2:", when="@3.6:5+ssh")
        depends_on("py-pypiwin32@223:", when="@3.5:4.2 platform=windows")
        depends_on("py-pywin32@304:", when="@6: platform=windows")
        depends_on("py-pywin32@227", when="@4.3:5 platform=windows")
        depends_on("py-requests@2.26:", when="@6:")
        depends_on("py-requests@2.14.2:2.17,2.18.1:", when="@3.3,3.4.1:5")
        depends_on("py-six@1.4:", when="@3.3,3.4.1:4")
        depends_on("py-urllib3@1.26:", when="@6:")
        depends_on("py-websocket-client@0.32:", when="@3.3,3.4.1:6")
    # END DEPENDENCIES

