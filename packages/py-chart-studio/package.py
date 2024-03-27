##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyChartStudio(PythonPackage):
    version("1.1.0", sha256="fd183185d6e6d31c642567145c1a862f941ca9c7695aac8b2f3ebbcbcea31a7a", url="https://pypi.org/packages/ca/ce/330794a6b6ca4b9182c38fc69dd2a9cbff60fd49421cb8648ee5fee352dc/chart_studio-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="7dcd66ccdba81ca54025cfcb76e0e68ed9922f474adc45848542f186567f60da", url="https://pypi.org/packages/b9/3f/d2f3f506ba1aaf109f549f8b01d1483cd3e324c5ebe6b206acee66efdf46/chart_studio-1.0.0-py3-none-any.whl")
    version("1.0.0-rc1", sha256="db249382bc864bedc50dedb4044a7cf9fc8e2d0bd2fd28b297e0eb4542738e35", url="https://pypi.org/packages/39/3d/ef446f576cbd876f4896a7ad60b8eb7959cb7ccd0f99204af87fdee33ccd/chart_studio-1.0.0rc1-py3-none-any.whl")
    version("1.0.0-alpha5", sha256="f77999428f7df6670863836a18d4fc90f0ca9730a48696b225c5541bec0dc9fe", url="https://pypi.org/packages/d0/aa/687ba28a8288a97475e8305b626b0fcafaf36cee4d404c78c973568f5338/chart_studio-1.0.0a5-py3-none-any.whl")
    version("1.0.0-alpha4", sha256="092619cd8ab22981b6042d4ff3c9d00fa547e16df94fc8a69fb47341a32bf0e4", url="https://pypi.org/packages/7b/19/87b93ab042937036e5bc3fae86b07ef5d6e51c7d6043fefd759dc86ad024/chart_studio-1.0.0a4-py3-none-any.whl")
    version("1.0.0-alpha3", sha256="59c8895300090d97dfeda45a99461423cb77125618f5d95ed36d8db0d9918747", url="https://pypi.org/packages/ba/1f/69680bef1928a8314bb63aa8f9a20a5c1afece2d343d88af97f9d7f0c24f/chart_studio-1.0.0a3-py3-none-any.whl")
    version("1.0.0-alpha2", sha256="2fb0a9a1557694fab2f6e8698bca4392c71dde0da5318c5522890bc81a2795cf", url="https://pypi.org/packages/91/d9/290bcbeab55be4cf7237780eab864ccf242ec309230c78c5e2135e67d1b7/chart_studio-1.0.0a2-py3-none-any.whl")
    version("1.0.0-alpha1", sha256="62271a1a272353208adcda4ae9ff756401daea5fd4121722fe11789d27c62e99", url="https://pypi.org/packages/58/06/253c821af68ef2e63ca2aa37c58ff2e41cd85a703625ffe8a30d2af68c39/chart_studio-1.0.0a1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-plotly", when="@:1.0.0-alpha1,1.0.0-alpha3:")
        depends_on("py-requests", when="@:1.0.0-alpha1,1.0.0-alpha3:")
        depends_on("py-retrying@1.3.3:", when="@:1.0.0-alpha1,1.0.0-alpha3:")
        depends_on("py-six", when="@:1.0.0-alpha1,1.0.0-alpha3:")

