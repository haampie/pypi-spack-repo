##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoContext(PythonPackage):
    version("4.3.0", sha256="5d9e95ca0faa78943ed66f6bc658dd637430f16125d86988e77844c741ff2f11", url="https://pypi.org/packages/0a/de/3f889cd55e69f0a91b396f6799ca31ea0d6869cde338e7c79335699090cb/jaraco.context-4.3.0-py3-none-any.whl")
    version("4.2.1", sha256="f617df446d8817c9f53ce37bdcbb16e13f02253027318339de02a1b48ca252e0", url="https://pypi.org/packages/97/fb/3a1c2648ac60aa336f4f197d94b501295883c2d145d9aa87d717fbbfdda7/jaraco.context-4.2.1-py3-none-any.whl")
    version("4.2.0", sha256="c99a215fab101ad56fbe42c8c7955f2c7310cab9ae917c9765f3f0a81b3f8d54", url="https://pypi.org/packages/20/fa/feddd9f93720fb73f6660fd6c248a40ecf092fff0b4bcba87968de948d73/jaraco.context-4.2.0-py3-none-any.whl")
    version("4.1.2", sha256="9327d3e6901923e5a7097aa2df4b9c2bc13f845c7672692e3827ebd1b3d67606", url="https://pypi.org/packages/57/6e/d87cbedeb34c707b0df6607c5565f01998dca79ef2e0ec8690d94aa2cb96/jaraco.context-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="17b909da2fb37ad237ca7ff9523977f8665a47a25b90aec6a99a3e0959c86141", url="https://pypi.org/packages/c7/bb/754558c2182e0545856a9a9c12a05645abfac64db42e042cfbf60d4c94b7/jaraco.context-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="84bae1c5835f1545f1d767e66fc92ad3e9be3b48dd6e9a81d06670cf67fb6649", url="https://pypi.org/packages/c1/a1/fa502fa1f61f262f9f8764b7168e4bc8fe760a307321afe5ea761a380cec/jaraco.context-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="1dd2a6c13a1be2ea9bd28b448ca3dfff6a20297d511ff13c495a001002fcf436", url="https://pypi.org/packages/73/25/03d48691bd2f99637856ce5378dac64acb0d1061be136186530f70afcfac/jaraco.context-4.0.0-py3-none-any.whl")
    version("3.0.0", sha256="ef94d41bb97ac4f1f93b355b072bd6e50bc3433eedc4dbb245df623cb99fd6a0", url="https://pypi.org/packages/f8/c2/e9f82881144b1b9a6cb57745f255ada774333dbc25a022df06c066237646/jaraco.context-3.0.0-py2.py3-none-any.whl")
    version("2.0", sha256="5145c41e8173d4629b10548b8d1dab148de99611f3d8a180db887ed1a2e59a4a", url="https://pypi.org/packages/0a/c3/5b2c39e9f40be3a010d7c329135ec0c9a8e4511b362b184cf2eb6fb46060/jaraco.context-2.0-py2.py3-none-any.whl")
    version("1.8", sha256="6b582ca7be93fdba3b48d5322ad1818c8105ddf61a1470cf10e8c9b1c865d0b3", url="https://pypi.org/packages/10/5b/d06167cad1cf66008c10f5e5d8d26f61e4603424d52c343d8e826084e517/jaraco.context-1.8-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jaraco-apt", when="@1.6.1:3")
        depends_on("py-yg-lockfile", when="@1.6.1:3")

