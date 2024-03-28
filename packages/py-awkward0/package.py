# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwkward0(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.15.5", sha256="5fdaa3b29ea2426665215478b9b9199e991da5ab1f1f2996dcbfe848e08a40a1", url="https://pypi.org/packages/9a/b3/376b258ea021eed2c9bdaa1011e0f7b25365157de472d9fae8a2443d9ff5/awkward0-0.15.5-py3-none-any.whl")
    version("0.15.4", sha256="7361d7ac412d1941d892acc673a600c852eae88ab88eda57a7ee3ef538fac7cb", url="https://pypi.org/packages/34/6f/89d805d71d5eead248684dd0ce397ea12a35c33faf6d241fba3428af847b/awkward0-0.15.4-py3-none-any.whl")
    version("0.15.3", sha256="77dfd4c624f6f44b5dff49485629291ff0abd9944d114471decbd046b7778dfd", url="https://pypi.org/packages/9f/2a/bea4f48fe068163dae7c086d7c16a88a56264acd6ac66a0c737d90840ecb/awkward0-0.15.3-py3-none-any.whl")
    version("0.15.2", sha256="25b2985bc8f5a8a02478dd62d529d30f5cee202b22f1c8b7ad2d13e4b0eca5c1", url="https://pypi.org/packages/93/74/90e008f7082103fe15e90f7b3de5226053baa9f360ef1cce2eb2184e5c98/awkward0-0.15.2-py3-none-any.whl")
    version("0.15.1", sha256="e04386b9ad0d221ec2e2e7a8bff32466a9aaff902f26c7abbe40d3c3108ef0e2", url="https://pypi.org/packages/10/72/a328a530a892a689f62f14ab73889cf161a02c7f2665910e0e9c21ca737a/awkward0-0.15.1-py3-none-any.whl")
    version("0.15.0", sha256="91b1d8709f3d2ceafd150d727e2592f07ba45fe3ff9ece079469d5a1210c8be4", url="https://pypi.org/packages/ba/4a/50228527482e6bdf3177334561f376d065682ee60d80e57a380c810be2c9/awkward0-0.15.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.13.1:")
    # END DEPENDENCIES

