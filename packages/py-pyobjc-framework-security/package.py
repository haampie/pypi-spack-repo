##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSecurity(PythonPackage):
    version("10.2", sha256="20ec8ebb41506037d54b40606590b90f66a89adceeddd9a40674b0c7ea7c8c82", url="https://pypi.org/packages/8f/3c/f251e7143a44b62f4e87f0cb7b42d30c8dbef1be0de4db45a4bdcfb4ac71/pyobjc-framework-Security-10.2.tar.gz")
    version("10.1", sha256="33becccea5488a4044792034d8cf4faf1913f8ca9ba912dceeaa54db311bd284", url="https://pypi.org/packages/04/f9/d105561be4172da0026ae5b1e85815efc3111f0e5e1be157a052218091bf/pyobjc-framework-Security-10.1.tar.gz")
    version("10.0", sha256="89837b93aaae053d80430da6a3dbd6430ca9d889aa43c3d53ed4ce81afa99462", url="https://pypi.org/packages/8a/65/236ae685e6e367ee396c526e39e14a72e19b2ac20a799527941be9c3add9/pyobjc-framework-Security-10.0.tar.gz")
    version("9.2", sha256="8d4f7a22db2fe666c7bff4a5825b49d2345e9a8d96ea085f1a614ad9a559b4e5", url="https://pypi.org/packages/57/52/64bbefd489f51ab2681326777c77f6bafa48948c60774311e428e21fc0d1/pyobjc-framework-Security-9.2.tar.gz")
    version("9.1.1", sha256="66b9967e170c3d7eabdb5ebb049c26aa1fba008e046bd66f008302594d3c2e0e", url="https://pypi.org/packages/8d/23/b6b39c70e94648e49fd7c6b7d8764b116ccbbaef3749082b91328eced6b9/pyobjc-framework-Security-9.1.1.tar.gz")
    version("9.1", sha256="5245087cd8b0e257756d212d4bf5a7f1782931d572cf9ebac38852628c5304e5", url="https://pypi.org/packages/16/98/55b1b9ce3a05a1adfdccccec80dea13dbb6b3b14992b6054c5f8c71e115d/pyobjc-framework-Security-9.1.tar.gz")
    version("9.1-beta1", sha256="cfe93afe4935a51a7499bbf89c9d23ac67972e03a70f6a92ef051ceded9f0521", url="https://pypi.org/packages/64/bb/5e35633246f022a6201fb7f602aa92718bea9f2799463ec1f6f58f5654be/pyobjc-framework-Security-9.1b1.tar.gz")
    version("9.0.1", sha256="d2093debe7467d85dd7ecef130d592abe6c13ffdbaf943d6624bae4a081046e0", url="https://pypi.org/packages/64/fa/a5b51b4c7fb86365cffaae11474d360a8d68910098b618a76a206b00938c/pyobjc-framework-Security-9.0.1.tar.gz")
    version("9.0", sha256="d441eeda097a428b7f72a0175d7d57f9eecc20711cb73acdcb5d21bc198dd230", url="https://pypi.org/packages/4f/1c/2c44c2afa960c2cd0edff3c6947ec531232426f28e858bc5ffd7f0aa842a/pyobjc-framework-Security-9.0.tar.gz")
    version("8.5.1", sha256="a2fad1a735248aeae019ff06dff2416d77c29f1331f7c27989209e1d6d3d27db", url="https://pypi.org/packages/00/3a/d9909a0a5ce79e76624391325079bc71f90151a5034d028ac6d696a026f1/pyobjc-framework-Security-8.5.1.tar.gz")
    version("8.5", sha256="6e9c26f37f73c3d697f815a868828a1010661711cde2dd04d31dab6d4429cce5", url="https://pypi.org/packages/93/46/2d6ec141b323d9322c3006d95015abbfb079e97ffbfcc18dce3e7f864f7b/pyobjc-framework-Security-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

