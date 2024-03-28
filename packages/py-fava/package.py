# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFava(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.18", sha256="592540cc0f531c4092760497304f05d708305b2b7b9093661c10ee4d760565b1", url="https://pypi.org/packages/0f/f4/81799aadb7be4f2d6d987c969df563989211ed6a12bba6f7e1d2bbbca6ff/fava-1.18-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-babel@2.6:", when="@1.8:1.18")
        depends_on("py-beancount@2.3:", when="@1.16:1.18")
        depends_on("py-cheroot", when="@1.8:1.18")
        depends_on("py-click", when="@1.6:1.18")
        depends_on("py-flask@0.10.1:", when="@1.6:1.18")
        depends_on("py-flask-babel@1:", when="@1.14:1.18")
        depends_on("py-jinja2@2.10:", when="@1.7:1.18")
        depends_on("py-markdown2@2.3:", when="@1.6:1.18")
        depends_on("py-ply", when="@1.7:")
        depends_on("py-simplejson@3.2:", when="@1.15:1.18")
        depends_on("py-werkzeug@0.15:", when="@1.12:1.18")
    # END DEPENDENCIES

