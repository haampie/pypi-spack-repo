# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkQuicklookthumbnailing(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="34349ff0b07b39ecfe5757eb80341a45f9d4426558b93946225f8b4fa2781c4c", url="https://pypi.org/packages/b2/e7/ccb104c6068b076113634d0ee16e68f14eb1131f42106bcd8fd19672797d/pyobjc_framework_QuickLookThumbnailing-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="984e4e92727caa5b2ebbe8c91fcde6acc416f15dd8e7aef94cb3999c4a7028ec", url="https://pypi.org/packages/cc/38/871c92148586ce1280aa3f9fb63f350b937e5c69108234d56bf9efa1e911/pyobjc_framework_QuickLookThumbnailing-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="7572750f84477bd9ef4bd6d1fbb88dd3fb3b39567b004307b347b97de861163a", url="https://pypi.org/packages/1d/63/fb7738c016c7d70b5f7958cae8087ba48a902b04d8276b62b0ec550defd4/pyobjc_framework_QuickLookThumbnailing-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="fa1b880999affc68f201735c7d77741fe45aec38d9be78285495db27666801ce", url="https://pypi.org/packages/47/6e/fd04d3beedb637b66ae5802fc0ccaf3b982b1d6978ec151a968ece0c5d79/pyobjc_framework_QuickLookThumbnailing-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="2d6fda21954347c1b16de34ec1bf4e3cada1766358f3e374f557ee7327279557", url="https://pypi.org/packages/79/ca/976ac9ae8ac8d09d06d2bd9c054a0ae34ef51502e4167be4e377cd83b5ab/pyobjc_framework_QuickLookThumbnailing-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="e276c9f963b552ef32552d66c9d0031013787c2965565df6efaf145f18944f59", url="https://pypi.org/packages/4c/66/350391b382c2a7871bdae27e3579058ecd7e39a3fa6768f20fb4d73c74d6/pyobjc_framework_QuickLookThumbnailing-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="1cac31fec11adb108357591856b07602812358f9adbb0e7611644a1e3d7d6ef4", url="https://pypi.org/packages/89/03/2eaab16da3ae813e7597e24aed8945e1998a99afb234e7a758844627d157/pyobjc_framework_QuickLookThumbnailing-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="d1172042459a0396316ddd7b361a02f5a045d4e33f3bc5881b56a1b9fa96a220", url="https://pypi.org/packages/47/52/e924962304c3dea909b0b638130df342781f7289e97cecdb284aeb3b9b21/pyobjc_framework_QuickLookThumbnailing-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="698b728cb3628b2bc84d0e367238d6b3d0c7e9b9f1cb9f7a9ec0e4e7a6853c98", url="https://pypi.org/packages/0b/f8/2862b0cfee5c716641794da723c12c7a8d764f96b407fd6c3be6f0b3f6d7/pyobjc_framework_QuickLookThumbnailing-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="ee7d935c3b7a14639d62de648501cf1660a8a3320af42e1612bba691b23acc3e", url="https://pypi.org/packages/82/52/a524af741b1cf3e80874385c4cde6d4b2887182509f9349b39e243a0f6dd/pyobjc_framework_QuickLookThumbnailing-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
    # END DEPENDENCIES

