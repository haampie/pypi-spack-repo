##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCssselect2(PythonPackage):
    version("0.7.0", sha256="fd23a65bfd444595913f02fc71f6b286c29261e354c41d722ca7a261a49b5969", url="https://pypi.org/packages/9d/3a/e39436efe51894243ff145a37c4f9a030839b97779ebcc4f13b3ba21c54e/cssselect2-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="3a83b2a68370c69c9cd3fcb88bbfaebe9d22edeef2c22d1ff3e1ed9c7fa45ed8", url="https://pypi.org/packages/e4/40/98fcfdf1a190aa0aeddf2fd0a432a4997c2c1f826f3f7b00fe42fc72c8ce/cssselect2-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="8d4690bce5f25013262997e64cef3e7bade877d3ef126f9cc624e5b1f294d934", url="https://pypi.org/packages/fb/92/db5aecff7a7b1ab2496d2766e08d384041c42f2ab1c5daeb6b71d03b5412/cssselect2-0.5.0-py3-none-any.whl")
    version("0.4.1", sha256="2f4a9f20965367bae459e3bb42561f7927e0cfe5b7ea1692757cf67ef5d7dace", url="https://pypi.org/packages/99/da/c86ec74495c69518720652f8aa8ab642d8af61a2098eede9db8b03d3c8b4/cssselect2-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="492ff21d3ff1b9d4d1a67911997fd6159a04715c55cf4ceffec957b37c961fcb", url="https://pypi.org/packages/c9/96/0d7a8f5737e7da2e54f5dd5c348c299661b0438eeb28bec4e0ce3ff82b03/cssselect2-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="97d7d4234f846f9996d838964d38e13b45541c18143bc55cf00e4bc1281ace76", url="https://pypi.org/packages/72/bb/9ad85eacc5f273b08bd5203a1d587479a93f27df9056e4e5f63276f4fd0e/cssselect2-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="07e9c3b1b52d81dd08b177532bbd6b9ced650d87abfd641f4e4ec7de34b98807", url="https://pypi.org/packages/c4/a1/1a37602bbcfa2f7c079758f31555776a00a947e43457a3e0110b2165c7d9/cssselect2-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="505d2ce3d3a1d390ddb52f7d0864b7efeb115a5b852a91861b498b92424503ab", url="https://pypi.org/packages/ed/f0/4fa1aa613bd8da257578146e14fe76379108ee52d8949bbefd039af89d12/cssselect2-0.2.1.tar.gz")
    version("0.2.0", sha256="d539662218df5db06feaa6688db88c0737a4f9d6a64554a0dba1e8e0d7488ad2", url="https://pypi.org/packages/60/5a/6b752376629c7c3493835c5e5310098424e026240803bbe17d153b8104ab/cssselect2-0.2.0.tar.gz")
    version("0.1", sha256="c7139f9ae6e2d53028a2efd3de2364d8a569263b676a7b2e111fef876dd49068", url="https://pypi.org/packages/38/9c/f8b89afb854e403645d5346761b442e99a04f87b6af71e8a404912537752/cssselect2-0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-tinycss2", when="@0.2.2:0.2,0.4:")
        depends_on("py-webencodings", when="@0.4:")

