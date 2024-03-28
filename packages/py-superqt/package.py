# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySuperqt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.2", sha256="c8c2d7418ccb518fe0405852effa63c5f395f557115ddbae80ff44ab10c08602", url="https://pypi.org/packages/ed/60/9d15dc2ebc0e4baac2f9dfcd8381f4f66543826a4b06b3f68185ee1cdd14/superqt-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="93c063b77581f9b0883b6198a6365d5cdacb5e4953fb2f7b0466d741c3bbfd30", url="https://pypi.org/packages/9e/25/f24abb44959276070c737bd45d2a2948b814360629a83a93d291dc42baf3/superqt-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="7628fbd6626f88e0da8e57c4ef4a14ec12f7ae8287ddd85a481558fb5f0422d9", url="https://pypi.org/packages/10/a3/157af9aeedb178c4abb6159da2fea0c6920aa2f50bdbc09fac9af0101cc9/superqt-0.6.0-py3-none-any.whl")
    version("0.5.4", sha256="2b4d912ddab18009628f1d1f73ff226c7b49e5840f921392dc019cbf1e5cb872", url="https://pypi.org/packages/c3/42/c3aac02df6f1d75d781fb9091c7bf58da7336b3ff03d2caf4e0ad25efcec/superqt-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="bb52b9fcf4b1d7bd5839b20a816c3856bd225f00dca902f053d937f586a82f00", url="https://pypi.org/packages/3b/4f/1362150dfae793ad5fea79cb7c5577dbf0952037f434a5169af174a75e21/superqt-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="d72eca82cf40547a5dd8a5e566b83a8fc8ad5b57d8eb4de82e76753bf05c1818", url="https://pypi.org/packages/4e/70/63d2922f95942031b4672b5791dd91f72f95caf387393bce0f8056236a47/superqt-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="d49d6a9196fa9f6c22fef383e61282abb2deb9b3b80deb467eb72c2f5afe7f74", url="https://pypi.org/packages/43/8f/3d0c2791bb647178d71a5d6d317082eb03203b025bad75bbe31936161d07/superqt-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="e12508cf6c20e0ac01e624b0819d61a020c0a48f861b8226f6ed19b1a9b1c487", url="https://pypi.org/packages/bb/67/ea6ef1298694c82eabfdc6e5f838304ccbaadb004498665aeda41e531491/superqt-0.5.0-py3-none-any.whl")
    version("0.2.4", sha256="02921e7aeb08b716e93925009bb6105ef9a9c60b003155ffff056a6d897f8b1f", url="https://pypi.org/packages/66/16/54ad5a349d7cd7fc8a3104c8c595ddd2f30f8d85b0b54a3740bb3cf86dbc/superqt-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="4a45bb8a67459f6caf676d240ff24741c9bce05464ca04c1b54d3448a38b7b38", url="https://pypi.org/packages/ca/b9/d116ad9956f585091251189839862aef8d365866f2a72f43781eb82397c2/superqt-0.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@0.5:0.6.1")
        depends_on("py-pygments@2.4:", when="@0.5:")
        depends_on("py-qtpy@1.1:", when="@0.5:")
        depends_on("py-typing-extensions@3.7.4.3:3.7,3.10.0.1:", when="@0.5.1:")
        depends_on("py-typing-extensions", when="@0.5:0.5.0")
    # END DEPENDENCIES

