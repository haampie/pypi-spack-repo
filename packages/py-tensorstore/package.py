##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorstore(PythonPackage):
    version("0.1.56", sha256="5f8f7bc056cb15bc0d45fedfe1ec38029d6f361aa2fb155a218a577a6d953013", url="https://pypi.org/packages/1a/73/d87c71fac5a85d2499256f509a6bbd3a0dfd5c31f5a3495190bb54c17aa2/tensorstore-0.1.56.tar.gz")
    version("0.1.55", sha256="ccdcceb507223d25b121d4cb15e94339948cfb9bbe08be77e972db0d74fc5485", url="https://pypi.org/packages/0d/9b/0207bcebe9b2887ed466d1e41f5dc6d95a27b8427a4955f0d05b4f2efb37/tensorstore-0.1.55.tar.gz")
    version("0.1.54", sha256="e1a9dcb0be7c828f752375409537d4b39c658dd6c6a0873fe21a24a556ec0e2a", url="https://pypi.org/packages/9b/83/39928c1569007a734006b5ac2eaba26d8751cd292cff9d06887c0de97003/tensorstore-0.1.54.tar.gz")
    version("0.1.53", sha256="45ef74b2dc9f2cd5f766bc373ded91d681cd021cc69d16592df48abaeb81af56", url="https://pypi.org/packages/d8/de/100f9cc727ebb52b65bbe0fa47ae57ef206577acd315258b0ea254d3ddcb/tensorstore-0.1.53.tar.gz")
    version("0.1.52", sha256="db2130a8b792ee2f1fb74a4e89ea049ecbb0070370d365d91870822cbf6cfca7", url="https://pypi.org/packages/a7/30/75098312c8009272994af811d31b90c525149dc03b1c296d817883129d8f/tensorstore-0.1.52.tar.gz")
    version("0.1.51", sha256="8a7610c0cc5263593dd8865160f7a1c51d8380706008cd0f866150b36550bd31", url="https://pypi.org/packages/77/e0/89732b1fa54dff98ddd77da88ec61aeb1f7c7678d7d7ef43e5f0464f48a7/tensorstore-0.1.51.tar.gz")
    version("0.1.50", sha256="e251226bfaca7829966e78712156df316137257328001d3295df849be577e61f", url="https://pypi.org/packages/a7/5f/d341bc67695dad52c5f86aace221cf39999d383708f058c410b8f98a9e6a/tensorstore-0.1.50.tar.gz")
    version("0.1.49", sha256="b0dc120ca4c4bcbb3ec28d826f56d3995fd47e375908f936662f0f7653859515", url="https://pypi.org/packages/97/36/d0aef0bdc54eeae6d1045fb2655120d32c3a06abd076186c464c3db39bd5/tensorstore-0.1.49.tar.gz")
    version("0.1.48", sha256="cf07a75aaa84098cf7b4d673485a326cde1695101225a04bc7b557fcc3c2cbb7", url="https://pypi.org/packages/8d/11/e503f2c903b37985ae5ed45b3c4aebe2d159c6484153bcca8dc0d9666956/tensorstore-0.1.48.tar.gz")
    version("0.1.47", sha256="734c8bdf63ced1d0d45ef008da4f4b54cebcedcac1a20cf255d5cf7679abd3ee", url="https://pypi.org/packages/5b/28/9cefca3712eff158bc81559f08baaff369bec1f2e761da77bf8606adcb26/tensorstore-0.1.47.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.46:")

