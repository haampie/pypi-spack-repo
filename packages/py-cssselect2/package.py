# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCssselect2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="fd23a65bfd444595913f02fc71f6b286c29261e354c41d722ca7a261a49b5969", url="https://pypi.org/packages/9d/3a/e39436efe51894243ff145a37c4f9a030839b97779ebcc4f13b3ba21c54e/cssselect2-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="3a83b2a68370c69c9cd3fcb88bbfaebe9d22edeef2c22d1ff3e1ed9c7fa45ed8", url="https://pypi.org/packages/e4/40/98fcfdf1a190aa0aeddf2fd0a432a4997c2c1f826f3f7b00fe42fc72c8ce/cssselect2-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="8d4690bce5f25013262997e64cef3e7bade877d3ef126f9cc624e5b1f294d934", url="https://pypi.org/packages/fb/92/db5aecff7a7b1ab2496d2766e08d384041c42f2ab1c5daeb6b71d03b5412/cssselect2-0.5.0-py3-none-any.whl")
    version("0.4.1", sha256="2f4a9f20965367bae459e3bb42561f7927e0cfe5b7ea1692757cf67ef5d7dace", url="https://pypi.org/packages/99/da/c86ec74495c69518720652f8aa8ab642d8af61a2098eede9db8b03d3c8b4/cssselect2-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="492ff21d3ff1b9d4d1a67911997fd6159a04715c55cf4ceffec957b37c961fcb", url="https://pypi.org/packages/c9/96/0d7a8f5737e7da2e54f5dd5c348c299661b0438eeb28bec4e0ce3ff82b03/cssselect2-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="97d7d4234f846f9996d838964d38e13b45541c18143bc55cf00e4bc1281ace76", url="https://pypi.org/packages/72/bb/9ad85eacc5f273b08bd5203a1d587479a93f27df9056e4e5f63276f4fd0e/cssselect2-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="07e9c3b1b52d81dd08b177532bbd6b9ced650d87abfd641f4e4ec7de34b98807", url="https://pypi.org/packages/c4/a1/1a37602bbcfa2f7c079758f31555776a00a947e43457a3e0110b2165c7d9/cssselect2-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="267eebc7378ade2e8be710cd0179606ad9c95ecc673138fccfcfba42c5ce153d", url="https://pypi.org/packages/12/e2/91fcd4cd32545beec6e11628d64d3e20f11b5a95dd1ccf3216fd69f176b7/cssselect2-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="363205c152674687c326c94ed9672a2aadf2c94ffce926106e844ebd633f1dcb", url="https://pypi.org/packages/35/32/f203cd884d7da7dc3f9edfaef4778808a66245f3deb9ffea34f712f6e50d/cssselect2-0.2.0-py2.py3-none-any.whl")
    version("0.1", sha256="c300158d2b8560cba59320f715a236a8675d0655fc24193c487f423a29db7b56", url="https://pypi.org/packages/41/f8/eb7134d8c44eab19eb2e8ed033c6f5e6f850a9181749c3be867cc61e117f/cssselect2-0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-tinycss2", when="@0.2.2:0.2,0.4:")
        depends_on("py-webencodings", when="@0.4:")
    # END DEPENDENCIES

