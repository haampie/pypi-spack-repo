# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAutomator(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="fb753e5bd40bfe720fa9e60e2ea5a1777b4c92082ffeba42b4055cdd56cb022d", url="https://pypi.org/packages/b0/c7/6f7231c6a560e95b6d32ad16712382229c7356497250f5f4dcd25079cbcf/pyobjc-framework-Automator-10.2.tar.gz")
    version("10.1", sha256="0e95fc90a2930d108d38b61b4365f3678edd5aa25d26598fe39924c890813e80", url="https://pypi.org/packages/e6/94/7323c54b937fc17fb0bdbc51423c76b76d1d945b8afd94e61f671d435b87/pyobjc-framework-Automator-10.1.tar.gz")
    version("10.0", sha256="261e36071f1a662f387bab48f711059e6e468ddd5054c0f2bae7af7e619a7aba", url="https://pypi.org/packages/52/e9/f4188382f2e60bd16b1657d840a27b0d7ae551497c7a0928f9266b2c421d/pyobjc_framework_Automator-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="f66b595cececdc0d6a911df9aed1c254ce8171381c643f4933966fd93f9d8d62", url="https://pypi.org/packages/e3/9f/bfa4a7d8360c295eac761c81bdd1ccf48489fc8e596e6e91fdc148b2af61/pyobjc_framework_Automator-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="284395b6b9e6b6183f0670f29f8b6d411b1e9ad482ae34405dae71bdcf6f3c46", url="https://pypi.org/packages/a1/33/5ede220388f81085838732f109168acc40b7cfc3864894f5b2a74d1c36a7/pyobjc_framework_Automator-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="8119cec8870fe661b62516a75336e315d5d5bbc50a1700ae624364a8a1506883", url="https://pypi.org/packages/69/bb/58b0c3fb3abcd8ae702e0c8bbec3e9de74d147480db79c394f5e9a9e9ed2/pyobjc_framework_Automator-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="d03bc0b92f5baede2eb35bde373774f708b9cfdf5fdde631d36e262eb5f63220", url="https://pypi.org/packages/e1/86/6eda972a255226ac4dfd9f2fb2a024bc22bed27ffe4f8aab33bde282c770/pyobjc_framework_Automator-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="2b783fc35b75cdef30b79eeab3799e45f23c40036949056abdde638769d7a4bf", url="https://pypi.org/packages/6f/28/7de2ba6007bbb8f4a12ba0159dc89213bc3eba97f0adeb224c80d3052d7d/pyobjc_framework_Automator-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="01eccedd465e2f57e91414968e6ce4e44f6cf3ced477b1787ba866d2de1cd0b7", url="https://pypi.org/packages/16/9e/6dcf9c24d5bb885c5246c44ed480393d2758e0dcd40379773131d4ab4cd8/pyobjc_framework_Automator-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="de6fb84837307e65710cd24d3f79adfe610784df2eb287ea4d40ebcd22c66523", url="https://pypi.org/packages/98/89/861783e6e471184a97a18c2d5bc85d637347b8f66cab2b02a3e6842a6232/pyobjc_framework_Automator-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

