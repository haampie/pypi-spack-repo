##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenmim(PythonPackage):
    version("0.3.9", sha256="71581498b68767f8e1f340575b91c9994ccc93656901639f11300e46247da263", url="https://pypi.org/packages/00/b3/95531cee452028869d0e08974561f83e9c256c98f62c7a45a51893a61c54/openmim-0.3.9-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click", when="@0.2:")
        depends_on("py-colorama", when="@0.2:")
        depends_on("py-model-index", when="@0.2:")
        depends_on("py-opendatalab", when="@0.3.9:")
        depends_on("py-pandas", when="@0.2:")
        depends_on("py-pip@19.3:", when="@0.2:")
        depends_on("py-requests", when="@0.2:")
        depends_on("py-rich", when="@0.2:")
        depends_on("py-tabulate", when="@0.2:")

