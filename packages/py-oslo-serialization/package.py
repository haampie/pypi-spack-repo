# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsloSerialization(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.0", sha256="a0acf0ff7ca88b3ee6514713571f614b5c20870005ed0eb90408fa7f9f3edb60", url="https://pypi.org/packages/a4/99/d02844a4ddd063dab89b8b9cfd176081ef9e60a5b57fa89cd3a62a406195/oslo.serialization-4.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msgpack@0.5.2:", when="@2.27:")
        depends_on("py-oslo-utils@3.33:", when="@2.23:")
        depends_on("py-pbr@2:2.0,3:", when="@2.19:")
        depends_on("py-pytz@2013.6:", when="@5.4: ^python@:3.8")
        depends_on("py-pytz@2013.6:", when="@1.3:5.3")
    # END DEPENDENCIES

