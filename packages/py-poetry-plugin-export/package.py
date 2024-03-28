# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPoetryPluginExport(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.1", sha256="b2258e53ae0d369a73806f957ed0e726eb95c571a0ce8b1f273da686528cc1da", url="https://pypi.org/packages/a5/1e/106eb732a21b809b17366666d97a2b797d30f125efa4202a142d8485dd59/poetry_plugin_export-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="2283b28e0209f9f9598c6fe44f30586ec91329ea1558f908708261e0516bf427", url="https://pypi.org/packages/6f/a4/e45a9ee0de134af25b9b5c6958f88f00938a3f77b513f66e940483bdc11b/poetry_plugin_export-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="2dce6204c9318f1f6509a11a03921fb3f461b201840b59f1c237b6ab454dabcf", url="https://pypi.org/packages/17/bb/78d7d920bb463e4bee64f44d8b0d4a286a80af7e76ff8326e5169103f44b/poetry_plugin_export-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="cd8267597970375ca29868daec5e7718bad500c7584663af3eeb0ed16f24e2bd", url="https://pypi.org/packages/e9/12/43553a79e1d3bf8de119125dfc3e1fcc8f4258d658b603908d02efaed256/poetry_plugin_export-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="5d9186d6f77cf2bf35fc96bd11fe650cc7656e515b17d99cb65018d50ba22589", url="https://pypi.org/packages/8e/85/ffc00ac05b50133f58549b712385a556a4312c30e0367a422fb172a686d5/poetry_plugin_export-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="941d7ba02a59671d6327b16dc6deecc9262477abbc120d728a500cf125bc1e06", url="https://pypi.org/packages/d9/07/fccaeb648bf9f46b64ca60fa51274ff1616fcc48ea614fa99514d87d31b5/poetry_plugin_export-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="6e5919bf84afcb08cdd419a03f909f490d8671f00633a3c6df8ba09b0820dc2f", url="https://pypi.org/packages/ca/9e/8ca64ca388309ccd216f8376a864b24676510ef877a0e2ec2e7d84c27e55/poetry_plugin_export-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="109fb43ebfd0e79d8be2e7f9d43ba2ae357c4975a18dfc0cfdd9597dd086790e", url="https://pypi.org/packages/5c/35/b88b68d6ef53840d694e2a9656670bc049b8c144930ca7c96662a0f26ac6/poetry_plugin_export-1.2.0-py3-none-any.whl")
    version("1.1.2", sha256="946e3313b3d00c18fb9a50522e9d5e6a7e111beaba8d6ae33297662fc2070ac1", url="https://pypi.org/packages/44/28/0e86f03be17db993dce6b81825687ab7587fc54ff0659d20f7bffc03d72c/poetry_plugin_export-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="170fa367794d2385975d75298fe5509f772d35216ee36b8fa50c0350a064b761", url="https://pypi.org/packages/32/75/afe03322cff9f4753ad549eab2429109207dc10efd74cbc1de8b6944b9d9/poetry_plugin_export-1.1.1-py3-none-any.whl")
    version("1.0.7", sha256="dd9d4552e7113a86c97908c13b9a439cb46830f247c7e4969e46a0d8d70e4d3f", url="https://pypi.org/packages/07/79/6875ad552af0f2bb98b60fcd281d17620f5ee49f652e34c54969596f780a/poetry_plugin_export-1.0.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-poetry@1.8:", when="@1.7:")
        depends_on("py-poetry@1.6:", when="@1.6")
        depends_on("py-poetry@1.5:", when="@1.4:1.5")
        depends_on("py-poetry@1.3:1.3.0.0,1.3.1:", when="@1.3")
        depends_on("py-poetry@1.2.2:", when="@1.2")
        depends_on("py-poetry@1.2.0:", when="@1.0.7:1.1")
        depends_on("py-poetry-core@1.7:", when="@1.6:")
        depends_on("py-poetry-core@1.6:", when="@1.4:1.5")
        depends_on("py-poetry-core@1.3:", when="@1.2:1.3")
        depends_on("py-poetry-core@1.1.0:", when="@1.0.7:1.1")
    # END DEPENDENCIES

