# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyarrow(PythonPackage):
    # BEGIN VERSIONS
    version("14.0.2", sha256="36cef6ba12b499d864d1def3e990f97949e0b79400d08b7cf74504ffbd3eb025", url="https://pypi.org/packages/d7/8b/d18b7eb6fb22e5ed6ffcbc073c85dae635778dbd1270a6cf5d750b031e84/pyarrow-14.0.2.tar.gz")
    version("13.0.0", sha256="83333726e83ed44b0ac94d8d7a21bbdee4a05029c3b1e8db58a863eec8fd8a33", url="https://pypi.org/packages/23/25/c918a8bb7d39ca99d4f751ccc19b007d1b50bca1105b0b5508788509623d/pyarrow-13.0.0.tar.gz")
    version("12.0.1", sha256="cce317fc96e5b71107bf1f9f184d5e54e2bd14bbf3f9a3d62819961f0af86fec", url="https://pypi.org/packages/c5/68/d3410e975bebbf5be00c1238d0418345d8ec5d88b7a6c102211a1c967edd/pyarrow-12.0.1.tar.gz")
    version("11.0.0", sha256="5461c57dbdb211a632a48facb9b39bbeb8a7905ec95d768078525283caef5f6d", url="https://pypi.org/packages/2c/e7/49cc11436f92a6a9001e4002fb8e5cd6733fc15a89a354cbc22b206a8171/pyarrow-11.0.0.tar.gz")
    version("10.0.1", sha256="1a14f57a5f472ce8234f2964cd5184cccaa8df7e04568c64edc33b23eb285dd5", url="https://pypi.org/packages/11/71/dd884e86aa92b2d602ee2064a485106ce5b447f8cae644f1a6f6a2e72016/pyarrow-10.0.1.tar.gz")
    version("8.0.0", sha256="4a18a211ed888f1ac0b0ebcb99e2d9a3e913a481120ee9b1fe33d3fedb945d4e", url="https://pypi.org/packages/e2/3e/fe46e9b9bae7f8268693c5d963fb37f88a59798d0ff041dd8452d5bbf9c2/pyarrow-8.0.0.tar.gz")
    version("7.0.0", sha256="da656cad3c23a2ebb6a307ab01d35fce22f7850059cffafcb90d12590f8f4f38", url="https://pypi.org/packages/12/e4/40ea3e2a2d71ef1503c1cae1534d50a3534120e49446a800aca7075f2fe7/pyarrow-7.0.0.tar.gz")
    version("4.0.1", sha256="11517f0b4f4acbab0c37c674b4d1aad3c3dfea0f6b1bb322e921555258101ab3", url="https://pypi.org/packages/7d/5d/87a22ad2210c6e53d5a87ea99fb1f503238775ab8c04189559e4eb0fd61f/pyarrow-4.0.1.tar.gz")
    version("3.0.0", sha256="4bf8cc43e1db1e0517466209ee8e8f459d9b5e1b4074863317f2a965cf59889e", url="https://pypi.org/packages/62/d3/a482d8a4039bf931ed6388308f0cc0541d0cab46f0bbff7c897a74f1c576/pyarrow-3.0.0.tar.gz")
    version("0.17.1", sha256="278d11800c2e0f9bea6314ef718b2368b4046ba24b6c631c14edad5a1d351e49", url="https://pypi.org/packages/ed/c9/85d179d5a0575e1b066fb94bfe1e37b6d3ca546b58e75b9d1ca4952320de/pyarrow-0.17.1.tar.gz")
    version("0.15.1", sha256="7ad074690ba38313067bf3bbda1258966d38e2037c035d08b9ffe3cce07747a5", url="https://pypi.org/packages/e0/e6/d14b4a2b54ef065b1a2c576537abe805c1af0c94caef70d365e2d78fc528/pyarrow-0.15.1.tar.gz")
    version("0.12.1", sha256="10db6e486c918c3af999d0114a22d92770687e3a6607ea3f14e6748854824c2a", url="https://pypi.org/packages/43/f9/457938a5025244eb073bee7cfcb4d5c767ce125a9bebdff94f4c25cfb356/pyarrow-0.12.1.tar.gz")
    version("0.11.0", sha256="07a6fd71c5d7440f2c42383dd2c5daa12d7f0a012f1e88288ed08a247032aead", url="https://pypi.org/packages/1d/b6/c4e63f8bdb175d2223df26ddf12e2a0ba3fa347890128b5f128cb3f72589/pyarrow-0.11.0.tar.gz")
    version("0.9.0", sha256="7db8ce2f0eff5a00d6da918ce9f9cfec265e13f8a119b4adb1595e5b19fd6242", url="https://pypi.org/packages/be/2d/11751c477e4e7f4bb07ac7584aafabe0d0608c170e4bff67246d695ebdbe/pyarrow-0.9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("dataset", default=False, description="dataset")
    variant("orc", default=False, description="orc")
    variant("parquet", default=False, description="parquet")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@13:")
        depends_on("python@3.7:", when="@7:12")
        depends_on("py-futures", when="@:0.9")
        depends_on("py-numpy@1.14.0:", when="@0.11:0")
        depends_on("py-numpy@1.10:", when="@:0.10")
        depends_on("py-six@1.0.0:", when="@:0.16")
    # END DEPENDENCIES

