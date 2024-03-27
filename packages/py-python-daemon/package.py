##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDaemon(PythonPackage):
    version("2.3.1", sha256="4e3bf67784c78aaa55ec001a2f832b464a54c5f9c89c11b311e2416a8c247431", url="https://pypi.org/packages/aa/b0/bc79d8ff019c2583d839e0143b1f91eafd4cfe92f86fb9d378a515dfb612/python_daemon-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="191c7b67b8f7aac58849abf54e19fe1957ef7290c914210455673028ad454989", url="https://pypi.org/packages/b1/cc/2ab0d910548de45eaaa50d0372387951d9005c356a44c6858db12dc6b2b7/python_daemon-2.3.0-py2.py3-none-any.whl")
    version("2.0.5", sha256="afde4fa433d94d007206ee31a0941d55b5eb232a5422b670aad628547b46bf68", url="https://pypi.org/packages/49/71/57f86781e77d4fe12e9ddfa0868954f8e4222d5f3a3def86b244ed5c30ee/python-daemon-2.0.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-docutils", when="@:0,2.2.1:")
        depends_on("py-lockfile@0.10:", when="@:0,2.2.1:")
        depends_on("py-setuptools", when="@:0,2.2.1:3.0.0")

