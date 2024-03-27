##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrpcioStatus(PythonPackage):
    version("1.62.1", sha256="af0c3ab85da31669f21749e8d53d669c061ebc6ce5637be49a46edcb7aa8ab17", url="https://pypi.org/packages/09/49/52e46bcea1c7b07b87982e4f7ea8657c8679f1591c4eafc75f84549939ae/grpcio_status-1.62.1-py3-none-any.whl")
    version("1.62.0", sha256="3baac03fcd737310e67758c4082a188107f771d32855bce203331cd4c9aa687a", url="https://pypi.org/packages/76/23/92157c891ebbed83f7df7f5f0a012a035b14a0f00aa94493f7f4f734081f/grpcio_status-1.62.0-py3-none-any.whl")
    version("1.60.1", sha256="3034fdb239185b6e0f3169d08c268c4507481e4b8a434c21311a03d9eb5889a0", url="https://pypi.org/packages/eb/97/e7dfe2d5566bca05f52af5d4f4a67ccb90878586d3cadbdf8de5a5d4be00/grpcio_status-1.60.1-py3-none-any.whl")
    version("1.60.0", sha256="7d383fa36e59c1e61d380d91350badd4d12ac56e4de2c2b831b050362c3c572e", url="https://pypi.org/packages/d9/bd/f46d6511088f314cfedc880721fd32d387b8513b22da01cf4771d7439a2b/grpcio_status-1.60.0-py3-none-any.whl")
    version("1.59.3", sha256="2fd2eb39ca4e9afb3c874c0878ff75b258db0b7dcc25570fc521f16ae0ab942a", url="https://pypi.org/packages/0f/31/9f87b4d6a5a03c92bab47d54bf516b7196667441e86550280178714bdb28/grpcio_status-1.59.3-py3-none-any.whl")
    version("1.59.2", sha256="24bdf3b3b83b9112f43bd0626f82510d12cc1d919a45028ac20eb6919218e508", url="https://pypi.org/packages/ea/4b/d31e321be28de4ea7d2dc00e0ec4b5c47696207bed4ced1b82b5146aa76c/grpcio_status-1.59.2-py3-none-any.whl")
    version("1.59.0", sha256="cb5a222b14a80ee050bff9676623822e953bff0c50d2d29180de723652fdf10d", url="https://pypi.org/packages/55/ce/e6d0382610240439ced22fe2183bcc387946bf80e5e0f17f5b5250978ff3/grpcio_status-1.59.0-py3-none-any.whl")
    version("1.58.0", sha256="36d46072b71a00147709ebce49344ac59b4b8960942acf0f813a8a7d6c1c28e0", url="https://pypi.org/packages/f6/48/2bcf11bc2df159564eac099ea38d80663d291a56fa2f2f561d08bf083dfa/grpcio_status-1.58.0-py3-none-any.whl")
    version("1.57.0", sha256="15d6af055914ebbc4ed17e55ebfb8e6bb17a45a57fea32e6af19978fb7844690", url="https://pypi.org/packages/d0/3f/347d93056572fdbd64d4f0fc58a18d420763a7118f8b177437d9dab0ae6f/grpcio_status-1.57.0-py3-none-any.whl")
    version("1.56.2", sha256="63f3842867735f59f5d70e723abffd2e8501a6bcd915612a1119e52f10614782", url="https://pypi.org/packages/ef/16/3018689d96918e9c4c7407adf96b721df4d6748ba65db82c5eaa63564335/grpcio_status-1.56.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-googleapis-common-protos@1.5.5:", when="@1.40:")
        depends_on("py-grpcio@1.62.1:", when="@1.62.1:")
        depends_on("py-grpcio@1.62.0:", when="@1.62.0")
        depends_on("py-grpcio@1.60.1:", when="@1.60.1:1.60")
        depends_on("py-grpcio@1.60.0:", when="@1.60.0")
        depends_on("py-grpcio@1.59.3:", when="@1.59.3:1.59")
        depends_on("py-grpcio@1.59.2:", when="@1.59.2")
        depends_on("py-grpcio@1.59.0:", when="@1.59.0")
        depends_on("py-grpcio@1.58.0:", when="@1.58.0:1.58")
        depends_on("py-grpcio@1.57.0:", when="@1.57.0:1.57")
        depends_on("py-grpcio@1.56.2:", when="@1.56.2:1.56")
        depends_on("py-protobuf@4.21.6:", when="@1.50:")

