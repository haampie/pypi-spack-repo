##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMonai(PythonPackage):
    version("1.3.0", sha256="6ac93decd6aff4c8272eb095e01c8a734bede07246a952cec3c9e2df5b116267", url="https://pypi.org/packages/08/94/e8a7ba00dd0c7ce959648b562043bd22125d65f5e519e566c822f71bc437/monai-1.3.0-202310121228-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-nibabel", when="@:0.1")
        depends_on("py-numpy@1.20.0:", when="@1.2:")
        depends_on("py-pillow", when="@:0.1")
        depends_on("py-tensorboard", when="@:0.1")
        depends_on("py-torch@1.9:", when="@1.2.0-rc3:")

