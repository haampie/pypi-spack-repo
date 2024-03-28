# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrame(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.5.3", sha256="612c22c94cc221590297cf5e0b231c5b48cc8d453682d814529a5fe99016ae9a", url="https://pypi.org/packages/e5/aa/37e9ba76b5b0d564bf7738936dae572d39fe32ec3a6c6cb96fbc3a567b3a/trame-3.5.3-py3-none-any.whl")
    version("3.5.2", sha256="40a7c7568566e2dc1100d954a4e54a44dfb26005a5975771da9a18c9df213897", url="https://pypi.org/packages/57/7f/f3e334e3a50b6d8934e37e05f9865b3d1433a6ae9ed44a78db9e58c10893/trame-3.5.2-py3-none-any.whl")
    version("3.5.1", sha256="ccf7945c98939d58c6c75fc5651980b8778f252b63ceb09d07601dfe59fb0f78", url="https://pypi.org/packages/a1/56/fe4fa0c66efa6b6d47932d2997646585b6f6c1cddf93b0962177e6eefb4e/trame-3.5.1-py3-none-any.whl")
    version("3.5.0", sha256="7788e967b98e2aec5fa0b685ac5cd13d3b1e5721c229ac864f99089dadb3212f", url="https://pypi.org/packages/ad/05/02e3c8857436af4b47514f193bf24dfe8ca45351498fd3461bb9c66902eb/trame-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="d98bb04cbf5076818a5f44f6e4dba955d924a959440657b68e483e2e6a1dc7aa", url="https://pypi.org/packages/fd/9e/733c874e40a5ff18148fe77b77d9d00d35fbdd0c26b77f7c7877658976c0/trame-3.4.0-py3-none-any.whl")
    version("3.3.0", sha256="95b8848618bf8c19b4796b59a8bdf84c8e0ffecefbdd01ca0147a9d63cc61710", url="https://pypi.org/packages/13/f3/b7188e2066e2ff5a648f4ca6ebfe50687607e5a8427c29e330298a1c0953/trame-3.3.0-py3-none-any.whl")
    version("3.2.8", sha256="285b8e4428fe3e3be052f48169270cd186611f584e6abc97fad122aa16b74964", url="https://pypi.org/packages/12/c1/ce32bf13da5127c7fa8b72443b157a835f0079b3c19d7d2017a77a2d58ab/trame-3.2.8-py3-none-any.whl")
    version("3.2.7", sha256="c0ff819b23ec1fc9ed6149397c99ff031182116b1451b9de5f8105dea164e185", url="https://pypi.org/packages/e6/98/7be96178d2b223c8e9712e1772e63319712eec3971eb8c53f4022d91d17b/trame-3.2.7-py3-none-any.whl")
    version("3.2.6", sha256="83fffe9cff31250dca91ccda4c5fae0e9972ffa614011299594e5b099f7a5b7c", url="https://pypi.org/packages/e7/bb/9d54c14299c03a974ac9aa96455e7b0c480cfc17a15baaa7d29871861f8f/trame-3.2.6-py3-none-any.whl")
    version("3.2.5", sha256="01eb44e1e05b7c51bcac07e6ca373242044746c75b9053cd63e2d6ba63eda18c", url="https://pypi.org/packages/22/3a/61080c25a5ce021781791387d39ce01d6fc4750fb5c7faab52d7d1339896/trame-3.2.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client@2.14:", when="@3.4:")
        depends_on("py-trame-client@2.12:", when="@3.2.7:3.3")
        depends_on("py-trame-client@2.10:", when="@3:3.2.6")
        depends_on("py-trame-server@2.13.1:", when="@3.4:")
        depends_on("py-trame-server@2.12:", when="@3.2.7:3.3")
        depends_on("py-trame-server@2.11.7:", when="@2.5.2:3.2.6")
    # END DEPENDENCIES

