# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyspark(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.1", sha256="e99fa7de92be406884bfd831c32b9306a3a99de44cfc39a2eefb6ed07445d5fa", url="https://pypi.org/packages/d1/48/cc321e742a93320c681b3c7a9fd405d518c6326c89da3d67e35b9868e941/pyspark-3.3.1.tar.gz")
    version("3.3.0", sha256="7ebe8e9505647b4d124d5a82fca60dfd3891021cf8ad6c5ec88777eeece92cf7", url="https://pypi.org/packages/b8/01/b2393cee7f6180d9150274e92c8bdc1c81220e2ad7554ee5febca1866899/pyspark-3.3.0.tar.gz")
    version("3.2.1", sha256="0b81359262ec6e9ac78c353344e7de026027d140c6def949ff0d80ab70f89a54", url="https://pypi.org/packages/f4/65/41eb22b7b4623d9f4560526cc456cb6425770c098a9dff6763111c4455cc/pyspark-3.2.1.tar.gz")
    version("3.1.3", sha256="39ac641ef5559a3d1286154779fc990316e9934520853615ae4785c1af52d14b", url="https://pypi.org/packages/c0/87/b1ebdce4cd29459787a35d32eda8fb200302ac534c1348f9348496336c04/pyspark-3.1.3.tar.gz")
    version("3.1.2", sha256="5e25ebb18756e9715f4d26848cc7e558035025da74b4fc325a0ebc05ff538e65", url="https://pypi.org/packages/89/db/e18cfd78e408de957821ec5ca56de1250645b05f8523d169803d8df35a64/pyspark-3.1.2.tar.gz")
    version("3.0.1", sha256="38b485d3634a86c9a2923c39c8f08f003fdd0e0a3d7f07114b2fb4392ce60479", url="https://pypi.org/packages/f0/26/198fc8c0b98580f617cb03cb298c6056587b8f0447e20fa40c5b634ced77/pyspark-3.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.3:3.4")
    # END DEPENDENCIES

