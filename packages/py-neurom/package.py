# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNeurom(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.4", sha256="a584e0979b54deee906dd716ea90de20773e20b527d83960d0fe655b0905eb4a", url="https://pypi.org/packages/88/b8/6b89a524f2e13f16ccaed9306088a31fdb1d48756d66aff376e4c91032d4/neurom-3.2.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("plotly", default=False, description="plotly")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@3.2.4:")
    # END DEPENDENCIES

