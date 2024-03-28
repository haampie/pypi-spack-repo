# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInquirer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
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
    version("2.10.1", sha256="7a01977602214d6d86e8ddef3a1300927c4e58223eab69893e550604a0ac9477", url="https://pypi.org/packages/3c/43/ba546389e8e0fcd821006c6e40a8f40a6f7d9d65fb77fca049e24161ea3f/inquirer-2.10.1-py3-none-any.whl")
    version("2.10.0", sha256="e49f6e37132eedda31c860fe36b19726f34f6d45f7d1bfb9bfb87169da0826f8", url="https://pypi.org/packages/be/86/c1b92c16565a3d1ea7e60e3cd34985dd6af65aa1ef207fdc80b78a1eb3d2/inquirer-2.10.0-py3-none-any.whl")
    version("2.9.2", sha256="ea44fe074e878e74af05b6902314d7d7b8ff5d2db5259bcb37d6c5ec9b75afa6", url="https://pypi.org/packages/c7/cf/9c3a415723c9fe6e876d37054a95a17e1a3cbb279ab4e6f7770b11b422af/inquirer-2.9.2-py3-none-any.whl")
    version("2.9.1", sha256="f50876f5073c8c5fc482b44b8ef4e9720061498abeb352f62b5c94cacf0e43e2", url="https://pypi.org/packages/36/84/39b8023e053fea797c08f818a69d5e79ba539b96441f33288649fb917ad4/inquirer-2.9.1-py3-none-any.whl")
    version("2.9.0", sha256="7063c23fec58b285df34438b20cf819e108fe7a88680475d404ab534df808bb7", url="https://pypi.org/packages/b5/21/622e79b3bd8d1399da7b1c3e46e4a1b2f452901d22beb5718d78b1040a04/inquirer-2.9.0-py3-none-any.whl")
    version("2.8.0", sha256="237c14a68bcf0b2950899aa11bcc342de613e9389e4bf6fcd2ef97fcb3b1590a", url="https://pypi.org/packages/6d/5a/300feaa18f211e88b5365302cc567258a397a7ef6050d1a139503c2bd881/inquirer-2.8.0-py2.py3-none-any.whl")
    version("2.7.0", sha256="d15e15de1ad5696f1967e7a23d8e2fce69d2e41a70b008948d676881ed94c3a5", url="https://pypi.org/packages/60/10/450a7edfaea3d09a4a7062bd567178bfb66233bae3ee0042934910e180de/inquirer-2.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@3.2:")
        depends_on("py-blessed@1.19:", when="@2.9:")
        depends_on("py-blessed@1.19:1.19.0", when="@2.8")
        depends_on("py-blessed@1.17.6", when="@2.7")
        depends_on("py-editor@1.6:", when="@3.2:")
        depends_on("py-python-editor@1.0.4:", when="@2.6.2:3.1")
        depends_on("py-readchar@3.0.6:", when="@2.10:")
        depends_on("py-readchar@2.0.1:", when="@2.9")
        depends_on("py-readchar@2.0.1:2", when="@2.6.3:2.8")
    # END DEPENDENCIES

