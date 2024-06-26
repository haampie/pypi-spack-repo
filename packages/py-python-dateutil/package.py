# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDateutil(PythonPackage):
    # BEGIN VERSIONS
    version("2.8.2", sha256="961d03dc3453ebbc59dbdea9e4e11c5651520a876d0f4db161e8674aae935da9", url="https://pypi.org/packages/36/7a/87837f39d0296e723bb9b62bbb257d0355c7f6128853c78955f57342a56d/python_dateutil-2.8.2-py2.py3-none-any.whl")
    version("2.8.1", sha256="75bb3f31ea686f1197762692a9ee6a7550b59fc6ca3a1f4b5d7e32fb98e2da2a", url="https://pypi.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl")
    version("2.8.0", sha256="7e6584c74aeed623791615e26efd690f29817a27c73085b78e4bad02493df2fb", url="https://pypi.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl")
    version("2.7.5", sha256="063df5763652e21de43de7d9e00ccf239f953a832941e37be541614732cdfc93", url="https://pypi.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl")
    version("2.5.2", sha256="5187ca69bb0a9de482cc5e1d247460b8b62a82fdaf455a13749087094b87754c", url="https://pypi.org/packages/45/f8/88de2335cf6162be0b5c165b3e229267fe3c522ffa9464ffb424359ba682/python_dateutil-2.5.2-py2.py3-none-any.whl")
    version("2.4.2", sha256="2ae63cf475f0bd049b722fac20813d62aedc14957dd5a3bf00d120d2b5404460", url="https://pypi.org/packages/22/75/666cd70de6a70cc7c6560429340ee7ef08196c93f552428983a808423755/python_dateutil-2.4.2-py2.py3-none-any.whl")
    version("2.4.0", sha256="b6f4f95d6ed922c947bf22b15f55ff29e7cf57281975ee01988450182bf6e20c", url="https://pypi.org/packages/a7/65/1d4e38ecca8f0b599748e11cea20ab1e011206d0ef1cce098b16e41e1857/python_dateutil-2.4.0-py2.py3-none-any.whl")
    version("2.2", sha256="eec865307ebe7f329a6a9945c15453265a449cdaaf3710340828a1934d53e468", url="https://pypi.org/packages/75/c5/85d027471fa665f8c8b8eb0b925f9d84b4eee745a257b16de4957de99e81/python-dateutil-2.2.tar.gz")
    version("1.5", sha256="6f197348b46fb8cdf9f3fcfc2a7d5a97da95db3e2e8667cf657216274fe1b009", url="https://pypi.org/packages/b4/7c/df59c89a753eb33c7c44e1dd42de0e9bc2ccdd5a4d576e0bfad97cc280cb/python-dateutil-1.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.5:", when="@2.4:2.4.0,2.6.1:")
    # END DEPENDENCIES

