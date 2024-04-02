# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydantic(PythonPackage):
    # BEGIN VERSIONS
    version("1.10.5", sha256="9e337ac83686645a46db0e825acceea8e02fca4062483f40e9ae178e8bd1103a", url="https://pypi.org/packages/28/59/5d2fc3499d9ce8ce48ee7e00f043d5cc429a9198bd96c3512809428ade15/pydantic-1.10.5.tar.gz")
    version("1.10.2", sha256="91b8e218852ef6007c2b98cd861601c6a09f1aa32bbbb74fab5b1c33d4a1e410", url="https://pypi.org/packages/7d/7d/58dd62f792b002fa28cce4e83cb90f4359809e6d12db86eedf26a752895c/pydantic-1.10.2.tar.gz")
    version("1.9.2", sha256="8cb0bc509bfb71305d7a59d00163d5f9fc4530f0881ea32c74ff4f74c85f3d3d", url="https://pypi.org/packages/fd/8f/3f7e88b507dbdfec8f1f914294aa8831edffb03d668799c65b4b46331c8a/pydantic-1.9.2.tar.gz")
    version("1.8.2", sha256="26464e57ccaafe72b7ad156fdaa4e9b9ef051f69e175dbbb463283000c05ab7b", url="https://pypi.org/packages/b9/d2/12a808613937a6b98cd50d6467352f01322dc0d8ca9fb5b94441625d6684/pydantic-1.8.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dotenv", default=False, description="dotenv")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.10:2.5")
    # END DEPENDENCIES

