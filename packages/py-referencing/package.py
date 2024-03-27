##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReferencing(PythonPackage):
    version("0.34.0", sha256="d53ae300ceddd3169f1ffa9caf2cb7b769e92657e4fafb23d34b93679116dfd4", url="https://pypi.org/packages/42/8e/ae1de7b12223986e949bdb886c004de7c304b6fa94de5b87c926c1099656/referencing-0.34.0-py3-none-any.whl")
    version("0.33.0", sha256="39240f2ecc770258f28b642dd47fd74bc8b02484de54e1882b74b35ebd779bd5", url="https://pypi.org/packages/90/10/1c92edb0a0a14b67ff825bc338e74bc49ab27d3f3bae3f9a02838cba546f/referencing-0.33.0-py3-none-any.whl")
    version("0.32.1", sha256="7e4dc12271d8e15612bfe35792f5ea1c40970dadf8624602e33db2758f7ee554", url="https://pypi.org/packages/14/2a/0a9f649354cd2d40f6c4f16eadabd9727377e3b9bc2ccec6cb630d9a6765/referencing-0.32.1-py3-none-any.whl")
    version("0.32.0", sha256="bdcd3efb936f82ff86f993093f6da7435c7de69a3b3a5a06678a6050184bee99", url="https://pypi.org/packages/b4/11/d121780c173336c9bc3a5b8240ed31f518957cc22f6311c76259cb0fcf32/referencing-0.32.0-py3-none-any.whl")
    version("0.31.1", sha256="c19c4d006f1757e3dd75c4f784d38f8698d87b649c54f9ace14e5e8c9667c01d", url="https://pypi.org/packages/ec/d8/e826b3f743d97e45d3ace674a5c6f026069428e608c5fde3d08d072c87f2/referencing-0.31.1-py3-none-any.whl")
    version("0.31.0", sha256="381b11e53dd93babb55696c71cf42aef2d36b8a150c49bf0bc301e36d536c882", url="https://pypi.org/packages/29/c1/69342fbc8efd1aac5cda853cea771763b95d92325c4f8f83b499c07bc698/referencing-0.31.0-py3-none-any.whl")
    version("0.30.2", sha256="449b6669b6121a9e96a7f9e410b245d471e8d48964c67113ce9afe50c8dd7bdf", url="https://pypi.org/packages/be/8e/56d6f1e2d591f4d6cbcba446cac4a1b0dc4f584537e2071d9bcee8eeab6b/referencing-0.30.2-py3-none-any.whl")
    version("0.30.1", sha256="185d4a29f001c6e8ae4dad3861e61282a81cb01b9f0ef70a15450c45c6513a0d", url="https://pypi.org/packages/dd/95/eba31f9bd6d2a16246bce844c5ca7c5ba777f0b854cca05d75a2e4e78e09/referencing-0.30.1-py3-none-any.whl")
    version("0.30.0", sha256="c257b08a399b6c2f5a3510a50d28ab5dbc7bbde049bcaf954d43c446f83ab548", url="https://pypi.org/packages/ea/c3/f75f0ce2cdacca3d68a70b1756635092a1add1002e34afb4895b9fb62598/referencing-0.30.0-py3-none-any.whl")
    version("0.29.3", sha256="7e059500cac23dc5d7d11687291ab60ba1e77ccdf9739b039c1177c06304e98c", url="https://pypi.org/packages/e6/54/f8b868da0d8035cdcae74dbc581c36336ba94d5a1c994d0406d3a8890969/referencing-0.29.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-attrs@22.2:", when="@0.9:")
        depends_on("py-rpds-py@0.7:", when="@0.25:")

