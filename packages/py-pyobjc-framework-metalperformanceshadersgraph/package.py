##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalperformanceshadersgraph(PythonPackage):
    version("10.2", sha256="7fedd831f9fc58708f6b01888abd42a2f08151c86db47280fe47be0f709811bf", url="https://pypi.org/packages/88/75/3cfed273b3aaf92d5cfde429ab4a188964855b333d93deb466ef3c347b72/pyobjc_framework_MetalPerformanceShadersGraph-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="467e84983c5ded8cfaea8cb425872d5069eda8c4cc1f803ca3afaed0e184c763", url="https://pypi.org/packages/fd/97/b7e4b2815218b77c8d6e48da0fa86a730eef3e05467381a93ab9ed4f488d/pyobjc_framework_MetalPerformanceShadersGraph-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="824f9721eb724de171c9e4515931a59daacbc743890eef5fe00aa70ad1927f30", url="https://pypi.org/packages/43/54/0aab283504b33b80ff91844e2234c559dc70a0f40da0e9483bc7f2d1dbf2/pyobjc_framework_MetalPerformanceShadersGraph-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="9bd43aac325c9284dfc524ebe264d801a19c845c7f08a768cdfccb2e492c830e", url="https://pypi.org/packages/41/70/ef413881ff15f3b6af42d4993fb075aed967e4f087d396c27e07c7df805b/pyobjc_framework_MetalPerformanceShadersGraph-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="1acabb99b91475f4757799aefaf36126f101f1a7e098b8a1a9ff1cf48aa8bc0b", url="https://pypi.org/packages/e9/43/8304339ea5978893af9ea9f5868aa3c8a2e2799908b027a71e1ebb087e56/pyobjc_framework_MetalPerformanceShadersGraph-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="00b2b3985fb3e63735fc7c780b4f4b75d31f704aff249c3026b48f33b0f67958", url="https://pypi.org/packages/4d/e0/441c80e5a4a7dcf93a32eb98f94355e9451a7fdf08e362b0bdaf9d901cfd/pyobjc_framework_MetalPerformanceShadersGraph-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="83ed5ed80d4fc94771d709a6b7e6534ab14e394a85488f9f649bd7c662bf3432", url="https://pypi.org/packages/07/32/00315861af6eb686751ab5e29293a04aa274230439971262f166d963efa0/pyobjc_framework_MetalPerformanceShadersGraph-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="bf5510fa3fe8ff48893f1380b88a499e268515dad5bd718f1f83fd336e0ec34c", url="https://pypi.org/packages/0c/05/1cca3c7b62c8b43bbe8b321d8afb04e9bee8c8dae64e0d1cfc4d3895da57/pyobjc_framework_MetalPerformanceShadersGraph-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="d794f5396f2a45a4640ebacb83e0db04a5d2b1c88daa2fd287efb246d49fb018", url="https://pypi.org/packages/d9/c4/35a16e1f80cc40d89c487c87a3e8e1953d00792c75238c629a0fc8f1bcb1/pyobjc_framework_MetalPerformanceShadersGraph-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="c98c2025b8916e6cd726e2776fdd44b5d606e1966f83ea90c08a0d218ff9bd8d", url="https://pypi.org/packages/d4/fc/104da47108d6fa4ed17099fc7b7232a128c9299c8613ad8980b1aade0313/pyobjc_framework_MetalPerformanceShadersGraph-8.5-py2.py3-none-any.whl")

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
        depends_on("py-pyobjc-framework-metalperformanceshaders@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metalperformanceshaders@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-metalperformanceshaders@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-metalperformanceshaders@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-metalperformanceshaders@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-metalperformanceshaders@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-metalperformanceshaders@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-metalperformanceshaders@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-metalperformanceshaders@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-metalperformanceshaders@8.5:", when="@8.5:8.5.0")

