# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWxpython(PythonPackage):
    # BEGIN VERSIONS
    version("4.1.1", sha256="00e5e3180ac7f2852f342ad341d57c44e7e4326de0b550b9a5c4a8361b6c3528", url="https://pypi.org/packages/b0/4d/80d65c37ee60a479d338d27a2895fb15bbba27a3e6bb5b6d72bb28246e99/wxPython-4.1.1.tar.gz")
    version("4.0.6", sha256="35cc8ae9dd5246e2c9861bb796026bbcb9fb083e4d49650f776622171ecdab37", url="https://pypi.org/packages/9a/a1/9c081e04798eb134b63def3db121a6e4436e1d84e76692503deef8e75423/wxPython-4.0.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@4.0.5:4.1.0")
        depends_on("py-pillow", when="@4.0.4:4.1.0")
        depends_on("py-six", when="@:4.0.0-alpha3,4.0.0-beta2:4.1.0")
    # END DEPENDENCIES

