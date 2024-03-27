##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStorm(PythonPackage):
    version("0.25", sha256="ec7cc8897638f94f6b75c6a2af74aa9b31f5492d7a2f9482c08a8dd7b46adb14", url="https://pypi.org/packages/c0/f6/4b30697087af83edbc25584938fff7de08645ea6c2addf22420b4a1c70c9/storm-0.25.tar.gz")
    version("0.23", sha256="01c59f1c898fb9891333abd65519ba2dd5f68623ac8e67b54932e99ce52593d3", url="https://pypi.org/packages/ec/88/5dfdcb5948606487da14b8423daf71a861f598a3f823e870e8cf2bf2e5e9/storm-0.23.tar.bz2")


