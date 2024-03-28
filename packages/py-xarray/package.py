# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXarray(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2024.2.0", sha256="a31a9b37e39bd5aeb098070a75d6dd4d59019eb339d735b86108b9e0cb391f94", url="https://pypi.org/packages/47/f6/f2d4a0a2a4eb6fc427f1e482987e24104c9710c4244c76ea75b55243ada0/xarray-2024.2.0-py3-none-any.whl")
    version("2024.1.1", sha256="0bec81303b088c8df4f075e1579c00cfd7e5069688e4434007f0b8d7df17fc1c", url="https://pypi.org/packages/d4/b5/2af411546a4c2be8d6315bc01be055fbad367bc9c57dbd773ad05db62b1c/xarray-2024.1.1-py3-none-any.whl")
    version("2024.1.0", sha256="df040f835441babf0a04c0bd6eacf7780f7dad6044a86603b16f6b4d204a99bd", url="https://pypi.org/packages/e9/c4/7f7ea950c721f002268d17e538c85108e5b09e4fe24e4b79e604bfb59660/xarray-2024.1.0-py3-none-any.whl")
    version("2023.12.0", sha256="3c22b6824681762b6c3fcad86dfd18960a617bccbc7f456ce21b43a20e455fb9", url="https://pypi.org/packages/54/a3/289d1b5703412247551fc9f2057e8726567bdd278d25c37ad834f78c851e/xarray-2023.12.0-py3-none-any.whl")
    version("2023.11.0", sha256="933b5101e965120ed58e29525667ab34aafcea1886c236ade72a34d7bb465d9c", url="https://pypi.org/packages/c3/0a/56eadeb54f258e88f2f31e79fcb84079f8757298f4257d716cbbc674c460/xarray-2023.11.0-py3-none-any.whl")
    version("2023.10.1", sha256="71ea549e9be6dfeab19c2736acf659967b861aad2397691a80e5fad0c61db2ad", url="https://pypi.org/packages/1a/66/39d1df58fc6f06c19551dd9c8da5f9504b424b7f7212424fe25e69f97149/xarray-2023.10.1-py3-none-any.whl")
    version("2023.10.0", sha256="cae883c10913a081c58f38d0dc39e92cc87e0fbb43e869331c60fd0430e97fb4", url="https://pypi.org/packages/fd/82/268ff8e9e15fd55b085ba3e8a632a50add5228ed221bc05117ad6dee2841/xarray-2023.10.0-py3-none-any.whl")
    version("2023.9.0", sha256="3fc4a558bd70968040a4e1cefc6ddb3f9a7a86ef6a48e67857156ffe655d3a66", url="https://pypi.org/packages/b5/36/1f4d4bc9be1957716ab93b8be8ea64df6b891ff3fc438f4964916fa6d714/xarray-2023.9.0-py3-none-any.whl")
    version("2023.8.0", sha256="eb42b56aea2c7d5db2a7d0c33fb005b78eb5c4421eb747f2ced138c70b5c204e", url="https://pypi.org/packages/cc/21/c3a9d3017c131cea3c2967957b05448ffc81cafced239796bbbdc98073e4/xarray-2023.8.0-py3-none-any.whl")
    version("2023.7.0", sha256="af8b55bf78b792b8ad9326eb9d89980602f1a51e93d8465b445aeea3accca27e", url="https://pypi.org/packages/cf/2f/e696512aa1e4e2ee1cf1e0bdbab6042f6c782058eb0a4367184ce4343f36/xarray-2023.7.0-py3-none-any.whl")
    version("2022.3.0", sha256="560f36eaabe7a989d5583d37ec753dd737357aa6a6453e55c80bb4f92291a69e", url="https://pypi.org/packages/4e/6e/2d2430e021fcce47771dcb168599b3d71f26f63a89bd3ff78f56759f1701/xarray-2022.3.0-py3-none-any.whl")
    version("0.18.2", sha256="a0b14b888b90a3ad8ecec5db9862f3fd02f8c0cc15066a3429d37da62fc37219", url="https://pypi.org/packages/98/4f/f5ef867f0e8a91eb528edfcfb6d0e82d758ae507fa0456eb1fe40e289362/xarray-0.18.2-py3-none-any.whl")
    version("0.17.0", sha256="ce204fb5015c3d382036f7c065c927df5684276976810aef43d78908c3ceb440", url="https://pypi.org/packages/a5/19/debc1f470b8b9e2949da221663c8102ed6728f4d38dc964085ca43de1428/xarray-0.17.0-py3-none-any.whl")
    version("0.16.2", sha256="88d0f80145999443730f87c7575e426d377f0b62677d915f21059cc364b4a1e1", url="https://pypi.org/packages/10/6f/9aa15b1f9001593d51a0e417a8ad2127ef384d08129a0720b3599133c1ed/xarray-0.16.2-py3-none-any.whl")
    version("0.14.0", sha256="9a4f97c6a7fdf9a6dd873ac679a86abfa1910263a85774d69bc3c0fa1e7967f5", url="https://pypi.org/packages/7e/84/e1127b7807a1a98da6d977939b11e89cb924b8b6d8917d9894eb8f39c230/xarray-0.14.0-py3-none-any.whl")
    version("0.13.0", sha256="6bea5d4874e686406a90a2007d13264adabe78c36609971f16270df8b08bdacf", url="https://pypi.org/packages/e0/7b/b969f686fa7d15232be520d7d82f9818afc2e7027c1c215d742dd9e244b2/xarray-0.13.0-py2.py3-none-any.whl")
    version("0.12.0", sha256="00d9c465989a004e48a015d834275eb16e4266fa43f8f9689ae5db590f623e04", url="https://pypi.org/packages/48/9a/3634efd35aeaa98fb0f0bdc7318e383e4723774cb6fd6f693cca975d70ec/xarray-0.12.0-py2.py3-none-any.whl")
    version("0.11.0", sha256="51013a4fbdad6def83a49233490da6f15650a0d4a65966c26d8e2b6cf7992269", url="https://pypi.org/packages/ab/f3/c3b45f15a82d7c89cbb6f0726d047d5d2b0ec8d1933731c125ac45a38b3d/xarray-0.11.0-py2.py3-none-any.whl")
    version("0.9.1", sha256="7f100df6e98febb10dc4c0274ac57540ff6c6b2f28add518dc75422a647d82bd", url="https://pypi.org/packages/ba/b6/52cefb47d8775673a2cfcce3e30e8138b329a7731aba3921bcd1ebae49e1/xarray-0.9.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("io", default=False)
    variant("parallel", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.2:")
        depends_on("py-cfgrib", when="@0.16.2:2023.3+io")
        depends_on("py-cftime", when="@0.16.2:+io")
        depends_on("py-dask+complete", when="@0.16.2:+parallel")
        depends_on("py-fsspec", when="@0.16.2:+io")
        depends_on("py-h5netcdf", when="@0.16.2:+io")
        depends_on("py-netcdf4", when="@0.16.2:+io")
        depends_on("py-numpy@1.23.0:", when="@2024:")
        depends_on("py-numpy@1.22.0:", when="@2023.10.1:2023")
        depends_on("py-numpy@1.21.0:", when="@2023.2:2023.10.0")
        depends_on("py-numpy@1.18.0:", when="@0.20:2022.3")
        depends_on("py-numpy@1.17.0:", when="@0.18:0.19")
        depends_on("py-numpy@1.15.0:", when="@0.15:0.17")
        depends_on("py-numpy@1.14.0:", when="@0.14")
        depends_on("py-numpy@1.12.0:", when="@0.10.8:0.13")
        depends_on("py-numpy@1.7:", when="@0.8:0.9")
        depends_on("py-packaging@22:", when="@2024:")
        depends_on("py-packaging@21.3:", when="@2022.12:2023")
        depends_on("py-packaging@20:", when="@0.21.1:2022.9")
        depends_on("py-pandas@1.5.0:", when="@2024:")
        depends_on("py-pandas@1.4.0:", when="@2023.2,2023.4:2023")
        depends_on("py-pandas@1.1.0:", when="@0.20:2022.3")
        depends_on("py-pandas@1.0.0:", when="@0.18:0.19")
        depends_on("py-pandas@0.25.0:", when="@0.15:0.17")
        depends_on("py-pandas@0.24.0:", when="@0.14")
        depends_on("py-pandas@0.19.2:", when="@0.10.8:0.13")
        depends_on("py-pandas@0.15:", when="@0.8:0.9")
        depends_on("py-pooch", when="@0.18.1:+io")
        depends_on("py-pydap", when="@2022.9:+io ^python@:3.9")
        depends_on("py-pydap", when="@0.16.2:2022.6+io")
        depends_on("py-rasterio", when="@0.16.2:2023.3+io")
        depends_on("py-scipy", when="@0.16.2:+io")
        depends_on("py-setuptools@40.4:", when="@0.17:0.19")
        depends_on("py-setuptools@38.4:", when="@0.16.1:0.16")
        depends_on("py-zarr", when="@0.16.2:+io")
    # END DEPENDENCIES

