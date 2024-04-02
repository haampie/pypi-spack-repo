# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWandb(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.9", sha256="b8752e5287aca9f8192eca7be352882975973cd3cd0c88815930498fd357569d", url="https://pypi.org/packages/a3/b4/279ec12c6c481d0f672e9cf89fbdf7e57f5aacaf23493c699e1c00671ce0/wandb-0.13.9-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs@1.4.3:", when="@0.13.8:")
        depends_on("py-click@7:8.0.0-rc1,8.0.1:", when="@:0.15.4")
        depends_on("py-dataclasses", when="@:0.15.9 ^python@:3.6")
        depends_on("py-docker-pycreds@0.4:")
        depends_on("py-gitpython@1:", when="@:0.13.10")
        depends_on("py-pathtools", when="@:0.16.0-beta1")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=windows")
        depends_on("py-protobuf@3.12.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=linux ^python@:3.8")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=linux ^python@3.9:")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=freebsd")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=darwin")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=cray")
        depends_on("py-psutil@5:")
        depends_on("py-pyyaml")
        depends_on("py-requests@2:")
        depends_on("py-sentry-sdk@1:")
        depends_on("py-setproctitle")
        depends_on("py-setuptools")
        depends_on("py-typing-extensions", when="@0.13.8: ^python@:3.9")
    # END DEPENDENCIES

