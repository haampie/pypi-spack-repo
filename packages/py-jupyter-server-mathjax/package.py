# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterServerMathjax(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.6", sha256="416389dde2010df46d5fbbb7adb087a5607111070af65a1445391040f2babb5e", url="https://pypi.org/packages/7d/77/6a98cc88f1061c0206b427b602efb6fcb9bc369e958aee11676d5cfc4412/jupyter_server_mathjax-0.2.6-py3-none-any.whl")
    version("0.2.3", sha256="740de2ed0d370f1856faddfaf8c09a6d7435d09d3672f24826451467b268969d", url="https://pypi.org/packages/e8/8c/3affa05f2c648fb74abdfde877781308a7b27dc5d56d7cf439c34cbfed5f/jupyter_server_mathjax-0.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jupyter-server@1.1:", when="@0.2.6:")
        depends_on("py-jupyter-server@1.1:1", when="@:0.2.5")
    # END DEPENDENCIES

