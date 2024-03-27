##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBravadoCore(PythonPackage):
    version("6.1.1", sha256="8cf1f7bbac2f7c696d37e970253938b5be4ddec92c8d5e64400b17469c3714b4", url="https://pypi.org/packages/ca/6d/1ffa5c64533bc2fa436afdb9ef287cb0c0d443ef1e84db0601b0af7ce6f5/bravado-core-6.1.1.tar.gz")
    version("6.1.0", sha256="e3ac495fca5d475addeae45a2be8a51fd4120416d2183d630f001dfcfcc628dc", url="https://pypi.org/packages/5f/26/7fdeaa8b87bbf2a7d05230d4e9f40b232aff4527fe2d582aa8d4d56cee88/bravado_core-6.1.0-py2.py3-none-any.whl")
    version("6.0.0", sha256="5076b7310d17fbd95f6c70e1e7ee9916bbfc8b9cecef465bd60422a68455ef8d", url="https://pypi.org/packages/b6/d3/b01e9a5aa76a71574196899e9c4e31c40d0e2cf7817c553759ca09032af7/bravado_core-6.0.0-py2.py3-none-any.whl")
    version("5.17.1", sha256="e231567cdc471337d23dfc950c45c5914ade8a78cde7ccf2ebb9433fcda29f40", url="https://pypi.org/packages/31/2e/38770d846b798a8ad84e32dab5bdd1ba6eaccbe4a3069f92660e5c86e8ed/bravado_core-5.17.1-py2.py3-none-any.whl")
    version("5.17.0", sha256="fa53e796ea574f905635a43871439a44713c2ef128c62a8fcc1d0ca8765cf855", url="https://pypi.org/packages/76/11/18e9d28a156c33f2d5f15a5e155dc7130250acb0a569255a2b6b307b596d/bravado_core-5.17.0-py2.py3-none-any.whl")
    version("5.16.1", sha256="64e8d6dae0de3d937d07ce35cbde8d045508871f300b65d68c87721259a38593", url="https://pypi.org/packages/75/8e/28720c0857e79057679f179d96c9295fbf9311933e776f559e8beb83d81d/bravado_core-5.16.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jsonref", when="@1:1.0,1.1.0:2.0,2.2:2.3,2.4.1:3,4.11.3:6.1.0")
        depends_on("py-jsonschema@2.5.1:+format", when="@4.11.3:6.1.0")
        depends_on("py-msgpack@0.5.2:", when="@5.16.1:6.1.0")
        depends_on("py-python-dateutil", when="@1:1.0,1.1.0:2.0,2.2:2.3,2.4.1:4.2.2,4.11.3:6.1.0")
        depends_on("py-pytz", when="@4.11.3:6.1.0")
        depends_on("py-pyyaml", when="@4.1:4.2.2,4.11.3:6.1.0")
        depends_on("py-requests", when="@5.17.1:6.1.0")
        depends_on("py-simplejson", when="@1:1.0,1.1.0:2.0,2.2:2.3,2.4.1:4.2.2,4.11.3:6.1.0")
        depends_on("py-six", when="@1.1.0:2.0,2.2:2.3,2.4.1:4.2.2,4.11.3:6.1.0")
        depends_on("py-swagger-spec-validator@2.0.1:", when="@4:4.2.2,4.11.3:6.1.0")

