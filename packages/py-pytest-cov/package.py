# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestCov(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.0", sha256="6ba70b9e97e69fcc3fb45bfeab2d0a138fb65c4d0d6a41ef33983ad114be8c3a", url="https://pypi.org/packages/a7/4b/8b78d126e275efa2379b1c2e09dc52cf70df16fc3b90613ef82531499d73/pytest_cov-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="2feb1b751d66a8bd934e5edfa2e961d11309dc37b73b0eabe73b5945fee20f6b", url="https://pypi.org/packages/fe/1f/9ec0ddd33bd2b37d6ec50bb39155bca4fe7085fa78b3b434c05459a860e3/pytest_cov-4.0.0-py3-none-any.whl")
    version("3.0.0", sha256="578d5d15ac4a25e5f961c938b85a05b09fdaae9deef3bb6de9a6e766622ca7a6", url="https://pypi.org/packages/20/49/b3e0edec68d81846f519c602ac38af9db86e1e71275528b3e814ae236063/pytest_cov-3.0.0-py3-none-any.whl")
    version("2.12.1", sha256="261bb9e47e65bd099c89c3edf92972865210c36813f80ede5277dceb77a4a62a", url="https://pypi.org/packages/ba/84/576b071aef9ac9301e5c0ff35d117e12db50b87da6f12e745e9c5f745cc2/pytest_cov-2.12.1-py2.py3-none-any.whl")
    version("2.12.0", sha256="95d4933dcbbacfa377bb60b29801daa30d90c33981ab2a79e9ab4452c165066e", url="https://pypi.org/packages/2c/70/184e8f4804b21dca4d78b6b76414c9d3b29cedbdef7ba28cdf14fe7de3e0/pytest_cov-2.12.0-py2.py3-none-any.whl")
    version("2.11.1", sha256="bdb9fdb0b85a7cc825269a4c56b48ccaa5c7e365054b6038772c32ddcdc969da", url="https://pypi.org/packages/e3/1a/6affecd2344efee7f2487fac82242474cbac09f9e04929da5944907baf11/pytest_cov-2.11.1-py2.py3-none-any.whl")
    version("2.11.0", sha256="626a8a6ab188656c4f84b67d22436d6c494699d917e567e0048dda6e7f59e028", url="https://pypi.org/packages/3f/12/d5089675aa7955c9b7e8b831184b2b13ccece146c5b23250b0102a0d76e2/pytest_cov-2.11.0-py2.py3-none-any.whl")
    version("2.10.1", sha256="45ec2d5182f89a81fc3eb29e3d1ed3113b9e9a873bcddb2a71faaab066110191", url="https://pypi.org/packages/e5/18/401594af67eda194a8b9167208621761927c937db7d60292608342bbac0a/pytest_cov-2.10.1-py2.py3-none-any.whl")
    version("2.10.0", sha256="6e6d18092dce6fad667cd7020deed816f858ad3b49d5b5e2b1cc1c97a4dba65c", url="https://pypi.org/packages/3d/13/ae3dec587b1cc07fb9f294e52ea9ad140266aea55adb9e12eade3625bd27/pytest_cov-2.10.0-py2.py3-none-any.whl")
    version("2.9.0", sha256="c87dfd8465d865655a8213859f1b4749b43448b5fae465cb981e16d52a811424", url="https://pypi.org/packages/b4/4d/56896f913ea61f0ba504c912bdd748f11e45ef14d5d40975bc8322dccfa0/pytest_cov-2.9.0-py2.py3-none-any.whl")
    version("2.8.1", sha256="cdbdef4f870408ebdbfeb44e63e07eb18bb4619fae852f6e760645fa36172626", url="https://pypi.org/packages/b9/54/3673ee8be482f81527678ac894276223b9814bb7262e4f730469bb7bf70e/pytest_cov-2.8.1-py2.py3-none-any.whl")
    version("2.8.0", sha256="a42cb9af7a429b6cd7c97be307cbb4cefca1d50c5b3018711558341979946851", url="https://pypi.org/packages/45/d7/1d0c77172b033301558fac9a82def90d75cbb4bb99d9095532d492af1b89/pytest_cov-2.8.0-py2.py3-none-any.whl")
    version("2.3.1", sha256="09f34ed04d5ea1a6dc7e5bc08435eaca9a2b55086c50f5cc0a3229b4001bc5f0", url="https://pypi.org/packages/67/94/93dd3288f9a6accfc25e4c636aa912824a2e66d08a464d6f62421da8742f/pytest_cov-2.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-coverage@5.2.1:+toml", when="@2.12:2.12.0,3:")
        depends_on("py-coverage@5.2.1:", when="@2.11,2.12.1:2")
        depends_on("py-coverage@4.4:", when="@2.6:2.10")
        depends_on("py-coverage@3.7.1:", when="@2.1:2.5")
        depends_on("py-pytest@4.6:", when="@2.10:")
        depends_on("py-pytest@3.6:", when="@2.6.1:2.9")
        depends_on("py-pytest@2.6:", when="@2.1:2.5")
        depends_on("py-toml", when="@2.12.1:2")
    # END DEPENDENCIES

