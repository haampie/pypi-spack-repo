##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCloudpathlib(PythonPackage):
    version("0.16.0", sha256="f46267556bf91f03db52b5df7a152548596a15aabca1c8731ef32b0b25a1a6a3", url="https://pypi.org/packages/0f/6e/45b57a7d4573d85d0b0a39d99673dc1f5eea9d92a1a4603b35e968fbf89a/cloudpathlib-0.16.0-py3-none-any.whl")
    version("0.15.1", sha256="fee8a31848ede95f4783ef84fe1e3ce7f85dd21b476fc0898d8b836335e41a99", url="https://pypi.org/packages/97/a2/e9a5bd762cccefc92a98c87354a65a8b75c280ab187a05e6d5851adbdae6/cloudpathlib-0.15.1-py3-none-any.whl")
    version("0.15.0", sha256="1054025c2bcc7409ff56b316d5967df3c4c47797be8aa7a5410998cf5f4d5007", url="https://pypi.org/packages/04/9e/9a18f4c98cbb12d101538e1f30f28462e6acab5bf4ead524f8fd4047830c/cloudpathlib-0.15.0-py3-none-any.whl")
    version("0.14.0", sha256="855e02e804dcbb69391e6453fdfafca1eb031abd898fe62aafb3d3947bad0235", url="https://pypi.org/packages/3a/5f/f006e12bef7a86ad24a303990d1111f5db27bf226517b94b3f07780d7fc0/cloudpathlib-0.14.0-py3-none-any.whl")
    version("0.13.0", sha256="817ae83f1b9630b9d914882f6249626680ccefcb4e45f2d27a195815f1099086", url="https://pypi.org/packages/d0/7c/39bcc86a9dc95ba30709605e8149304e67b85bf8e41994b9b6df194bc421/cloudpathlib-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="5b75a53b4a0ee25d5e740ace8769aa67ab481555f4a9f7590cdfccc7ec791636", url="https://pypi.org/packages/86/d9/ceb0720dfd0c2c8e8580f8f1753392f6592859f5989682010c6ed5b13065/cloudpathlib-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="2f1088cf33548faae3fd442b63da6fb5910ba960fed157dc5b8aca7b5cc72560", url="https://pypi.org/packages/44/b4/998fcd49402a0b5e253a19ee1e4623a073eec8c4324068a975ecde9c6b73/cloudpathlib-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="67d78dcaee1afbfffe3a55adc0a18b29a96e17b61af9de23b6fde47103dd3173", url="https://pypi.org/packages/5c/6c/3f3dbc144aba17eae543f7939cea2d479b662ee09858659d13c8e758b4fa/cloudpathlib-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="e1c735f08da68c02d4889e54a389a2330ffa9388cc5e1ff6fc56b5e4730778bf", url="https://pypi.org/packages/d3/4b/df34f2bf4d66068c74912749a9e2f0092ee560006d35d8ec6bd03c558d9c/cloudpathlib-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="ef94f951cc988e2a6b3e64e99baa10a66efabdfb45efed5561f0674d2b0619b1", url="https://pypi.org/packages/c1/c3/7ee174c9c88b011573bbad9bf7c7fd339a10f751f5bef97e41725d5d604b/cloudpathlib-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="674ac6e88922ff359dcf04ff4b0c0927132df134f004de7252401d5e4d4daf63", url="https://pypi.org/packages/af/4e/798b46f42ebe84a4af8e47e6034a0ab8e8971518cf3922d79ff0298c13f2/cloudpathlib-0.8.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4.0.1:", when="@0.14: ^python@:3.10")

