##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsOauthlib(PythonPackage):
    version("2.0.0", sha256="7dd8a5c40426b779b0868c404bdef9768deccf22749cde15852df527e6269b36", url="https://pypi.org/packages/3b/5d/63d4ae3b9daea098d5d6f5da83984853c1bbacd5dc826764b249fe119d24/requests_oauthlib-2.0.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="7d3bdc908f5e9b80137fbc445bf8db94295bb006bcbd9520fef55f28f44ed376", url="https://pypi.org/packages/d1/10/7c95d0f74dc6fb10ed1b3b5f07e937d68243c78241d4dba1bcfaa1917dd8/requests_oauthlib-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="7a3130d94a17520169e38db6c8d75f2c974643788465ecc2e4b36d288bf13033", url="https://pypi.org/packages/db/3a/457f30ab4e80b0e978686ccd43f17309e9fdc242d8619491a9156a19fda5/requests_oauthlib-1.4.0-py2.py3-none-any.whl")
    version("1.4.0.dev0", sha256="f06a7994e3156c9438441d11194fc7f09b0d83f09036b40dbe24eb1c7095b695", url="https://pypi.org/packages/00/84/b22310658bbb14755c8d973cb1eb8186c25c39452f3cf54dd53628fd162c/requests_oauthlib-1.4.0.dev0-py2.py3-none-any.whl")
    version("1.3.1", sha256="2577c501a2fb8d05a304c09d090d6e47c306fef15809d102b327cf8364bddab5", url="https://pypi.org/packages/6f/bb/5deac77a9af870143c684ab46a7934038a53eb4aa975bc0687ed6ca2c610/requests_oauthlib-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="b4261601a71fd721a8bd6d7aa1cc1d6a8a93b4a9f5e96626f8e4d91e8beeaa6a", url="https://pypi.org/packages/23/eb/68fc8fa86e0f5789832f275c8289257d8dc44dbe93fce7ff819112b9df8f/requests-oauthlib-1.3.0.tar.gz")
    version("1.2.0", sha256="bd6533330e8748e94bf0b214775fed487d309b8b8fe823dc45641ebcd9a32f57", url="https://pypi.org/packages/de/a2/f55312dfe2f7a344d0d4044fdfae12ac8a24169dc668bd55f72b27090c32/requests-oauthlib-1.2.0.tar.gz")
    version("1.1.0", sha256="eabd8eb700ebed81ba080c6ead96d39d6bdc39996094bd23000204f6965786b0", url="https://pypi.org/packages/62/49/88b3b9019c649f63e722208dc540dbcb144c6f53e24bf438117bec8e64dc/requests-oauthlib-1.1.0.tar.gz")
    version("1.0.0", sha256="e21232e2465808c0e892e0e4dbb8c2faafec16ac6dc067dd546e9b466f3deac8", url="https://pypi.org/packages/94/e7/c250d122992e1561690d9c0f7856dadb79d61fd4bdd0e598087dce607f6c/requests_oauthlib-1.0.0-py2.py3-none-any.whl")
    version("0.8.0", sha256="50a8ae2ce8273e384895972b56193c7409601a66d4975774c60c2aed869639ca", url="https://pypi.org/packages/77/34/d0957563f20b259a31c12f14e858d79f2e66eb539d3c1b9ab7077ef030ca/requests_oauthlib-0.8.0-py2.py3-none-any.whl")
    version("0.7.0", sha256="87e1c05c1b4b4220af0c7ff4e6572ff7fba8032166cb1a12d2e1acd4a5fdaf4f", url="https://pypi.org/packages/ff/2c/efaf0fdea8a6979d0ebee360771418345f1f0906bd478a908256df63ff51/requests_oauthlib-0.7.0-py2.py3-none-any.whl")
    version("0.3.3", sha256="37557b4de3eef50d2a4c65dc9382148b8331f04b1c637c414b3355feb0f007e9", url="https://pypi.org/packages/0f/8a/a7afc508dd7cf6883fb318bdf0c2a0fd65443e396ccd27977c6f146040a3/requests-oauthlib-0.3.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-oauthlib@3:", when="@1.3.1:")
        depends_on("py-oauthlib@0.6.2:", when="@0.6.2:1.0")
        depends_on("py-requests@2:", when="@0.6.2:1.0,1.3.1:")

