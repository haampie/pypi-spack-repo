##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBdbag(PythonPackage):
    version("1.6.3", sha256="3586002920ee552d4b23de025c05f9c2b8d01e9ef8a99ed1db0f7c391c320fe7", url="https://pypi.org/packages/dc/d6/71c569260ac1f98ed472bc26b8e52f59a711c82d67b89401b5a1a01937c6/bdbag-1.6.3-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-bagit@1.8.1:", when="@1.6:")
        depends_on("py-bagit-profile@1.3.1:", when="@1.6:")
        depends_on("py-certifi", when="@1.3:")
        depends_on("py-pytz", when="@1.3:")
        depends_on("py-requests@2.7:", when="@1.5:1.7.1")
        depends_on("py-setuptools-scm@:5", when="@1.6.1:")
        depends_on("py-tzlocal@2.1:2", when="@1.6")

