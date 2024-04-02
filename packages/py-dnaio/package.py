# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDnaio(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.0", sha256="d0528c23516fe4e947970bdef33c423f0a30ab3b083bd4f6f049fd66d8cef803", url="https://pypi.org/packages/5b/45/fe12f29d76add9e63290535f0397adc761ceea11e84f995d006b1cb911fe/dnaio-1.2.0.tar.gz")
    version("0.10.0", sha256="de51a50948f00b864297d74eddb588fbee5ac229855754e77564d18b24619d18", url="https://pypi.org/packages/ed/fc/d46a2dd24b238fbf4592a699b1250399ccb1bb8a516ee9c0fc9f30deae17/dnaio-0.10.0.tar.gz")
    version("0.9.1", sha256="a1a14181995b27197b7e2b8897994a3107c649b9fc2dfe263caff3c455b0d0c4", url="https://pypi.org/packages/9e/0e/43a7114773a69dec82167f696fb7518517991546b7e4e2a27c7762de3fa6/dnaio-0.9.1.tar.gz")
    version("0.4.2", sha256="fa55a45bfd5d9272409b714158fb3a7de5dceac1034a0af84502c7f503ee84f8", url="https://pypi.org/packages/be/46/4aebdff29822d98010b2b6b5b50f690e9a804cbd072787e2642b43e7f3f3/dnaio-0.4.2.tar.gz")
    version("0.3", sha256="47e4449affad0981978fe986684fc0d9c39736f05a157f6cf80e54dae0a92638", url="https://pypi.org/packages/1f/be/73d03ccdc8f721b938c5201d3031c676fa164fc6641f6d722160e5b63036/dnaio-0.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.8:")
        depends_on("py-xopen@1.4:", when="@1:")
        depends_on("py-xopen@0.8.2:", when="@0.4:0.4.2")
        depends_on("py-xopen", when="@0.2:0.3")
    # END DEPENDENCIES

