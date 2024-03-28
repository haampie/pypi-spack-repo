# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProtoPlus(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.24.0.dev0", sha256="0a4ef8203cc14ef92c69fadfa7e262292227536823dbe6433ecd51aeb579c7f4", url="https://pypi.org/packages/35/d1/60bd69e46d986381ebc412231448c756659c8d2ce14e656ff9af92f0f790/proto_plus-1.24.0.dev0-py3-none-any.whl")
    version("1.23.0", sha256="a829c79e619e1cf632de091013a4173deed13a55f326ef84f05af6f50ff4c82c", url="https://pypi.org/packages/ad/41/7361075f3a31dcd05a6a38cfd807a6eecbfb6dbfe420d922cd400fc03ac1/proto_plus-1.23.0-py3-none-any.whl")
    version("1.23.0-rc2", sha256="9126e6de8e8fe1de17fd007090bf2664c10de26e0380e11abfabe698ef986b36", url="https://pypi.org/packages/9b/ee/372b8de23daa91d87ecb51686cda861028e5ca4715a9bc569c49bc603cd2/proto_plus-1.23.0rc2-py3-none-any.whl")
    version("1.23.0-rc1", sha256="fc297f610c320346f88d397bc214960fa1ed97c3c0f425462132232b90e155b9", url="https://pypi.org/packages/11/f1/97635d61ef8e43ad7109ebbf6b871580e7dd2fda438561aa2799cceb968b/proto_plus-1.23.0rc1-py3-none-any.whl")
    version("1.22.3", sha256="a49cd903bc0b6ab41f76bf65510439d56ca76f868adf0274e738bfdd096894df", url="https://pypi.org/packages/36/5b/e02636d221917d6fa2a61289b3f16002eb4c93d51c0191ac8e896d527182/proto_plus-1.22.3-py3-none-any.whl")
    version("1.22.2", sha256="de34e52d6c9c6fcd704192f09767cb561bb4ee64e70eede20b0834d841f0be4d", url="https://pypi.org/packages/f5/0e/a277783e8b7544008e625956dee8bbdec8c65fc4ae103fc5065a290abe92/proto_plus-1.22.2-py3-none-any.whl")
    version("1.22.2-rc1", sha256="cbd2ce7a608d3251c00169e27308b1354b998f3650812bc6acbe52fe0e36b5e4", url="https://pypi.org/packages/ab/ee/ac5b2c128eacd7b323ef22bd016acc6dcd2836ba069524620be11378d0e7/proto_plus-1.22.2rc1-py3-none-any.whl")
    version("1.22.1", sha256="ea8982669a23c379f74495bc48e3dcb47c822c484ce8ee1d1d7beb339d4e34c5", url="https://pypi.org/packages/fd/5b/4567ec6de6d11cc49f76856cde967bcd0d1b47e9c7abdf5bec31aa288344/proto_plus-1.22.1-py3-none-any.whl")
    version("1.22.0", sha256="a27192d8cdc54e044f137b4c9053c9108cf5c065b46d067f1bcd389a911faf5b", url="https://pypi.org/packages/ad/34/b6289226392c1055d8a3e16649840a3ae0250c449d199261869695eac24b/proto_plus-1.22.0-py3-none-any.whl")
    version("1.20.6", sha256="c6c43c3fcfc360fdab46b47e2e9e805ff56e13169f9f2e45caf88b6b593215ab", url="https://pypi.org/packages/92/ce/a3baf8ae4e5c1c08f92500b7efe3ecca7ef3817dbee1b54067f10e150828/proto_plus-1.20.6-py3-none-any.whl")
    version("1.20.5", sha256="fa29fec8a91cf178bc1d8bf9263769421d2dba7787eae42b67235676e211c158", url="https://pypi.org/packages/f3/53/f17ded017fe8da0d7ec9b298d32df3bb90ca80a38b2adfccee12c74db929/proto_plus-1.20.5-py3-none-any.whl")
    version("1.20.4", sha256="3cfaac30676793d5ee764a0982bc30481beb5059f315e2a2422d7c73ded5b601", url="https://pypi.org/packages/d7/b8/ceb7a6531ba722df2fec4a81a6d0a58156add7531094127210912d0d73ae/proto_plus-1.20.4-py3-none-any.whl")
    version("1.20.3", sha256="b06be21c3848fbc20387d1d6891a9b97dfa1cdd0f10d3d42ef70b5700ec0f423", url="https://pypi.org/packages/1c/db/840bbdc67548560f930b6a352b1075f2ea228b9a910bfa8f9ef3b5aa3dfb/proto_plus-1.20.3-py3-none-any.whl")
    version("1.20.2", sha256="5155d02363f2dcc796fc2925698774efc376202ab58ee83f53f419a06c2f5ab8", url="https://pypi.org/packages/bc/73/61509dcf2ff967532034d01fe29454092eacfe90a6ae914100446e163d9e/proto_plus-1.20.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-protobuf@3.19.0:4", when="@1.20.6:")
        depends_on("py-protobuf@3.19.0:3", when="@1.20.5")
        depends_on("py-protobuf@3.19.0:", when="@1.19.7:1.20.4")
    # END DEPENDENCIES

