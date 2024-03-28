# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZfit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.17.0", sha256="981b66e50026f2910038c182a8550b991ea7ccf5d880213745433bed39be5c71", url="https://pypi.org/packages/c3/73/fb062991a372f9529a900b525a878b5f0e0bd4e84826c3b3d40106d56e41/zfit-0.17.0-py2.py3-none-any.whl")
    version("0.16.0", sha256="da77356fe95d7f05ef7b3a4ca3afe6611cd31860381d0ce31563bf6a45fd13ff", url="https://pypi.org/packages/22/b6/318484a2d3e5c8969195d452f5d97bd57b65510451f629dfec50af736a53/zfit-0.16.0-py2.py3-none-any.whl")
    version("0.15.5", sha256="00a1138429e8a7f830c9e229b9c0bcd6071b95dadd8c87eb81191079fb679225", url="https://pypi.org/packages/02/36/f044510c1610b88c967d26c77f762b6e23baeb7eb711ae35fed2c0737130/zfit-0.15.5-py2.py3-none-any.whl")
    version("0.14.1", sha256="66d1e349403f1d6c6350138d0f2b422046bcbdfb34fd95453dadae29a8b0c98a", url="https://pypi.org/packages/90/14/a920033e2f27880a0520856e71d4a4e11e7e1e014398832f3ec946b35fcc/zfit-0.14.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("hs3", default=False)
    variant("nlopt", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:3.11", when="@0.18:")
        depends_on("python@:3.11", when="@0.14:0.17")
        depends_on("python@:3.10", when="@0.13")
        depends_on("python@:3.9", when="@0.7:0.9")
        depends_on("python@:3.8", when="@0.6")
        depends_on("py-asdf", when="@0.13:+hs3")
        depends_on("py-attrs", when="@0.15.2:0.18.0,0.18.2:")
        depends_on("py-boost-histogram", when="@0.9:")
        depends_on("py-colorama", when="@0.5:")
        depends_on("py-colored", when="@0.5:")
        depends_on("py-colorlog")
        depends_on("py-deprecated", when="@0.9:")
        depends_on("py-dill", when="@0.13:")
        depends_on("py-dotmap", when="@0.6:")
        depends_on("py-frozendict", when="@0.13:")
        depends_on("py-hist", when="@0.9:")
        depends_on("py-iminuit@2.3:", when="@0.6:0.11,0.14.1:")
        depends_on("py-jacobi", when="@0.11:")
        depends_on("py-nlopt@2.7.1:", when="@0.10:+nlopt")
        depends_on("py-numdifftools", when="@0.4:")
        depends_on("py-numpy@1.16.0:", when="@0.4:")
        depends_on("py-ordered-set", when="@0.3.7:")
        depends_on("py-pandas")
        depends_on("py-pydantic@:1", when="@0.14.1:")
        depends_on("py-pyyaml", when="@0.13:")
        depends_on("py-scipy@1.2.0:")
        depends_on("py-tabulate", when="@0.5:")
        depends_on("py-tensorflow@2.13.0:2.13", when="@0.15:0.17")
        depends_on("py-tensorflow-probability@0.21", when="@0.17")
        depends_on("py-tensorflow-probability@0.20:0.21", when="@0.15:0.16")
        depends_on("py-tensorflow-probability@0.20", when="@0.14")
        depends_on("py-texttable")
        depends_on("py-typing-extensions", when="@0.14:0.17 ^python@:3.8")
        depends_on("py-typing-extensions", when="@0.13")
        depends_on("py-uhi", when="@0.9.0-alpha3:")
        depends_on("py-uproot@4.0.0:", when="@0.13:")
        depends_on("py-xxhash", when="@0.10:")
        depends_on("py-zfit-interface", when="@0.9:")

        # marker: sys_platform != "darwin" or platform_machine != "arm64"
        # depends_on("py-tensorflow@2.12.0:2.12", when="@0.14")

        # marker: sys_platform == "darwin" and platform_machine == "arm64"
        # depends_on("py-tensorflow-macos@2.11:2.12", when="@0.14")
    # END DEPENDENCIES

