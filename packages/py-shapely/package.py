# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyShapely(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.3", sha256="4d65d0aa7910af71efa72fd6447e02a8e5dd44da81a983de9d736d6e6ccbe674", url="https://pypi.org/packages/36/8f/03929218f8d7003c3eafa5ffad1fb3f185459d336fa9cc31d3e67f442f97/shapely-2.0.3.tar.gz")
    version("2.0.2", sha256="1713cc04c171baffc5b259ba8531c58acc2a301707b7f021d88a15ed090649e7", url="https://pypi.org/packages/01/c0/ef2c5eff1e8381710e211a063d0aa3e7215cea9e6fd8c31e75bf5f93df85/shapely-2.0.2.tar.gz")
    version("2.0.1", sha256="66a6b1a3e72ece97fc85536a281476f9b7794de2e646ca8a4517e2e3c1446893", url="https://pypi.org/packages/10/a7/de139da3ce303101c357a9ba801328cba85cf6ace157da31a4007bca85e4/shapely-2.0.1.tar.gz")
    version("2.0.0", sha256="11f1b1231a6c04213fb1226c6968d1b1b3b369ec42d1e9655066af87631860ea", url="https://pypi.org/packages/61/76/6e635cc4ba33e8c170ef5934dad5c269dc5cb9607e878efb2aba12f78361/shapely-2.0.0.tar.gz")
    version("1.8.5.post1", sha256="ef3be705c3eac282a28058e6c6e5503419b250f482320df2172abcbea642c831", url="https://pypi.org/packages/92/2e/a8bbe3c6b414c3c61c4b639ab16d5b1f9c4c4095817d417b503413e613c0/Shapely-1.8.5.post1.tar.gz")
    version("1.8.5", sha256="e82b6d60ecfb124120c88fe106a478596bbeab142116d7e7f64a364dac902a92", url="https://pypi.org/packages/21/d0/82ea9573c9ba8e7a5709ee08681249ad25411382f6440f548981286f3b74/Shapely-1.8.5.tar.gz")
    version("1.8.4", sha256="a195e51caafa218291f2cbaa3fef69fd3353c93ec4b65b2a4722c4cf40c3198c", url="https://pypi.org/packages/b5/9a/625d4fc91ef85873801a16700840786117df4c016162a4532c998a7fe6bc/Shapely-1.8.4.tar.gz")
    version("1.8.3", sha256="1ce9da186d48efc50130af96d62ffb4d2e175235143d804ef395aad156d45bb3", url="https://pypi.org/packages/35/6d/ef38757796e756377be74bcae96c6283b21365afc96796c9d2b6ff6ddbe7/Shapely-1.8.3.tar.gz")
    version("1.8.2", sha256="572af9d5006fd5e3213e37ee548912b0341fb26724d6dc8a4e3950c10197ebb6", url="https://pypi.org/packages/93/3c/cda77e57a08c49569de5bd90376c547bcb981420100adcb0f3770ed681b1/Shapely-1.8.2.tar.gz")
    version("1.8.1.post1", sha256="93ff06ff05fbe2be843b93c7b1ad8292e56e665ba01b4708f75ae8a757972e9f", url="https://pypi.org/packages/30/36/a0a03a29924479c28ed85ab0f21661a98783142fa0c2c75dfdef8c9fe228/Shapely-1.8.1.post1.tar.gz")
    version("1.8.1", sha256="0956a3aced40c31a957a52aa1935467334926844a6776b469acb0760a5e6aba8", url="https://pypi.org/packages/96/d6/7a079ff26207f2357b152f21a5d53a1e8f6b3205bf9a90fb9a52560e0dcf/Shapely-1.8.1.tar.gz")
    version("1.8.0", sha256="f5307ee14ba4199f8bbcf6532ca33064661c1433960c432c84f0daa73b47ef9c", url="https://pypi.org/packages/1c/0c/454c80f71bd5ece52fb06d2905bf956b9122f4be539d5ae5df4b10dd3e14/Shapely-1.8.0.tar.gz")
    version("1.7.1", sha256="1641724c1055459a7e2b8bbe47ba25bdc89554582e62aec23cb3f3ca25f9b129", url="https://pypi.org/packages/42/f3/0e1bc2c4f15e05e30c6b99322b9ddaa2babb3f43bc7df2698efdc1553439/Shapely-1.7.1.tar.gz")
    version("1.7.0", sha256="e21a9fe1a416463ff11ae037766fe410526c95700b9e545372475d2361cc951e", url="https://pypi.org/packages/44/ec/4eddbf9d17a917c51fb4ad159aa7137f506681e91ab559cf87d120e1d78d/Shapely-1.7.0.tar.gz")
    version("1.6.4", sha256="b10bc4199cfefcf1c0e5d932eac89369550320ca4bdf40559328d85f1ca4f655", url="https://pypi.org/packages/55/60/d04f6cf9834125f1d205cd43d14ebcf58d2cbc74d6e702d1ea59b0bbe2dd/Shapely-1.6.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.14.0:1", when="@2.0.3:")
        depends_on("py-numpy@1.14.0:", when="@2.0.2")
    # END DEPENDENCIES

