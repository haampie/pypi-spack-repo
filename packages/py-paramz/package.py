##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParamz(PythonPackage):
    version("0.9.6", sha256="4916be6f77f457316bcac8460be9c226026aed81fe7be302b32c0ba74e2ac6dd", url="https://pypi.org/packages/67/5b/f9b09d1e5b67ee147492f7117ee5519cc70bbcd595e313b2d6b31dba33ef/paramz-0.9.6-py3-none-any.whl")
    version("0.9.5", sha256="0917211c0f083f344e7f1bc997e0d713dbc147b6380bc19f606119394f820b9a", url="https://pypi.org/packages/d8/37/4abbeb78d30f20d3402887f46e6e9f3ef32034a9dea65d243654c82c8553/paramz-0.9.5.tar.gz")
    version("0.9.4", sha256="179ca77a965e6e724217257793e3c8c022285ea2190a85e0826ac98dea316219", url="https://pypi.org/packages/fd/78/b0f0164a32518bfd3b98cb2e149b7a4d5504d13fb503b31a6c59b958ed18/paramz-0.9.4.tar.gz")
    version("0.9.2", sha256="7b38c2487602c423ac402214c3b3fa6bbe22b294e2f9e5f9f3842182e1541599", url="https://pypi.org/packages/c9/be/1384468e43daf7b89ed123792861ecbca04aecc0c892f2a0732ca0bc2b91/paramz-0.9.2.tar.gz")
    version("0.9.1", sha256="8a5a2fe5cdb033eb869c49e81fde2a9d0055fadb53a8af1665a7f48f320179cf", url="https://pypi.org/packages/a9/13/097b3223aff557d000b418d6ba3bdc0ca6c3ed672aefbb0e62420ca8d5ac/paramz-0.9.1.tar.gz")
    version("0.9.0", sha256="8523f8ebebc093434d59dcb83ffd44f53177cd19e2309be4cde5f65f4c4684c8", url="https://pypi.org/packages/e4/3e/374a4427f43a34b9dd17cfd79d6c2ef170d051fa08ed2318024e113d4826/paramz-0.9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-decorator@4.0.10:", when="@0.9.6:")
        depends_on("py-numpy@1.7:", when="@:0.0.11,0.9.6:")
        depends_on("py-scipy", when="@:0.0.11,0.9.6:")
        depends_on("py-six", when="@:0.0.11,0.9.6:")

