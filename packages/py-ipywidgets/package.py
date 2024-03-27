##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpywidgets(PythonPackage):
    version("8.1.2", sha256="bbe43850d79fb5e906b14801d6c01402857996864d1e5b6fa62dd2ee35559f60", url="https://pypi.org/packages/70/1a/7edeedb1c089d63ccd8bd5c0612334774e90cf9337de9fe6c82d90081791/ipywidgets-8.1.2-py3-none-any.whl")
    version("8.1.1", sha256="2b88d728656aea3bbfd05d32c747cfd0078f9d7e159cf982433b58ad717eed7f", url="https://pypi.org/packages/4a/0e/57ed498fafbc60419a9332d872e929879ceba2d73cb11d284d7112472b3e/ipywidgets-8.1.1-py3-none-any.whl")
    version("8.1.0", sha256="6c8396cc7b8c95dfb4e9ab0054f48c002f045e7e5d7ae523f559d64e525a98ab", url="https://pypi.org/packages/b8/d4/ce436660098b2f456e2b8fdf76d4f33cbc3766c874c4aa2f772c7a5e943f/ipywidgets-8.1.0-py3-none-any.whl")
    version("8.0.7", sha256="e0aed0c95a1e55b6a123f64305245578bdc09e52965a34941c2b6a578b8c64a0", url="https://pypi.org/packages/a3/af/9d5f256025100b578b11d7280e76fda349255666f752b618a613785cb58d/ipywidgets-8.0.7-py3-none-any.whl")
    version("8.0.6", sha256="a60bf8d2528997e05ac83fd19ea2fbe65f2e79fbe1b2b35779bdfc46c2941dcc", url="https://pypi.org/packages/50/7d/2c8b7bba2b1c2b5d1299f22fa7853f09b573c84e63b62870c13a6ec11990/ipywidgets-8.0.6-py3-none-any.whl")
    version("8.0.5", sha256="a6e5c0392f86207fae304688a670afb26b2fd819592cfc0812777c2fdf22dbad", url="https://pypi.org/packages/e4/e5/783e5336ba667c56cde503ce76c5d49aed11fd0c07cfaea32b1896d64f20/ipywidgets-8.0.5-py3-none-any.whl")
    version("8.0.4", sha256="ebb195e743b16c3947fe8827190fb87b4d00979c0fbf685afe4d2c4927059fa1", url="https://pypi.org/packages/f3/fc/bd076538811d63babf8ceea0ff3d8d024171569a47f5dba7757c5fd0462c/ipywidgets-8.0.4-py3-none-any.whl")
    version("8.0.3", sha256="db7dd35fb1217636cbdbe0ba0bd2216d91a7695cb28b5c1dca17e62cd51378de", url="https://pypi.org/packages/37/9e/a8af39f78f49588a347a94cc76253cc83e791a1f661d2a6110dcf032dc85/ipywidgets-8.0.3-py3-none-any.whl")
    version("8.0.2", sha256="1dc3dd4ee19ded045ea7c86eb273033d238d8e43f9e7872c52d092683f263891", url="https://pypi.org/packages/e4/56/990c10ca8751182ace2464cb0e4baafb7087a40c185c9142b9cd18683fac/ipywidgets-8.0.2-py3-none-any.whl")
    version("8.0.1", sha256="fc0744df3a964ecfd68a6d2debe547fe89db252b8d7bb3db5740aba72edb0e6c", url="https://pypi.org/packages/e5/5a/5577b93efe7f8b21cfe0063bd0ed501aeebdc1e6d2cfaddde2612e945f28/ipywidgets-8.0.1-py3-none-any.whl")
    version("7.8.1", sha256="29f7056d368bf0a7b35d51cf0c56b58582da57c78bb9f765965fef7c332e807c", url="https://pypi.org/packages/14/3f/fa7fcf85061819f5a10ed09eaef38fe97d0f3f91d14674bbb26c3fc2a622/ipywidgets-7.8.1-py2.py3-none-any.whl")
    version("7.8.0", sha256="47e5d57c2f73f6464ea422978106a119ab2721d88e2d4982282ebb54eb59a88e", url="https://pypi.org/packages/dc/0f/efa0531c38e7651d7b229e4746ed83ddd286d0ad80a316b175a4b14e8c1c/ipywidgets-7.8.0-py2.py3-none-any.whl")
    version("7.7.5", sha256="d9644e473282ca28a6bc0327372bcad7a41877d0092fea1ed70bd15f28be9270", url="https://pypi.org/packages/34/65/e97c8528ce10091a7467fe82ade2d101270a233b9fb7324012ed0ebd0586/ipywidgets-7.7.5-py2.py3-none-any.whl")
    version("7.7.4", sha256="295b7c9ba2c2e9d0c720b15bfe1f7c082db83540864d3ebc5bf57c92ae008bd6", url="https://pypi.org/packages/32/d2/fdef71ee265d3776f234264c57107bf0be54551319b22bcff9c66745532c/ipywidgets-7.7.4-py2.py3-none-any.whl")
    version("7.7.3", sha256="c537a31feb4717d42b2331c9201a5c08e214693ca7439563fd4f1b64705312b9", url="https://pypi.org/packages/e4/b4/b35e08aa1580768121157eb04eba14294715d5de87a5ad8405793e49ab0a/ipywidgets-7.7.3-py2.py3-none-any.whl")
    version("7.7.2", sha256="3d47a7826cc6e2644d7cb90db26699451f8b42379cf63b761431b63d19984ca2", url="https://pypi.org/packages/d9/33/b318bd7cb2672a59466c3dcd24760f2221c163e851c9006b6c26af2c9152/ipywidgets-7.7.2-py2.py3-none-any.whl")
    version("7.7.1", sha256="aa1076ab7102b2486ae2607c43c243200a07c17d6093676c419d4b6762489a50", url="https://pypi.org/packages/fa/b2/4af75a543f6c3475a982e814fecd9bf13ba06210c64a6da85475a39bd16b/ipywidgets-7.7.1-py2.py3-none-any.whl")
    version("7.7.0", sha256="e58ff58bc94d481e91ecb6e13a5cb96a87b6b8ade135e055603d0ca24593df38", url="https://pypi.org/packages/86/7d/06b48ec5fd605775c7e85b3ea397d8f0294f66d570bcee59496eb5195fc5/ipywidgets-7.7.0-py2.py3-none-any.whl")
    version("7.6.6", sha256="07fa90abe25182fa72cb1b43212bcdb3ffbc2c9684af5a0cf3f2724bc0df0e83", url="https://pypi.org/packages/14/4c/0a2c721e85fd1fc397cee7773a5a4d9125e205abebd1dc551aa73274dd5b/ipywidgets-7.6.6-py2.py3-none-any.whl")
    version("7.6.5", sha256="d258f582f915c62ea91023299603be095de19afb5ee271698f88327b9fe9bf43", url="https://pypi.org/packages/6b/bb/285066ddd710779cb69f03d42fa72fbfe4352b4895eb6abab551eae1535a/ipywidgets-7.6.5-py2.py3-none-any.whl")
    version("7.6.3", sha256="e6513cfdaf5878de30f32d57f6dc2474da395a2a2991b94d487406c0ab7f55ca", url="https://pypi.org/packages/11/53/084940a83a8158364e630a664a30b03068c25ab75243224d6b488800d43a/ipywidgets-7.6.3-py2.py3-none-any.whl")
    version("7.5.1", sha256="13ffeca438e0c0f91ae583dc22f50379b9d6b28390ac7be8b757140e9a771516", url="https://pypi.org/packages/56/a0/dbcf5881bb2f51e8db678211907f16ea0a182b232c591a6d6f276985ca95/ipywidgets-7.5.1-py2.py3-none-any.whl")
    version("7.4.2", sha256="0f2b5cde9f272cb49d52f3f0889fdd1a7ae1e74f37b48dac35a83152780d2b7b", url="https://pypi.org/packages/30/9a/a008c7b1183fac9e52066d80a379b3c64eab535bd9d86cdc29a0b766fd82/ipywidgets-7.4.2-py2.py3-none-any.whl")
    version("5.2.2", sha256="baf6098f054dd5eacc2934b8ea3bef908b81ca8660d839f1f940255a72c660d2", url="https://pypi.org/packages/51/b1/81b0f4ad11922a8180ce20496af28d67ecd1232fb5ad472088542bea0fae/ipywidgets-5.2.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-comm@0.1.3:", when="@7.8:7,8.1:")
        depends_on("py-ipykernel@4.5.1:", when="@6.0.0:7.7.3,7.7.5:7.7,8:8.0.4,8.0.6:8.0")
        depends_on("py-ipython@6.1:", when="@8:")
        depends_on("py-ipython@4.0.0:", when="@5.2.3:5,6.0.0:7")
        depends_on("py-ipython-genutils@0.2:", when="@7.6.4:7")
        depends_on("py-jupyterlab-widgets@3.0.10:", when="@8.1.2:")
        depends_on("py-jupyterlab-widgets@3.0.9:", when="@8.1.1")
        depends_on("py-jupyterlab-widgets@3.0.7:", when="@8.0.6:8.1.0")
        depends_on("py-jupyterlab-widgets@3.0.0:", when="@8.0.0:8.0.5")
        depends_on("py-jupyterlab-widgets@1.0.0:2", when="@7.6.6:7.6,7.7.2:7")
        depends_on("py-jupyterlab-widgets@1.0.0:", when="@7.6.0:7.6.5,7.7:7.7.1")
        depends_on("py-nbformat@4.2:", when="@6.0.0:7.7.0,8:8.0.0-rc0")
        depends_on("py-traitlets@4.3.1:", when="@6.0.0:")
        depends_on("py-widgetsnbextension@4.0.10:", when="@8.1.2:")
        depends_on("py-widgetsnbextension@4.0.9:", when="@8.1.1")
        depends_on("py-widgetsnbextension@4.0.7:", when="@8.0.6:8.1.0")
        depends_on("py-widgetsnbextension@4.0.0:", when="@8.0.0:8.0.5")
        depends_on("py-widgetsnbextension@3.6.6:3", when="@7.8.1:7")
        depends_on("py-widgetsnbextension@3.6.5:3", when="@7.8:7.8.0")
        depends_on("py-widgetsnbextension@3.6.4:3", when="@7.7.5:7.7")
        depends_on("py-widgetsnbextension@3.6.0:3", when="@7.7.0:7.7.4")
        depends_on("py-widgetsnbextension@3.5.0:3.5", when="@7.5.0:7.7.0-alpha0")
        depends_on("py-widgetsnbextension@3.4", when="@7.4")

