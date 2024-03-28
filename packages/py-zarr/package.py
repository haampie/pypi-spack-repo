# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZarr(PythonPackage):
    # BEGIN VERSIONS
    version("2.17.1", sha256="e25df2741a6e92645f3890f30f3136d5b57a0f8f831094b024bbcab5f2797bc7", url="https://pypi.org/packages/fe/fd/7db2cb2c87cc47f971065edf2d7ab1e54202b286f6d01bf5c197c660cd69/zarr-2.17.1-py3-none-any.whl")
    version("2.17.0", sha256="d287cb61019c4a0a0f386f76eeaa7f0b1160b1cb90cf96173a4b6cbc135df6e1", url="https://pypi.org/packages/f1/69/ecaaa497d704c58621d0828bd1336d8040e09c94e822ca8d28410fbdeff2/zarr-2.17.0-py3-none-any.whl")
    version("2.16.1", sha256="de4882433ccb5b42cc1ec9872b95e64ca3a13581424666b28ed265ad76c7056f", url="https://pypi.org/packages/ba/55/0f5ec28561a1698ac5c11edc5724f8c6d48d01baecf740ffd62107d95e7f/zarr-2.16.1-py3-none-any.whl")
    version("2.16.0", sha256="6cf9e6e4c58b9233262e024394e68921a438a6af5a7428bd6bdb1e4e8d05b69a", url="https://pypi.org/packages/57/8e/b74c2a80c7df474c300bab3b761c35d6cfa6468d6d23f891d518ec7c828e/zarr-2.16.0-py3-none-any.whl")
    version("2.15.0", sha256="7296b9f42cdc9096c5349527e71492c1b05ed5464027bfa5d008339796d00b9f", url="https://pypi.org/packages/13/be/86e126be33e72a86e82516da6993d2664d68699f6f737c930dc860b840cd/zarr-2.15.0-py3-none-any.whl")
    version("2.15.0-alpha2", sha256="14d162e8314913ce317a1265b754f4fcb5fc5590af2b3e631abd7e0384d8e17a", url="https://pypi.org/packages/a3/58/098367ccde641130ea5340521ffba6d4a63dbd5e77354767af6ce569996d/zarr-2.15.0a2-py3-none-any.whl")
    version("2.15.0-alpha1", sha256="b22b8897bf4e5c2b936d0321d9527ffb38458a581bdbde5b2f8c9a10d7e22472", url="https://pypi.org/packages/0f/f3/2396f7ba7c02be0dd13faffde74d51ddabf2b0b0ed85e7dc7aa1a53de55c/zarr-2.15.0a1-py3-none-any.whl")
    version("2.14.2", sha256="feb72d6ccc43c447661861020dbf2e685a8367e80d890b6f5905954400394ed2", url="https://pypi.org/packages/7f/32/fd3560c7a721c4ff64ad482f75f759fd506431fb20e8f25a481175d908f9/zarr-2.14.2-py3-none-any.whl")
    version("2.14.1", sha256="652cab30d13b837faf12dcaa7e3061c539eb186f6ccf9526e8909ed6b6f5d333", url="https://pypi.org/packages/ef/fd/9ba7c4c574b376f7f8e0a62a6913507c4b2aca94b1dfac16a5639b7d2d53/zarr-2.14.1-py3-none-any.whl")
    version("2.14.0", sha256="388a24345c27f1ab1624e7296dabbb9184c9ef8a92cb232ae523c841a9616947", url="https://pypi.org/packages/be/80/8ed3d840ab3b265bd0b0528d1a8c3c2ec964e491f1674d52dd57169bd2af/zarr-2.14.0-py3-none-any.whl")
    version("2.13.6", sha256="ce5d88e5e0e07487d7872e381e69593edb18b750c216a961d838a818c54bb6ed", url="https://pypi.org/packages/c3/c9/bfc168b69e2630d33ab28a9ff3355f30d6e5348e8ac5839c1500003a5b23/zarr-2.13.6-py3-none-any.whl")
    version("2.13.3", sha256="883305e8ded972e25992269b0355436f11d7057b2943d278bf33cdcd2debfe2d", url="https://pypi.org/packages/93/72/aa1d08e723048647dcd9826e0fe25eb2711f4e2973fe5ef5354dba77c794/zarr-2.13.3-py3-none-any.whl")
    version("2.10.2", sha256="10e67dc6163b08497ce0a0d6dfe1ed07f71d5abfcb040f5b7eeb5d33ebf5da3e", url="https://pypi.org/packages/42/17/9aef39c229de767ffc320e43a73e98983e9f941b0fbd10dba1fd09fe0168/zarr-2.10.2-py3-none-any.whl")
    version("2.6.1", sha256="e4eb501ff472cf97b7e497a504a2fb818d6d3bff398997bcfe9438c2cc1a3665", url="https://pypi.org/packages/60/67/d69a3fcd34254df8dce23e1a4d570509f8a373fc58e40cb8681cf26795f6/zarr-2.6.1-py3-none-any.whl")
    version("2.5.0", sha256="f86c95fef1442d974adae3269c0b5a5e5200f0d46b6572bad6a9ee2c1a262478", url="https://pypi.org/packages/22/17/37cc7afabdec7b5759d68fab0bc5afd950799a4ce2189826caf5ee087414/zarr-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="53aa21b989a47ddc5e916eaff6115b824c0864444b1c6f3aaf4f6cf9a51ed608", url="https://pypi.org/packages/a3/87/383d77399148ef0772da3472b513ecf143252e7c365c51b0f06714800366/zarr-2.4.0.tar.gz")
    version("2.3.2", sha256="c62d0158fb287151c978904935a177b3d2d318dea3057cfbeac8541915dfa105", url="https://pypi.org/packages/d0/d0/02a3457f4e86a8f74104e7686c43b6bf0c76534b626f174eb20786a6f781/zarr-2.3.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.17:")
        depends_on("py-asciitree", when="@:0.0,2.5:")
        depends_on("py-fasteners", when="@:0.0,2.5:")
        depends_on("py-numcodecs@0.10.0:", when="@2.13.0:")
        depends_on("py-numcodecs@0.6.4:", when="@:0.0,2.5:2.13.0-alpha2")
        depends_on("py-numpy@1.21.1:", when="@2.17:")
        depends_on("py-numpy@1.20.0:1.21.0-rc2,1.21.1:", when="@2.16.1:2.16")
        depends_on("py-numpy@1.20.0:", when="@2.13.6:2.16.0")
        depends_on("py-numpy@1.7:", when="@:0.0,2.5:2.13.3")
    # END DEPENDENCIES

