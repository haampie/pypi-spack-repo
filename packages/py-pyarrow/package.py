# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyarrow(PythonPackage):
    # BEGIN VERSIONS
    version("15.0.2", sha256="9c9bc803cb3b7bfacc1e96ffbfd923601065d9d3f911179d81e72d99fd74a3d9", url="https://pypi.org/packages/35/a1/b7c9bacfd17a9d1d8d025db2fc39112e0b1a629ea401880e4e97632dbc4c/pyarrow-15.0.2.tar.gz")
    version("15.0.1", sha256="21d812548d39d490e0c6928a7c663f37b96bf764034123d4b4ab4530ecc757a9", url="https://pypi.org/packages/ac/f8/38a8498b294a6d3c74cd81bb411c510d52dfdd40d082651ded761fa7a964/pyarrow-15.0.1.tar.gz")
    version("15.0.0", sha256="876858f549d540898f927eba4ef77cd549ad8d24baa3207cf1b72e5788b50e83", url="https://pypi.org/packages/b3/1b/bc36a07706f630709bfd5a7936d2875e153e3d084a6d95dae583c3ad9de7/pyarrow-15.0.0.tar.gz")
    version("14.0.2", sha256="36cef6ba12b499d864d1def3e990f97949e0b79400d08b7cf74504ffbd3eb025", url="https://pypi.org/packages/d7/8b/d18b7eb6fb22e5ed6ffcbc073c85dae635778dbd1270a6cf5d750b031e84/pyarrow-14.0.2.tar.gz")
    version("14.0.1", sha256="b8b3f4fe8d4ec15e1ef9b599b94683c5216adaed78d5cb4c606180546d1e2ee1", url="https://pypi.org/packages/e0/c3/48602ef0a293af9297c0c65cdef8a2339256e485c54a4ff375d3e95d3415/pyarrow-14.0.1.tar.gz")
    version("14.0.0", sha256="45d3324e1c9871a07de6b4d514ebd73225490963a6dd46c64c465c4b6079fe1e", url="https://pypi.org/packages/15/b3/6c9071ffd108a7affd5e56164fa76dbe3df0323c56f4db22f9f643281fdc/pyarrow-14.0.0.tar.gz")
    version("13.0.0", sha256="83333726e83ed44b0ac94d8d7a21bbdee4a05029c3b1e8db58a863eec8fd8a33", url="https://pypi.org/packages/23/25/c918a8bb7d39ca99d4f751ccc19b007d1b50bca1105b0b5508788509623d/pyarrow-13.0.0.tar.gz")
    version("12.0.1", sha256="cce317fc96e5b71107bf1f9f184d5e54e2bd14bbf3f9a3d62819961f0af86fec", url="https://pypi.org/packages/c5/68/d3410e975bebbf5be00c1238d0418345d8ec5d88b7a6c102211a1c967edd/pyarrow-12.0.1.tar.gz")
    version("12.0.0", sha256="19c812d303610ab5d664b7b1de4051ae23565f9f94d04cbea9e50569746ae1ee", url="https://pypi.org/packages/98/52/ccf4f4c6f70fcd67767faaf23db3cbc5f766af9c4aeaf3961adfbf22f126/pyarrow-12.0.0.tar.gz")
    version("11.0.0", sha256="5461c57dbdb211a632a48facb9b39bbeb8a7905ec95d768078525283caef5f6d", url="https://pypi.org/packages/2c/e7/49cc11436f92a6a9001e4002fb8e5cd6733fc15a89a354cbc22b206a8171/pyarrow-11.0.0.tar.gz")
    version("10.0.1", sha256="1a14f57a5f472ce8234f2964cd5184cccaa8df7e04568c64edc33b23eb285dd5", url="https://pypi.org/packages/11/71/dd884e86aa92b2d602ee2064a485106ce5b447f8cae644f1a6f6a2e72016/pyarrow-10.0.1.tar.gz")
    version("10.0.0", sha256="b153b05765393557716e3729cf988442b3ae4f5567364ded40d58c07feed27c2", url="https://pypi.org/packages/bd/3d/9594c09e1e2fe2e5ed7ef5c22e4347fee2ea243bccd960442e2c97731fd2/pyarrow-10.0.0.tar.gz")
    version("9.0.0", sha256="7fb02bebc13ab55573d1ae9bb5002a6d20ba767bf8569b52fce5301d42495ab7", url="https://pypi.org/packages/80/2e/22fb489b4be6bc5c7202b7afd4ea3e941f9b1d79c0e3f59f64be8e92160d/pyarrow-9.0.0.tar.gz")
    version("8.0.0", sha256="4a18a211ed888f1ac0b0ebcb99e2d9a3e913a481120ee9b1fe33d3fedb945d4e", url="https://pypi.org/packages/e2/3e/fe46e9b9bae7f8268693c5d963fb37f88a59798d0ff041dd8452d5bbf9c2/pyarrow-8.0.0.tar.gz")
    version("7.0.0", sha256="da656cad3c23a2ebb6a307ab01d35fce22f7850059cffafcb90d12590f8f4f38", url="https://pypi.org/packages/12/e4/40ea3e2a2d71ef1503c1cae1534d50a3534120e49446a800aca7075f2fe7/pyarrow-7.0.0.tar.gz")
    version("6.0.1", sha256="423990d56cd8f12283b67367d48e142739b789085185018eb03d05087c3c8d43", url="https://pypi.org/packages/38/c6/97a4133eea642155e7a73cb946d889cadc461a1e6b93f5627af9fdd7b3f3/pyarrow-6.0.1.tar.gz")
    version("6.0.0", sha256="5be62679201c441356d3f2a739895dcc8d4d299f2a6eabcd2163bfb6a898abba", url="https://pypi.org/packages/52/e2/c56a075b0231780560365ca51a8cf775cc792938116bee9cacbc1f4ae582/pyarrow-6.0.0.tar.gz")
    version("5.0.0", sha256="24e64ea33eed07441cc0e80c949e3a1b48211a1add8953268391d250f4d39922", url="https://pypi.org/packages/68/7c/0e38bfb949ededdd9b648d54cba47972835704543d7409d6f853504d0581/pyarrow-5.0.0.tar.gz")
    version("4.0.1", sha256="11517f0b4f4acbab0c37c674b4d1aad3c3dfea0f6b1bb322e921555258101ab3", url="https://pypi.org/packages/7d/5d/87a22ad2210c6e53d5a87ea99fb1f503238775ab8c04189559e4eb0fd61f/pyarrow-4.0.1.tar.gz")
    version("4.0.0", sha256="606dbfc128eec5673f48fd15e30c2cc23acdcdee3b5ab5f923078c9f787d6608", url="https://pypi.org/packages/a3/8e/43fc8348b9f4845ede3b0c02bc2a6c2f6c59b8978eec65b02daaded45a21/pyarrow-4.0.0.tar.gz")
    version("3.0.0", sha256="4bf8cc43e1db1e0517466209ee8e8f459d9b5e1b4074863317f2a965cf59889e", url="https://pypi.org/packages/62/d3/a482d8a4039bf931ed6388308f0cc0541d0cab46f0bbff7c897a74f1c576/pyarrow-3.0.0.tar.gz")
    version("2.0.0", sha256="b5e6cd217457e8febcc98a6c279b96f72d5c31a24cd2bffd8d3b2da701d2025c", url="https://pypi.org/packages/fd/b7/78115614c4b227796cc87fff907930f6ae6dd999c5000d3d6ae5c2e54582/pyarrow-2.0.0.tar.gz")
    version("1.0.1", sha256="0b67124beb16dcd47b4cd7a8bac989826aee6eac6a280066476b7289206b1175", url="https://pypi.org/packages/c1/82/04249512513b31d7cd9f6fa63cf0d1c64c4705da32e3c3ece9d676e235ff/pyarrow-1.0.1.tar.gz")
    version("1.0.0", sha256="5ae4da65ba94d27cd1f1d583186de42511061f430f09bd112843c03ac3bcf9d0", url="https://pypi.org/packages/f2/c6/93744c9b5243fa8a129b44e39b34b9bd4261ed42fe93c9dfb6ddd99f8af8/pyarrow-1.0.0.tar.gz")
    version("0.17.1", sha256="278d11800c2e0f9bea6314ef718b2368b4046ba24b6c631c14edad5a1d351e49", url="https://pypi.org/packages/ed/c9/85d179d5a0575e1b066fb94bfe1e37b6d3ca546b58e75b9d1ca4952320de/pyarrow-0.17.1.tar.gz")
    version("0.17.0", sha256="fb1cdfda872700feee8ce8cc1f4a7e4220728d6e31eb067a0f95595f11e724f3", url="https://pypi.org/packages/92/1f/206195564030e712f85952117171df7bba7e8f945aaeb6f4cedbc731079a/pyarrow-0.17.0.tar.gz")
    version("0.15.1", sha256="7ad074690ba38313067bf3bbda1258966d38e2037c035d08b9ffe3cce07747a5", url="https://pypi.org/packages/e0/e6/d14b4a2b54ef065b1a2c576537abe805c1af0c94caef70d365e2d78fc528/pyarrow-0.15.1.tar.gz")
    version("0.12.1", sha256="10db6e486c918c3af999d0114a22d92770687e3a6607ea3f14e6748854824c2a", url="https://pypi.org/packages/43/f9/457938a5025244eb073bee7cfcb4d5c767ce125a9bebdff94f4c25cfb356/pyarrow-0.12.1.tar.gz")
    version("0.11.0", sha256="07a6fd71c5d7440f2c42383dd2c5daa12d7f0a012f1e88288ed08a247032aead", url="https://pypi.org/packages/1d/b6/c4e63f8bdb175d2223df26ddf12e2a0ba3fa347890128b5f128cb3f72589/pyarrow-0.11.0.tar.gz")
    version("0.9.0", sha256="7db8ce2f0eff5a00d6da918ce9f9cfec265e13f8a119b4adb1595e5b19fd6242", url="https://pypi.org/packages/be/2d/11751c477e4e7f4bb07ac7584aafabe0d0608c170e4bff67246d695ebdbe/pyarrow-0.9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    variant("dataset", default=False)
    variant("orc", default=False)
    variant("parquet", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-futures", when="@:0.9")
        depends_on("py-numpy@1.14.0:", when="@0.11:0")
        depends_on("py-numpy@1.10:", when="@:0.10")
        depends_on("py-six@1.0.0:", when="@:0.16")
    # END DEPENDENCIES

