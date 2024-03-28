# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDmTree(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.8", sha256="0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430", url="https://pypi.org/packages/f8/6d/f1997aac42e0f550c1e952a0b920eaa0bfc4d27d0421499881b934b969fc/dm-tree-0.1.8.tar.gz")
    version("0.1.7", sha256="30fec8aca5b92823c0e796a2f33b875b4dccd470b57e91e6c542405c5f77fd2a", url="https://pypi.org/packages/1c/ed/a9848a5d3dff0fc5c9c6f5120ae98c152ff47700a731958ff034a576ee27/dm-tree-0.1.7.tar.gz")
    version("0.1.6", sha256="6776404b23b4522c01012ffb314632aba092c9541577004ab153321e87da439a", url="https://pypi.org/packages/ec/45/be407a60068204dd5248dae5a4d325370d9b1b3c2cb2a1adb0d673a0d3ae/dm-tree-0.1.6.tar.gz")
    version("0.1.5", sha256="a951d2239111dfcc468071bc8ff792c7b1e3192cab5a3c94d33a8b2bda3127fa", url="https://pypi.org/packages/70/0a/bc3e9865603332c525fc218aceb023762aeffc2a86ff99b347b67ee3f2a8/dm-tree-0.1.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.12:", when="@0.1.1,0.1.4:0.1.5")
    # END DEPENDENCIES

