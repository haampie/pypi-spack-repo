# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGeocube(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.2", sha256="c3cbe475388ea4a5b2fac1474ff02e22920d3a40801af7defe464f41ebc0a949", url="https://pypi.org/packages/d1/5a/03b2378cac6ae4a0ec92100237ad05a03407011fa8bb131fc3e2c18b12ab/geocube-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="5c97131010cd8d556a5fad2a3824452120640ac33a6a45b6ca9ee3c28f2e266f", url="https://pypi.org/packages/3f/60/350d5d329080c3eb49ec74eee8ba526bc29deb864cf28b814964b3f0126a/geocube-0.3.1.tar.gz")
    version("0.0.17", sha256="bf8da0fa96d772ebaea0b98bafa0ba5b8639669d5feb07465d4255af177bddc0", url="https://pypi.org/packages/af/62/86d4ddd39ed705b3856be579202cae2143f84ada9b164717bd187dc4059e/geocube-0.0.17.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.4.3:")
        depends_on("python@3.9:", when="@0.4:0.4.2")
        depends_on("py-appdirs", when="@0.3.2:")
        depends_on("py-click@6:", when="@0.3.2:")
        depends_on("py-geopandas@0.7:", when="@0.3.2:")
        depends_on("py-numpy@1.20.0:", when="@0.3.2:")
        depends_on("py-odc-geo", when="@0.3.2:")
        depends_on("py-pyproj@2:", when="@0.3.2:")
        depends_on("py-rasterio", when="@0.3.2:0.4.2")
        depends_on("py-rioxarray@0.4:", when="@0.3.2:")
        depends_on("py-scipy", when="@0.3.2:")
        depends_on("py-xarray@0.17:", when="@0.3.2:")
    # END DEPENDENCIES

