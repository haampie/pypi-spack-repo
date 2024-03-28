# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameVtk(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.5", sha256="b89c6a164b6ec7e63b8a181547a7dda2a859f0fb16835e2686afc861d8c7b397", url="https://pypi.org/packages/80/40/edfb25e7088fa41d40fcfa04991b19e090aa00dcab5901c46fb1bbec51d5/trame_vtk-2.8.5-py3-none-any.whl")
    version("2.8.4", sha256="52713049163d037e0134bdfa0f8771315061e8dfd05c733e6f657492a45a59b5", url="https://pypi.org/packages/23/3f/989347a6ed40c9af067178381e8471a534052fbef8f51baca3f47e9ba50f/trame_vtk-2.8.4-py3-none-any.whl")
    version("2.8.3", sha256="2eb239ef77b2471e195e1d0ac93d4896908daf75cd74309b5699db7bece2ba0c", url="https://pypi.org/packages/33/26/c8b889abc7bdb05b2d9778024a5ce440af371582c3923eff985c6e867208/trame_vtk-2.8.3-py3-none-any.whl")
    version("2.8.2", sha256="b3ee001ea508bab32a9d902817cdafa2ce694c97fad5f475320cd9aa8351cc00", url="https://pypi.org/packages/28/ea/5fcd45886783310949f8cdf3b43689809533967ee2807e793a648239cdba/trame_vtk-2.8.2-py3-none-any.whl")
    version("2.8.1", sha256="1590d94825b5e9bf412b7af5310df77091c76ac66d10780bf828584ddd4cf5b5", url="https://pypi.org/packages/0e/7e/f82f39c5e05d3dcfb272eae3a7579edf7273a999b5e644afb675e40b7634/trame_vtk-2.8.1-py3-none-any.whl")
    version("2.8.0", sha256="1be403dbf16756c275fe73e9afca0a55dd56477b90db3bb0ef23daa3a47cc54d", url="https://pypi.org/packages/ce/4d/6da7faa4d9dd53dd9dc21eba377fd47f053c2fae726ddce8f195b4ebba3c/trame_vtk-2.8.0-py3-none-any.whl")
    version("2.7.1", sha256="9c77e5f87331f703c36feb590957cdce025fde2478551cca0832728b76f0d19a", url="https://pypi.org/packages/7e/cf/0a3da5af23f0af4c367c50bde2c6fdb1be7294c9bd0e1e032c9582d0fddb/trame_vtk-2.7.1-py3-none-any.whl")
    version("2.7.0", sha256="a517f410741800ed030d49ef425c823b52b26bc92b328525dabbc093c4daddd3", url="https://pypi.org/packages/9b/83/2e221c4fa783fefb345d261233ce56c7dcbfa87aee3b9e792706b9d4cce5/trame_vtk-2.7.0-py3-none-any.whl")
    version("2.6.3", sha256="6bc90437695eceedc52f2845554b218e2460db650ce3e6d5f9cf07759796d4f7", url="https://pypi.org/packages/b8/ca/4f4a9ed5a8c5f80b15f41dc27449c73c293a468f8492becd5e491e1b5439/trame_vtk-2.6.3-py3-none-any.whl")
    version("2.6.2", sha256="0085c2e6a928ed0d7ef9434ca1ca7f419572bbd10fe173020c86145a3dff8604", url="https://pypi.org/packages/9a/e8/c14de958da48dbcdcd1c506596b21f28fed1f8a6f37898a7892db1fd5f64/trame_vtk-2.6.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client")
    # END DEPENDENCIES

