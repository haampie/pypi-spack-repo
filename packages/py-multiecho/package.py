##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiecho(PythonPackage):
    version("0.29", sha256="5c1420907a8df1710701e80746a8a6361426af890e3ecd43ec23a7cec0985c11", url="https://pypi.org/packages/6e/09/e7584d968854e5c4977a423cb7de65db087647caed4d800c7e248b2e924e/multiecho-0.29-py3-none-any.whl")
    version("0.28", sha256="4e8f9507616053133bab97535ea4efa5a9b78e9c046280f684fd50cdd72160bb", url="https://pypi.org/packages/10/6e/2d42e6ebc5fcca1a4038342b64836ce22bd8f785a054b8d5365c0d823fb3/multiecho-0.28-py3-none-any.whl")
    version("0.25", sha256="58ed56b26270efb85b82651cbb32a644b9f7cdcb5cabfedb5973dd0ab44e16c2", url="https://pypi.org/packages/23/75/c860c93ffb68d160a4f52dc77fe7f8ce8db90a0aad0ba90a74d970feaa0f/multiecho-0.25-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-coloredlogs")
        depends_on("py-nibabel")
        depends_on("py-numpy")

