##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFury(PythonPackage):
    version("0.7.1", sha256="02f09bcc78261136b2264a32df641ee3f71456d73578bc5dfdcf9deab3931e25", url="https://pypi.org/packages/2d/90/2012ea88843452a5848fe700ff1fca2bd8eb6efa27e88666a712751ac144/fury-0.7.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy@1.7.1:", when="@:0.8")
        depends_on("py-pillow@5.4.1:", when="@0.5:")
        depends_on("py-scipy@0.9:", when="@:0.8")
        depends_on("py-vtk@8.1.2:8,9.0.1:", when="@0.6:0.7")

