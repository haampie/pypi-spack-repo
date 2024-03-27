##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDatadetection(PythonPackage):
    version("10.2", sha256="4435ebaa3b3fa3de855690469fefd2d8a3568f702f51540707efaf4363ec94aa", url="https://pypi.org/packages/f9/87/907f9d1161f055fd319624ea2f20e35416faea75ccd49130fab9477fdbc5/pyobjc_framework_DataDetection-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="f23fa282297ed385c9df384a0765e4f9743b8916de8a58137f981ab0425b80f5", url="https://pypi.org/packages/4d/d8/d3ffd15d349632da0b93a36fd91244c15fac32f1bb9f0c736c39e9e69c96/pyobjc_framework_DataDetection-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="6f6420b187475cccf20757577b005bc16b4a606dd8d9d431b59151e571fa6b12", url="https://pypi.org/packages/49/5b/051d2c2bb7e1041faf976a3981a16995953d16f10afee9b5ef54df2c0969/pyobjc_framework_DataDetection-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="9bcf1edbc4af8e430cacfac475c1e6db354f1f40799d51ab040489d8eed7d09f", url="https://pypi.org/packages/6c/01/8b2f6d8b1af2ab94a884c0e9b97d04325ab258886c0b46f676a4467a35b3/pyobjc_framework_DataDetection-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="9fc15ee738e282f613019f031d8ab9d0f34d8327c652aa810b8334d9ccdcb623", url="https://pypi.org/packages/a9/88/55991a8da74701f41af8835e8b673db7a29c03d5714dfdbbdd5e21edb0aa/pyobjc_framework_DataDetection-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="4ff4b0f09dc091f27c2ee180a72aa823f9bc1ad544fe02bc4c6b75758b760d11", url="https://pypi.org/packages/32/8d/700a793f288455c281dcee6764bf910881184b36fdf7cb1cd9fe9471fea1/pyobjc_framework_DataDetection-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="5b0bc15a9ceb9dc9bc24717dc293b3e8c1caf0741beef0a479cb6df10039051e", url="https://pypi.org/packages/18/bb/4a93b42d8574a9e864e0818a607e1704cfe2d772a5992c6ef74c0e589e20/pyobjc_framework_DataDetection-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="8337ad2b403928b200b3cd7810aa160303bdafc06db9bcedca4d95a9fe34ff88", url="https://pypi.org/packages/2b/f0/495c09f4cfb6c362d62e406b8690ebf3a250c290a2f512ecbab68802b0e6/pyobjc_framework_DataDetection-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="741078742758ea84f24ec52395403ab0369be2a946c1dc7ecfc0f7421c95e056", url="https://pypi.org/packages/75/29/54e31537eb3e84970916bde4021a972814b5aa51cddb198cabfdd9903a3c/pyobjc_framework_DataDetection-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="784cb6c68f9870d51c0f6220da811c4e4308c4523eab0ac7d5a9c2ea2c928117", url="https://pypi.org/packages/59/af/2050fc7d83546531c00a80c9803f9b0622058d2ae9e3bb1a11796f0b401c/pyobjc_framework_DataDetection-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

