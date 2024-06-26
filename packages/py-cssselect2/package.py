# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCssselect2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="fd23a65bfd444595913f02fc71f6b286c29261e354c41d722ca7a261a49b5969", url="https://pypi.org/packages/9d/3a/e39436efe51894243ff145a37c4f9a030839b97779ebcc4f13b3ba21c54e/cssselect2-0.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.5:")
        depends_on("py-tinycss2", when="@0.2.2:0.2,0.4:")
        depends_on("py-webencodings", when="@0.4:")
    # END DEPENDENCIES

