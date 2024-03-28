# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudBatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.17.14", sha256="0bebf878e3f4cb470ba788dc9d9d78a11db2c16bea7cc9da9bfde24522bc1914", url="https://pypi.org/packages/d7/62/742d6e95bc8567a8b501c3919161a6bffe74a87a9fece535f2b0d130057e/google_cloud_batch-0.17.14-py2.py3-none-any.whl")
    version("0.17.13", sha256="6aa5d0b83b3cafdb8383478f4286202469715a0dad348bf8fafbe6d15b624348", url="https://pypi.org/packages/bc/98/13133b34c010ac240d2154dfdb1be230da56196f814abc6006b63c9d709d/google_cloud_batch-0.17.13-py2.py3-none-any.whl")
    version("0.17.12", sha256="4d6d0f6c392c5ed2e1fe59d38f1151b1414abcf9daa50ffb25a5981984fd0b63", url="https://pypi.org/packages/0a/ee/907acae76f4acb70687f1cdb88644bab50bf7c8ecf335f3aaf4f75cc4dc2/google_cloud_batch-0.17.12-py2.py3-none-any.whl")
    version("0.17.11", sha256="c5efcefae0736b5aa80c3f29b9e1b18ab401407c08dd0d21a60ffdd6b2eb7b63", url="https://pypi.org/packages/d9/66/af0a14a43f244f837962b31571ece429bfd62e85a4e3e9e5db24814ec3ac/google_cloud_batch-0.17.11-py2.py3-none-any.whl")
    version("0.17.10", sha256="136199c23b59a248b35ce19e73dfe40fdec4566268ac2279afcf3e1af56fea26", url="https://pypi.org/packages/ab/60/4a17e124045ce2c6b5054a6fb70b13452f7ed7115f0ec0b64609df663155/google_cloud_batch-0.17.10-py2.py3-none-any.whl")
    version("0.17.9", sha256="dd67dfa0cc76b469f2afe3facc41253faad6c9179234dba609bc1ba1e04d76c2", url="https://pypi.org/packages/5b/07/99b1f6180e99c2b98b24a59bcbf7d0c6fe296081e31655c1ab8ea7743b81/google_cloud_batch-0.17.9-py2.py3-none-any.whl")
    version("0.17.8", sha256="b186b746ed4caee87ff968671c51d286c45fe4924cc065f0d76d94e501e6a798", url="https://pypi.org/packages/f9/69/d97d1bc3c7b169a8bb120451582c2f231d5f3977289da100eb6500114a3f/google_cloud_batch-0.17.8-py2.py3-none-any.whl")
    version("0.17.7", sha256="a1471f339591bfb76eef815744ad1d598133e52a62588b648972275f4154f385", url="https://pypi.org/packages/b7/4a/afde68dffae6a836200936ebfedb5e3af5ff6384b395031a38b941ad0fa0/google_cloud_batch-0.17.7-py2.py3-none-any.whl")
    version("0.17.6", sha256="7f99195a490f00dc4aee9dc3e4716283af57d2dc358dab2b069385347b0694c7", url="https://pypi.org/packages/17/8f/80b3a95f5dee830b67d059f6822d34e6e90b597f2ffd40351d168fe7a8a1/google_cloud_batch-0.17.6-py2.py3-none-any.whl")
    version("0.17.5", sha256="93ef6bfaec54f45999e02a20772eb388db3a4d75542b51b293af8e185ca468ad", url="https://pypi.org/packages/05/24/c8f4dd2bcb21f524e0eebdbbe518c3446daba1881aae2dab7cf7c4304c3f/google_cloud_batch-0.17.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-api-core@1.34.1:1,2.11:+grpc", when="@0.17.12:")
        depends_on("py-google-api-core@1.34:1,2.11:+grpc", when="@0.5:0.17.11")
        depends_on("py-google-auth@2.14.1:2.23,2.25.1:", when="@0.17.14:")
        depends_on("py-google-auth@2.14.1:", when="@0.17.11:0.17.13")
        depends_on("py-proto-plus@1.22.3:", when="@0.17.6-rc0:")
        depends_on("py-proto-plus@1.22.2:", when="@0.8:0.17.5 ^python@3.11:")
        depends_on("py-proto-plus@1.22:", when="@0.1.2:0.17.5")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@0.3.2:")
    # END DEPENDENCIES

