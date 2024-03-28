# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCwlUpgrader(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.11", sha256="435b706b7ccc64c6b0af6785a0cebbdfa285af9e70f321dc7b43b363ba9b385c", url="https://pypi.org/packages/00/38/ced647e8885c87d4f378ca80b9112373288fd200932293deb46fc6f5a2e5/cwl_upgrader-1.2.11-py3-none-any.whl")
    version("1.2.10", sha256="0946ffd5b338d0ec738d8b1a2d2de2f797cc34b4b3c09c6b164eb42ea1423e2b", url="https://pypi.org/packages/34/05/fa0cc60e8e8c07b952eebc98ff056b3c245b8d3027356dfffc0cb6f99670/cwl_upgrader-1.2.10-py3-none-any.whl")
    version("1.2.9", sha256="191b202fb039a964d4d3885570b3864f409cdf063d84ebaac5d7bd8810e6eefe", url="https://pypi.org/packages/88/94/58a972dd0cda3055ecf3051a121c322904da286991c5a02332ff9e2d93c0/cwl_upgrader-1.2.9-py3-none-any.whl")
    version("1.2.8", sha256="b953460294677e7c18c610f0e4c07d5cd064032f5db4a09252fb2330c12a9595", url="https://pypi.org/packages/4b/5c/d1aede7c2784b4d0e7371b13dabcdbc327072472fccfb463ee93ec76c258/cwl_upgrader-1.2.8-py3-none-any.whl")
    version("1.2.7", sha256="a39cbc537b64b773ccb563301bd6f595d7813eba76b1f4e9d3243b09876ac841", url="https://pypi.org/packages/62/b2/b61d901970fd568b2cb783c58593e2e3307c366b965fa012b36ca041f7c9/cwl_upgrader-1.2.7-py3-none-any.whl")
    version("1.2.6", sha256="2b8722370c530ca2f3a5bb53482e425598d7fc1fe44d652c6701f3cda6c851f5", url="https://pypi.org/packages/45/d3/2cca5b216852d1168987948783184349540e45d3e51cb0b746debd7abb11/cwl_upgrader-1.2.6-py3-none-any.whl")
    version("1.2.5", sha256="1e1d258c1ebef81dc2b45a6b81a638065e6afbf65ab3b324c7690e26109b60f1", url="https://pypi.org/packages/31/60/c014e142fcf62d7528ae6db57768e87f993fe287f54a6cc7f59d5229a5e9/cwl_upgrader-1.2.5-py3-none-any.whl")
    version("1.2.4", sha256="7d2b8b835f9f4c1068dfead0b7d9f60a88f27e5368d54d0301f2135942b35619", url="https://pypi.org/packages/4f/b4/11831dd7fb8abb19980dff3bad55bc7d11dc9d9d9f8e2583adc4ca91d2ea/cwl_upgrader-1.2.4-py3-none-any.whl")
    version("1.2.3", sha256="0862b4044568c48f0ad5a91da3c14d9fd834b6d80e194aa2a06ffbc6fe4fe1ae", url="https://pypi.org/packages/8e/ae/044201174aab4f1b990d6e61ffcbeba18082ff5d6bc59f4e137a6bc3127b/cwl_upgrader-1.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ruamel-yaml@0.16:", when="@1.2.10:")
        depends_on("py-ruamel-yaml@0.16:0.17", when="@1.2.9")
        depends_on("py-ruamel-yaml@0.16:0.17", when="@1.2.8 ^python@3.10:")
        depends_on("py-ruamel-yaml@0.15.98:0.17", when="@1.2.8 ^python@3.9:")
        depends_on("py-ruamel-yaml@0.15.78:0.17", when="@1.2.8")
        depends_on("py-ruamel-yaml@0.15.71:0.17", when="@1.2.8")
        depends_on("py-ruamel-yaml@0.16:0.17.26", when="@1.2.7 ^python@3.10:")
        depends_on("py-ruamel-yaml@0.15.98:0.17.26", when="@1.2.7 ^python@3.9:")
        depends_on("py-ruamel-yaml@0.15.78:0.17.26", when="@1.2.7")
        depends_on("py-ruamel-yaml@0.15.71:0.17.26", when="@1.2.7")
        depends_on("py-ruamel-yaml@0.16:0.17.22", when="@1.2.6 ^python@3.10:")
        depends_on("py-ruamel-yaml@0.15.98:0.17.22", when="@1.2.6 ^python@3.9:")
        depends_on("py-ruamel-yaml@0.15.78:0.17.22", when="@1.2.6")
        depends_on("py-ruamel-yaml@0.15.71:0.17.22", when="@1.2.5:1.2.6")
        depends_on("py-ruamel-yaml@0.16:0.17.21", when="@1.2.3:1.2.5 ^python@3.10:")
        depends_on("py-ruamel-yaml@0.15.98:0.17.21", when="@1.2.3:1.2.5 ^python@3.9:")
        depends_on("py-ruamel-yaml@0.15.78:0.17.21", when="@1.2.3:1.2.5")
        depends_on("py-ruamel-yaml@0.15.71:0.17.21", when="@1.2.3:1.2.4")
        depends_on("py-schema-salad", when="@1.1:")
        depends_on("py-setuptools", when="@0.4:")
    # END DEPENDENCIES

