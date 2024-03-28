# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetrickit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="14cb02fd8fc338f6f15df5fd14c95419871b768cc8f5f71b1e0e99fde46b4712", url="https://pypi.org/packages/0a/b2/a5aa2544a35408094f17bcd471f0a72ac48d58d096fb974afc767e0e781a/pyobjc-framework-MetricKit-10.2.tar.gz")
    version("10.1", sha256="6887cec4b7aa489ec16af2f77f7c447bc0a0493456fe1c4910d95a5b3e587fcd", url="https://pypi.org/packages/9e/9d/6b2790ba5eb9134156d2a59b81b197aeb33ab0bbd245c0db10e9c70d2a0e/pyobjc-framework-MetricKit-10.1.tar.gz")
    version("10.0", sha256="15f4d384f95ab3656ae183d2fa15e1c59e91b6a5566a4edd105684a70c79401b", url="https://pypi.org/packages/cb/88/e064af08d70e499d80f80440dccab4742c60c41959b902b39f92ea09c99e/pyobjc-framework-MetricKit-10.0.tar.gz")
    version("9.2", sha256="a205b1054dc2e8cf6878f03cb379189cfda8ef4aa74e5f644a2dcde7e8a2e1fb", url="https://pypi.org/packages/92/16/f330cecdbdf0f0aec81c75b2efe2056ded8751d3019ab320a48770d4e8bf/pyobjc-framework-MetricKit-9.2.tar.gz")
    version("9.1.1", sha256="6601f61035761fa701d4b398a34b1eb904435bf589ad7b17eed039aa412a5e6e", url="https://pypi.org/packages/da/9e/f4b8ad677b523242d7c85a0bd6616f99cb7cb0b9d535fe714305e7d74bf2/pyobjc-framework-MetricKit-9.1.1.tar.gz")
    version("9.1", sha256="7d7bb467ba713cdb4d154d2fbfa199262d9c125ea12cb7620b6bf0713e1ff0d0", url="https://pypi.org/packages/fe/60/227771d87af1e474de5f635ca3682aa7eed3de3cf57d85c3b4134a6a758a/pyobjc-framework-MetricKit-9.1.tar.gz")
    version("9.0.1", sha256="81260069f8319ecf402968364ebe5af683e568f74cdb6d0005043238473462dc", url="https://pypi.org/packages/79/ab/bbfcb968ca6abb6d530ca318f9950643337f5e29be81da490620689584eb/pyobjc-framework-MetricKit-9.0.1.tar.gz")
    version("9.0", sha256="9be1a04c0c0eec20b17588876cf8809b5db6a9d65cf5bb4e4b4dda21f0ea3d3e", url="https://pypi.org/packages/c9/59/5db0baa8feadcf651b1413e17d5b78c5cbb4f73aab60a2b5f19240a1dbad/pyobjc-framework-MetricKit-9.0.tar.gz")
    version("8.5.1", sha256="dcfba3d90e8682e06798b01dded17add8a336b4914e5c70aabf86bc46c2159d8", url="https://pypi.org/packages/38/c5/39f781b9a3f1313be5044ab69713d0224a73bfd2648ca2d6e8239297efa2/pyobjc-framework-MetricKit-8.5.1.tar.gz")
    version("8.5", sha256="82d73117cd9df768948552ea46fe6651ed48a2747b026d1667e11a3d44e765c9", url="https://pypi.org/packages/1b/a2/93879bc78b2f5e94781fcae3c072bee1c0f32856d5a57b5366790c3a65d9/pyobjc-framework-MetricKit-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

