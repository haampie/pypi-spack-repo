# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyItolapi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.4", sha256="bba9b28e87003954908ae7cd12f62ef91d76d559d847e1f9526ac361c9df91b8", url="https://pypi.org/packages/63/5e/d6c5cc94c2530b0e6b0d7a3ded92f4aeb030cc025849606f840cad0d0ecb/itolapi-4.1.4-py3-none-any.whl")
    version("4.1.3", sha256="e8f1e8eaf89deca71874cfd93eee5e43d2b3999267c7be5c26bbd44a27a841b9", url="https://pypi.org/packages/32/32/3f6296d8d04b3f40f6ca488eb6fe870565805ce0fc3e4b75a2d45fe35873/itolapi-4.1.3-py3-none-any.whl")
    version("4.1.2", sha256="5eb44a21ef2db4fdb890a1e2ec6b29b0a5f6b2a253872e5032915ca88823d8c0", url="https://pypi.org/packages/b4/ec/e67083cb4c6ac58763ff8eb0f4128de7cf8d6a9d082c4e686e7b8a0595f6/itolapi-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="1c91da2f9c0b2aa9674be6d13bd5344f3ef352ac1053fef0110dcd9eee45e27d", url="https://pypi.org/packages/f7/63/88cff34ef914ccdc9526c30113ea435acceab141b38669e6e00b3a8f5eb9/itolapi-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="dffa31057c28a403e42168c215a8d8d3e6420e89aa4df02ce01aca1d2a8d1094", url="https://pypi.org/packages/bb/40/ee872c189a4cd6980cc9ba18417244f6c23e521445ed84eb3138a89101b3/itolapi-4.1.0-py3-none-any.whl")
    version("4.0.2", sha256="1d4912a54f86e857345232e270db6e376aa87923b3d050bd3ea346ac7096e7b3", url="https://pypi.org/packages/2c/0d/083fa2a71ed7da20154b423471f2e8aca7b4e08593b2f454f836c0b02ddf/itolapi-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="f4607a8a26047e2a5e6a7c7b2dbf1c5740439c8f15796018f7151467a0c2d173", url="https://pypi.org/packages/3f/c0/0ca08acdb4c69630c8b725efcdb31c71a3ca1a86f6c13d6e7f180e23ae07/itolapi-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="24734eb9e9e263b4ba0979bb7c22ca29cde475628b6fc770a016bb38e0d5cc07", url="https://pypi.org/packages/fb/17/089430b9aeb2beac1aedc6cac9a9493355fb42aad84a0e00a7791bccaee1/itolapi-4.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@2:", when="@1.3.2:3.0.1,3.0.3:")
    # END DEPENDENCIES

