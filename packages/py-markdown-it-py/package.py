# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkdownItPy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.0", sha256="355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", url="https://pypi.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl")
    version("2.2.0", sha256="5a35f8d1870171d9acc47b99612dc146129b631baf04970128b568f190d0cc30", url="https://pypi.org/packages/bf/25/2d88e8feee8e055d015343f9b86e370a1ccbec546f2865c98397aaef24af/markdown_it_py-2.2.0-py3-none-any.whl")
    version("1.1.0", sha256="98080fc0bc34c4f2bcf0846a096a9429acbd9d5d8e67ed34026c03c61c464389", url="https://pypi.org/packages/08/6b/33c40781e26c76e26825528f417f5414c501807f1f7fced82119c29aa832/markdown_it_py-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("linkify", default=False)
    variant("plugins", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19:21", when="@1.1:2.0")
        depends_on("py-linkify-it-py@1:", when="@2.2:+linkify")
        depends_on("py-linkify-it-py@1", when="@0.5.8:2.1+linkify")
        depends_on("py-mdit-py-plugins", when="@1.0.0-beta2:+plugins")
        depends_on("py-mdurl@0.1:", when="@2:")
    # END DEPENDENCIES

