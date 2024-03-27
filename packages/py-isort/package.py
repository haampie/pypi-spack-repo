##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIsort(PythonPackage):
    version("5.13.2", sha256="8ca5e72a8d85860d5a3fa69b8745237f2939afe12dbf656afbcb47fe72d947a6", url="https://pypi.org/packages/d1/b3/8def84f539e7d2289a02f0524b944b15d7c75dab7628bedf1c4f0992029c/isort-5.13.2-py3-none-any.whl")
    version("5.13.1", sha256="56a51732c25f94ca96f6721be206dd96a95f42950502eb26c1015d333bc6edb7", url="https://pypi.org/packages/22/15/3bd09f1fb8bfa9385ecbccbb9aa1c2cce992f4427b1aa852def9e7d81318/isort-5.13.1-py3-none-any.whl")
    version("5.13.0", sha256="15e0e937819b350bc256a7ae13bb25f4fe4f8871a0bc335b20c3627dba33f458", url="https://pypi.org/packages/ec/1d/4f685e2287dddcebc71624eadfe1fb0b550e39c2a2caa0b90dc47613c6de/isort-5.13.0-py3-none-any.whl")
    version("5.12.0", sha256="f84c2818376e66cf843d497486ea8fed8700b340f308f076c6fb1229dff318b6", url="https://pypi.org/packages/0a/63/4036ae70eea279c63e2304b91ee0ac182f467f24f86394ecfe726092340b/isort-5.12.0-py3-none-any.whl")
    version("5.11.5", sha256="ba1d72fb2595a01c7895a5128f9585a5cc4b6d395f1c8d514989b9a7eb2a8746", url="https://pypi.org/packages/5f/f6/c55db45970fbd14de6ab72082f1b8a143c3a69aa031c1e0dd4b9ecc8d496/isort-5.11.5-py3-none-any.whl")
    version("5.11.4", sha256="c033fd0edb91000a7f09527fe5c75321878f98322a77ddcc81adbd83724afb7b", url="https://pypi.org/packages/91/3b/a63bafb8141b67c397841b36ad46e7469716af2b2d00cb0be2dfb9667130/isort-5.11.4-py3-none-any.whl")
    version("5.11.3", sha256="83155ffa936239d986b0f190347a3f2285f42a9b9e1725c89d865b27dd0627e5", url="https://pypi.org/packages/cd/11/7bf65b28548c7cb626e4a70807cee496361b3c789cce57bd48ce4008d1e4/isort-5.11.3-py3-none-any.whl")
    version("5.11.2", sha256="e486966fba83f25b8045f8dd7455b0a0d1e4de481e1d7ce4669902d9fb85e622", url="https://pypi.org/packages/cc/95/ccd309181d2b05afbe98cf452210f7e3bd73731ec1849db5c210e2df2117/isort-5.11.2-py3-none-any.whl")
    version("5.11.1", sha256="bf02c95f1fe615ebbe13a619cfed1619ddfe8941274c9e3de3143adca406cb02", url="https://pypi.org/packages/5b/55/53df1bfaf98e08224f5880546ddd09fbc7271b316bf401de5d46aabcdcee/isort-5.11.1-py3-none-any.whl")
    version("5.11.0", sha256="1b8631908ecc1b7108801801e510c4bf908962b77bd44882a3873566542f7255", url="https://pypi.org/packages/b0/71/0b9f4c86859eeb661f3a3537f6bfdb8d438060e0433bf84fdf03fce283fa/isort-5.11.0-py3-none-any.whl")
    version("5.10.1", sha256="6f62d78e2f89b4500b080fe3a81690850cd254227f27f75c3a0c491a1f351ba7", url="https://pypi.org/packages/b8/5b/f18e227df38b94b4ee30d2502fd531bebac23946a2497e5595067a561274/isort-5.10.1-py3-none-any.whl")
    version("5.9.3", sha256="e17d6e2b81095c9db0a03a8025a957f334d6ea30b26f9ec70805411e5c7c81f2", url="https://pypi.org/packages/c4/1d/f4e03047d6767e35c1efb13a280c1ef8b88807230f902da4cfc431a9f602/isort-5.9.3-py3-none-any.whl")
    version("5.9.1", sha256="8e2c107091cfec7286bc0f68a547d0ba4c094d460b732075b6fba674f1035c0c", url="https://pypi.org/packages/b3/3f/4e39910865572d2ff209e601d9c1d15180ef1b735538a0c7bc2d15b63ac6/isort-5.9.1-py3-none-any.whl")
    version("4.3.20", sha256="f57abacd059dc3bd666258d1efb0377510a89777fda3e3274e3c01f7c03ae22d", url="https://pypi.org/packages/1c/d9/bf5848b376e441ff358a14b954476423eeeb8c9b78c10074b7f53ce2918d/isort-4.3.20-py2.py3-none-any.whl")
    version("4.2.15", sha256="79f46172d3a4e2e53e7016e663cc7a8b538bec525c36675fcfd2767df30b3983", url="https://pypi.org/packages/4d/d5/7c8657126a43bcd3b0173e880407f48be4ac91b4957b51303eab744824cf/isort-4.2.15.tar.gz")

    with default_args(type="run"):
        depends_on("py-pip-api", when="@5.13:5.13.0")
        depends_on("py-pipreqs", when="@5.13:5.13.0")
        depends_on("py-requirementslib", when="@5.13:5.13.0")

