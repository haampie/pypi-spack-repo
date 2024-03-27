##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnndata(PythonPackage):
    version("0.10.6", sha256="2c625149472fab4430f402208e7bf1efa6a7d45fa5c14827c8122305f4dca206", url="https://pypi.org/packages/9a/02/49ea1209f0604a57f71749531c745d20fbd10ccb3683f8b0bb9806ad3e45/anndata-0.10.6-py3-none-any.whl")
    version("0.10.5.post1", sha256="3be9d5863d60d7a72d57a6e0392a3e7f3bb2bbfc79a038ddc53192a41517f5fc", url="https://pypi.org/packages/42/c7/23c2b5d3dd764650d235b574fdcac8d7252e6ae2f90273f65e95b9ca4e34/anndata-0.10.5.post1-py3-none-any.whl")
    version("0.10.5", sha256="fbcf934a3e99e7dda89b1d48f36f675504ea2e65ab4408daa9526bc305c14ebd", url="https://pypi.org/packages/f8/33/b0250f6b841d6c53f8b089697dfffcca44bbb2f76d7859bf17ea723506b0/anndata-0.10.5-py3-none-any.whl")
    version("0.10.4", sha256="a2561b734dcf0f4a93ab67e3c8b3c8b288815a9fcba7c7096ded92b84cee68ba", url="https://pypi.org/packages/24/d4/9f819dfdcf8aa0e8be1a042a9ef923ad31960182ace937627a00a295d7e2/anndata-0.10.4-py3-none-any.whl")
    version("0.10.3", sha256="ec27c203c4d2f0b3a92fb9ca21692ac6022f71dd3fbc3e32d8c54cae59b5f7d8", url="https://pypi.org/packages/8a/87/201514af3bf08db52e11b7d94e6129f0a75503194b81614ff48883101c4c/anndata-0.10.3-py3-none-any.whl")
    version("0.10.2", sha256="2a1724a89f7c8132b19ba78bc15c4abb31059897256aa0f1aca334b802587cd2", url="https://pypi.org/packages/d9/99/eec250f471ac193380d45148231ca2a01f31e72018be6ca85839ac99053b/anndata-0.10.2-py3-none-any.whl")
    version("0.10.1", sha256="6daa5dfd003328fda44dec077c4c7f008dc9d252eb3c91da6a1ec7fdc42d1d0c", url="https://pypi.org/packages/de/00/92e332708619832624f48e72d23d6c57aa53c79a02685e085d8e04f878f4/anndata-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="14e512b2865f1adf0b07e8988fc6dd1db2d8a0a9330f7ef405f3ed1ce071141f", url="https://pypi.org/packages/c5/cf/67fb3a8dab49a4b845b10597b4dfd5521bbb0a8c3a5777ead3541c1991b5/anndata-0.10.0-py3-none-any.whl")
    version("0.9.2", sha256="badab44bf0b4d598ae49403ee634a6ffc8896d9aa21db52f0f6af98d6fe1fceb", url="https://pypi.org/packages/a7/ee/767a05c299d95b438ef9c8ab6dbc15896cfb9121cf4327fe1da160a45343/anndata-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="6666a39f9d6c4645a70115f38c17ccc2e2ffd9c0d08a1636c395253d73de26f1", url="https://pypi.org/packages/ef/3a/4611e83c2bfca85518535aad65efb15f68c2c7c0831054b3011e6fb9a90d/anndata-0.9.1-py3-none-any.whl")
    version("0.8.0", sha256="2a929360c3c893370865e8ee3d3b9d95ee93239da91bafc5bf5f3c306796746e", url="https://pypi.org/packages/46/7f/ffe1546142d98ed55e7bb70eaedad92861d8e2ab07398ef7f06f4f46d06d/anndata-0.8.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.10:")
        depends_on("py-array-api-compat@1.4.1:1.4,1.5.1:", when="@0.10.6:")
        depends_on("py-array-api-compat", when="@0.10:0.10.5")
        depends_on("py-exceptiongroup", when="@0.10: ^python@:3.10")
        depends_on("py-h5py@3.1:", when="@0.10.6:")
        depends_on("py-h5py@3.0.0:", when="@0.8:0.10.5")
        depends_on("py-natsort", when="@0.5:0.5.1,0.6.1:0.6.4,0.6.15,0.6.18,0.6.22-rc1,0.7-rc1,0.7:")
        depends_on("py-numpy@1.23.0:", when="@0.10.6:")
        depends_on("py-numpy@1.16.5:", when="@0.7.6:0.10.5")
        depends_on("py-packaging@20:", when="@0.7.6:")
        depends_on("py-pandas@1.4.0:2.0,2.1.0:2.1.1,2.1.3:", when="@0.10.6:")
        depends_on("py-pandas@1.1.1:2.0,2.1.0:2.1.1,2.1.3:", when="@0.10.3:0.10.5")
        depends_on("py-pandas@1.1.1:2.0,2.1.0:", when="@0.10:0.10.2")
        depends_on("py-pandas@1.1.1:2.0.0,2.0.2:", when="@0.9.2:0.9")
        depends_on("py-pandas@1.1.1:", when="@0.7.6:0.9.1")
        depends_on("py-scipy@1.8.1:", when="@0.10.6:")
        depends_on("py-scipy@1.4.1:", when="@0.7.6:0.10.5")

