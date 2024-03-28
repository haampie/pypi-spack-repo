# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameServer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.17.2", sha256="d27214d4395d3f778a527017db094449bdeb88586efccd60a6c9280e8c0ea25c", url="https://pypi.org/packages/fa/d2/46603ca2b9e992b90eb178d79503fb88bcdf9b1da39020a6950ae9dcc93a/trame_server-2.17.2-py3-none-any.whl")
    version("2.17.1", sha256="b87d06d005ccf8dba53b0565c217e856953dfe4de02aceea8b9a31c5ed0dad61", url="https://pypi.org/packages/7f/7f/ebd2d749dce8db1f660b68935c83f5d42f1b076032753219b42ea078aae0/trame_server-2.17.1-py3-none-any.whl")
    version("2.17.0", sha256="7d821828e8c4d8b52309d8c80d59373e0b664d0ceb41e7f27347c8dd5e4f44a3", url="https://pypi.org/packages/51/b7/0c365207bc05843879b99862f89f3f21b53888b249c7c795850d1aaa758c/trame_server-2.17.0-py3-none-any.whl")
    version("2.16.1", sha256="e8085492b57cff2a4823573d63c108f2fa03dd2d3f8b1a08711e32995e86f038", url="https://pypi.org/packages/c2/3d/e48e0da19eeb1b034ad7ecba56678c178c3660d1c7d95f5cd15a657e90e0/trame_server-2.16.1-py3-none-any.whl")
    version("2.16.0", sha256="51e4a38a8ba6be0c6bea9d08bf97bdd67a0b4bdada2557bdbd6d0a7b05c42e4d", url="https://pypi.org/packages/6b/a9/79150f358577836276e25e257e817f258a818303e3faad55e9d538162761/trame_server-2.16.0-py3-none-any.whl")
    version("2.15.0", sha256="77303a609ac64ea941ea0e522a6aee8683fbd306185ae25038edd863f1131d10", url="https://pypi.org/packages/be/88/4a845fc9098dab2cb450b04aeb3dd7b114eb13e82dd5183fa3df55c09e96/trame_server-2.15.0-py3-none-any.whl")
    version("2.14.0", sha256="1966d8e721b6f1e2d8ce7968cc0aa0ebf5a4382781dabaf34781df83fcd2aed7", url="https://pypi.org/packages/ba/a0/30970e0e694c97400a69fd724532d50c5849494049aa3c0f77b7f6a2086e/trame_server-2.14.0-py3-none-any.whl")
    version("2.13.1", sha256="88724d4c9f9246bfca6b2f90460b61736338525d485b9f42c6fa59ea52c07341", url="https://pypi.org/packages/e6/4b/54dcc1dad2a8ba7b5e79060696947c9863dd60176dd559687b11a009d285/trame_server-2.13.1-py3-none-any.whl")
    version("2.13.0", sha256="81f43c221cdbd41347d1910bbe5584fe58786df9ba7a84f7d78d2e3e6d111abd", url="https://pypi.org/packages/73/b0/1521c04ded3a35f798f9745b917e883693c063fa9a061d70c732479ceb89/trame_server-2.13.0-py3-none-any.whl")
    version("2.12.1", sha256="3ed69f2769f26c3e51419d5e6b84ca61320868e17307cace34044111bf71b71d", url="https://pypi.org/packages/7e/6c/dc1f70308f8b1da38a751c93e5f47b150c5278ad4711bae3a38a57cc86e0/trame_server-2.12.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-more-itertools", when="@2.13:")
        depends_on("py-wslink@1.12.2:", when="@2.12:")
    # END DEPENDENCIES

