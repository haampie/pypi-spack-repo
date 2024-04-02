# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTestinfra(PythonPackage):
    # BEGIN VERSIONS
    version("1.18.0", sha256="4a0a70355b007729d78446c86bffd80bcea4ffe9adc9571f9c9779476c49153d", url="https://pypi.org/packages/ed/46/54039e4611bd887c642cc9772e067f87fabed48324b461a6ffe07a6ccafa/testinfra-1.18.0.tar.gz")
    version("1.13.0", sha256="f3ae25ad77150021975671e87dfec34538823f8d563326165fa876a07c53e820", url="https://pypi.org/packages/c3/4d/55915550958066a98e6eb7b228082e5c9579660d3e70b3843eda0326d96d/testinfra-1.13.0-py2.py3-none-any.whl")
    version("1.12.0", sha256="56877ab52fbeeac97cb311662c7ed7403210f2db941bbeb2df004aacf522435a", url="https://pypi.org/packages/c4/75/b81c05e5b859944c9f373463e271cafbd14096187a2c9709fb2f0d62d283/testinfra-1.12.0-py2.py3-none-any.whl")
    version("1.11.1", sha256="a4ed92a797ce18ff3fd8141b5cd4dee82bb75c642855acfab22b9e3d62f1b071", url="https://pypi.org/packages/45/2c/8f241662a2fdc63412578ea2de074315fe2259d50f0b29956922dad41c39/testinfra-1.11.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@:3.0.1,3.0.3:", when="@:1.17,2.1:5")
        depends_on("py-six@1.4:", when="@:1.17,2.1:3")
    # END DEPENDENCIES

