##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNtlmAuth(PythonPackage):
    version("1.5.0", sha256="f1527c581dbf149349134fc2d789d50af2a400e193206956fa0ab456ccc5a8ba", url="https://pypi.org/packages/ff/84/97c550164b54942b0e908c31ef09d9469f3ba4cd7332a671e2125732f63b/ntlm_auth-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="11f7a3cec38155b7cecdd9bbc8c37cd738d8012f0523b3f98d8caefe394feb97", url="https://pypi.org/packages/50/09/5e397eb18685b14fd8b209e26cdb4fa6451c82c1bcc651fef05fa73e7b27/ntlm_auth-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="ce5b4483ed761f341a538a426a71a52e5a9cf5fd834ebef1d2090f9eef14b3f8", url="https://pypi.org/packages/d5/3d/1c54e92f62bbc747a638da94adb439f99dc2d2f3041fe41a06b0da4f2808/ntlm_auth-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="9b13eaf88f16a831637d75236a93d60c0049536715aafbf8190ba58a590b023e", url="https://pypi.org/packages/8e/5b/4047779fb456b0de503c4acb7b166becf2567efb772abb53998440791d3c/ntlm_auth-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="3e5c0d07652e81f14b9627139949fd7052a04178b314b57577db957855d3b989", url="https://pypi.org/packages/69/bc/230987c0dc22c763529330b2e669dbdba374d6a10c1f61232274184731be/ntlm_auth-1.1.0-py2.py3-none-any.whl")
    version("1.0.6", sha256="07e79b7695deaf3fd17abfbe181382cf42afaa61d2eac3a87eee67b6544a5f75", url="https://pypi.org/packages/6d/ac/40df272d335418e6a7d8da1eff962e556ecc98f04de126e3c21bdd7686dc/ntlm_auth-1.0.6-py2.py3-none-any.whl")
    version("1.0.5", sha256="42998e8915ef26a9d4112e4dd7e97382faf1ffb07f2da12490af83a5bb0b1355", url="https://pypi.org/packages/58/72/bb905af4a94e369b68af113e884e07fac073eae5f4af4577a679c7d9a11a/ntlm_auth-1.0.5-py2.py3-none-any.whl")
    version("1.0.4", sha256="fbc8c916c6b0ef66ae631307f1d41a6d2fd8aa380d4b7a659dc0beaf4a440f2d", url="https://pypi.org/packages/47/a8/93ad0f75f2e9e8e55eacea9190595dd548eed4f7ac84c13581572af2c10a/ntlm_auth-1.0.4-py2.py3-none-any.whl")
    version("1.0.3", sha256="314d289bcf4ee6f2bb2fbb5fc9f9a3edd9c191b6e1c5046e32ce8097ba172489", url="https://pypi.org/packages/9b/38/bd3697b538d8a4fc7638335e9b737fc2da4f5b446c594df1687b5a594011/ntlm_auth-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="98e85fe982ed34c109759cccf32a4773a48fb8713d84e6898daeb8d905d17379", url="https://pypi.org/packages/55/b7/639bd6d15f4db06f815566c5521c3b72c23e7de15a8025547fcf42c16449/ntlm_auth-1.0.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ordereddict", when="@1.0.2,1.0.4:1.0.5")
        depends_on("py-six", when="@:1.0")

