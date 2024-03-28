# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyElasticTransport(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.13.0", sha256="aec890afdddd057762b27ff3553b0be8fa4673ec1a4fd922dfbd00325874bb3d", url="https://pypi.org/packages/aa/2f/7606c450a4ba07cd8ba818845ea2dca880a76fad5536f6d038289713a619/elastic_transport-8.13.0-py3-none-any.whl")
    version("8.12.0", sha256="87d9dc9dee64a05235e7624ed7e6ab6e5ca16619aa7a6d22e853273b9f1cfbee", url="https://pypi.org/packages/d6/35/94475b9a18eec053ebce144ff1e28c175772ce82244ada6ffc10b1a65bcc/elastic_transport-8.12.0-py3-none-any.whl")
    version("8.11.0", sha256="dfb5d8a0cb649c159ebf4d9b1f55b7c8d00bb65687c53060b54cc9b2a7c84344", url="https://pypi.org/packages/10/9c/81a65ce8e6a03b415a0b424f63525dd96d49153b6b77dfb19d480522029a/elastic_transport-8.11.0-py3-none-any.whl")
    version("8.10.0", sha256="e73ac3c7ad4e9209436207143d797d3f6b62a399a34d2729e069e44c9ea2cadc", url="https://pypi.org/packages/45/e3/e1bc11677b89030c4ffbf464177b64c533df85cde655e3ecc66bda99b3e5/elastic_transport-8.10.0-py3-none-any.whl")
    version("8.4.1", sha256="c718ce40e8217b6045604961463c10da69a152dda07af4e25b3feae8d7965fc0", url="https://pypi.org/packages/7e/1c/13bb1826382a1275e9191e9ab5cac3c59247f49c4b4dd96b131ec123d9ff/elastic_transport-8.4.1-py3-none-any.whl")
    version("8.4.0", sha256="19db271ab79c9f70f8c43f8f5b5111408781a6176b54ab2e54d713b6d9ceb815", url="https://pypi.org/packages/bd/3b/a2f4a4f1f7578ceaff490961753a75984efc17c17b1f6f59c3a866debeca/elastic_transport-8.4.0-py3-none-any.whl")
    version("8.1.2", sha256="10914d0c5c268d9dcfee02cfbef861382d098309ba4eedab820062841bd214b3", url="https://pypi.org/packages/40/a3/c1c3bae86ec32ae417bc08e915f4ad62cae9a1c9303402465b8fd1453959/elastic_transport-8.1.2-py3-none-any.whl")
    version("8.1.1", sha256="2ee1ec56ccfad1354a36056fa942af726510fffba46b267292ba7d584a1bd406", url="https://pypi.org/packages/af/e2/68f089f5eec623ecbae35c74be92270ac12cd3239b2d16e0bb7185821270/elastic_transport-8.1.1-py3-none-any.whl")
    version("8.1.0", sha256="0bb2ae3d13348e9e4587ca1f17cd813a528a7cc07f879505f56d69c81823b660", url="https://pypi.org/packages/d4/df/7ec7f9ee8f0768bc42846e03a98aefd93b0ed4dffb51db0ab80e206ed5ce/elastic_transport-8.1.0-py3-none-any.whl")
    version("8.0.1", sha256="ae2800ac5abd03f91fe951b8b20e6c315d69cec10aeac9898bb5229e3dbeb3b0", url="https://pypi.org/packages/56/a9/89d2d94f544f36c92702d5c63dd9b03e7ee0c95d6c65b7d45291683a1996/elastic_transport-8.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-certifi", when="@0.1:0,7:")
        depends_on("py-urllib3@1.26.2:", when="@8.10:")
        depends_on("py-urllib3@1.26.2:1", when="@8:8.4")
    # END DEPENDENCIES

