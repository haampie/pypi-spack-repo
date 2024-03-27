##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkContactsui(PythonPackage):
    version("10.2", sha256="2dd5f1993c36caf13527de0890c6c49c08a339e58bc3b3fa303d5a04b672b418", url="https://pypi.org/packages/26/ed/aecdafd1111939e6419cb6e7373c863ae9fe8f612849653504eaf96edb1c/pyobjc-framework-ContactsUI-10.2.tar.gz")
    version("10.1", sha256="0b97e4c5599ab269f53597dd8f47a45599434c833e72185d5d3a257413a6faf4", url="https://pypi.org/packages/84/a3/762ce00316980ad33926ad9ede1a80679097e1072bc6a408165b85d96839/pyobjc-framework-ContactsUI-10.1.tar.gz")
    version("10.0", sha256="38f885b861af10e5773f4dbbabd4170bcd35610d879763caac47623ff7a410a9", url="https://pypi.org/packages/e1/8f/454dc1448a947c8736c6f6bab8b848c16c575de97bb0f575fa9269f76147/pyobjc-framework-ContactsUI-10.0.tar.gz")
    version("9.2", sha256="7247e28c6ba06c48f31f39bdac15b7fe0efef336aba375e282ff00346e53a18e", url="https://pypi.org/packages/4f/5f/644d203fc7cbb4a69fc24b050eb2c073354681e0479d74a83ac01d6e8104/pyobjc-framework-ContactsUI-9.2.tar.gz")
    version("9.1.1", sha256="110f3bf9c4b96c4c90badf51bd74aa943f774bababd28a81e703d87939c9b939", url="https://pypi.org/packages/d9/05/cb6e42fe330e5501e0719ee50576202425672936b5823dc5ff643f114ae2/pyobjc-framework-ContactsUI-9.1.1.tar.gz")
    version("9.1", sha256="6471ceb05c15207d8628ac72c1a8da9424175fed3561e1aaaec7f585d0cb3c5c", url="https://pypi.org/packages/29/9d/0f33a0c4cd5636c9e75002992d16dedb0c672d29b1b78883ff49ee0b72d8/pyobjc-framework-ContactsUI-9.1.tar.gz")
    version("9.0.1", sha256="235d7692b2ec778d31568d8996cad36b2497bb273f309f8976c5239c77242a75", url="https://pypi.org/packages/02/85/c8606c7f7163d18076638cae905b26aef64d525d41b2f06ea81fa99ad3cd/pyobjc-framework-ContactsUI-9.0.1.tar.gz")
    version("9.0", sha256="dd28e444d3fb649ed35c7d3baf6a8f913780d3c32653569fc31dc4a86b24c4e1", url="https://pypi.org/packages/da/cc/724dd7548bff7abcc37db8221baddbb1d901090ed1bab706ce6aa2748199/pyobjc-framework-ContactsUI-9.0.tar.gz")
    version("8.5.1", sha256="416b48eebdb70fb3b7ca483c325a5beed0822415b0a1ba4f146d5d3358009b2d", url="https://pypi.org/packages/11/50/be2344f77b9b013733e8209e34b4a39e50048572a98422f5bd966e913d54/pyobjc-framework-ContactsUI-8.5.1.tar.gz")
    version("8.5", sha256="72d01c265250d2cbb4e13aff46da44a1da5dbc7b45119dcc6d7a82bc384f05cd", url="https://pypi.org/packages/a0/2c/d46ce7369c32931cbb46d8716890afcde148166575b0e9416d3acd54b7ce/pyobjc-framework-ContactsUI-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-contacts@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-contacts@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-contacts@10:", when="@10:10.0")

