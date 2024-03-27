##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestAstropyHeader(PythonPackage):
    version("0.2.2", sha256="6088db080166d59f27c045247ad038ac8656f7c35d5c979cb87ed9a8f7efdee0", url="https://pypi.org/packages/10/db/3bde86b77504c01f8cc174ccce13029aa5e26daaae9fcdc08826f1f0c7a5/pytest_astropy_header-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="f90c75e0304c40527c282b8853a474e2b943cb81b07157212f9389e9d1ad1504", url="https://pypi.org/packages/e6/a3/a133dcefbfddb7a9f7c09cf2a39f73caa1585bb5d23d326f7cd18c01a802/pytest_astropy_header-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="49221f7799a2e665074902d7c9a5b8ddb5387de30db5a1a031951472cb6147fc", url="https://pypi.org/packages/54/cb/ef5a0f7e9119465cfd6dbfdaeac123e4ad81f168d127685a14beb7fd6f3f/pytest_astropy_header-0.2.0-py3-none-any.whl")
    version("0.1.2", sha256="e942726c0d61173e3b6722f65f811607371b3141a97f04c54f01f1e1b4402fef", url="https://pypi.org/packages/7a/26/2cd8eab76d9f1475068d9d3e6904967921244df11002abfbfc9630642ee9/pytest_astropy_header-0.1.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pytest@4.6:", when="@0.2:")
        depends_on("py-pytest@2.8:", when="@:0.1")

