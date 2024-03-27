##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHist(PythonPackage):
    version("2.7.2", sha256="089c8e1941999bcd9738beebfee2a665058c900c8c257a9667af594a6a3f1847", url="https://pypi.org/packages/b8/2a/96dabd3bb197ad289615f1c8852ce8a3a844d30feade1bb77b20a120c9a4/hist-2.7.2-py3-none-any.whl")
    version("2.7.1", sha256="11902fdd52a580e8cc5f2961e5428e1a3c3b3cf56d696954831d6eb7090b840e", url="https://pypi.org/packages/3a/8a/0ac9bff883dd88f04a16b25ff09653123cf0877f47d42d5021f2b53015a1/hist-2.7.1-py3-none-any.whl")
    version("2.7.0", sha256="1f060453e748d1a4f520e2a2597d129082a5040ef9489c6f531f8887c8d931cd", url="https://pypi.org/packages/25/0b/b515dba68493108b53f17210b914e9920de10a6b3f48c7b93d806ad92029/hist-2.7.0-py3-none-any.whl")
    version("2.6.3", sha256="0bc4798cfa4706c2007fe206eed622b1a7cf358cbd75421f398cf75f220315a9", url="https://pypi.org/packages/3f/15/67606c84dfd0c024a122b631b0c539a6e0f611977b18276447e5f62bbe97/hist-2.6.3-py3-none-any.whl")
    version("2.6.2", sha256="8028c34f8185429f2063bcd012a0cb0d228fe882cf43ab9269f06c63269db159", url="https://pypi.org/packages/31/e3/5be921ea90a20f26d163a9cda1cc5069e745f9a0b8124f71853f0ce145d0/hist-2.6.2-py3-none-any.whl")
    version("2.6.1", sha256="bde4936ffbef70ced93aedd69eb921c0d851ad00a152e41bf6b93c396c8f7aff", url="https://pypi.org/packages/09/72/541e00346028efdd6274c15bcc8ccb4f9ec8e8e8461117ef9539a93014e0/hist-2.6.1-py3-none-any.whl")
    version("2.6.0", sha256="adab433632beea77b390b4487f112e99a30a24d645ef510d2f0b9ede900a4727", url="https://pypi.org/packages/ce/ba/17c001c84d4fb519c95663e2f93dfdd7d787fa7dcac35eef8e382df069e3/hist-2.6.0-py3-none-any.whl")
    version("2.5.2", sha256="4d54c0b6afe62e6a1b4c8b7018b63085770b589aba4f887c02a1e49c3b4016d2", url="https://pypi.org/packages/77/90/091c1527c9fa3f6c653ba049fb7e0a197fc59b05bf84670c2c97252e199c/hist-2.5.2-py3-none-any.whl")
    version("2.5.1", sha256="c2d1d2bb3c2fc50b599386f97d31487e97d65cd5f1910bc5448ce04e0815fff0", url="https://pypi.org/packages/a5/70/b159d2a2bf385b791f0926ef7b9cbcacc486a023a9788450e148f573fb64/hist-2.5.1-py3-none-any.whl")
    version("2.5.0", sha256="f5b13473c93861b61b762683748a677242006500d3e37bac878d8c74dad4aed9", url="https://pypi.org/packages/a6/3a/e25e842513d6401f7552852580102a04448a5a57010390837b79c3006aa7/hist-2.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-boost-histogram@1.3.1:", when="@2.7.2:")
        depends_on("py-boost-histogram@1.3.1:1.3", when="@2.6:2.7.1")
        depends_on("py-boost-histogram@1.2", when="@2.5")
        depends_on("py-histoprint@2.2:", when="@2.5:")
        depends_on("py-more-itertools", when="@2.5:2.5.1 ^python@:3.9")
        depends_on("py-numpy@1.26:", when="@2.7.2: ^python@3.12:")
        depends_on("py-numpy@1.14.5:", when="@2.7.2: ^python@:3.11")
        depends_on("py-numpy@1.14.5:", when="@2.5:2.7.1")
        depends_on("py-scipy@1.4.0:", when="@2.0.0-alpha4:2.0.0-beta1")
        depends_on("py-typing-extensions@4:", when="@2.7: ^python@:3.10")
        depends_on("py-uncertainties@3:", when="@2:2.0.0-beta1")

