# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCurrentscape(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.12", sha256="b1bef26352f240d09e413d312deb06d212afe158de85c9dcae96e371968d1d9c", url="https://pypi.org/packages/dd/de/423d92aff7c18e418672db238a379e0f7b5379508daeb1854996916ac371/currentscape-1.0.12-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-palettable")
    # END DEPENDENCIES

