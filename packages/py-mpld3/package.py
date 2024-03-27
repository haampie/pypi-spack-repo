##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMpld3(PythonPackage):
    version("0.5.8", sha256="41938e65de4ba41a1b53d92e7c8609e7172e09b33ef5db42bb6f73701106c8b7", url="https://pypi.org/packages/5f/fc/08fdadba29ebd37a402dd27048a7222a48075e281989a7a122fa1dcab065/mpld3-0.5.8-py3-none-any.whl")
    version("0.5.5", sha256="b080f3535238a71024c0158280ab4f6091717c45347c41c907012f8dd6da1bd5", url="https://pypi.org/packages/73/7b/01d3b2977cdc0127c04a04c8f52effa76a47be9ccf400bb10629b1bdc806/mpld3-0.5.5.tar.gz")
    version("0.3", sha256="4d455884a211bf99b37ecc760759435c7bb6a5955de47d8daf4967e301878ab7", url="https://pypi.org/packages/91/95/a52d3a83d0a29ba0d6898f6727e9858fe7a43f6c2ce81a5fe7e05f0f4912/mpld3-0.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-jinja2", when="@0.5.6:")
        depends_on("py-matplotlib", when="@0.5.6:")

