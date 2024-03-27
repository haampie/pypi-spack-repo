##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNipype(PythonPackage):
    version("1.8.6", sha256="e404ba7781d2418c107107436ec509348137651fca56e5b3c9f9cb5235af6bd4", url="https://pypi.org/packages/60/02/d4e8c990e14d7efcb35038a3d1743ff5068d66d92c1fcc298c9654bae55d/nipype-1.8.6-py3-none-any.whl")
    version("1.8.5", sha256="6474fd162c164f318a08b250b62ccefbaf9bb6fa80f173728c7d6fb1e8d3fd8d", url="https://pypi.org/packages/63/15/fb96e68d6becea5725a57bf220afd7d50ec04a2b9284341e9cbd6c05d5ec/nipype-1.8.5-py3-none-any.whl")
    version("1.8.4", sha256="dd1190110eacf89c0ebceba633652660f6b80ee0a1484efeddb574e2ceb6ccd6", url="https://pypi.org/packages/4f/68/1675a648c0540c4c6545d6e0f33c7f7b103537431349e166380faa01daf5/nipype-1.8.4-py3-none-any.whl")
    version("1.8.3", sha256="8258495c234e38a990862039437ce6dc45e61f446c56fde5d6f1c2e7f1b5133a", url="https://pypi.org/packages/8b/3a/18ecd703dcb927ebbbc045cb266de9ebf1e2a709d26b03f27958644a172a/nipype-1.8.3-py3-none-any.whl")
    version("1.8.2", sha256="00106a707083687da5a9687bf4f41a86170b0b05af803bda73f2260073302daa", url="https://pypi.org/packages/06/92/8c6308cdbcdcc7ecb41da3cd8d098be40bdd31903b42a492bb7b81f07fdd/nipype-1.8.2-py3-none-any.whl")
    version("1.8.1", sha256="4b3eff6ef6ffd27f672e53347573a064653745885990aff387e896709c373238", url="https://pypi.org/packages/a4/60/112c5571b22a7cfb6a62d1eb449d1291f68fe932817ddf9074a2c1d7b0ed/nipype-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="75306a171f75c99c9928f21a5d319e74a2d3c975962ec048b5d2e30d47a4db97", url="https://pypi.org/packages/6c/18/35ecae1a26a29adf6aec72ffd9f23f50a145d1965a345571da852ea99b6c/nipype-1.8.0-py3-none-any.whl")
    version("1.7.1", sha256="f5212357fca5dce0d23be941718190a4287ff116b0d1e808b475af74d6b24df5", url="https://pypi.org/packages/55/b1/f460276fb64e0674ba4b240c47992c0c548c47c5b55722a4c4d1b354a465/nipype-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="21e64add7c892e14dd7bc2463523af727b19c8128b73f0fef86ee23cbb47006a", url="https://pypi.org/packages/85/20/d39f66275b333ec78a11455a6ab6bc3ad1eb6b54eea4f7c157354ed539ae/nipype-1.7.0-py3-none-any.whl")
    version("1.6.1", sha256="8d36685ff6ae7773e9e4f3b99fc95c94034d370d64afd83d4eb2caf0de6299f4", url="https://pypi.org/packages/a6/1b/5a47f6c7d3f5ebd64ebd72c454b4ff3deca96218a114f90ee47dc4e37bed/nipype-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="bb471aad456073fb994b51cc74894827e21bd61da2b1dfdba41fad9cd5d8bd77", url="https://pypi.org/packages/1f/0e/348956e47dfa73e359c55f9249d61fdd0526ab24d761a0b94299b1a9f88b/nipype-1.6.0-py3-none-any.whl")
    version("1.4.2", sha256="f3466496093d622436a2666de98562baf6b186b3eda12712f9cfb20c1f126ffd", url="https://pypi.org/packages/73/f2/e094bf653b5ec180f8227901056ff35ffd7edfc23f967b67dd4238d0f4c7/nipype-1.4.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click@6.6:", when="@0.13.0,0.14:")
        depends_on("py-etelemetry@0.2:", when="@1.5.0:")
        depends_on("py-etelemetry", when="@1.2.3:1.5.0-rc1")
        depends_on("py-filelock@3:", when="@1.2.3:")
        depends_on("py-looseversion", when="@1.8.1:")
        depends_on("py-mock", when="@0.13.0,0.14:1.1.7")
        depends_on("py-networkx@2:", when="@1.6:")
        depends_on("py-networkx@1.9:", when="@0.14:1.5")
        depends_on("py-neurdflib", when="@1.1.4:1.5.0-rc1")
        depends_on("py-nibabel@2.1:", when="@0.13.0,0.14:")
        depends_on("py-numpy@1.17.0:", when="@1.8:")
        depends_on("py-numpy@1.15.3:", when="@1.1.6:1.7")
        depends_on("py-packaging", when="@0.14:")
        depends_on("py-prov@1.5.2:", when="@1.1.4:")
        depends_on("py-pydot@1.2.3:", when="@0.14:")
        depends_on("py-pydotplus", when="@0.13.0,0.14:1.5")
        depends_on("py-python-dateutil@2.2:", when="@0.14:")
        depends_on("py-rdflib@5.0.0:", when="@1.5.0:")
        depends_on("py-scipy@0.14:", when="@0.14:")
        depends_on("py-simplejson@3.8:", when="@0.12:0.12.0-rc1,0.13.0,0.14:")
        depends_on("py-traits@4.6:4,5.1:6.3", when="@1.8.4:")
        depends_on("py-traits@4.6:4,5.1:", when="@1.2:1.8.3")
        depends_on("py-xvfbwrapper", when="@0.12:0.12.0-rc1")

