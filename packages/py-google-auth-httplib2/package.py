##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleAuthHttplib2(PythonPackage):
    version("0.2.0", sha256="b65a0a2123300dd71281a7bf6e64d65a0759287df52729bdd1ae2e47dc311a3d", url="https://pypi.org/packages/be/8a/fe34d2f3f9470a27b01c9e76226965863f153d5fbe276f83608562e49c04/google_auth_httplib2-0.2.0-py2.py3-none-any.whl")
    version("0.1.1", sha256="42c50900b8e4dcdf8222364d1f0efe32b8421fb6ed72f2613f12f75cc933478c", url="https://pypi.org/packages/d3/3d/e4991229886c0d522d9552151a43ff7adcc61e026e60ce8bd508387f84cf/google_auth_httplib2-0.1.1-py2.py3-none-any.whl")
    version("0.1.0", sha256="31e49c36c6b5643b57e82617cb3e021e3e1d2df9da63af67252c02fa9c1f4a10", url="https://pypi.org/packages/ba/db/721e2f3f32339080153995d16e46edc3a7657251f167ddcb9327e632783b/google_auth_httplib2-0.1.0-py2.py3-none-any.whl")
    version("0.0.4", sha256="aeaff501738b289717fac1980db9711d77908a6c227f60e4aa1923410b43e2ee", url="https://pypi.org/packages/bd/4e/992849016f8b0c27fb604aafd0a7a724db16128906197bd1245c6f18e6a1/google_auth_httplib2-0.0.4-py2.py3-none-any.whl")
    version("0.0.3", sha256="f1c437842155680cf9918df9bc51c1182fda41feef88c34004bd1978c8157e08", url="https://pypi.org/packages/33/49/c814d6d438b823441552198f096fcd0377fd6c88714dbed34f1d3c8c4389/google_auth_httplib2-0.0.3-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-auth")
        depends_on("py-httplib2@0.19:", when="@0.1.1:")
        depends_on("py-httplib2@0.15:", when="@0.1:0.1.0")
        depends_on("py-httplib2@0.9.1:", when="@0.0.3:0.0")
        depends_on("py-six", when="@0.0.4:0.1.0")

