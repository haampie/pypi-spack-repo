##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribHtmlhelp(PythonPackage):
    version("2.0.5", sha256="393f04f112b4d2f53d93448d4bce35842f62b307ccdc549ec1585e950bc35e04", url="https://pypi.org/packages/c2/e9/74c4cda5b409af3222fda38f0774e616011bc935f639dbc0da5ca2d1be7d/sphinxcontrib_htmlhelp-2.0.5-py3-none-any.whl")
    version("2.0.4", sha256="8001661c077a73c29beaf4a79968d0726103c5605e27db92b9ebed8bab1359e9", url="https://pypi.org/packages/28/7a/958f8e3e6abe8219d0d1f1224886de847ab227b218f4a07b61bc337f64be/sphinxcontrib_htmlhelp-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="abee4e6c5471203ad2fc40dc6a16ed99884a5d6b15a6f79c9269a7e82cf04149", url="https://pypi.org/packages/d0/a1/5b678486ce3f7f3135ac5396db4591e967fc6709f27aa57fe13c97180953/sphinxcontrib_htmlhelp-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="3fc535431dced1d3f50d30e3d9135873a724f6c38eeb4ac967ebb5c06d7bff9c", url="https://pypi.org/packages/57/41/ad44d14fd5273a7b20905fa4dd8444abf1795f6581666f6272e7d8cabf5a/sphinxcontrib_htmlhelp-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="c38cb46dccf316c79de6e5515e1770414b797162b23cd3d06e67020e1d2a6903", url="https://pypi.org/packages/6e/ee/a1f5e39046cbb5f8bc8fba87d1ddf1c6643fbc9194e58d26e606de4b9074/sphinxcontrib_htmlhelp-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="d412243dfb797ae3ec2b59eca0e52dac12e75a241bf0e4eb861e450d06c6ed07", url="https://pypi.org/packages/63/40/c854ef09500e25f6432dcbad0f37df87fd7046d376272292d8654cc71c95/sphinxcontrib_htmlhelp-2.0.0-py2.py3-none-any.whl")
    version("1.0.3", sha256="3c0bc24a2c41e340ac37c85ced6dafc879ab485c095b1d65d2461ac2f7cca86f", url="https://pypi.org/packages/36/62/8222554b29b3acde8420128d6d3999c5904d40922ef4b6ccb370e2be7421/sphinxcontrib_htmlhelp-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="d4fd39a65a625c9df86d7fa8a2d9f3cd8299a3a4b15db63b50aac9e161d8eff7", url="https://pypi.org/packages/e4/35/80a67cc493f4a8a9634ab203a77aaa1b84d79ccb1c02eca72cb084d2c7f7/sphinxcontrib_htmlhelp-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="e31c8271f5a8f04b620a500c0442a7d5cfc1a732fa5c10ec363f90fe72af0cb8", url="https://pypi.org/packages/8c/55/e3d2302b033b25b4a67abe436cabb19e3bfa17fbc7b9ec44b1bfd9a41dbb/sphinxcontrib_htmlhelp-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="aab51724df91c3075a573d83033b51a720860547c6f4128646d7ff648a3a1b85", url="https://pypi.org/packages/fb/af/ab3dda6f276f9c67f72b2d631e8e8a013dbb5fe4b665792ca0536289bc45/sphinxcontrib_htmlhelp-1.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.0.2:")
        depends_on("py-sphinx@5.0.0:", when="@2.0.2:2.0.4")

