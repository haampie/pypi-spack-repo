##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonPptx(PythonPackage):
    version("0.6.23", sha256="dd0527194627a2b7cc05f3ba23ecaa2d9a0d5ac9b6193a28ed1b7a716f4217d4", url="https://pypi.org/packages/72/49/6eee83072983473e9905ffddd5c2032b9a0ca4616425560d6d582287b467/python_pptx-0.6.23-py3-none-any.whl")
    version("0.6.21", sha256="7798a2aaf89563565b3c7120c0acfe9aff775db0db3580544e3bf4840c2e378f", url="https://pypi.org/packages/eb/c3/bd8f2316a790291ef5aa5225c740fa60e2cf754376e90cb1a44fde056830/python-pptx-0.6.21.tar.gz")

    with default_args(type="run"):
        depends_on("py-lxml@3.1.0:", when="@0.6.22:")
        depends_on("py-pillow@3.3.2:", when="@0.6.23:")
        depends_on("py-xlsxwriter@0.5.7:", when="@0.6.22:")

