# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterlabServer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.25.4", sha256="eb645ecc8f9b24bac5decc7803b6d5363250e16ec5af814e516bc2c54dd88081", url="https://pypi.org/packages/6a/2c/ea4fdd7d4bb72106419fff1fcda7c111bd905b00afed3d8efc1a6d6e4538/jupyterlab_server-2.25.4-py3-none-any.whl")
    version("2.25.3", sha256="c48862519fded9b418c71645d85a49b2f0ec50d032ba8316738e9276046088c1", url="https://pypi.org/packages/ab/ac/a19c579bb8ab2a2aefcf47cd3787683e6e136378d7ab2602be3b8e628030/jupyterlab_server-2.25.3-py3-none-any.whl")
    version("2.25.2", sha256="5b1798c9cc6a44f65c757de9f97fc06fc3d42535afbf47d2ace5e964ab447aaf", url="https://pypi.org/packages/a2/97/abbbe35fc67b6f9423309988f2e411f7cb117b08321866d3d8b720f4c0d4/jupyterlab_server-2.25.2-py3-none-any.whl")
    version("2.25.1", sha256="dce9714d91fb3e53d2b37d0e0619fa26ed223c8e7b8c81cca112926de19b53a4", url="https://pypi.org/packages/de/86/9484f35ea09efc3f8b90e58398e9b9783b9e7e9ee5b24fbb41f5e465d7a2/jupyterlab_server-2.25.1-py3-none-any.whl")
    version("2.25.0", sha256="c9f67a98b295c5dee87f41551b0558374e45d449f3edca153dd722140630dcb2", url="https://pypi.org/packages/96/cd/cdabe44549d60e0967904f0bdd9e3756b521112317612a3997eb2fda9181/jupyterlab_server-2.25.0-py3-none-any.whl")
    version("2.24.0", sha256="5f077e142bb8dc9b843d960f940c513581bceca3793a0d80f9c67d9522c4e876", url="https://pypi.org/packages/a7/0d/6d4eab0391bd4df1c43f308368d5e177b0fa8ac632267222a23b71317091/jupyterlab_server-2.24.0-py3-none-any.whl")
    version("2.23.0", sha256="a5ea2c839336a8ba7c38c8e7b2f24cedf919f0d439f4d2e606d9322013a95788", url="https://pypi.org/packages/cb/14/8f1c4b9b80db855d48a762e248efd41649d102841b6bfadbd26b8c25e054/jupyterlab_server-2.23.0-py3-none-any.whl")
    version("2.22.1", sha256="1c8eb55c7cd70a50a51fef42a7b4e26ef2f7fc48728f0290604bd89b1dd156e6", url="https://pypi.org/packages/ad/31/cfb84feb3803c1e0e69dbe6928ab9251b9a1548b9092a5013413c0dd49f8/jupyterlab_server-2.22.1-py3-none-any.whl")
    version("2.22.0", sha256="f4a7263ada89958854631a64bed45285caeac482925233159709f643c5871490", url="https://pypi.org/packages/32/49/53a9cb7b27fd1aad65b3f0be5744c6d358945b4ed4fa3342c8a441b57bbc/jupyterlab_server-2.22.0-py3-none-any.whl")
    version("2.21.0", sha256="ff1e7a81deb2dcb433215d469000988590fd5a5733574aa2698d643a6c9b3ace", url="https://pypi.org/packages/a0/e3/1af3f5be602852d7abe46b80b86d915e907fca6a308e44e6b6e848b92f00/jupyterlab_server-2.21.0-py3-none-any.whl")
    version("2.10.3", sha256="62f3c598f1d48dfb9b27729ed17772e38115cbe61e7d60fe68a853791bdf1038", url="https://pypi.org/packages/cb/22/308fdf317ed12c7f8e6081797bcccc53de3c7a34d89cbf975069194f7c41/jupyterlab_server-2.10.3-py3-none-any.whl")
    version("2.6.0", sha256="10ca364e764a6ca1e387530dfe5a09dc8fd563f1739b2b7b5a49e8cf5c4140ee", url="https://pypi.org/packages/01/c4/461a38d71c5c9c756d8adf2e3acd6fd133512fae2bc22779c09e5b287149/jupyterlab_server-2.6.0-py3-none-any.whl")
    version("1.3.0-rc0", sha256="a9647d3cf3eca4b27be782014f6ab0dcc22274543ac0d17ade07ba85c84046b4", url="https://pypi.org/packages/29/1d/cf7bd1e0aee9f72fb9616eccfa55ddc54135ee29aaefd9acd26ef8f78160/jupyterlab_server-1.3.0rc0-py3-none-any.whl")
    version("1.2.0", sha256="55d256077bf13e5bc9e8fbd5aac51bef82f6315111cec6b712b9a5ededbba924", url="https://pypi.org/packages/b4/eb/560043dcd8376328f8b98869efed66ef68307278406ab99c7f63a34d4ae2/jupyterlab_server-1.2.0-py3-none-any.whl")
    version("1.1.5", sha256="ee62690778c90b07a62a9bc5e6f530eebe8cd7550a0ef0bd1363b1f2380e1797", url="https://pypi.org/packages/e9/7b/08d35a18a6aa02203b9c58a370fdc82619d312039394cbc5ccd1434dff3f/jupyterlab_server-1.1.5-py3-none-any.whl")
    version("1.1.0", sha256="6aeaa1133069ec8d109f474b628059da2ec2e73f4e448c89e56821e6cfc26c0f", url="https://pypi.org/packages/74/bc/e87bb9dc5d20b6af9efa9551e5cb4e02bbd5bd100484e35acfa60a9bbba0/jupyterlab_server-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-babel@2.10:", when="@2.16.4:")
        depends_on("py-babel", when="@1.3:2.16.3")
        depends_on("py-entrypoints@0.2.2:", when="@2.7:2.12")
        depends_on("py-importlib-metadata@4.8.3:", when="@2.16.0: ^python@:3.9")
        depends_on("py-jinja2@3.0.3:", when="@2.11:")
        depends_on("py-jinja2@2.10:", when="@1.0.5:2.10")
        depends_on("py-json5@0.9:", when="@2.16.4:")
        depends_on("py-json5", when="@1.0.0:2.16.3")
        depends_on("py-jsonschema@4.18.0:", when="@2.25:")
        depends_on("py-jsonschema@4.17.3:", when="@2.17:2.24")
        depends_on("py-jsonschema@3.0.1:", when="@0.3.4:2.16")
        depends_on("py-jupyter-server@1.21:", when="@2.16.5:")
        depends_on("py-jupyter-server@1.4:1", when="@2.3:2.10")
        depends_on("py-notebook@4.2.0:", when="@:0.3.2,0.3.4:2.0.0-alpha0")
        depends_on("py-packaging@21.3:", when="@2.16.4:")
        depends_on("py-packaging", when="@1.3:2.16.3")
        depends_on("py-requests@2.31:", when="@2.25:")
        depends_on("py-requests@2.28:", when="@2.16.4:2.24")
        depends_on("py-requests", when="@1.1:2.16.3")
    # END DEPENDENCIES

