# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalperformanceshaders(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="66e6f671279b1f7edbaed1bea8ab1eb57f617e000c1e871c190b60ad60c1d727", url="https://pypi.org/packages/13/7a/319128121fddaf6dc68f2eed3e146e1ed7dde558186f368bc67631fbc2d6/pyobjc-framework-MetalPerformanceShaders-10.2.tar.gz")
    version("10.1", sha256="335a49c69ac95e412c581592a148a32c0fcf434097e50da378f21fe09be13738", url="https://pypi.org/packages/cf/f3/80bfcb76dbc169608fb529f162d3a71939919a960f379ecaa146dec39bc6/pyobjc-framework-MetalPerformanceShaders-10.1.tar.gz")
    version("10.0", sha256="eeb3d9e5b44db876ebc93dd3d492dbc4a52b6fee96558d13a66fb283b7757ee4", url="https://pypi.org/packages/6e/e7/ee8e20b428ef6ad59a0bac0a49205724882cca78d375cbdd0326c0e11373/pyobjc-framework-MetalPerformanceShaders-10.0.tar.gz")
    version("9.2", sha256="c456a6f392a4d57344a14a78b67f01c0c58c52e66e206c7bf1eb07c5fab8c871", url="https://pypi.org/packages/a4/2d/4821b92111a81a0d4b08ed4a12b9d7b91f2452cb4746ce4b7afdd7913e17/pyobjc-framework-MetalPerformanceShaders-9.2.tar.gz")
    version("9.1.1", sha256="f00b4d7990ec9e4ac7351d310412ef7e4c45be8299c922eb7a4ff58e6a2ba064", url="https://pypi.org/packages/13/61/61dcd16e330f7e3a2f0a22d3d3755974df8502041acebf908418edda0da6/pyobjc-framework-MetalPerformanceShaders-9.1.1.tar.gz")
    version("9.1", sha256="ddc396e99dd981e6c439c26905b725ecfe6da67f59df43a24153ce5aad8fcd2a", url="https://pypi.org/packages/8b/71/a12726a4298f6251d1448de8f3abbc2df8b817d1cd330e7811f9a6ec5f0a/pyobjc-framework-MetalPerformanceShaders-9.1.tar.gz")
    version("9.1-beta1", sha256="5ef43c324cd8efc6b7dc60f504d0982d5fd21d29a7e46a12196a73438d440c5a", url="https://pypi.org/packages/89/e1/1a83506a7b5c2633aa8f1a29644de3f322913bdeacf3e4b7b7a9aed1c3a2/pyobjc-framework-MetalPerformanceShaders-9.1b1.tar.gz")
    version("9.0.1", sha256="ecddfef23bbdd4f9942bdeabbcbc037c7256e49ed4646707672cf977e00f92c1", url="https://pypi.org/packages/f4/a6/0b87d1a51e9129edd5d65d7ed4191c3fd7489751a95af5eb02532cae3d70/pyobjc-framework-MetalPerformanceShaders-9.0.1.tar.gz")
    version("9.0", sha256="f5e46368b6623c80dd3329cba834bac89e83b8124119bd0d8fd670f0931ab12c", url="https://pypi.org/packages/cf/23/869d2466085a35a65cdcf196fd72cc378f69af900aee7b0df2c6f1fbb684/pyobjc-framework-MetalPerformanceShaders-9.0.tar.gz")
    version("8.5.1", sha256="e5316ce6c882fb42905f709b84671587f33bface95524dda00ec4e5610461c6a", url="https://pypi.org/packages/84/0e/6519a4cf2fab96635b2011eadf935ec7e9dd20e8c89e217b757d9a4db191/pyobjc-framework-MetalPerformanceShaders-8.5.1.tar.gz")
    version("8.5", sha256="9219b19709bcc1d85c900ae1ea3f5f8fc0c03be62daf25565ff313839ad41b4e", url="https://pypi.org/packages/64/bd/d821e24389f422ef1b1f0672e43738a0bcca58106250e51b6bb19bba8b14/pyobjc-framework-MetalPerformanceShaders-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-metal@10:", when="@10:10.0")
    # END DEPENDENCIES

