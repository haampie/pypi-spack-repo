# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonPicard(PythonPackage):
    # BEGIN VERSIONS
    version("0.7", sha256="52643e2d644d9317559da3f3a26eb3661bbd813dd7a7061d39f7084618c8c938", url="https://pypi.org/packages/5f/eb/9de3b1ad3712700abb702b6ea6590caeeab1bc3bda08d31785121bde159f/python_picard-0.7-py3-none-any.whl")
    version("0.6", sha256="26c7928f7aba69011f1236bf35388a420088018350e840d2608031c5f338e0f7", url="https://pypi.org/packages/c6/39/23ee91bfcf542a0554dd69991f6a695102322e631174e6e65d309c17b370/python_picard-0.6-py3-none-any.whl")
    version("0.4", sha256="e2b961f6a5c9494a0240a1a7ed995fc3a8260ffbb2bf47f81d9ae4e7f64e5548", url="https://pypi.org/packages/dd/c9/3b3c717ccf9e2525e38edb8ab583e2262ee6f06d0873c2bee08ebfb2a5bb/python_picard-0.4-py3-none-any.whl")
    version("0.3", sha256="f5b1fbdcca358b6c15ff978a87727bb98f97777d20a79dc9aff7a9d84df81fb3", url="https://pypi.org/packages/2e/08/2c22d1702a3aa4f84ec8f816c006b4c8dd16fdb04c06c4ffd56c1f97c8d5/python-picard-0.3.tar.gz")
    version("0.2", sha256="fbf87cfc6d4c8d8ac94e29e59e8fad108d24c48f969293bd1f017616f16fd4db", url="https://pypi.org/packages/09/01/2cf99b6ef821906de248355341d7b6e1d422eaaeb1b85a7cbdf04cac4a1a/python-picard-0.2.tar.gz")
    version("0.1", sha256="610da7e0a26e01012f66a67ce3936ab72df2d80767233e0f7d59c397d94bbd47", url="https://pypi.org/packages/30/07/e91164102728302d0450f9b3f312f3a6060c727abd0696bf35c01f24cb23/python-picard-0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numexpr", when="@0.4:")
        depends_on("py-numpy", when="@0.6:")
        depends_on("py-scikit-learn", when="@0.7:")
        depends_on("py-scipy", when="@0.7:")
    # END DEPENDENCIES

