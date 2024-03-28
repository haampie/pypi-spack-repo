# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrometheusFlaskExporter(PythonPackage):
    # BEGIN VERSIONS
    version("0.21.0", sha256="6dc4a010c299d1ed94b6151d91f129c4513fb8aa04310db00be4ccb0006de400", url="https://pypi.org/packages/55/fa/09ee59e31dca1b2d9db3e8a85e8cda7d7174af09b52dc8dd370bfb1aa535/prometheus_flask_exporter-0.21.0-py3-none-any.whl")
    version("0.18.2", sha256="fc487e385d95cb5efd045d6a315c4ecf68c42661e7bfde0526af75ed3c4f8c1b", url="https://pypi.org/packages/f3/c1/2cc385fadf18dc75fe24c18899269eda4dcc60221d61eff7da4a6cc5c01d/prometheus_flask_exporter-0.18.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flask", when="@0.18.3:")
        depends_on("py-prometheus-client", when="@0.18.3:")
    # END DEPENDENCIES

