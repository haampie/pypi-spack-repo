##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMultiapiStorage(PythonPackage):
    version("0.3.7", sha256="06c9dd8f2270d93575681b966f383aa0d3199c3b8b2c9ccda49b3c8b5e2d8a1d", url="https://pypi.org/packages/39/84/ad0784da1e48759233214842389b94a841519d4f5ff6b8bf50927d9a6f7b/azure_multiapi_storage-0.3.7-py2.py3-none-any.whl")
    version("0.3.6", sha256="bc6dac11a142c8d654ac612c07b23c01cdc787529153c81aef00d6831447f12b", url="https://pypi.org/packages/d3/d9/a7da2efcc6d75226ec1126883915ece7c45d7bec4c2ad83efe28be582c3d/azure_multiapi_storage-0.3.6-py2.py3-none-any.whl")
    version("0.3.5", sha256="d31340b073f20b55f1a3736e390b4dc227061ba7d99af8a84584e8b3a724ff49", url="https://pypi.org/packages/e6/a9/79b98b5d27b407dd6bae32c453f3151819becd74c27e2bcdf7e6fb3806e7/azure_multiapi_storage-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="d3136025522bb58b13d3119cd7b93d5ffd419307d130ebcb121eec2d32f7dc86", url="https://pypi.org/packages/a5/df/f9963f85e56491340f86c333fd0b84eb1f32a593039f3de2537d3e3b8afd/azure_multiapi_storage-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="b76527225a3d4d042d7d3e1ee5fb1eda91cc53cbd5b51915e80e39265887d4c7", url="https://pypi.org/packages/69/6d/b1684e6cd27ab883c6e26e402596cb8a53f40b6401aaa8c28ce6af123adb/azure_multiapi_storage-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="76e49a2db7dea2a9793ab64770d6df753a5c9da9f55836d25df750e01bbab3aa", url="https://pypi.org/packages/c8/ae/443970797a2498107704d6c7204cf6ec9c7fe5d801feb6f21cf9ac1a861a/azure_multiapi_storage-0.3.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common")
        depends_on("py-azure-core", when="@0.3:0.5")
        depends_on("py-azure-nspkg", when="@:0.3.2")
        depends_on("py-cryptography", when="@:0.5")
        depends_on("py-python-dateutil")
        depends_on("py-requests")

