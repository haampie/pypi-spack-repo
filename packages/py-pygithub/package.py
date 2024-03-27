##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygithub(PythonPackage):
    version("2.2.0", sha256="41042ea53e4c372219db708c38d2ca1fd4fadab75475bac27d89d339596cfad1", url="https://pypi.org/packages/37/56/6e038f8cd6b76984005cd5cf90926caa6898b4220984a32dbbdc044a3f18/PyGithub-2.2.0-py3-none-any.whl")
    version("2.1.1", sha256="4b528d5d6f35e991ea5fd3f942f58748f24938805cb7fcf24486546637917337", url="https://pypi.org/packages/be/04/810d131be173cba445d3658a45512b2b2b3d0960d52c4a300d6ec5e00f52/PyGithub-2.1.1-py3-none-any.whl")
    version("2.1.0.post0", sha256="ff71016073f124ecb3fc2a756f0365180f88f40ff1c753107b0e115e94bd0493", url="https://pypi.org/packages/d1/fe/fef8795433b3d0752b3fb764a833574b49aa49fce0ed1cd3e10150c5ac25/PyGithub-2.1.0.post0-py3-none-any.whl")
    version("1.59.1", sha256="3d87a822e6c868142f0c2c4bf16cce4696b5a7a4d142a7bd160e1bdf75bc54a9", url="https://pypi.org/packages/2c/71/aff5465d9e3d448a5d4beab1dc7c8dec72037e3ae7e0d856ee08538dc934/PyGithub-1.59.1-py3-none-any.whl")
    version("1.59.0", sha256="126bdbae72087d8d038b113aab6b059b4553cb59348e3024bb1a1cae406ace9e", url="https://pypi.org/packages/81/99/df45c40bf862817354b06bb25b45cd01b98a6e2849969926943ecf8ffb20/PyGithub-1.59.0-py3-none-any.whl")
    version("1.58.2", sha256="f435884af617c6debaa76cbc355372d1027445a56fbc39972a3b9ed4968badc8", url="https://pypi.org/packages/2b/64/a39f7b0d0860490b43707f01f84cecce661039968d9cfc082414a29e5b1d/PyGithub-1.58.2-py3-none-any.whl")
    version("1.58.1", sha256="4e7fe9c3ec30d5fde5b4fbb97f18821c9dbf372bf6df337fe66f6689a65e0a83", url="https://pypi.org/packages/af/09/5f5a51e8e7a3245cc1af0c5c71b4f6bbcd3c96c5317e4c4e864c728aa1e5/PyGithub-1.58.1-py3-none-any.whl")
    version("1.58.0", sha256="b7bac601492a2b6c876ef326e4ffa3c1923e32707e415da76bfb8307ee8ffb7e", url="https://pypi.org/packages/d0/de/2c9ab7a1ae4684b7e8dc79794100380ef1509519ead6e06ab3534fe09ace/PyGithub-1.58.0-py3-none-any.whl")
    version("1.57", sha256="5822febeac2391f1306c55a99af2bc8f86c8bf82ded000030cd02c18f31b731f", url="https://pypi.org/packages/5a/9e/71e48e5557e3d1bf9c904f3f8bddea29d253d3565c85229cbd2004dcd143/PyGithub-1.57-py3-none-any.whl")
    version("1.56", sha256="d15f13d82165306da8a68aefc0f848a6f6432d5febbff13b60a94758ce3ef8b5", url="https://pypi.org/packages/86/b4/31d769a7f078324670d0a101da7dc210ea335b9bf266382fb446455810c4/PyGithub-1.56-py3-none-any.whl")
    version("1.55", sha256="2caf0054ea079b71e539741ae56c5a95e073b81fa472ce222e81667381b9601b", url="https://pypi.org/packages/c1/1f/9dc4ba315eeea222473cf4c15d3e665f32d52f859d9d6e73219d0a408969/PyGithub-1.55-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-deprecated", when="@1.46:")
        depends_on("py-pyjwt@2.4:+crypto", when="@1.58.1:")
        depends_on("py-pyjwt@2.4:", when="@1.57:1.58.0")
        depends_on("py-pyjwt@2.0.0:", when="@1.55:1.56")
        depends_on("py-pynacl@1.4:", when="@1.55:")
        depends_on("py-python-dateutil", when="@2:2.1")
        depends_on("py-requests@2.14:", when="@1.46:1.53,1.54.1:")
        depends_on("py-typing-extensions@4:", when="@2.1:")
        depends_on("py-urllib3@1.26:", when="@2.1.1:")
        depends_on("py-urllib3", when="@2.1:2.1.0")

