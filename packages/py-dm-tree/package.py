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
    version("0.1.4", sha256="c4477ba8fee2fd7113ce0ef48a5bcf4f881100dcf5e609853368bbab96f4095e", url="https://pypi.org/packages/e9/e2/3a6413fd1804325ba42dc05a6dfc29bf47f3ab7122b2da8feda5fcbaff59/dm-tree-0.1.4.tar.gz")
    version("0.1.2", sha256="41b102cd06fb32c87c8bb35efa18aa6fc76db6359703f0858d588cd66d46c716", url="https://pypi.org/packages/5d/26/cd2b72779f7f448894837c1c11ad3bb73dfdeffa3b77d80235c1ba39fa9f/dm-tree-0.1.2.tar.gz")
    version("0.1.1", sha256="6abcec0f84d39113a3b2ebdf1a5973a7b1ca3ffbd313a1d30f4d8de156421b77", url="https://pypi.org/packages/88/4e/b1a79e99e024780ef4ad675babacd719fe61588e91a2c46788242071bd14/dm-tree-0.1.1.tar.gz")
    version("0.1.0", sha256="c9eb38877276091f255566a2bc98f69dd2362c80f70a6c97574b18aa2b1adb4d", url="https://pypi.org/packages/61/1b/8dc4cb0b7de051c1777cbf79121d94374661aea76b5c847e21fb9669296b/dm-tree-0.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.12:", when="@0.1.1,0.1.4:0.1.5")
    # END DEPENDENCIES

