# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMneQtBrowser(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.2", sha256="dd143462cfa2d9088a26b4b469fd398e0d2216761bdff1387eb920920a9e4e19", url="https://pypi.org/packages/23/31/26975ad8b0433448aefd4bbdf5bbde5f59e4e3f29c869c4464c0e9903429/mne_qt_browser-0.6.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.6.2:")
        depends_on("py-colorspacious")
        depends_on("py-darkdetect", when="@0.3:")
        depends_on("py-matplotlib")
        depends_on("py-mne@1:", when="@0.5:")
        depends_on("py-numpy")
        depends_on("py-packaging", when="@0.5:")
        depends_on("py-pyopengl", when="platform=darwin")
        depends_on("py-pyqtgraph@0.12.3:")
        depends_on("py-qdarkstyle", when="@0.3:")
        depends_on("py-qtpy")
        depends_on("py-scipy")
        depends_on("py-scooby")
    # END DEPENDENCIES

