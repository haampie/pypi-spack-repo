##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOdcGeo(PythonPackage):
    version("0.4.3", sha256="3a665daf1702fe2f407225e5ca4903b823a35cfdcc711992977e812f89cee8a8", url="https://pypi.org/packages/6e/ed/dcca41dd01ab673cb33251c29c6022bdfc722e49f6dc69c6383aae4a78db/odc_geo-0.4.3-py3-none-any.whl")
    version("0.4.2", sha256="ec7f3baea9461afda2eee670848bdb9ba776d236ddf2a8df7dabaa1326c2edba", url="https://pypi.org/packages/ae/2b/71c3d3ef3de8aa0464d3974d8b15505416aa9d8861003ced6de00557ed32/odc_geo-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="e03074229181a3ff6115cec6a822be66e916ad644febd0f47ab96b2804a1b45c", url="https://pypi.org/packages/17/cd/6df614b4c83ad8c4a78283c8a529251e0ef9a687e7708317a048d207ebf6/odc_geo-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="3c640be428855fbe8d8727c857cf0cc6430b241e0144765efa58ddb24952a436", url="https://pypi.org/packages/d3/22/e5d46866a4c191410525cba332aaddc3270146233b583aebde6efdc7d118/odc_geo-0.4.0-py3-none-any.whl")
    version("0.3.3", sha256="c6b42f1fc407b76aca4efa134ace8bbe30861b0d2118657c76f16ef169917ec3", url="https://pypi.org/packages/ab/85/367077ae628108ddc0a8731fe77454d9e952b51125fb367b6d88d79b8042/odc_geo-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="8a60f82dde06fd6aa3a7ce149b4361e5b009fb7cb5949d137f1dff017c71cd50", url="https://pypi.org/packages/17/14/4a100a20d3855532f7e0b5bc951be0ccad015e86f0aa0d443b697d64354d/odc_geo-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="53d5d343cfa3e73a695f990ca958c2da9e1d61f65fb6749406ca595c3b7db80f", url="https://pypi.org/packages/4a/57/d7161a75621cf9f3033305d39303889883396b3e94a5de1854fee9af9778/odc_geo-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="b4aed7c848a0a6fd1cf946e863d214178681c3a257c8afbe1bf3f3614c22a607", url="https://pypi.org/packages/09/58/1ee07c99c42c3cb36503bcc794ec7177cc1a1012e24de74c43ceea39d9ad/odc_geo-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="9ff1e8463688c3de00176405ba737060b5b5fa073f82ca182fde96b6d322f43c", url="https://pypi.org/packages/23/58/d53ca91f9fcef50ea1e02a1cb90919e3e514131e5e5c3f77e4d9d47357fb/odc_geo-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="e64c4a9ce18b6669b9bcb17242a0ec2f9978b87305a644f300bc12159b3674a0", url="https://pypi.org/packages/09/56/ebaace1ef989a75d39c7710277cde3c8c38eaacf11c8a3c8d9548121a636/odc_geo-0.2.1-py3-none-any.whl")
    version("0.1.2", sha256="6f1d5bfb030ea9c1f21e16a8b5b3b1cb68b4d25f5e714fda767317b2bff69f97", url="https://pypi.org/packages/db/a8/136de018114e21fa7b78272e9d9ed80c30a1abac9351fa2ce99e1aa5e778/odc_geo-0.1.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-affine")
        depends_on("py-cachetools")
        depends_on("py-numpy")
        depends_on("py-pyproj@3.0.0:", when="@0.3.1:")
        depends_on("py-pyproj", when="@:0.3.0")
        depends_on("py-shapely")

