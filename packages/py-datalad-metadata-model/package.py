# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladMetadataModel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.10", sha256="13c186aebfd5f9367850eb54e63bf4f21fbd80d72b951949c072d7411469ab95", url="https://pypi.org/packages/9d/69/e1ae4839a98b880b6ee28fd9cd01db62dfa316748cca392e7908425312ab/datalad_metadata_model-0.3.10-py3-none-any.whl")
    version("0.3.5", sha256="b550e16508b6d21bbc7a3c6a28fb0b470799361a46aafbd28f6a152503b5fc15", url="https://pypi.org/packages/0e/b8/0f87fdb1f1b37ecec1367e337d3c70ed351a7ef4e48295bf66ecbae2280e/datalad_metadata_model-0.3.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs", when="@0.1.0-rc3:")
        depends_on("py-click", when="@0.1.0-rc3:")
        depends_on("py-fasteners", when="@0.1.0-rc3:")
    # END DEPENDENCIES

