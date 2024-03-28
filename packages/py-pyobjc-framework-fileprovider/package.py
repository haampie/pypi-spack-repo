# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFileprovider(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1accc2965c59395152d04b2f4a096cb4a5364bca8094695ce2b60d2f794bff74", url="https://pypi.org/packages/b0/e5/15fc9fafa5686ff08c53e3b36f9c3445de76dca8695b6efc7c28b22f1028/pyobjc-framework-FileProvider-10.2.tar.gz")
    version("10.1", sha256="617811be28bd5d9b0cc87389073ade7593f89ee342a5d6d5ce619912748d8e00", url="https://pypi.org/packages/22/b2/ca2943a70d4a180fde69dea925254adc2dcd4eddafdf1cb110f1162b8bba/pyobjc-framework-FileProvider-10.1.tar.gz")
    version("10.0", sha256="432165e8ae9e85437bd4b36be4fe1a467f03f5e9d6aca07228ac5385a96b2d44", url="https://pypi.org/packages/cf/a6/ab9973cc15d348f83abe46b23ed8f3b20f45efd258df98101de51cb2824d/pyobjc-framework-FileProvider-10.0.tar.gz")
    version("9.2", sha256="8344e629ff8ccc66996eef43fbae19af9e656471edd6bfa9582f749db84c18a0", url="https://pypi.org/packages/27/ec/beb6018f20b9872e0ec24de5b532521634430ba3470d20d876359d4f7160/pyobjc-framework-FileProvider-9.2.tar.gz")
    version("9.1.1", sha256="b57f548575b80ec6b777e63f145a8ca2f79d0b940a8b9cda7aa93adfb426f21d", url="https://pypi.org/packages/c9/e5/718dd3f10a81a2ade7cd63e973b76a0f46062b2be235c516d696357ec01d/pyobjc-framework-FileProvider-9.1.1.tar.gz")
    version("9.1", sha256="29c4261f460186b3f97225b5a644962ce9a29b6f150992c9aac1e80a654b0881", url="https://pypi.org/packages/04/df/4ab68676580311d79934bed9aa17109567390930c1ba52c651bdd83d69e7/pyobjc-framework-FileProvider-9.1.tar.gz")
    version("9.1-beta1", sha256="ac927156dda94d8d7f3ccf3283704d5e205be8ad6a3c3597eb18aa9431fcd1c6", url="https://pypi.org/packages/f6/23/4916d56bb639108b2c0de1491e6bc69b35aeea3b8b7bfac43b647b11775a/pyobjc-framework-FileProvider-9.1b1.tar.gz")
    version("9.0.1", sha256="80405ce146e2556a36a3918f7fa37d60905d9338483cb0521415a10dffb6027e", url="https://pypi.org/packages/0c/fb/7b67afdaf61544af991d30f4d7fb88c503a86f588283c4c9eccd6356c7c6/pyobjc-framework-FileProvider-9.0.1.tar.gz")
    version("9.0", sha256="2854c65cc96a8293e56d7964a6c84bb0381721771c40b19db6665c08f0693205", url="https://pypi.org/packages/dc/0d/59c6c6b079d5fa67297a0c8edbe065dfd6bd03619273a880a8bc20c79a84/pyobjc-framework-FileProvider-9.0.tar.gz")
    version("8.5.1", sha256="89574119acb36f74ced77b7195a29ad367bee7a11c7e60663f73a2bbda0144f8", url="https://pypi.org/packages/a4/2c/7ea6353fa9d651f0382171c759e55ab38ebb0c0e2a2ec64a9f648080b465/pyobjc-framework-FileProvider-8.5.1.tar.gz")
    version("8.5", sha256="9500dc18f6091f4127d882ba71d9e2c174d3051acc1b070b6547810189a0bfd1", url="https://pypi.org/packages/12/27/9d02402b480a047c41c040163b787879f4fa904ab3d33a00e16cb7fb670a/pyobjc-framework-FileProvider-8.5.tar.gz")
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

