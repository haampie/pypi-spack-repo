##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkInstantmessage(PythonPackage):
    version("10.2", sha256="65db5cb1f163700a6cb915506f8f7ae2f28d8d3f6464f7b122b0535b1694859a", url="https://pypi.org/packages/82/76/5453d27459ee4d2183981603ac4a6f0bd21872eff7a9b45303ee7e448755/pyobjc_framework_InstantMessage-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="c03a9a99faaa14ff0a477114b691d628117422a15995523deb25ff2d1d07a36d", url="https://pypi.org/packages/03/02/b1284ce955c74e731686edc83964251c28a521af2f533c7b3ba9143ced8b/pyobjc_framework_InstantMessage-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="c53dd8ddf2b28dd87cdb67c21798b15d432d659abc633fc3c0a27433bc7a241a", url="https://pypi.org/packages/ea/32/979ff5a181c0167f9901957a25140d86392b233443185f5b3d516cad403e/pyobjc_framework_InstantMessage-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="91abbec9ea55ff1af6a4cf69073b73fc6fb074777fd3aa5a08f5482e70a0e3ca", url="https://pypi.org/packages/9b/4c/b8c4cd22c50b958b08c7f32f6c73efc175a063bdb7d839d641261493e521/pyobjc_framework_InstantMessage-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="a9283431715d04e7890ae70f88b957eb3087c9766e5b529ae9e6fe37823840db", url="https://pypi.org/packages/5f/3d/77e239a699ca74b49d31de71fd907dcd67f49015dfa36d84a2a688234ded/pyobjc_framework_InstantMessage-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="031a54d13c4881dff57ad2bd4872e7934095c91d17386e745ba3d74914c86ad4", url="https://pypi.org/packages/54/b2/25d3fda241dc54b7b8a0953378959662d23a2a81edff3e62ca04a51d5a85/pyobjc_framework_InstantMessage-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="c2beda162affa8d08bc0ca6dc4db97aff17b8317db6662b1359028c8a41a1483", url="https://pypi.org/packages/ea/63/dc081738d4e381b9d23e8ee1c49e34efd881f33b8f758c2ecc951914769b/pyobjc_framework_InstantMessage-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b607da937b67e079b9024010cfe122d11395639d9b071c82796b66df93ea42fd", url="https://pypi.org/packages/ef/02/65a6c9338f37a4ee5077fbcd4f8ec6b5a6271bbd639fb640bf04e2e148cd/pyobjc_framework_InstantMessage-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="493401544cef8f371a78c8557009ef3c2ace182b534c5b76c55b4cacf98e3c14", url="https://pypi.org/packages/62/39/800d89c25d81384b805990a45823744487a53f4efd3f2007e567d6876f17/pyobjc_framework_InstantMessage-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="4f4c1f49a63ff223e856a8ac89eb884e10920d202df82674d8e13679300f75d0", url="https://pypi.org/packages/b4/74/2214977771916658baf4fc31b381d377c32a9790700410b8b99447fc7bc1/pyobjc_framework_InstantMessage-8.5-py2.py3-none-any.whl")

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
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-quartz@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-quartz@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-quartz@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-quartz@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-quartz@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-quartz@8.5:", when="@8.5:8.5.0")

