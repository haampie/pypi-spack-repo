##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGsutil(PythonPackage):
    version("5.24", sha256="1f841645cda40fcc817e9ca84d285cdf541cc015fd38a5862017b085756729a0", url="https://pypi.org/packages/c3/c6/d8b3b7f71a8768b6a5471240aa114a513e3ebcb394baf081b76cf1ded862/gsutil-5.24.tar.gz")
    version("5.2", sha256="08857eedbd89c7c6d10176b14f94fb1168d5ef88f5b5b15b3e8a37e29302b79b", url="https://pypi.org/packages/6e/44/b54142efd7de9bdfcceaa9dac9dcd478ba4b77dba1f4ed4a16ffe131f1f5/gsutil-5.2.tar.gz")
    version("4.59", sha256="349e0e0b48c281659acec205917530ae57e2eb23db7220375f5add44688d3ddf", url="https://pypi.org/packages/04/32/268098abebab37c7eac8c2808acae37597b7a921abc5e3cd8baa6b1ae2fa/gsutil-4.59.tar.gz")


