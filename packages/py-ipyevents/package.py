# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpyevents(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.1", sha256="9f255fdab40e7598b1143ace90153c5f4e52be15dc6f1b94f575a043a5970c17", url="https://pypi.org/packages/45/9c/b2ae585af6f6b436df3924f45fada2a36e3a083cc4b01f50d9a291e0ca92/ipyevents-2.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipywidgets@7.6.0:", when="@0.9:")
    # END DEPENDENCIES

