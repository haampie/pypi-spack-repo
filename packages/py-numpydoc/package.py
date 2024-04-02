# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpydoc(PythonPackage):
    # BEGIN VERSIONS
    version("1.5.0", sha256="c997759fb6fc32662801cece76491eedbc0ec619b514932ffd2b270ae89c07f9", url="https://pypi.org/packages/c4/81/ad9b8837442ff451eca82515b41ac425f87acff7e2fc016fd1bda13fc01a/numpydoc-1.5.0-py3-none-any.whl")
    version("1.1.0", sha256="c53d6311190b9e3b9285bc979390ba0257ba9acde5eca1a7065fc8dfca9d46e8", url="https://pypi.org/packages/60/1d/9e398c53d6ae27d5ab312ddc16a9ffe1bee0dfdf1d6ec88c40b0ca97582e/numpydoc-1.1.0-py3-none-any.whl")
    version("0.6.0", sha256="974584a8293182ae995113ee2dce9f4be939c3f40c6c2daf11f9df33f961b5cb", url="https://pypi.org/packages/a9/22/e2069cf728e84dc0c7b80fc5021a4f878688e08f093a470ce4a1540cce45/numpydoc-0.6.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.2-rc1:1.5")
        depends_on("py-jinja2@2.10:", when="@1.2-rc1:1.2.0,1.3-rc1:")
        depends_on("py-jinja2@2.3:", when="@1:1.1")
        depends_on("py-sphinx@4.2:", when="@1.5")
        depends_on("py-sphinx@1.6.5:", when="@1:1.1")
    # END DEPENDENCIES

