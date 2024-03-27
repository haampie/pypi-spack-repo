##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXarrayEinstats(PythonPackage):
    version("0.7.0", sha256="f39403341ebf5b634ab1f1bd0e1bb2dc51046e0df31aa908dfbe2fa6a493712e", url="https://pypi.org/packages/4a/61/1471d0738051be02bea0d84350026f01bfea4d9e9df76c560d7d915b3a9f/xarray_einstats-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="4c6f556a9d8603245545cb88583c04398b10a70c572936a2f48678330545883a", url="https://pypi.org/packages/ad/fc/99e00b0498d9f7258a89bd1b76baa8d8af84dd745d48b6f99f5fb399a91e/xarray_einstats-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="cfe63d788077b667624c96d0b0a9144323861888a4d519777083234929b0de2d", url="https://pypi.org/packages/1a/c3/148ee9d962338acc2a67078b9bf0e862771830e324bdfc5564cd78aec507/xarray_einstats-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="72383da0b19c1a7024c5703e1fe5b0efcfc7349fdd2e75cfa7fa3141fd6aff1e", url="https://pypi.org/packages/18/de/ecc5d49b2ca6969163f5ec26ca6620057a5e0447b7356e434406d289a9c4/xarray_einstats-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="689bdbf152737bb5ec89b286a53dcb18ad531deb68ad957a10471151f0f12a97", url="https://pypi.org/packages/d4/34/99a887017d50d5e5a0fbe641e2ad1fcc887e5794724d022af8187d0ac03b/xarray_einstats-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="e98355440a6178f7dc799d1edd865165ec330d69da72e030b58f5a3d879d98ae", url="https://pypi.org/packages/9d/f4/271ea19df0858469e2c4fd23b178a4d746388a75c1f57ff04ddefa0a8b51/xarray_einstats-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="cb723bcb56231d16ad183e8c3eb750565d96c18b48dfa43bcbafc8359f3d7d5d", url="https://pypi.org/packages/92/21/46ebf23adbfef52d8dbe70234712aae24c94a06b4fa8a5e468acf40eba2f/xarray_einstats-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="260ed8023fa2860f2984e464da1206e20fae2d4e1d6bc24b1b79c5d463c85fe4", url="https://pypi.org/packages/ba/1f/99678332b9a0ec2b8a747622f3fccc60139a1ca89b3626188be8efa2dad3/xarray_einstats-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="b3fa8383b9729c48be40e00596ca6f641f74c9d7ca5a087197d1f9fbf21dc457", url="https://pypi.org/packages/5c/95/c23eaa0ea0b9cbb4e4df54df992e119fa417b5a4c4bf61a81f8073cc72a1/xarray_einstats-0.2.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.6:")
        depends_on("py-numpy@1.22.0:", when="@0.7:")
        depends_on("py-numpy@1.20.0:", when="@0.4:0.5")
        depends_on("py-numpy@1.19.0:", when="@0.3")
        depends_on("py-numpy@1.21.0:", when="@:0.2,0.6")
        depends_on("py-scipy@1.8.0:", when="@0.7:")
        depends_on("py-scipy@1.7.0:", when="@0.6")
        depends_on("py-scipy@1.6.0:", when="@0.4:0.5")
        depends_on("py-scipy@1.5.0:", when="@0.3")
        depends_on("py-scipy", when="@:0.2")
        depends_on("py-xarray@2022.9:", when="@0.5.1:")
        depends_on("py-xarray@0.16:", when="@0.3:0.5.0")
        depends_on("py-xarray@0.20:", when="@:0.2")

