# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMdanalysistests(PythonPackage):
    # BEGIN VERSIONS
    version("2.7.0", sha256="326d65d7f14da8d1b047aab87ca312a68459a5fd18ddf6d8cb9ac9c3ca51d9e5", url="https://pypi.org/packages/db/b6/2437074f21e0ecf1cb00f86331784fb1b525795bfa4c8e8024da23774f61/MDAnalysisTests-2.7.0.tar.gz")
    version("2.6.1", sha256="043f7451f4d9c42ea9e6609a81a6002948e2c74fd268282e0831416789b22e5e", url="https://pypi.org/packages/63/81/ffe48b43bb5a6d307ead256dd28802bc45ee629e24a03051eb82edc3d84e/MDAnalysisTests-2.6.1.tar.gz")
    version("2.6.0", sha256="16fdd10e5240b606e8f9210b7cbd9e4be110e6b8d79bb6e72ce6250c4731a817", url="https://pypi.org/packages/bb/fb/cada869fc9ba3198ffdced0ab7547804ce01697bc53f6939894fffa4cef2/MDAnalysisTests-2.6.0.tar.gz")
    version("2.5.0", sha256="a15b53b7f8bed67900a2bf542bbb3cab81dc71674fa6cddb3248dd11880e4c9d", url="https://pypi.org/packages/19/cf/88c013b519e9959dfb8a999b2e028b7171bd81c6a8714be219d3548b115d/MDAnalysisTests-2.5.0.tar.gz")
    version("2.4.3", sha256="6fbdeccdbfb249f76520ee3605d007cd70292187e3754d0184c71e5afe133abb", url="https://pypi.org/packages/3e/05/5f4d1d5ddef2b366a22ea46ffb9657fead0c7351ccff6754d786e98048ad/MDAnalysisTests-2.4.3.tar.gz")
    version("2.4.2", sha256="6e8fb210a4268691c77717ea5157e82d85874a4f7ee0f8f177718451a44ee793", url="https://pypi.org/packages/a4/37/d4bc68f0972bffac071ec6a2d04a57016ccaab67d2f4b5125a5a915f09da/MDAnalysisTests-2.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.5:")
        depends_on("python@3.8:", when="@2.2:2.4")
        depends_on("py-hypothesis", when="@2.7:")
        depends_on("py-mdanalysis@2.7:", when="@2.7:")
        depends_on("py-pytest@3.3:", when="@2.7:")
    # END DEPENDENCIES

