##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMock(PythonPackage):
    version("4.0.3", sha256="122fcb64ee37cfad5b3f48d7a7d51875d7031aaf3d8be7c42e2bee25044eee62", url="https://pypi.org/packages/5c/03/b7e605db4a57c0f6fba744b11ef3ddf4ddebcada35022927a2b5fc623fdf/mock-4.0.3-py3-none-any.whl")
    version("3.0.5", sha256="d157e52d4e5b938c550f39eb2fd15610db062441a9c2747d3dbfa9298211d0f8", url="https://pypi.org/packages/05/d2/f94e68be6b17f46d2c353564da56e6fb89ef09faeeff3313a046cb810ca9/mock-3.0.5-py2.py3-none-any.whl")
    version("3.0.3", sha256="d659f8ef8810ff4c3f8f973d113a05d291a08ab0f7ed17bd60887983b93a0f9a", url="https://pypi.org/packages/24/15/ced6036cb01628f17cb9b8c43426b9d32ae68143221d99cd3f630bffddae/mock-3.0.3-py2.py3-none-any.whl")
    version("2.0.0", sha256="b158b6df76edd239b8208d481dc46b6afd45a846b7812ff0ce58971cf5bc8bba", url="https://pypi.org/packages/0c/53/014354fc93c591ccc4abff12c473ad565a2eb24dcd82490fae33dbf2539f/mock-2.0.0.tar.gz")
    version("1.3.0", sha256="1e247dbecc6ce057299eb7ee019ad68314bb93152e81d9a6110d35f4d5eca0f6", url="https://pypi.org/packages/98/05/dd44a19f1dd9f274baae2018b843d31fbeff99399114b16ac965b4f99269/mock-1.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@3.0.1:3")

