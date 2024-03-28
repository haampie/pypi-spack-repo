# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleReauth(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.1", sha256="cb39074488d74c8853074dde47368bbf8f739d4a4338b89aab696c895b6d8368", url="https://pypi.org/packages/69/e1/67ffaa3a645b86318ce30717af7145070ebccec5eef5c623ae08b86129b8/google_reauth-0.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyu2f")
    # END DEPENDENCIES

