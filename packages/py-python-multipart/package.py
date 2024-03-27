##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonMultipart(PythonPackage):
    version("0.0.9", sha256="97ca7b8ea7b05f977dc3849c3ba99d51689822fab725c3703af7c866a0c2b215", url="https://pypi.org/packages/3d/47/444768600d9e0ebc82f8e347775d24aef8f6348cf00e9fa0e81910814e6d/python_multipart-0.0.9-py3-none-any.whl")
    version("0.0.8", sha256="999725bf08cf7a071073d157a27cc34f8669af98da0d2435bde1cc1493a50ec3", url="https://pypi.org/packages/c0/3e/9fbfd74e7f5b54f653f7ca99d44ceb56e718846920162165061c4c22b71a/python_multipart-0.0.8-py3-none-any.whl")
    version("0.0.7", sha256="b1fef9a53b74c795e2347daac8c54b252d9e0df9c619712691c1cc8021bd3c49", url="https://pypi.org/packages/94/35/142fff3d85da49377ada6936ad9b776263549ab22656969b2fcd0bdb10f7/python_multipart-0.0.7-py3-none-any.whl")
    version("0.0.6", sha256="ee698bab5ef148b0a760751c261902cd096e57e10558e11aca17646b74ee1c18", url="https://pypi.org/packages/b4/ff/b1e11d8bffb5e0e1b6d27f402eeedbeb9be6df2cdbc09356a1ae49806dbf/python_multipart-0.0.6-py3-none-any.whl")
    version("0.0.5", sha256="f7bb5f611fc600d15fa47b3974c8aa16e93724513b49b5f95c81e6624c83fa43", url="https://pypi.org/packages/46/40/a933ac570bf7aad12a298fc53458115cc74053474a72fbb8201d7dc06d3d/python-multipart-0.0.5.tar.gz")
    version("0.0.4", sha256="8fdde85044f0c81df85d174611808ffcec60411883b08be8a154a0f08b418a9e", url="https://pypi.org/packages/76/c7/62bd01eb4dd3102ae40ca2b578f9967745e5016076973ba9d4645ab58728/python-multipart-0.0.4.tar.gz")
    version("0.0.3", sha256="f43d40b9a6b5ea87f9f644c9df7a6837aa88d37ce5e14b1fc3df43facc450147", url="https://pypi.org/packages/0f/19/34da8a84c0384b57dc6c6aeebb250eaa9ea99d81927a73dca0aa933a5c4e/python-multipart-0.0.3.tar.gz")
    version("0.0.2", sha256="ddcc89b2d1b5d77eaa75e3d5e3a3b2b421d945a592ec491f5818edb0a7dff262", url="https://pypi.org/packages/4f/2e/5d4fa0b8899f5a4f001b538326a70789fb2c1a056fb0323854edabe7ee41/python-multipart-0.0.2.tar.gz")
    version("0.0.1", sha256="ae940d053341378e53937d6e7f2081d26b4435dbd53dcd901be73ef3d6ff70be", url="https://pypi.org/packages/c7/bb/c083a3ffcc9f4186ee880935d288b77bef7e27c6f8e94f42d71067870058/python-multipart-0.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.4:", when="@0.0.4")

