# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySoundfile(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.1", sha256="e8e1017b2cf1dda767aef19d2fd9ee5ebe07e050d430f77a0a7c66ba08b8cdae", url="https://pypi.org/packages/6f/96/5ff33900998bad58d5381fd1acfcdac11cbea4f08fc72ac1dc25ffb13f6a/soundfile-0.12.1.tar.gz")
    version("0.12.0", sha256="e50c42733ff5396e49a6a689722fa362387b2c403273bcc195994bf4a8e2df3f", url="https://pypi.org/packages/d9/ec/14564fc73cbf50cbc92a51094966011b303b66a1c66884f227bbbb7eb7f7/soundfile-0.12.0.tar.gz")
    version("0.11.0", sha256="931738a1c93e8684c2d3e1d514ac63440ce827ec783ea0a2d3e4730e3dc58c18", url="https://pypi.org/packages/e5/be/d5546b16c06f98d0eada0730a135d2650b1e947d2ebd656d4efb9b3c371c/soundfile-0.11.0.tar.gz")
    version("0.10.3.post1", sha256="490cff42650733d1832728b937fe99fa1802896f5ef4d61bcf78cf7ebecb107b", url="https://pypi.org/packages/bc/7c/440d411e1bf2ef40ec450bb65a2b85ed8b23aaf12b7a99a1888ab551029c/SoundFile-0.10.3.post1.tar.gz")
    version("0.10.2", sha256="637f6218c867b8cae80f6989634a0813b416b3e6132480d056e6e5a89a921571", url="https://pypi.org/packages/9d/6d/b0687afe9f08809ce035348b4172a248aaf44def7f29e4b575677312176d/SoundFile-0.10.2.tar.gz")
    version("0.10.1", sha256="8e841dd7ccf1b2dc064c19271df95ee8b53868e8edb7a0df2873e0144010154d", url="https://pypi.org/packages/14/5a/219d032dfc386d791973e59b078190ae91096b2ff3fac2fd8be5f08fbe92/SoundFile-0.10.1.tar.gz")
    version("0.9.0.post1", sha256="e01b53f6ba6dce389f388c819b43466b8708e85e9d832a8a3a1ff95af7c60731", url="https://pypi.org/packages/0b/44/b631e3e82448989112c862b5ce066822f21eac0bc0735d2ac787a583a18f/SoundFile-0.9.0.post1.tar.gz")
    version("0.9.0", sha256="6179c20d9c70f2c928c74584ae5f054c5020dfecf59842168f026bcd8839bb53", url="https://pypi.org/packages/63/96/6c538b397bed75e7018d6d77c73035988214d03dc2b4c9b4772010c62dec/SoundFile-0.9.0.tar.gz")
    version("0.8.1", sha256="fe189a852befa99927dd47d2723f8a5187a46d802368650f6eea104683653ed5", url="https://pypi.org/packages/02/f7/310ba710f3a653c342b6ab2cca81a154dac2ce7919e65d385c9198276619/SoundFile-0.8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cffi@1:", when="@0.10")
        depends_on("py-numpy", when="@0.10+numpy")
    # END DEPENDENCIES

