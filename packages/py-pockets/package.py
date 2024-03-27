##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPockets(PythonPackage):
    version("0.9.1", sha256="68597934193c08a08eb2bf6a1d85593f627c22f9b065cc727a4f03f669d96d86", url="https://pypi.org/packages/e9/2f/a4583c70fbd8cd04910e2884bcc2bdd670e884061f7b4d70bc13e632a993/pockets-0.9.1-py2.py3-none-any.whl")
    version("0.9", sha256="e5cafcd5cce265c2571fe8340167a09f842aa2f824b65b2818101b16fd3046fc", url="https://pypi.org/packages/b9/86/853ae2152be1787c6030c85258bfc9797e202419be060ae712716aef6b4a/pockets-0.9-py2.py3-none-any.whl")
    version("0.8", sha256="e55b1f704cf1506d0246660b3425d2b7ac52349a286d709b19a2c1748570f3a6", url="https://pypi.org/packages/aa/61/c9ee2712d2650da33d7b9c184fec4f88b5bd56a6dfc4ec19fdcda2b86231/pockets-0.8-py2.py3-none-any.whl")
    version("0.7.2", sha256="21a2405543c439ac091453ed187f558cf5294d3f85f15310f214ad4de057e0af", url="https://pypi.org/packages/eb/63/9e52ca9bdfe83ba0297be1cdc714ec420fe59aa55ab96bb6c39325df6ba5/pockets-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="9f94e2160679da739872170afadc8431480a71e7d94996b39c67470e0e7a2e08", url="https://pypi.org/packages/8f/e1/65090542cf45c7fa96b56bddf480b29b8c88e2479fb009624a589cd9ab93/pockets-0.7.1-py2.py3-none-any.whl")
    version("0.7", sha256="ae6e0908907b5b79bc21e06d472aca403aa88c1a7128a5d3cca33bdfaf76c326", url="https://pypi.org/packages/ec/38/32fa34b6d222db3db3e8e206251b5b55ead643bd7ca4ceb651d3b29bdfc6/pockets-0.7-py2.py3-none-any.whl")
    version("0.6.8", sha256="827b46239633e5493830add7694ce73ffdaed23c0202dfbc74d002ba6d5ee2ed", url="https://pypi.org/packages/35/f6/683cb479144ff57019a2942c7b5f72187c6247a77a807b042942a2828e64/pockets-0.6.8-py2.py3-none-any.whl")
    version("0.6.7", sha256="aea5debbeb6eda3ebd364f4218f5329dde3d047a9de9e98a3070c541406c24da", url="https://pypi.org/packages/1e/58/a41214ac3cb331369ce6177f844d0caa4592bf50be6a81ed61f887fa476c/pockets-0.6.7-py2.py3-none-any.whl")
    version("0.6.6", sha256="cd74918c9bfdcb665ff39bf70f25825d0c3110e7bcdb6b1a5eaf913113613596", url="https://pypi.org/packages/be/e9/a6f9b54135402c54ce79715b09f779925702edd413e75e7f51556f11763e/pockets-0.6.6-py2.py3-none-any.whl")
    version("0.6.5", sha256="790d102593c151cf86f0119a631cd532c4f8ee06960879b72c39a2f214185c4b", url="https://pypi.org/packages/e8/62/6b9a535a8dbd0853dafd3a4a9960e08b9183eb17aab945e6b4d8d2e57d40/pockets-0.6.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six@1.5.2:", when="@0.3.1:")

