##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsFutures(PythonPackage):
    version("1.0.0", sha256="633804c773b960cef009efe2a5585483443c6eac3c39cc64beba2884013bcdd9", url="https://pypi.org/packages/63/9e/7b986554f6de56f1d43f9fdc410631009af6034027efa31f90867d264319/requests_futures-1.0.0-py2.py3-none-any.whl")
    version("0.9.7", sha256="a9ca2c3480b6fac29ec5de59c146742e2ab2b60f8c68581766094edb52ea7bad", url="https://pypi.org/packages/2c/f0/d9a6d4472286405956dd5ac6279fe932a86151df9816bc35afe601495819/requests-futures-0.9.7.tar.gz")

    with default_args(type="run"):
        depends_on("py-requests@1.2:", when="@1:")

