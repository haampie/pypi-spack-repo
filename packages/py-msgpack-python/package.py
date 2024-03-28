# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMsgpackPython(PythonPackage):
    # BEGIN VERSIONS
    version("0.5.6", sha256="378cc8a6d3545b532dfd149da715abae4fda2a3adb6d74e525d0d5e51f46909b", url="https://pypi.org/packages/8a/20/6eca772d1a5830336f84aca1d8198e5a3f4715cd1c7fc36d3cc7f7185091/msgpack-python-0.5.6.tar.gz")
    version("0.5.5", sha256="7f5d6e59228b65c47cfdae76a4aea71f6902525f18256862cda69888a686b5f9", url="https://pypi.org/packages/7c/ce/8ed474ab7ce0ef9c67d18e816e921cade83fecd59cd2cd52d825cec8166e/msgpack-python-0.5.5.tar.gz")
    version("0.5.4", sha256="c1f3f8d02206f84258a3b4f99fbc0a4e3c849721c9361196c3bfd5243e4304cd", url="https://pypi.org/packages/8b/b8/3ab1585ec7ac02afff2427d5727b922d2907466edd932d98002f0a18c29a/msgpack-python-0.5.4.tar.gz")
    version("0.5.2", sha256="23f688905bb9fbf00faa7346e72a72e670e68f3f5d94aeea5c123dd0e07de49c", url="https://pypi.org/packages/ad/21/c5bcc0dd1d073e1da1a30e3eaed6bf667c1b43d7a2fcda0ccf17efdca730/msgpack-python-0.5.2.tar.gz")
    version("0.5.1", sha256="69aa1eb0e13be1d3bd495ca937eae66df4431126f5cfd5491dc40370e5644853", url="https://pypi.org/packages/af/98/c4c3bfe11ec19f9178b4db6888f3d765e98603f48352842a7f22c6de1f09/msgpack-python-0.5.1.tar.gz")
    version("0.5.0", sha256="4f4d9f98941a2c4fba76c4157b309b304e30dddd2fc351770f85639c455df5cc", url="https://pypi.org/packages/77/e4/818d354fbecc02c01369357849a53b125417ca49200a433a8c59ecd6990b/msgpack_python-0.5.0-py3-none-any.whl")
    version("0.4.8", sha256="1a2b19df0f03519ec7f19f826afb935b202d8979b0856c6fb3dc28955799f886", url="https://pypi.org/packages/21/27/8a1d82041c7a2a51fcc73675875a5f9ea06c2663e02fcfeb708be1d081a0/msgpack-python-0.4.8.tar.gz")
    version("0.4.7", sha256="5e001229a54180a02dcdd59db23c9978351af55b1290c27bc549e381f43acd6b", url="https://pypi.org/packages/a3/fb/bcf568236ade99903ef3e3e186e2d9252adbf000b378de596058fb9df847/msgpack-python-0.4.7.tar.gz")
    version("0.4.6", sha256="bfcc581c9dbbf07cc2f951baf30c3249a57e20dcbd60f7e6ffc43ab3cc614794", url="https://pypi.org/packages/15/ce/ff2840885789ef8035f66cd506ea05bdb228340307d5e71a7b1e3f82224c/msgpack-python-0.4.6.tar.gz")
    version("0.4.5", sha256="a07cd6615a6bf38cfa2f010b121c7e77b74a3e7b971ef3e475c3d33308014cbb", url="https://pypi.org/packages/e9/af/feabdc370f9ffce1e2a9799422599ff53078e88410a72dab02c0667ccfeb/msgpack-python-0.4.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msgpack", when="@0.5:0.5.0")
    # END DEPENDENCIES

