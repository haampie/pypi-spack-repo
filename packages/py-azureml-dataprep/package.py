##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlDataprep(PythonPackage):
    version("2.11.0", sha256="755c0d7cfe228705aee7adc97813fb6d7d6ecb048b66f47c1fd5897f2709c3a2", url="https://pypi.org/packages/b5/2d/93d4f59df163f5ac3569df36f2e59c26ecd234576c782ffe6a5da4664532/azureml_dataprep-2.11.0-py3-none-any.whl")
    version("2.10.3", sha256="6bda202ab692e573e33b468f9e5d25f3f1c73b2d0654b094f5069b9a6e4b562c", url="https://pypi.org/packages/25/f4/cb3c5c13ab4c8f0eec70b259cbcdd7fea2daaf22491c3c8c61c76bdbd596/azureml_dataprep-2.10.3-py3-none-any.whl")
    version("2.10.2", sha256="65a888e44b2144a18317022dfcf52027a08637913e2f019dff52664d8ae9489b", url="https://pypi.org/packages/f6/a9/c9ffa16e621249f0328f773b5fd59b9c141b0f2603d042d3d96fc0c29320/azureml_dataprep-2.10.2-py3-none-any.whl")
    version("2.10.1", sha256="a36f807112ff1e64d21265b8e7f40154c93e3bead539e2a74c9d74200fd77c86", url="https://pypi.org/packages/e8/bb/7067a58daf81e32bae7dd92a38b46d6fe35a1b2bcf69d4e77f7254703032/azureml_dataprep-2.10.1-py3-none-any.whl")
    version("2.10.0", sha256="172ffd348d5fef492acbb3c8dd28fb60b3b53d80a517b058a4559b57edff993b", url="https://pypi.org/packages/17/5c/d1837a8d32f539ae1bf51189b46a88f29ce7092687e5b9ad81a217c69385/azureml_dataprep-2.10.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-identity@1.2:1.4", when="@2.4.3:2.4,2.5.2:2.23")
        depends_on("py-azureml-dataprep-native@30", when="@2.10:2.11")
        depends_on("py-azureml-dataprep-rslex@1.9", when="@2.11")
        depends_on("py-azureml-dataprep-rslex@1.8", when="@2.10")
        depends_on("py-cloudpickle@1.1:1", when="@2:2.25")
        depends_on("py-dotnetcore2@2.1.14:2", when="@2:3")

