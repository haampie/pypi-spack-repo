##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPulsarGalaxyLib(PythonPackage):
    version("0.14.16", sha256="4a5de778d3444471148eea2b3ef7c4d7b05c5af72273a6a26022c5aa87440487", url="https://pypi.org/packages/a2/bf/ab741655a2e519441267347f4e4b5f0a5f825589d27de4a198c7606319dc/pulsar_galaxy_lib-0.14.16-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-paramiko", when="@0.12:0.13.0,0.14:")
        depends_on("py-paste", when="@:0.7.0.0,0.8:0.13.0,0.14.0.dev:0.14.0")
        depends_on("py-pastedeploy", when="@0.12:0.13.0,0.14:")
        depends_on("py-pastescript", when="@:0.7.0.0,0.8:0.13.0,0.14.0.dev:0.14.0")
        depends_on("py-psutil", when="@:0.7.0.0,0.8:0.13.0,0.14:")
        depends_on("py-pyyaml", when="@:0.7.0.0,0.8:0.13.0,0.14:")
        depends_on("py-typing-extensions", when="@0.14.14:0.14,0.15.0.dev:")
        depends_on("py-webob", when="@:0.7.0.0,0.8:0.13.0,0.14:")

