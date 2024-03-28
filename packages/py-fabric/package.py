# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFabric(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.2", sha256="91c47c0be68b14936c88b34da8a1f55e5710fd28397dac5d4ff2e21558113a6f", url="https://pypi.org/packages/d6/1f/e99e23ee01847147fa194e8d41cfcf2535a2dbfcb51414c541cadb15c5d7/fabric-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="23440a56510a981c97aaa2d4be17c759d6c60e5691bc49a66eb70f319d55f118", url="https://pypi.org/packages/e5/d3/f3e4c990eac9b48b7774b1f81ff24dc371a587174418e9ad060f0c6608ca/fabric-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="b6c5e3345da60b0d0c54d5ace22d110081550bbd03023b38c6edf1f3453c0b33", url="https://pypi.org/packages/82/a0/699cda78b695a1f73fc21cde7977b5e9d5f8679808fa9bf0ac3537bdd0e1/fabric-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="0a13217db1aa203167376119b0e165081c5906c31e2b2104410685d1310ef8fb", url="https://pypi.org/packages/3a/67/c7cc17474a43ebd19c73d01f3f191e96dc473f5ff36b12c477f28ff06684/fabric-3.1.0-py3-none-any.whl")
    version("3.0.1", sha256="a616a47b0e929c46c0c85619634a8a7522aa03378e1aea275c0a548385653ddf", url="https://pypi.org/packages/01/ae/77c964d9d3f18aa11064b7c0b30c0751cf5ba6f09dee9d7c92b3176dd7c8/fabric-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="2a05508854ddef5a020a0be9aa7787e5397b528deb5936bbd2493c0b8eaaefa3", url="https://pypi.org/packages/af/dc/4f0eb553757fd81368a5b43d548ba1cff3ad9c246e25d4e22241dcc223f0/fabric-3.0.0-py3-none-any.whl")
    version("2.7.1", sha256="7610362318ef2d391cc65d4befb684393975d889ed5720f23499394ec0e136fa", url="https://pypi.org/packages/8f/ef/26dc626427009c575dab62a4cf0d0ef38620a2c1be2a2db571a16bc56a29/fabric-2.7.1-py2.py3-none-any.whl")
    version("2.7.0", sha256="e8bfe851719a88be24f40ad7e96ac5bf023ce1af650b561d7641ed1eaed55fe5", url="https://pypi.org/packages/59/ef/e2f1bb57fe8e90816cc176c40f465a38cac677c7db8a3a89ae134c4a871c/fabric-2.7.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="7a71714b8b8f28cf828eceb155196f43ebac1bd4c849b7161ed5993d1cbcaa40", url="https://pypi.org/packages/c1/9d/59df62b620985871a4ba7d8b509b84340bbd1573257e55a427ae2df2d56e/fabric-2.6.0-py2.py3-none-any.whl")
    version("2.5.0", sha256="160331934ea60036604928e792fa8e9f813266b098ef5562aa82b88527740389", url="https://pypi.org/packages/d7/cb/47feeb00dae857f0fbd1153a61e902e54ed77ccdc578b371a514a3959a19/fabric-2.5.0-py2.py3-none-any.whl")
    version("2.4.0", sha256="98538f2f3f63cf52497a8d0b24d18424ae83fe67ac7611225c72afb9e67f2cf6", url="https://pypi.org/packages/d9/e4/e6fa248c94ee5d45def54b609fcf70f39d0b7f7050f2d4405c5f156b5516/fabric-2.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@1.1:", when="@2:2.4")
        depends_on("py-decorator@5:", when="@3.1:")
        depends_on("py-deprecated@1.2:", when="@3.2.1:")
        depends_on("py-invoke@2:", when="@3:")
        depends_on("py-invoke@1.3:1", when="@2.5:2")
        depends_on("py-invoke@1.1:1", when="@2.2:2.4")
        depends_on("py-paramiko@2.4:", when="@2:")
        depends_on("py-pathlib2", when="@2.6:2")
    # END DEPENDENCIES

