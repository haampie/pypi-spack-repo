# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCiInfo(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.0", sha256="e9e05d262a6c48aa03cd904475de5ce8c4da8a5435e516631c795d0487dc9e07", url="https://pypi.org/packages/13/c3/8ac768b389d5b6dda1c3ce7992b3acd2b46401f9b71439123858b17b1a2c/ci_info-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="c59143d3aef96efcf46e6ec924275b3967eb9f6e922b1fbcb59bacc6bb77fc5c", url="https://pypi.org/packages/cf/01/664a10490000d7154fa71358af87681696b8116a12d869a267063c470fbc/ci_info-0.2.0-py3-none-any.whl")
    version("0.1.1", sha256="88374bc89c70d89c592daa8a7115d57b781003adda405cefc58a7c304f3c7784", url="https://pypi.org/packages/92/9f/52d2d07f26b1fbae553b5edacea126d3c28dec62112fe1a3e26abe9d4d9c/ci_info-0.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@:0.1")
    # END DEPENDENCIES

