# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenmim(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.9", sha256="71581498b68767f8e1f340575b91c9994ccc93656901639f11300e46247da263", url="https://pypi.org/packages/00/b3/95531cee452028869d0e08974561f83e9c256c98f62c7a45a51893a61c54/openmim-0.3.9-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click")
        depends_on("py-colorama")
        depends_on("py-model-index")
        depends_on("py-opendatalab", when="@0.3.9:")
        depends_on("py-pandas")
        depends_on("py-pip@19.3:")
        depends_on("py-requests")
        depends_on("py-rich")
        depends_on("py-tabulate")
    # END DEPENDENCIES

