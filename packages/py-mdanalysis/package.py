# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMdanalysis(PythonPackage):
    # BEGIN VERSIONS
    version("2.7.0", sha256="572e82945e5d058e3749ec5f18e6b3831ef7f2119cb54672567ae9a977201e93", url="https://pypi.org/packages/3e/67/c4ec984d4648c2435717fe8f35c54f22d6375eb0383060f8ebc21587bd13/MDAnalysis-2.7.0.tar.gz")
    version("2.6.1", sha256="9cc69b94bddd026f26ffcaf5bdbed6d568c1c10e19a341d84f8d37a2a70222f2", url="https://pypi.org/packages/c0/2a/ac39b12836ef0d27937b4765d8e17b09b94f7de9092d4cf657dd336f2663/MDAnalysis-2.6.1.tar.gz")
    version("2.6.0", sha256="210b198a115165004c36fbbbe5eb83a13323f52b10ccaef30dd40bfe25ba3e61", url="https://pypi.org/packages/b8/1b/12f34fc28e41c12d05f299012fed63cedf2d733057ca5ea7ef1854efb027/MDAnalysis-2.6.0.tar.gz")
    version("2.5.0", sha256="06ce4efab6ca1dbd2ee2959fc668049e1d574a8fe94ab948a4608244da1d016b", url="https://pypi.org/packages/a8/49/d03958061c86cbb2d2c8aa4019fd7cb575f5fd49988f6df69e957c64a28f/MDAnalysis-2.5.0.tar.gz")
    version("2.4.3", sha256="c4fbdc414e4fdda69052fff2a6e412180fe6fa90a42c24793beee04123648c92", url="https://pypi.org/packages/6b/21/c8e7b9655e7819e6e12fd45b35175a13b73262626aefa0a2d1c6766708bc/MDAnalysis-2.4.3.tar.gz")
    version("2.4.2", sha256="ae2ee5627391e73f74eaa3c547af3ec6ab8b040d27dedffe3a7ece8e0cd27636", url="https://pypi.org/packages/7d/6b/f0ea2ab44ed0a2448737d779e02d3ae719c186dc9e3ce4cd0d75b4026dcc/MDAnalysis-2.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("analysis", default=False, description="analysis")
    variant("extra_formats", default=False, description="extra_formats")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.5:")
        depends_on("python@3.8:", when="@2.2:2.4")
        depends_on("py-biopython@1.80:", when="@2.7:+analysis")
        depends_on("py-fasteners", when="@2.7:")
        depends_on("py-griddataformats@0.4:", when="@2.7:")
        depends_on("py-joblib@0.12:", when="@2.7:")
        depends_on("py-matplotlib@1.5.1:", when="@2.7:")
        depends_on("py-mda-xdrlib", when="@2.7:")
        depends_on("py-mmtf-python@1:", when="@2.7:")
        depends_on("py-networkx@2:", when="@2.7:+analysis")
        depends_on("py-numpy@1.22.3:1", when="@2.7:")
        depends_on("py-packaging", when="@2.7:")
        depends_on("py-scikit-learn", when="@2.7:+analysis")
        depends_on("py-scipy@1.5.0:", when="@2.7:")
        depends_on("py-seaborn", when="@2.7:+analysis")
        depends_on("py-threadpoolctl", when="@2.7:")
        depends_on("py-tidynamics@1:", when="@2.7:+analysis")
        depends_on("py-tqdm@4.43:", when="@2.7:")
    # END DEPENDENCIES

