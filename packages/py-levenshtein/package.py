# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLevenshtein(PythonPackage):
    # BEGIN VERSIONS
    version("0.25.0", sha256="0bca15031e6b684f82003c9a399172fac6e215410d385f026a07165c69e75fd5", url="https://pypi.org/packages/0d/89/1f97cd2068360c015eaaac7a47b6e813584c732b28a76ab510b70943c276/Levenshtein-0.25.0.tar.gz")
    version("0.24.0", sha256="0cbcf3c9a7c77de3a405bfc857ab94341b4049e8c5c6b917f5ffcd5a92ff169a", url="https://pypi.org/packages/2f/ab/5cc0595dace8dfda4d781e561fe688de65e79182e10d081a82ca6d2259a3/Levenshtein-0.24.0.tar.gz")
    version("0.23.0", sha256="de7ccc31a471ea5bfafabe804c12a63e18b4511afc1014f23c3cc7be8c70d3bd", url="https://pypi.org/packages/d5/db/6163301400a4b2d86f6f0d05d36eab23880de047d0e41081a186519d4dfa/Levenshtein-0.23.0.tar.gz")
    version("0.22.0", sha256="86d285d770551cb648d4fcfe5243449a479e694e56b65272dc6cbda879012051", url="https://pypi.org/packages/e1/d7/4d5a5969d2ef6a4a702e0f3e77244bb270480c02d40f68fb93d2662a75eb/Levenshtein-0.22.0.tar.gz")
    version("0.21.1", sha256="2e4fc4522f9bf73c6ab4cedec834783999b247312ec9e3d1435a5424ad5bc908", url="https://pypi.org/packages/c4/04/9179c510aec74ab84f3e6378526365b9fbe6d2a0d031ea178877c3bd5451/Levenshtein-0.21.1.tar.gz")
    version("0.21.0", sha256="545635d9e857711d049dcdb0b8609fb707b34b032517376c531ca159fcd46265", url="https://pypi.org/packages/ff/2a/f90caf823d1f751b4c604d1839402e4c7a59f45f5c4d98e3737c5a8dd117/Levenshtein-0.21.0.tar.gz")
    version("0.20.9", sha256="70a8ad5e28bb76d87da1eb3f31de940836596547d6d01317c2289f5b7cd0b0ea", url="https://pypi.org/packages/22/ea/b2c2c26477111be2938dca870044583f6e785d952c0c424c7ccf0dbe0144/Levenshtein-0.20.9.tar.gz")
    version("0.20.8", sha256="a8cc52849264d3aa6e16c9daca95a02d59e9496c86f18def7131413cfba617cc", url="https://pypi.org/packages/23/76/c2e16792fae01016a14e01259f19ffc7191f293cb1c7cbcad3024d26b614/Levenshtein-0.20.8.tar.gz")
    version("0.20.7", sha256="b26fb439a7fbb522af63bbd781fbf51ec0c0659134a93f5bc8e9e68641df811e", url="https://pypi.org/packages/2d/c0/27bef0839c674b1dd84f18079704430896f3b29c17ad8bf3ef2ffc2d5f44/Levenshtein-0.20.7.tar.gz")
    version("0.20.6", sha256="4ec8380f15e8e30fa0cd2d982563467e5d14e6f33e762b10fc15fe66c68a3b12", url="https://pypi.org/packages/a5/c9/4b93c31e063e1b3a0e4040ba611123ab61b6c0a95fc1a653551e5cc87956/Levenshtein-0.20.6.tar.gz")
    version("0.20.2", sha256="e1528eb56d74146582aa4180a71c8808f0428fa0e08812c39923cac97faf414a", url="https://pypi.org/packages/e2/ab/968a332d8ace90277debda7517520c770c2aa140d35469fc1ffa6d24b388/Levenshtein-0.20.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-rapidfuzz@3.1:", when="@0.23:")
        depends_on("py-rapidfuzz@2.3:", when="@0.22")
    # END DEPENDENCIES

