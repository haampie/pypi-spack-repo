##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyprojectMetadata(PythonPackage):
    version("0.7.1", sha256="28691fbb36266a819ec56c9fa1ecaf36f879d6944dfde5411e87fc4ff793aa60", url="https://pypi.org/packages/c4/cb/4678dfd70cd2f2d8969e571cdc1bb1e9293c698f8d1cf428fadcf48d6e9f/pyproject_metadata-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="e4b82a1d2d2b1374eebe7140177af9b3eb1dd0ff15297ed934f38b644c8af20e", url="https://pypi.org/packages/60/85/7de60a21931341f2b4907e4886f34f4c64cd19a28507b6940f284a857b10/pyproject_metadata-0.7.0-py3-none-any.whl")
    version("0.6.1", sha256="36577274efd87df1bedb6fb335620cf7f4959d5457ef39881a7710c5b8c356a9", url="https://pypi.org/packages/87/d4/beeb6ecb90df146a0d8e23599133d4298a0ae9a1ab1547146216965b2551/pyproject_metadata-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="ab6472ec8610a4f2d4785d847e6866b9eefa4c34e40cae2f224ce04ce6296969", url="https://pypi.org/packages/2d/7e/ccc42dba03a858581bfd03f57a5fa1065c7c21a768bb683b47ec7ffb48b7/pyproject_metadata-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="c13f3c6b7665851d52cb85ff77393090227b07bfff339955bf7ab97ba0b2f462", url="https://pypi.org/packages/dd/01/49d0ed3a97a8552a2083d176e66f1232efd288c59c4496ab7b7eeb31b89c/pyproject_metadata-0.5.0-py3-none-any.whl")
    version("0.0.0.dev0", sha256="1958ae1499abcd13b61ebd2c290b3e316fe735125a65c565e978867cbb0524ea", url="https://pypi.org/packages/b4/a0/11be6167e043f7a747d5e01203a9a4aba49c9a9f9e54d3b613aa5c54ccd1/pyproject_metadata-0.0.0.dev0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-packaging@22:", when="@0.7:0.7.0")
        depends_on("py-packaging@19:", when="@0.5:0.6,0.7.1:")

