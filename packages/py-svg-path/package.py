# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySvgPath(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.3", sha256="4bd4747679b527f8db9868e1623bee9f416540b658285d903885768d8a427e5a", url="https://pypi.org/packages/d6/ea/ec6101e1710ac74e88b10312e9b59734885155e47d7dbb1171e4d347a364/svg.path-6.3-py2.py3-none-any.whl")
    version("6.2", sha256="c3b12e6d372771b466078837252eb13b655ea2658437c426cc67fc6262433dc8", url="https://pypi.org/packages/ba/8f/08a177d11ae1becbc76a9da461d238ebbf5646f691bb824c01fae384b890/svg.path-6.2-py2.py3-none-any.whl")
    version("6.1", sha256="03fe9d9df412e8ee3eb6d54c319a6b55d41f1787806eb6fd92c751af76e9a6da", url="https://pypi.org/packages/cc/74/17e89fdaf5f26f91eb5d874add958c265a32963221066c02773dce638bbb/svg.path-6.1-py2.py3-none-any.whl")
    version("6.0", sha256="609e676201befe817433d2df6d0fd94ff4103b45d13bc545e8bd37d37f5d482a", url="https://pypi.org/packages/4c/d0/b1e113a71ecba20201854a6a2ca0dc732574584af626b03c09ee8400fb85/svg.path-6.0-py2.py3-none-any.whl")
    version("5.1", sha256="cbe627ba097ed3c5bc449dd76734ff40c1d8c5a6361608405ade86a782744632", url="https://pypi.org/packages/7c/ca/af329a07764973ca1896208973abf6fcdb597dd6e7921b4c49e07a3daa2e/svg.path-5.1-py2.py3-none-any.whl")
    version("5.0.1", sha256="666a219f36293dfe4e778672fd53e7b072e5768acde33853bb93de85e12f58b7", url="https://pypi.org/packages/ad/4b/de33364264d6c074c4c91f2742e1395f5b97c798913625538b126cae1af4/svg.path-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="d79890a0f61ad7c9a59527460adb8986a31ca1c24c83d0eed2a58ce93f19c0e5", url="https://pypi.org/packages/df/85/99a6c40c5ec85895afcc3da57e5966f19e7681555a95f45ba680f3b01dad/svg.path-5.0.0-py2.py3-none-any.whl")
    version("4.1", sha256="6fcaf541ea6d0b32a67d147add3ccf097cc55bdf227bc47649a786ce4cb4a70f", url="https://pypi.org/packages/d8/ba/d3af96c562e2e3641da0af008e4382f528f13dc82e474a065e1092b015f1/svg.path-4.1-py2.py3-none-any.whl")
    version("4.0.2", sha256="52bd79036e4958c97abd5af8f31938bce35f1e5f3720729f928e0a0c5c661603", url="https://pypi.org/packages/d7/e4/0595a7d576ff26ab780ae8c30080f4e0bfc5c47d4402f02a925da85995e2/svg.path-4.0.2-py2.py3-none-any.whl")
    version("4.0.1", sha256="92a17fa63cec3d0c6967d22d48dee40708631e11644982e7a6fc772c9145fa5a", url="https://pypi.org/packages/4d/28/3f712ce1042ac694dcf26ce9443d9a88ce3aab98b1e688e4a9ca1e4c3d85/svg.path-4.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@3:4.0.1")
    # END DEPENDENCIES

