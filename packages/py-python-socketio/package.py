# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonSocketio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.4", sha256="b09f5ab6253f54f745a4a36ff29d2e15c2cd6cc07587c7e8e73d5410f30f50c8", url="https://pypi.org/packages/c7/30/9bb9747a78a8680deffeaf82d36e89db20452b72c0fddaf65574227832b9/python_socketio-1.8.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("eventlet", default=False, description="eventlet")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

