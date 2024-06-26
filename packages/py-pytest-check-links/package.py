# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestCheckLinks(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.4", sha256="df548424e052ef2aee081f62e2fbc4883de5e5ad7bf28d6b3aa8e41d93c2635f", url="https://pypi.org/packages/e6/1e/e02d0ee404c7050a7c4aea26a1813c47e4d47085fcdf8025a70c8344d5aa/pytest_check_links-0.3.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils", when="@0.3:0.4.2,0.4.3.dev:0.4.3,0.5:0")
        depends_on("py-html5lib", when="@:0.4.2,0.4.3.dev:0.4.3,0.5:0")
        depends_on("py-nbconvert", when="@:0.4.2,0.4.3.dev:0.4.3,0.5:0")
        depends_on("py-nbformat", when="@:0.4.2,0.4.3.dev:0.4.3,0.5:0")
        depends_on("py-pytest@2.8:", when="@:0.4.2")
        depends_on("py-six", when="@:0.3")
    # END DEPENDENCIES

