##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDateutil(PythonPackage):
    version("2.9.0.post0", sha256="a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427", url="https://pypi.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl")
    version("2.9.0", sha256="cbf2f1da5e6083ac2fbfd4da39a25f34312230110440f424a14c7558bb85d82e", url="https://pypi.org/packages/13/7f/98d6f9ca8b731506c85785bbb8806c01f5966a4df6d68c0d1cf3b16967e1/python_dateutil-2.9.0-py2.py3-none-any.whl")
    version("2.8.2", sha256="961d03dc3453ebbc59dbdea9e4e11c5651520a876d0f4db161e8674aae935da9", url="https://pypi.org/packages/36/7a/87837f39d0296e723bb9b62bbb257d0355c7f6128853c78955f57342a56d/python_dateutil-2.8.2-py2.py3-none-any.whl")
    version("2.8.1", sha256="75bb3f31ea686f1197762692a9ee6a7550b59fc6ca3a1f4b5d7e32fb98e2da2a", url="https://pypi.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl")
    version("2.8.0", sha256="7e6584c74aeed623791615e26efd690f29817a27c73085b78e4bad02493df2fb", url="https://pypi.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl")
    version("2.7.5", sha256="063df5763652e21de43de7d9e00ccf239f953a832941e37be541614732cdfc93", url="https://pypi.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl")
    version("2.7.4", sha256="f7cde3aecf8a797553d6ec49b65f0fbcffe7ffb971ccac452d181c28fd279936", url="https://pypi.org/packages/2f/e9/b02e8a1a8c53a55a4f37df1e8e111539d0a3e76828bcd252947a5200b797/python_dateutil-2.7.4-py2.py3-none-any.whl")
    version("2.7.3", sha256="1adb80e7a782c12e52ef9a8182bebeb73f1d7e24e374397af06fb4956c8dc5c0", url="https://pypi.org/packages/cf/f5/af2b09c957ace60dcfac112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.whl")
    version("2.7.2", sha256="3220490fb9741e2342e1cf29a503394fdac874bc39568288717ee67047ff29df", url="https://pypi.org/packages/0c/57/19f3a65bcf6d5be570ee8c35a5398496e10a0ddcbc95393b2d17f86aaaf8/python_dateutil-2.7.2-py2.py3-none-any.whl")
    version("2.7.1", sha256="6c0e72580272b561d8594362ab0e6b5b2191c703982150fc06ed45f7fae725be", url="https://pypi.org/packages/95/27/d6be8938e2cd9c956c2c6c0b3253e1c62d6db29a52b477943da3c3ec728c/python_dateutil-2.7.1-py2.py3-none-any.whl")
    version("2.5.2", sha256="063907ef47f6e187b8fe0728952e4effb587a34f2dc356888646f9b71fbb2e4b", url="https://pypi.org/packages/22/b7/923674117d83465c0ccab5d5fa1b66caba59d6fa7428089fd2470a1e29cd/python-dateutil-2.5.2.tar.gz")
    version("2.4.2", sha256="3e95445c1db500a344079a47b171c45ef18f57d188dffdb0e4165c71bea8eb3d", url="https://pypi.org/packages/b6/ff/5eaa688dd8ce78913f47438f9b40071a560126ac3e95f9b9be27dfe546a7/python-dateutil-2.4.2.tar.gz")
    version("2.4.0", sha256="b6f4f95d6ed922c947bf22b15f55ff29e7cf57281975ee01988450182bf6e20c", url="https://pypi.org/packages/a7/65/1d4e38ecca8f0b599748e11cea20ab1e011206d0ef1cce098b16e41e1857/python_dateutil-2.4.0-py2.py3-none-any.whl")
    version("2.2", sha256="eec865307ebe7f329a6a9945c15453265a449cdaaf3710340828a1934d53e468", url="https://pypi.org/packages/75/c5/85d027471fa665f8c8b8eb0b925f9d84b4eee745a257b16de4957de99e81/python-dateutil-2.2.tar.gz")
    version("1.5", sha256="6f197348b46fb8cdf9f3fcfc2a7d5a97da95db3e2e8667cf657216274fe1b009", url="https://pypi.org/packages/b4/7c/df59c89a753eb33c7c44e1dd42de0e9bc2ccdd5a4d576e0bfad97cc280cb/python-dateutil-1.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.5:", when="@2.4:2.4.0,2.6.1:")

