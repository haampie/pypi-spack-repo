# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHumanize(PythonPackage):
    # BEGIN VERSIONS
    version("4.6.0", sha256="401201aca462749773f02920139f302450cb548b70489b9b4b92be39fe3c3c50", url="https://pypi.org/packages/22/2b/30e8725481b071ca53984742a443f944f9c74fb72f509a40b746912645e1/humanize-4.6.0-py3-none-any.whl")
    version("4.4.0", sha256="8830ebf2d65d0395c1bd4c79189ad71e023f277c2c7ae00f263124432e6f2ffa", url="https://pypi.org/packages/9d/fc/28d2b631c5220b2a594d5d13b6ad79ee60d50688f1cd43f6707c06fb0db4/humanize-4.4.0-py3-none-any.whl")
    version("4.0.0", sha256="8d86333b8557dacffd4dce1dbe09c81c189e2caf7bb17a970b2212f0f58f10f2", url="https://pypi.org/packages/89/8a/eea987b881522536af2a8fc008214a2bf1ac14b61ae483643165cedbbf35/humanize-4.0.0-py3-none-any.whl")
    version("3.12.0", sha256="4c71c4381f0209715cd993058e717c1b74d58ae2f8c6da7bdb59ab66473b9ab0", url="https://pypi.org/packages/fd/5e/9840102591431f86c2e99c5a8e4f18bb399f9f2e982b0dbba87c98ae800f/humanize-3.12.0-py3-none-any.whl")
    version("0.5.1", sha256="a43f57115831ac7c70de098e6ac46ac13be00d69abbf60bdcac251344785bb19", url="https://pypi.org/packages/8c/e0/e512e4ac6d091fc990bbe13f9e0378f34cf6eecd1c6c268c9e598dcf5bb9/humanize-0.5.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@3:3.12")
    # END DEPENDENCIES

