##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGriddataformats(PythonPackage):
    version("1.0.2", sha256="4562bb2da9a064a8e6640e5fb853e204c8f32f6403651703f6b0ef58a009054c", url="https://pypi.org/packages/89/ab/9cae972ca177f7c64017f4b76f3780c832da52737b95c3e39ed0701af7a7/GridDataFormats-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="c2c45c9ea18f29ffd8fe311d5322b4cba4f4e4c76980ec4e2e9a7f296b208a46", url="https://pypi.org/packages/03/f7/a676afdb039c77eb012f4cdbed231e44555cc90025ce660d17cbeecdc9f9/GridDataFormats-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="5dc05c4b2c28e462838b9197aa64e1f0f2476190aa473dc92dec24c0ac637218", url="https://pypi.org/packages/b9/16/ceb3cdc16abdb24293267407e2770cda9caf70623fd2a5521511c266545d/GridDataFormats-1.0.0-py2.py3-none-any.whl")
    version("0.7.0", sha256="016f6dc3f7d3271611e5117e4520e64584824d0f39e8ce24f2dd55f49d9ffb07", url="https://pypi.org/packages/80/ea/cba7fb38f2901a39924a5787d63d000347678f1b32474d9b2db42ca36bb3/GridDataFormats-0.7.0-py2.py3-none-any.whl")
    version("0.6.0", sha256="87160faa31ca21cf304da70e533453871c922549ef34146a6f3e7ccd9a3b6997", url="https://pypi.org/packages/78/e4/c8cd5f6a8814f33a2112325b062cd79e7748d7cacf89077365de9d7200b7/GridDataFormats-0.6.0-py2.py3-none-any.whl")
    version("0.5.0", sha256="2b1647da540d62cb6643ce8834ae30e9244dfbb30a4554c06740ed1938ee49ad", url="https://pypi.org/packages/9b/7e/796ea78dc3a29c119b1171f6c692cc5fb1bb2ece029429bf39fce27f4cd0/GridDataFormats-0.5.0-py2.py3-none-any.whl")
    version("0.4.1", sha256="e6f2353567276e8bf257cde031571dd80f953952140678c2171c21e13e52896a", url="https://pypi.org/packages/6c/c1/f88b3048a2c90014be1e8dfdf676ad2b2acd51cad668903ee4b2fbaf8a8b/GridDataFormats-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="93900219c9caf8cdce7e3e8e3cea98093cfb73ac09138ab8195466efc1a8e045", url="https://pypi.org/packages/c9/79/777d7b6d65f6a6e7481536b8ebec053e2e3d5357de1d76add04f347ac6d7/GridDataFormats-0.4.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.2:")
        depends_on("py-mrcfile", when="@0.7:")
        depends_on("py-numpy@1.21.0:", when="@1.0.2:")
        depends_on("py-numpy@1.19.0:", when="@1:1.0.1")
        depends_on("py-numpy@1.3:", when="@0.4:0")
        depends_on("py-scipy", when="@0.4.1:")
        depends_on("py-six", when="@0.4:0")

