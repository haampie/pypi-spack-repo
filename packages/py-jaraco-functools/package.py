# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoFunctools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.0.0", sha256="daf276ddf234bea897ef14f43c4e1bf9eefeac7b7a82a4dd69228ac20acff68d", url="https://pypi.org/packages/4c/57/726a9c80c1b36f98b497debd72f4c81ae444d55abf9647367e5d53e1cc93/jaraco.functools-4.0.0-py3-none-any.whl")
    version("3.9.0", sha256="df2e2b0aadd2dfcee2d7e0d7d083d5a5b68f4c8621e6915ae9819a90de65dd44", url="https://pypi.org/packages/59/03/ad425c2411f7f14c904cb1235d78749f6e9dfa7b5f157e841710e6fccbc3/jaraco.functools-3.9.0-py3-none-any.whl")
    version("3.8.1", sha256="784718fbc5d70c5a7bd881c362d23d561913102eb1381cec21327c8ebda3351c", url="https://pypi.org/packages/d0/e8/330459e6e321e46f50a3fdf5cfc02e358b5149be51985ce279aada1e764c/jaraco.functools-3.8.1-py3-none-any.whl")
    version("3.8.0", sha256="49f070d49b6cd131aa203e65d86fb4924bbec76fa70ab66fce06442193e2f826", url="https://pypi.org/packages/b3/dc/c365684d34633ae3cd1a6672b6d35baa3d233376f5480cf29bd7f305284e/jaraco.functools-3.8.0-py3-none-any.whl")
    version("3.7.0", sha256="bf41c7163dad130036567f32f5ac8291d5be7583c25ed91f37e5b15c7dacee41", url="https://pypi.org/packages/ed/87/b33eb4897ae94dad6e4b900408b370352d171167862719717104f8ab6193/jaraco.functools-3.7.0-py3-none-any.whl")
    version("3.6.0", sha256="f43fdb95a9b96e85eb2a5126481cb7c96cf342dc9ff4d4d45d322186d33720b8", url="https://pypi.org/packages/ae/3f/40ab9df938e670e71a03cc80c383015cbb79db21fea4dd5f48713d965b14/jaraco.functools-3.6.0-py3-none-any.whl")
    version("3.5.2", sha256="163d6369dd2fc6590712677cbf83b06ee0e4a1a0c720f4b377eae04175ce458e", url="https://pypi.org/packages/7b/7f/7d9df66685dc9ae452ee4e6cd521b2624e9341a169595f3ad07b106ab6c2/jaraco.functools-3.5.2-py3-none-any.whl")
    version("3.5.1", sha256="c8774f73323de42250a659934215da1d899b02c66a6133f1cb79f02a5aff4f38", url="https://pypi.org/packages/15/62/188af1d0a07f4161cbda3847d5504753451d8a1e0af1b9fa710cb6d766ae/jaraco.functools-3.5.1-py3-none-any.whl")
    version("3.5.0", sha256="141f95c490a18eb8aab86caf7a2728f02f604988a26dc36652e3d9fa9e4c49fa", url="https://pypi.org/packages/fb/36/5b86ff4d8013596bd5276f7c1bcf500dc5993a2a9d07d5d3307f5f44e29f/jaraco.functools-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="0e02358b3d86fab7963b0afa2181211dfa478ced708b057dba9b277bde9142bb", url="https://pypi.org/packages/bc/19/644fb6d99e1a649bc1e427c3028585e659dfef9fe25b2d1b59f959d03164/jaraco.functools-3.4.0-py3-none-any.whl")
    version("2.0", sha256="e9e377644cee5f6f9128b4dab1631fca74981236e95a255f80e4292bcd2b5284", url="https://pypi.org/packages/12/a4/3e7366d0f5e75dcad7be88524c8cbd0f3a9fb1db243269550981740c57fe/jaraco.functools-2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-more-itertools", when="@1.13:")
        depends_on("py-typing-extensions", when="@3.9:3 ^python@:3.10")
    # END DEPENDENCIES

