# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQdldl(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.7.post0", sha256="f346a114c8342ee6d4dbd6471eef314199fb268d3bf7b95885ca351fde2b023f", url="https://pypi.org/packages/df/b1/47b04a296f983646c27d79bf13058f936b2a5b9e255f138c15e11f0e27b7/qdldl-0.1.7.post0.tar.gz")
    version("0.1.7", sha256="6c86639d11e301e78af2cce885249a286f675cce96d0e6d60f5b14f859d0f10e", url="https://pypi.org/packages/95/bf/26b48c697b9592b78b98a2bfc12f9f4a91876662c84b5feff58c88725438/qdldl-0.1.7.tar.gz")
    version("0.1.5.post3", sha256="69c092f6e1fc23fb779a80a62e6fcdfe2eba05c925860248c4d6754f4736938f", url="https://pypi.org/packages/3a/8c/677f80788a7fe3337661c12afab9f188d68c819ccaf4329668a5deb515c6/qdldl-0.1.5.post3.tar.gz")
    version("0.1.5.post2", sha256="7daf7ad1bfff1da71da06e82d5147bdb1ac866581617d8f06cc4eeda48e2a149", url="https://pypi.org/packages/08/8c/35bf914d768e29954617113597ed313340da730f4a8a58374a0dc70295c5/qdldl-0.1.5.post2.tar.gz")
    version("0.1.5.post0", sha256="c392c7427651d8b226423c7aba4a0f2338a1f38a4bbdabac6bc4afd8bc934f06", url="https://pypi.org/packages/ec/a3/db0e7c9fec5387dc33cbd2819329c141ba76497148aa9fab4bd1a7c2a279/qdldl-0.1.5.post0.tar.gz")
    version("0.1.5", sha256="c136bdc3d3a35adfbad28cb8007e94b2b9315d13cf1bcab1ae8429674d18a593", url="https://pypi.org/packages/86/6a/cedac7758afb6db8a7b08f0310ab952b15fca41d946b7d04d3d70ecc7ce4/qdldl-0.1.5.tar.gz")
    version("0.1.3", sha256="2e98bfcc43de55225b82f5895f8266e79a305b174490c60bc559c1538f1be920", url="https://pypi.org/packages/1b/eb/ad738bae61a5f4dba846216f5a16401eb65b49c2cd6ba1688a8c964f3f83/qdldl-0.1.3.tar.gz")
    version("0.1.2", sha256="267cb4feb7ce692198e97fb8108f8ad2c18fc99c6dc102c19b19ed1a4b8359e2", url="https://pypi.org/packages/83/45/3ca412a90454a9c889449683087d462bc703307c34465a4eab7c3dcffd3a/qdldl-0.1.2.tar.gz")
    version("0.1.1", sha256="cc5001520625c9fd77d27fd69cbd0d0ec5c745565597c7d5d83734e478841a1e", url="https://pypi.org/packages/c5/6b/39cc89b307a44da23d61a87f21f0c63dd869e77a4bc4f29a1ad1c270b121/qdldl-0.1.1.tar.gz")
    version("0.1.0", sha256="99f4ba9c5e46c129154ad929582c4bd4d6ce795aab1470000ab42a1d435fa31d", url="https://pypi.org/packages/80/81/7fe52940e0ca7ceedb962730ebbf0b7cf28c83d55a3cccb4cb1ac0252771/qdldl-0.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.7:", when="@:0.1.3")
        depends_on("py-scipy@0.13.2:", when="@:0.1.3")
    # END DEPENDENCIES

