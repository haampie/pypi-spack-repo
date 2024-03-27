##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutodocsumm(PythonPackage):
    version("0.2.12", sha256="b842b53c686c07a4f174721ca4e729b027367703dbf42e2508863a3c6d6c049c", url="https://pypi.org/packages/3c/51/69ddabcb5b61e75b4b5e0135ab03e01a9c7851290dbab55eb7402a1a0359/autodocsumm-0.2.12-py3-none-any.whl")
    version("0.2.11", sha256="f1d0a623bf1ad64d979a9e23fd360d1fb1b8f869beaf3197f711552cddc174e2", url="https://pypi.org/packages/c6/37/0a08e3e1d8b78185837c0c483267b87660ae74cdee0c91dc56ae83093965/autodocsumm-0.2.11-py3-none-any.whl")
    version("0.2.10", sha256="cac15a879e7cf2ebac00fe05ec691ae48d7c5b8e75eceae2f61f98905ac0c2d8", url="https://pypi.org/packages/30/a2/745e121bb48e492d1e8e630bb083951506a5754cbc6d9d196a67df40d6db/autodocsumm-0.2.10-py3-none-any.whl")
    version("0.2.9", sha256="bb12dd4d9041da527656ac73341d473b4220462c9680de63e61b4a63911c34ee", url="https://pypi.org/packages/8c/7e/4546370c2cf82592408a9581b9edff74f63c81e6f015e2830c952acd4ae4/autodocsumm-0.2.9-py3-none-any.whl")
    version("0.2.8", sha256="08f0401bb2c6f2bc92848ebd200c53a3966d1d23658e7d70c52f12b088941f79", url="https://pypi.org/packages/df/84/d9a65c48d7d89bb714245aee802aa41cf2ade370bb5e0bcfe72ddbf07e50/autodocsumm-0.2.8-py3-none-any.whl")
    version("0.2.7", sha256="cea7e2f900e5ac10baa6e831683e9241b0892226210609c087b94f109e0f6ab6", url="https://pypi.org/packages/4c/d3/29b2e2b9d4e0d4ee8b90dd0d8275eab86f4fe9175e86557fbe4b253fb5ec/autodocsumm-0.2.7.tar.gz")
    version("0.2.6", sha256="139ca69c5d6b5cf27c41c7ad9c309663f8ead84be2f6a29eefbcfb5166596cf3", url="https://pypi.org/packages/41/93/6bf36291b67ac4a51de04330203717945f6ac1b479768f6aff5e4b486ce7/autodocsumm-0.2.6.tar.gz")
    version("0.2.5", sha256="384f9b3cca08bb8b4e01517766b0a87425ebaade931e1bca938880790ff7fca6", url="https://pypi.org/packages/af/05/9af2d565b3e2dca3e924f437b0d270ea0181ee6a62a7a7507a7d4a8eeadc/autodocsumm-0.2.5.tar.gz")
    version("0.2.4", sha256="6abf09273885a8247cf0f553ad2d243bcf94a1cb3b02e87f67bde3490cbbf7a0", url="https://pypi.org/packages/07/52/6f914e88da979ec26ce698828cdbb9615c2aeafb40a73d6314b6cfb7fc00/autodocsumm-0.2.4.tar.gz")
    version("0.2.3", sha256="92aac24efb39c9912d383683e401165ff9fa20ff87b78e41658b9731e35a055b", url="https://pypi.org/packages/20/19/ac440aa3b6a8bd32e53f60dccc19a245993029e8c81251b87a562de07242/autodocsumm-0.2.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-sphinx@2.2:", when="@0.2.11:")
        depends_on("py-sphinx@2.2:6", when="@0.2.10")
        depends_on("py-sphinx@2.2:5", when="@0.2.9")
        depends_on("py-sphinx@2.2:4", when="@0.2.8")

