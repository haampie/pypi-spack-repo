##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySoundfile(PythonPackage):
    version("0.12.1", sha256="2dc3685bed7187c072a46ab4ffddd38cef7de9ae5eb05c03df2ad569cf4dacbc", url="https://pypi.org/packages/ad/bd/0602167a213d9184fc688b1086dc6d374b7ae8c33eccf169f9b50ce6568c/soundfile-0.12.1-py2.py3-none-manylinux_2_17_x86_64.whl")
    version("0.12.0", sha256="5e34870f8e8aef60be350fd4c0aa7f294497b615e39e4bbbe5e87181af93aad5", url="https://pypi.org/packages/d5/2c/86e3810cf60f62a6dfe142df103f2d70afb20d4755186e7b2c5af7546d26/soundfile-0.12.0-py2.py3-none-win_amd64.whl")
    version("0.11.0", sha256="a4ab6f66ad222d8e144dcb6abc73fbb867c11da2934b677f9b129778a6c65112", url="https://pypi.org/packages/5b/c5/4a67efccbb2a8e2ae277a2f679d3ccdd2fcf882e882fd51cd671511336d5/soundfile-0.11.0-py2.py3-none-win_amd64.whl")
    version("0.10.3.post1", sha256="490cff42650733d1832728b937fe99fa1802896f5ef4d61bcf78cf7ebecb107b", url="https://pypi.org/packages/bc/7c/440d411e1bf2ef40ec450bb65a2b85ed8b23aaf12b7a99a1888ab551029c/SoundFile-0.10.3.post1.tar.gz")
    version("0.10.2", sha256="637f6218c867b8cae80f6989634a0813b416b3e6132480d056e6e5a89a921571", url="https://pypi.org/packages/9d/6d/b0687afe9f08809ce035348b4172a248aaf44def7f29e4b575677312176d/SoundFile-0.10.2.tar.gz")
    version("0.10.1", sha256="8e841dd7ccf1b2dc064c19271df95ee8b53868e8edb7a0df2873e0144010154d", url="https://pypi.org/packages/14/5a/219d032dfc386d791973e59b078190ae91096b2ff3fac2fd8be5f08fbe92/SoundFile-0.10.1.tar.gz")
    version("0.9.0.post1", sha256="e01b53f6ba6dce389f388c819b43466b8708e85e9d832a8a3a1ff95af7c60731", url="https://pypi.org/packages/0b/44/b631e3e82448989112c862b5ce066822f21eac0bc0735d2ac787a583a18f/SoundFile-0.9.0.post1.tar.gz")
    version("0.9.0", sha256="6179c20d9c70f2c928c74584ae5f054c5020dfecf59842168f026bcd8839bb53", url="https://pypi.org/packages/63/96/6c538b397bed75e7018d6d77c73035988214d03dc2b4c9b4772010c62dec/SoundFile-0.9.0.tar.gz")
    version("0.8.1", sha256="fe189a852befa99927dd47d2723f8a5187a46d802368650f6eea104683653ed5", url="https://pypi.org/packages/02/f7/310ba710f3a653c342b6ab2cca81a154dac2ce7919e65d385c9198276619/SoundFile-0.8.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-cffi@1:", when="@0.10:")

