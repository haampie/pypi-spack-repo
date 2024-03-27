##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCutadapt(PythonPackage):
    version("4.7", sha256="8738a35b363eaf615665a4e7d1b4beb385cd93fb7ffdcf82cd4ab6457acc879b", url="https://pypi.org/packages/92/0f/acf2c1055b31c0cf9edc4a46dd6b900905989d78602aef62293b52057fcb/cutadapt-4.7.tar.gz")
    version("4.4", sha256="4554157c673022e1c433fcd6e3b803008fef60c8e71c01215e4aa04b0f09fe83", url="https://pypi.org/packages/0d/45/88d84af8d51310227e5c5c835946ebc059ae9156502203ce0b64c95e4550/cutadapt-4.4.tar.gz")
    version("4.3", sha256="319de860f975977e080ea42d9d255322060693ca39b7be51187831311702fe29", url="https://pypi.org/packages/c0/70/e7572395f3ef8ff5c6ae067b9b12e0d76b79af190ca9bf35e6270ce10b7f/cutadapt-4.3.tar.gz")
    version("4.2", sha256="ab0ac450baecc1576cc5ccbc06eab2685be9ee7676763938237d954a644237f1", url="https://pypi.org/packages/45/20/7e4d6ebfa2826ff2823e92113c4f7d3502ea0d9a70a5df614a22863edffd/cutadapt-4.2.tar.gz")
    version("4.1", sha256="be745ff24adfb4a3eaf715dfad0e2ccdfad7792ef00c1122adf4fbf3aed9227b", url="https://pypi.org/packages/a3/30/4a889a6916d7480c153774777e634b89865f95cb02f2c3209762c7ef984b/cutadapt-4.1.tar.gz")
    version("2.10", sha256="936b88374b5b393a954852a0fe317a85b798dd4faf5ec52cf3ef4f3c062c242a", url="https://pypi.org/packages/4b/9d/3f98c2619206430ad11e485a2a2f6b3e37f792f11523fee372739abdc1cd/cutadapt-2.10.tar.gz")
    version("2.9", sha256="cad8875b461ca09cea498b4f0e78b0d3dcd7ea84d27d51dac4ed45080bf1499e", url="https://pypi.org/packages/07/fb/416956d0c5a1949b97b3859933c5e9a8a0922a8daa33507486a2f510662a/cutadapt-2.9.tar.gz")
    version("2.5", sha256="ced79e49b93e922e579d0bb9d21298dcb2d7b7b1ea721feed484277e08b1660b", url="https://pypi.org/packages/82/32/20742c90e86ac605c43b8ea3789966413d381bc4e80c712691f84ff3fb7c/cutadapt-2.5.tar.gz")
    version("1.13", sha256="aa9f2c1f33dc081fe94f42b1250e4382b8fb42cabbf6e70a76ff079f211d5fc0", url="https://pypi.org/packages/4b/a0/caf0a418d64a69da12c0f5ede20830f0b7dba2d29efa3f667f1ce69e78da/cutadapt-1.13.tar.gz")

    with default_args(type="run"):
        depends_on("py-dnaio@1.2:", when="@4.7:")
        depends_on("py-dnaio@0.3", when="@2.5")
        depends_on("py-xopen@1.6:", when="@4.5:")
        depends_on("py-xopen@0.8.1:0.8", when="@2.5")

