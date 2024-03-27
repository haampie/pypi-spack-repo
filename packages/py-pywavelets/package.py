##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPywavelets(PythonPackage):
    version("1.6.0-rc1", sha256="218223b63f571ece43bb7d3011a5b68039fee8e6a77562607b181f2671f04d30", url="https://pypi.org/packages/7b/cf/d4401b02e6b175bb6f654f0700d1aa4cdeada1843ec64ef2c939456e2d5a/pywavelets-1.6.0rc1.tar.gz")
    version("1.5.0", sha256="d9e25c7cabef7ccd53f5fead26ab22152fe4cb937bad7411b5d506e2b5de38f6", url="https://pypi.org/packages/ee/ce/cfce0d615746d9b9ccc698401599183d6edb6d1bb0ae234bd717a840711d/pywavelets-1.5.0.tar.gz")
    version("1.4.1", sha256="6437af3ddf083118c26d8f97ab43b0724b956c9f958e9ea788659f6a2834ba93", url="https://pypi.org/packages/6e/d4/008dceeb95fafcf141f39393bdfc10921d0b62a325c2794ac533195a1eb3/PyWavelets-1.4.1.tar.gz")
    version("1.4.0", sha256="8e22ec03e5727dbec1ed1771b92e26ac2b484a21b716776d6ee5183da76bd911", url="https://pypi.org/packages/48/ec/fe84e23bf150a473532937716ffc6c783b53337936e17b3bb1e2a3b42156/PyWavelets-1.4.0.tar.gz")
    version("1.3.0", sha256="cbaa9d62052d9daf8da765fc8e7c30c38ea2b8e9e1c18841913dfb4aec671ee5", url="https://pypi.org/packages/32/ab/b96b19cae562aecaa57f0cdb501be169a38ec685ddcc91f1de20f849b22e/PyWavelets-1.3.0.tar.gz")
    version("1.2.0", sha256="6cbd69b047bb4e00873097472133425f5f08a4e6bc8b3f0ae709274d4d5e9a8d", url="https://pypi.org/packages/35/e9/decd467448cde227aad94ff2976046afd3a51ad461ba9a325840687e8836/PyWavelets-1.2.0.tar.gz")
    version("1.1.1", sha256="1a64b40f6acb4ffbaccce0545d7fc641744f95351f62e4c6aaa40549326008c9", url="https://pypi.org/packages/17/6b/ef989cfb3acff2ea966c5f28a7443ccaec2ee136675dfa0366db2635f78a/PyWavelets-1.1.1.tar.gz")
    version("1.0.3", sha256="a12c7a6258c0015d2c75d88b87393ee015494551f049009e8b63eafed2d78efc", url="https://pypi.org/packages/86/0f/89c06eadc4d6003ff88ba365ff476be0f5a805d2e270b05cc863f2c01a4f/PyWavelets-1.0.3.tar.gz")
    version("1.0.2", sha256="0cbee5363e805a11effa982f533a203b21a602cd058efcb49304cc081b17ac9d", url="https://pypi.org/packages/b8/bd/8f25dae2d4b30f2253858a098edb0c3c3a2b12451173e9aa00e15e8e060f/PyWavelets-1.0.2.tar.gz")
    version("1.0.1", sha256="3c5cece36d4e17d395be6e9ac6b80ce7b774a1f71c251756c6163e63b6d878dc", url="https://pypi.org/packages/b4/42/074c6adcd1586926650d8365bcc3e1ab42f81a68c620c4242aa9297b01d9/PyWavelets-1.0.1.tar.gz")
    version("0.5.2", sha256="ce36e2f0648ea1781490b09515363f1f64446b0eac524603e5db5e180113bed9", url="https://pypi.org/packages/4b/df/3fff2a8b96ef7df6e4e8642fb7569c3717ae562dd76afe0f96525c0af784/PyWavelets-0.5.2.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.5:")
        depends_on("py-numpy@1.22.4:", when="@1.6:")
        depends_on("py-numpy@1.22.4:1", when="@1.5")
        depends_on("py-numpy@1.13.3:", when="@1.1")
        depends_on("py-numpy@1.9.1:", when="@1:1.0")

