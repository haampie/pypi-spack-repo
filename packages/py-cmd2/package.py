# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmd2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.3", sha256="f1988ff2fff0ed812a2d25218a081b0fa0108d45b48ba2a9272bb98091b654e6", url="https://pypi.org/packages/f3/9a/495a0577cbae4a11dc0b2a2174688f0bab83d1b81245a105f1613a365828/cmd2-2.4.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@16.3:")
        depends_on("py-importlib-metadata@1.6:", when="^python@:3.7")
        depends_on("py-pyperclip@1.6:")
        depends_on("py-pyreadline3", when="@2.4: platform=windows")
        depends_on("py-typing-extensions", when="^python@:3.7")
        depends_on("py-wcwidth@0.1.7:")
    # END DEPENDENCIES

