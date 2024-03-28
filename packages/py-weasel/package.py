# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWeasel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.4", sha256="ee48a944f051d007201c2ea1661d0c41035028c5d5a8bcb29a0b10f1100206ae", url="https://pypi.org/packages/d5/e5/b63b8e255d89ba4155972990d42523251d4d1368c4906c646597f63870e2/weasel-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="141b12fd0d38599ff8c567208d1db0f5af1b532363fadeba27d7bc87d751d88a", url="https://pypi.org/packages/a6/76/41433e70b7c9ed47db8206536ecc6408362db44111c27f59e76af20377f2/weasel-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="f2921a7fa78ad69dcd7068fa40a43786f3acf7edd6c35b44763e9163e045b664", url="https://pypi.org/packages/de/f5/6786a5fd1ab6a38511f3772c9002f312a2d509c1237ae514631adf145ad4/weasel-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="69b47452b599437acccfcee2d0206d7ef1ed57ea3a6cee564864d74a6e5627db", url="https://pypi.org/packages/43/2d/54e7767e5be4dfd868ee4f8c1fd76cddf2af599ea2abd8f6d7b1e293a1f0/weasel-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="77df44bb94fd651e2178b6914e0d9067a03f38a79c73eade7936d29970a76203", url="https://pypi.org/packages/0b/37/50466825ac1a335f3205ab22eb3baa34e7621e47829ff1bdc08b2484c720/weasel-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="b07edb0cd0dba1dec277f68c0450f9ee637ac715c1ae28990f88db9c6a8d9acd", url="https://pypi.org/packages/d2/2b/94d755de15d8cf2dd52857f0d99884ae149aeeb39a192477227b96b3beb5/weasel-0.2.0-py3-none-any.whl")
    version("0.1.1", sha256="e33f88504670b9d6531c8467b7fc8d02831ac96a55d5ae6f842cfb62900f8d6a", url="https://pypi.org/packages/a4/5c/05fd82fa1bdc30498b0b0838bd50d3ddd5b9b61316075bc695f547d5b572/weasel-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="1e9a5971b63df237a96477301c0f64ab149de4ab8b6798f024682ce3edea2a27", url="https://pypi.org/packages/dd/f7/719fb4757da6efb2a0f3339e4c57377dfe01a678397e8935c7adc7fe449a/weasel-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-catalogue@2.0.6:2.0", when="@0.1:0.3.0")
        depends_on("py-cloudpathlib@0.7:0.16", when="@0.3.3:")
        depends_on("py-cloudpathlib@0.7:0.15", when="@0.2:0.3.2")
        depends_on("py-confection@0.0.4:", when="@0.2:")
        depends_on("py-confection@0.0.4:0.0", when="@0.1")
        depends_on("py-packaging@20:", when="@0.1:")
        depends_on("py-pathy@0.10:", when="@0.1")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:", when="@0.2:")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:1", when="@0.1")
        depends_on("py-requests@2.13:", when="@0.1:")
        depends_on("py-smart-open@5.2.1:6", when="@0.2:")
        depends_on("py-srsly@2.4.3:", when="@0.1:")
        depends_on("py-typer@0.3:0.9", when="@0.3.2:")
        depends_on("py-typer@0.3:0.7", when="@0.1:0.3.1")
        depends_on("py-wasabi@0.9.1:", when="@0.1:")
    # END DEPENDENCIES

