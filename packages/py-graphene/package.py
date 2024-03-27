##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGraphene(PythonPackage):
    version("3.3", sha256="bb3810be33b54cb3e6969506671eb72319e8d7ba0d5ca9c8066472f75bf35a38", url="https://pypi.org/packages/24/70/96f6027cdfc9bb89fc07627b615cb43fb1c443c93498412beaeaf157e9f1/graphene-3.3-py2.py3-none-any.whl")
    version("3.2.2", sha256="753de13948cbf42e32cc87fb533167c88907066eb984251fdbb006c0aab8da00", url="https://pypi.org/packages/38/3d/41d439ed01fccb02f9489df2b8a7a7eb81dd93a4bb060997892b7221b9ed/graphene-3.2.2-py2.py3-none-any.whl")
    version("3.2.1", sha256="2ef689f514ba9e65e88961798cf4c637ca580e541168f9aee2ffbe21fd46f388", url="https://pypi.org/packages/b3/a2/40727944d4587b4d945799a92965f58eb51b1ef8b5bf4d45ce937fade347/graphene-3.2.1-py2.py3-none-any.whl")
    version("3.2", sha256="8df657721284b1e6797644433c67c4906f21bb3c1f14ec80969f927abaa7ca5f", url="https://pypi.org/packages/20/73/c3a99e75fb88ec8600d87c9ed7ea43cc440862e80170c2d232e704735202/graphene-3.2-py2.py3-none-any.whl")
    version("3.1.1", sha256="1c0d43560a86536b7816bb05e3685beebf140118e091a9c445cd10f55acb20fd", url="https://pypi.org/packages/be/8a/2a2b883b69af0e9a7622c8ab7f903a4f5467af76d78a675bd895064f37bb/graphene-3.1.1-py2.py3-none-any.whl")
    version("3.1", sha256="99becdccd2683c2db1a8486e98d007b5e64fa2ff0922e6c1b08e19233031368d", url="https://pypi.org/packages/60/be/249729cfe0313ff4f57a8be2d1846ce072b590188e6d878dbeea01b9b91b/graphene-3.1-py2.py3-none-any.whl")
    version("3.0", sha256="57ce5ee7c9dc194224a1df96e4f7cb48d31eae96c791091d059f8f3d4d131390", url="https://pypi.org/packages/70/1d/220a9c48401c51bbeefa495a9e62142df16316b19b18dc5ac59be2964f47/graphene-3.0-py2.py3-none-any.whl")
    version("2.1.9", sha256="3d446eb1237c551052bc31155cf1a3a607053e4f58c9172b83a1b597beaa0868", url="https://pypi.org/packages/ef/a2/b3e68706bf45abc2f9d70f099a4b4ca6305779577f4a03458d78fb39cd42/graphene-2.1.9-py2.py3-none-any.whl")
    version("2.1.8", sha256="09165f03e1591b76bf57b133482db9be6dac72c74b0a628d3c93182af9c5a896", url="https://pypi.org/packages/05/97/45e743b372f65a619f8d1eb2897efb74fb1b0ffddc731ad37e0aa187ec5c/graphene-2.1.8-py2.py3-none-any.whl")
    version("2.1.7", sha256="acf808d50d053b94f7958414d511489a9e490a7f9563b9be80f6875fc5723d2a", url="https://pypi.org/packages/05/7b/a0f0e846e9418abd4addde6c29c132d407dee48995be425f797cae45ad86/graphene-2.1.7-py2.py3-none-any.whl")
    version("2.1.6", sha256="2ac16d6bb3bdba4da3daa0f6d15b74ac585ed6a016980f502c77c3e687c763bb", url="https://pypi.org/packages/d2/96/6afc1a61f9d7c1159a59b44bcdc37b68dceaa424e5a8ed9afc051082413d/graphene-2.1.6-py2.py3-none-any.whl")
    version("2.1.3", sha256="faa26573b598b22ffd274e2fd7a4c52efa405dcca96e01a62239482246248aa3", url="https://pypi.org/packages/a6/75/73bec3147071034ba73fad9aa2a8f4a41910a93b2cba1bc579420752aa3b/graphene-2.1.3-py2.py3-none-any.whl")
    version("2.1.2", sha256="8fd8e6195c56c15b2936e7dee2e156692eba4752ee1978f65e10925eafe8d014", url="https://pypi.org/packages/17/c8/d326bb2bb207af057d9cd8b986bdc09afa56c54ccf642e0a864e6e9e3970/graphene-2.1.2-py2.py3-none-any.whl")
    version("2.1.1", sha256="66d4918763e6addc818161212e65f329bae9d67b59805e38ca890c28ef2cb887", url="https://pypi.org/packages/63/0a/0a5eb042c7891c23c80480144f490b1b9a08c4aa91041a1b25bd02649f45/graphene-2.1.1-py2.py3-none-any.whl")
    version("2.1", sha256="dc95daa3f808fa1c1b26b780d103216a3d562eb95f72744a054b5bf6609d5c5c", url="https://pypi.org/packages/37/92/b8b543b7a0eeaed5d499c1e4569c646f59ddcf01f59a8f00f7714219422a/graphene-2.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-aniso8601@8:", when="@3.0-beta8:3.0.0,3.1:")
        depends_on("py-aniso8601@3:7", when="@2.1.8:2")
        depends_on("py-aniso8601@3:6", when="@2.1.6:2.1.7")
        depends_on("py-aniso8601@3", when="@2.1:2.1.3")
        depends_on("py-graphql-core@3.1.0:3.2", when="@3.1:")
        depends_on("py-graphql-core@3.1.2:3.1", when="@3.0-beta8:3.0.0")
        depends_on("py-graphql-core@2.1:2", when="@2.1.3:2")
        depends_on("py-graphql-core@2:2.0.0,2.1-rc0:2", when="@2.0.1:2.1.2")
        depends_on("py-graphql-relay@3.1:", when="@3.1:")
        depends_on("py-graphql-relay@3.0.0:", when="@3:3.0.0")
        depends_on("py-graphql-relay@2", when="@2.1.7:2")
        depends_on("py-graphql-relay@0.4.5:0", when="@2.0.1:2.1.6")
        depends_on("py-promise@2.1:2.1.0,2.2-rc1:", when="@2.0.1:2.1.3")
        depends_on("py-six@1.10:", when="@2.0.1:2")

