# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandasStubs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.1.240316", sha256="0126a26451a37cb893ea62357ca87ba3d181bd999ec8ba2ca5602e20207d6682", url="https://pypi.org/packages/01/4a/21e284b0f5125ee6fbc84d767503f18c87cd1bd70633dd0a13aca8a09a4e/pandas_stubs-2.2.1.240316-py3-none-any.whl")
    version("2.2.0.240218", sha256="e97478320add9b958391b15a56c5f1bf29da656d5b747d28bbe708454b3a1fe6", url="https://pypi.org/packages/7a/0a/9bb9fd7fe2adcb98a2be46483689e6e75258ff90317b7b0b56e8b43aae5f/pandas_stubs-2.2.0.240218-py3-none-any.whl")
    version("2.1.4.231227", sha256="211fc23e6ae87073bdf41dbf362c4a4d85e1e3477cb078dbac3da6c7fdaefba8", url="https://pypi.org/packages/c0/6d/c5c23926fcc7526a5df32a8f3b3540948be8dd4c25f4a097f9091d40535c/pandas_stubs-2.1.4.231227-py3-none-any.whl")
    version("2.1.4.231218", sha256="9c9a8db37b83ff4ff9f672644099abc624ed407aa46d9dcb5f305de9925b3d29", url="https://pypi.org/packages/f9/f8/793e985b559ad697afe4c922644dd559c00ad0e93594ea2affb95c5e6569/pandas_stubs-2.1.4.231218-py3-none-any.whl")
    version("2.1.1.230928", sha256="992d97159e054ca3175ebe8321ac5616cf6502dd8218b03bb0eaf3c4f6939037", url="https://pypi.org/packages/ad/22/ef8d68f5506b4dad7b9597de0d6370c0103a7ec4cd2c258750ddc16597cd/pandas_stubs-2.1.1.230928-py3-none-any.whl")
    version("2.0.3.230814", sha256="4b3dfc027d49779176b7daa031a3405f7b839bcb6e312f4b9f29fea5feec5b4f", url="https://pypi.org/packages/0c/e9/e9550b05e262afc75b014b79224b6910f7cbc85cc40448b709ac90a58ecd/pandas_stubs-2.0.3.230814-py3-none-any.whl")
    version("2.0.2.230605", sha256="39106b602f3cb6dc5f728b84e1b32bde6ecf41ee34ee714c66228009609fbada", url="https://pypi.org/packages/09/1d/2b9b5905d869c3e65d1c35e2a6420cbe4313a277aabfae6001670ef04075/pandas_stubs-2.0.2.230605-py3-none-any.whl")
    version("2.0.1.230501", sha256="7ffc6528290df44881d1d78b7239161ba203e4b6570b71949fc4a4e5eabca8a5", url="https://pypi.org/packages/1c/5a/b39ae497a6fd4fe5b2ee2bca1d3be61972d3e9c8c6b9e23e4ab14c025610/pandas_stubs-2.0.1.230501-py3-none-any.whl")
    version("2.0.0.230412", sha256="311ab8b42ee574d9fea5061d1f63aeca297e472de6073ba84bf2a017c6cb1b6b", url="https://pypi.org/packages/d9/39/bc134cb9728bf843b5ca869affd737504821cb5af5bc61899faa5b7dc2c4/pandas_stubs-2.0.0.230412-py3-none-any.whl")
    version("1.5.3.230321", sha256="4bf36b3071dd55f0e558ac8efe07676a120f2ed89e7a3df0fb78ddf2733bf247", url="https://pypi.org/packages/28/a2/91a899e048732db612686ad43444f4b984af21fdd10f8e8633d4b46ed200/pandas_stubs-1.5.3.230321-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.1:")
        depends_on("python@:3.11", when="@1.5.2:1")
        depends_on("python@:3.10", when="@1.4:1.5.1")
        depends_on("py-numpy@1.26.0:", when="@2.1: ^python@:3.12")
        depends_on("py-numpy@:1.24.3", when="@2.0.3:2.0 ^python@:3.8.0")
        depends_on("py-numpy@1.25.0:", when="@2.0.3:2.0 ^python@3.9:")
        depends_on("py-numpy@1.24.3:", when="@2.0.2")
        depends_on("py-types-pytz@2022.1.1:", when="@1.4.3.220718:")
    # END DEPENDENCIES

