##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathos(PythonPackage):
    version("0.3.2", sha256="d669275e6eb4b3fbcd2846d7a6d1bba315fe23add0c614445ba1408d8b38bafe", url="https://pypi.org/packages/f4/7f/cea34872c000d17972dad998575d14656d7c6bcf1a08a8d66d73c1ef2cca/pathos-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="b1c7145e2adcc19c7e9cac48f110ea5a63e300c1cc10c2947d4857dc97a47b46", url="https://pypi.org/packages/d8/08/ac94fa6f9eefe32963b8a54e573dab0dbc0d3df24fd34924bd9ce7eab7c4/pathos-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="b1f5a79b1c79a594330d451832642ee5bb61dd77dc75ba9e5c72087c77e8994c", url="https://pypi.org/packages/0a/97/56b396300e5832bb95abe28944c1b8a0098ce179dce131a26e5d0e6daa05/pathos-0.3.0-py3-none-any.whl")
    version("0.2.9", sha256="a8dbddcd3d9af32ada7c6dc088d845588c513a29a0ba19ab9f64c5cd83692934", url="https://pypi.org/packages/52/e6/fe7bb138358d27d750c5e88f1fb041af0750f7f1551ae39437f11009f2d9/pathos-0.2.9.tar.gz")
    version("0.2.8", sha256="789ae53487e5f9393fcc2b9703188a1b97f20206c429654134a7152f591bafe7", url="https://pypi.org/packages/23/6b/7ffe02bdb5f5cf4b2290cc906b415dde7c886dbb11928dda40d39e6654dd/pathos-0.2.8-py2.py3-none-any.whl")
    version("0.2.7", sha256="13e40b6d3af87b3f9fa2e03a116345fe8e10942ed33fe371c76a4d5779b20e02", url="https://pypi.org/packages/10/9e/0100b1d500851fc8e093da5463ca38e013c86ea0855e7c510ca0d3e1f7c1/pathos-0.2.7-py2.py3-none-any.whl")
    version("0.2.6", sha256="51b48e54870e4f83a262e49b6369116ab2ecc5a217569a84c7ab726e27b1bc10", url="https://pypi.org/packages/be/ea/b2cf3a6561fc5deb64de8ae0af5e3e4e2db03ca588cb7415efce4a8de26e/pathos-0.2.6.zip")
    version("0.2.5", sha256="21ae2cb1d5a76dcf57d5fe93ae8719c7339f467e246163650c08ccf35b87c846", url="https://pypi.org/packages/c6/a2/cd59f73d5ede4f122687bf8f63de5d671c9561e493ca699241f05b038278/pathos-0.2.5.tar.gz")
    version("0.2.4", sha256="610dc244b6b5c240396ae392bb6f94d7e990b0062d4032c5e9ab00b594ed8720", url="https://pypi.org/packages/ed/6f/c6d34bda9f6383b693418f7b2340e8e6692e5a0ed154e918c09399fbf2ec/pathos-0.2.4.tar.gz")
    version("0.2.3", sha256="954c5b0a8b257c375e35d311c65fa62a210a3d65269195557de38418ac9f61f9", url="https://pypi.org/packages/b1/3e/391c9a3c639fc5ce7502ac16fde81dcc5508f2a9cc0d1acc650725400b52/pathos-0.2.3.tar.gz")
    version("0.2.0", sha256="e35418af733bf434da83746d46acca94375d6e306b3df330b2a1808db026a188", url="https://pypi.org/packages/1d/a0/e5107f85bcb397c82ee875d005d88a537d4fdc1d1498f34bb15dfba7ca49/pathos-0.2.0.tgz")

    with default_args(type="run"):
        depends_on("py-dill@0.3.8:", when="@0.3.2:")
        depends_on("py-dill@0.3.7:", when="@0.3.1")
        depends_on("py-dill@0.3.6:", when="@0.3:0.3.0")
        depends_on("py-dill@0.3.4:", when="@0.2.8")
        depends_on("py-dill@0.3.3:", when="@0.2.7")
        depends_on("py-multiprocess@0.70.16:", when="@0.3.2:")
        depends_on("py-multiprocess@0.70.15:", when="@0.3.1")
        depends_on("py-multiprocess@0.70.14:", when="@0.3:0.3.0")
        depends_on("py-multiprocess@0.70.12:", when="@0.2.8")
        depends_on("py-multiprocess@0.70.11:", when="@0.2.7")
        depends_on("py-pox@0.3.4:", when="@0.3.2:")
        depends_on("py-pox@0.3.3:", when="@0.3.1")
        depends_on("py-pox@0.3.2:", when="@0.3:0.3.0")
        depends_on("py-pox@0.3:", when="@0.2.8")
        depends_on("py-pox@0.2.9:", when="@0.2.7")
        depends_on("py-ppft@1.7.6.8:", when="@0.3.2:")
        depends_on("py-ppft@1.7.6.7:", when="@0.3.1")
        depends_on("py-ppft@1.7.6.6:", when="@0.3:0.3.0")
        depends_on("py-ppft@1.6.6.4:", when="@0.2.8")
        depends_on("py-ppft@1.6.6.3:", when="@0.2.7")

