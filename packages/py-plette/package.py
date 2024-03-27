##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPlette(PythonPackage):
    version("1.0.0", sha256="a853b7a8f9e106c652a44ad356a88ac06c45036cc6ee01c6ba6165cfd752982c", url="https://pypi.org/packages/6b/eb/c7531a7ef30bead6ba686bef94b655e03cf6e42f9a98aaa01763dc89896d/plette-1.0.0-py2.py3-none-any.whl")
    version("0.4.4", sha256="42d68ce8c6b966874b68758d87d7f20fcff2eff0d861903eea1062126be4d98f", url="https://pypi.org/packages/99/8e/b49b6eb9f9e32e90d0012e38626eebe60d80d14af0e88984bb6ed15eef96/plette-0.4.4-py2.py3-none-any.whl")
    version("0.4.3", sha256="3a9a0d40efbbeda623e88bec1b2ad833b4dd99c9e1019179c5894ee9eae8ee15", url="https://pypi.org/packages/c3/a1/a25f128bb9e30c47e4883ddf786680f25d470b946f0ea3f405cdbf3b2068/plette-0.4.3-py2.py3-none-any.whl")
    version("0.4.2", sha256="7bf014ff695d8badf5a058227db0f0bd1fa7ffd6e54ad8b851bc36c20a4a7894", url="https://pypi.org/packages/ac/ea/8685b026dae76491331e9da6cbfe30856cfeaa314d6294e99110e31df364/plette-0.4.2-py2.py3-none-any.whl")
    version("0.4.1", sha256="294bea74c280efdfe2e5f4ea434a8f4ae72265baa19a3b1282240dfa3d97e13c", url="https://pypi.org/packages/f2/a3/2303bf3252901172849771db6b65b386dd776839cf8a2bced02d9917f388/plette-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="cb7cb98c39beb9a1694c6fc8c1f32a503276dd0f18a79c07358e5b856037070d", url="https://pypi.org/packages/b8/97/3253d34110400504508c9d14b5d6741e134067819c377833aedb74902ecb/plette-0.4.0-py2.py3-none-any.whl")
    version("0.3.1", sha256="965d7d1d9c1e8ca1f9ec1223df7bfbf3ce8ac82ec52374e8e8b26886cebd0c09", url="https://pypi.org/packages/72/5a/1cfd17a54a0c99804228c97d406b7e821536a4c0459d9a08e62107cafc95/plette-0.3.1-py2.py3-none-any.whl")
    version("0.3.0", sha256="1736c7b0ca4f6fd7efd0a49d6e446ad85945459544228c534d60fb148e7542f7", url="https://pypi.org/packages/39/79/7f7b3cdd1ab15fd261772bfbda95120dd5ffef221c4dcd7f89fe29f5895f/plette-0.3.0-py2.py3-none-any.whl")
    version("0.2.3", sha256="d6c9b96981b347bddd333910b753b6091a2c1eb2ef85bb373b4a67c9d91dca16", url="https://pypi.org/packages/5b/7d/d1cabc9ff3ab139a4655a1f74fce340c2426c30801481a0fcad35967d03a/plette-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="c0e3553c1e581d8423daccbd825789c6e7f29b7d9e00e5331b12e1642a1a26d3", url="https://pypi.org/packages/b6/b9/2c88b933bd7981496cebdbf5a51fb5b00b5edf3269b63cb67af41c556254/plette-0.2.2-py2.py3-none-any.whl")

    variant("validation", default=False)

    with default_args(type="run"):
        depends_on("py-cerberus", when="+validation")
        depends_on("py-six", when="@:0.2")
        depends_on("py-tomlkit")

