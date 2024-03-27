##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInquirer(PythonPackage):
    version("3.2.4", sha256="273a4e4a4345ac1afdb17408d40fc8dccf3485db68203357919468561035a763", url="https://pypi.org/packages/17/e0/d7febc18212b2006f06542ca59e86fb982ac514e5df9ffb727b351c54f5c/inquirer-3.2.4-py3-none-any.whl")
    version("3.2.3", sha256="68fa2cfaa652212f035f73794aa1db2e6c0a9c8cef81ab6825b45120fa8ea345", url="https://pypi.org/packages/5b/1c/9a2b4e2bffa74bf7d39b2070455c2d2a2572a624baaac3f5d089f7283a34/inquirer-3.2.3-py3-none-any.whl")
    version("3.2.2", sha256="b475aa9094011f2b640aac0843396b2ec54fa73a9121ef2f277ca290fd6b2f80", url="https://pypi.org/packages/27/3e/c85ab518db1b561830b4e660efc129c7a5439a306c537d469491df982a79/inquirer-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="e1a0a001b499633ca69d2ea64da712b449939e8fad8fa47caebc92b0ee212df4", url="https://pypi.org/packages/a9/78/2bbc28190501b652782226a2bdcc4f7741ff927471b84774ddbdf9cb9854/inquirer-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="8b6c6d117414aa1f05e31a6d57679e414232ede022042529bd3bc63dd8683f39", url="https://pypi.org/packages/ec/d5/ece65f798372a59609b340143934883f6823276902e9b7ee8199b8b1e947/inquirer-3.2.0-py3-none-any.whl")
    version("3.1.4", sha256="8ca28834b6c6f69e0bf19cab2e2bea2c465312bb74bd6317b88a46458163a051", url="https://pypi.org/packages/3c/b7/2b4a352659d78386e0f7f5405486aa1c41664666d33e9e8506640f702f70/inquirer-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="a7441fd74d06fcac4385218a1f5e8703f7a113f7944e01af47b8c58e84f95ce5", url="https://pypi.org/packages/a5/e7/009c1ad178a2ec0ab21606ef3efc151b2a7be56a3735a521c93049425a02/inquirer-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="52103c2ddc17e0bf40157b5609721e263941a439d29fb0c4fb40a3196c4f50ba", url="https://pypi.org/packages/6e/85/881b6c99db6eb81ba2a878db3e6b9522e971bc3ad5dffa0eea01dfd25125/inquirer-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="e43ce52cde7f66e73cc24e2dda9afc686ca1c1e8df5b0b3277691083f07cdccc", url="https://pypi.org/packages/a2/09/6a0a6aa8de47d5e5dfd8e863e39ff4bb24cb4dfce7e5291e4799a844f20f/inquirer-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="33bb086b982dcda4b5560efbe8f3eb00f891f89d37990629bf2adad2260e5d3b", url="https://pypi.org/packages/11/12/2fdae48c3bf295f6a1b973c22860471a1b0fa16c43d3ae7de36b03165fec/inquirer-3.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@3.2:")
        depends_on("py-blessed@1.19:", when="@2.9:")
        depends_on("py-editor@1.6:", when="@3.2:")
        depends_on("py-python-editor@1.0.4:", when="@2.9:3.1")
        depends_on("py-readchar@3.0.6:", when="@2.10:")

