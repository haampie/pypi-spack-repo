# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenpyxl(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.0-beta1", sha256="c9c32c7304ad9de30aa6632dd9836469fce0338e91f3e7875a1395f9163a3eec", url="https://pypi.org/packages/e2/5e/1fe4ea74f5c0afc681cbb1f34836fa251280c5aa3012dc803f6aac1382d6/openpyxl-3.2.0b1-py2.py3-none-any.whl")
    version("3.1.2", sha256="f91456ead12ab3c6c2e9491cf33ba6d08357d802192379bb482f1033ade496f5", url="https://pypi.org/packages/6a/94/a59521de836ef0da54aaf50da6c4da8fb4072fb3053fa71f052fd9399e7a/openpyxl-3.1.2-py2.py3-none-any.whl")
    version("3.1.1", sha256="a0266e033e65f33ee697254b66116a5793c15fc92daf64711080000df4cfe0a8", url="https://pypi.org/packages/9e/57/1d3c2ce7f6f783be9b21569fc468a9f3660e35cc17017abfbbc26d3bd061/openpyxl-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="24d7d361025d186ba91eff58135d50855cf035a84371b891e58fb6eb5125660f", url="https://pypi.org/packages/0d/89/f78a9a895e221ec8b13ae7f9495f340a0fb43563b13e2891b5df134f20ea/openpyxl-3.1.0-py2.py3-none-any.whl")
    version("3.0.10", sha256="0ab6d25d01799f97a9464630abacbb34aafecdcaa0ef3cba6d6b3499867d0355", url="https://pypi.org/packages/7b/60/9afac4fd6feee0ac09339de4101ee452ea643d26e9ce44c7708a0023f503/openpyxl-3.0.10-py2.py3-none-any.whl")
    version("3.0.9", sha256="8f3b11bd896a95468a4ab162fc4fcd260d46157155d1f8bfaabb99d88cfcf79f", url="https://pypi.org/packages/1c/a6/8ce4d2ef2c29be3235c08bb00e0b81e29d38ebc47d82b17af681bf662b74/openpyxl-3.0.9-py2.py3-none-any.whl")
    version("3.0.8", sha256="52150a09b660fe444af7abe2592b156c14e324526b1968a57705525547317a7f", url="https://pypi.org/packages/77/db/eac34eeb903dff79610716b7bc25a819b2f7305bae3cc86e5a7e09956c13/openpyxl-3.0.8-py2.py3-none-any.whl")
    version("3.0.7", sha256="46af4eaf201a89b610fcca177eed957635f88770a5462fb6aae4a2a52b0ff516", url="https://pypi.org/packages/39/08/595298c9b7ced75e7d23be3e7596459980d63bc35112ca765ceccafbe9a4/openpyxl-3.0.7-py2.py3-none-any.whl")
    version("3.0.6", sha256="1a4b3869c2500b5c713e8e28341cdada49ecfcff1b10cd9006945f5bcefc090d", url="https://pypi.org/packages/d4/c5/1a5f82b3020bfb27f21b302f96c8ae6a34475070015d1b1e0b197a97e2af/openpyxl-3.0.6-py2.py3-none-any.whl")
    version("3.0.5", sha256="f7d666b569f729257082cf7ddc56262431878f602dcc2bc3980775c59439cdab", url="https://pypi.org/packages/5c/90/61f83be1c335a9b69fa773784a785d9de95c7561d1661918796fd1cba3d2/openpyxl-3.0.5-py2.py3-none-any.whl")
    version("3.0.4", sha256="6e62f058d19b09b95d20ebfbfb04857ad08d0833190516c1660675f699c6186f", url="https://pypi.org/packages/f9/d8/be9dc2b17ba47f1db9032ed7e19915145b4c093f66bb36f0d919d2dc8ccf/openpyxl-3.0.4-py2.py3-none-any.whl")
    version("3.0.3", sha256="547a9fc6aafcf44abe358b89ed4438d077e9d92e4f182c87e2dc294186dc4b64", url="https://pypi.org/packages/95/8c/83563c60489954e5b80f9e2596b93a68e1ac4e4a730deb1aae632066d704/openpyxl-3.0.3.tar.gz")
    version("2.4.5", sha256="78c331e819fb0a63a1339d452ba0b575d1a31f09fdcce793a31bec7e9ef4ef21", url="https://pypi.org/packages/85/19/0794013228f8e68dbdfdde3fb5f75cd14e729ff55dee77c3500db3db59d8/openpyxl-2.4.5.tar.gz")
    version("2.2.0", sha256="c34e3f7e3106dbe6d792f35d9a2f01c08fdd21a6fe582a2f540e39a70e7443c4", url="https://pypi.org/packages/de/6c/46a2c08780ae44d6e4b7f2cb36fcf2b6d9a0ff30c188870d5b5805194fad/openpyxl-2.2.0.tar.gz")
    version("1.8.6", sha256="87fdfe6ada6a296e696777bdd9b1eba019d38332d5e1efdbeb6ea7e1f02161ac", url="https://pypi.org/packages/eb/38/e52d897f0529c470a335b347c6b4e7feb5992d231e3601f2ea0b33745075/openpyxl-1.8.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-et-xmlfile", when="@2.6.0-beta1,3.0.4:")
        depends_on("py-jdcal", when="@2.6.0-beta1,3.0.4:3.0.6")
    # END DEPENDENCIES

