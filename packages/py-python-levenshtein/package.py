# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonLevenshtein(PythonPackage):
    # BEGIN VERSIONS
    version("0.25.0", sha256="fc4a985d664b307f3b7f245d25f28236ece41c039de894f0e26e77614b0eef68", url="https://pypi.org/packages/c9/79/eaa5f632f10be7b9ff85673be2246926e5a6a83fc489a228a22a95b5dcf0/python_Levenshtein-0.25.0-py3-none-any.whl")
    version("0.24.0", sha256="36f96d0ba407969f44f2f012373a930d3e100b68206b2b2f56600ba0f08ca50b", url="https://pypi.org/packages/39/b7/8e2eaf39f68ce9aab9f6aa5cda3027847b4245a44acd781c85cf6f6da8fc/python_Levenshtein-0.24.0-py3-none-any.whl")
    version("0.23.0", sha256="486a47b189e3955463107aa36b57fb1e2b3b40243b9cc2994cde9810c78195c0", url="https://pypi.org/packages/27/89/c45dbdbd479453cfc8c4c1271c9f67fd607deaf84880e31c67b682980456/python_Levenshtein-0.23.0-py3-none-any.whl")
    version("0.22.0", sha256="86910223ce1be3a3a621327ee789c23843f9d0a960e1a365fe683ad21c9adab9", url="https://pypi.org/packages/18/5f/7214d4e80d82b328109b4373f43e2187c2ba946f70fd13f3918ba83e2a0e/python_Levenshtein-0.22.0-py3-none-any.whl")
    version("0.21.1", sha256="5f49ebb4772a274aac4aeb190fc23ad537ebe778dec15a8f17975f746478c691", url="https://pypi.org/packages/ae/9c/208f8ad7eb38492ac4f829790a500bcfca88b1d0a1c988f6480a52a6f681/python_Levenshtein-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="2e05a10989cae751669dc08c5d4934e2da489c9afb1545ecc1d8c8edb822b5ae", url="https://pypi.org/packages/62/b9/eebe6a6a4bfd681004be0db6a0b604950368e787f31626dbc93ccbc59aaa/python_Levenshtein-0.21.0-py3-none-any.whl")
    version("0.20.9", sha256="2a6f8c97ba554d7399e0b450e1fce5d90d6354b1c1762e419671de27f25736c5", url="https://pypi.org/packages/c9/bd/fef1536c7ea8d22305c6d54fecf4e7abfc5b4b55782ff9193cdcea4ff8b9/python_Levenshtein-0.20.9-py3-none-any.whl")
    version("0.20.8", sha256="a932f149c72d2707963947ba9df9729ac36983d2e9db4eb93e4d5b69a8899070", url="https://pypi.org/packages/df/65/1e7f5c7c4bcb88b20a57efe9051ef04a14f06849619acd417698a40f4ef4/python_Levenshtein-0.20.8-py3-none-any.whl")
    version("0.20.7", sha256="88a58b95e3340a918489dac0c78f731323c0a4d8f5564f839ffea80155574e77", url="https://pypi.org/packages/41/d1/8e8163dc28e9ca19abeac1898c0f50803b72d9a55898711424607cad15a8/python_Levenshtein-0.20.7-py3-none-any.whl")
    version("0.20.6", sha256="edfe6f724bf93ba37e177a0766d8dd93867fdb969f10ee4ceacb0f72022fd50f", url="https://pypi.org/packages/60/58/26a4922d646fda213c28b6ad0a16e885aefb66adc8b848172eb50bcf2f8c/python_Levenshtein-0.20.6-py3-none-any.whl")
    version("0.12.2", sha256="dc2395fbd148a1ab31090dd113c366695934b9e85fe5a4b2a032745efd0346f6", url="https://pypi.org/packages/2a/dc/97f2b63ef0fa1fd78dcb7195aca577804f6b2b51e712516cc0e902a9a201/python-Levenshtein-0.12.2.tar.gz")
    version("0.12.0", sha256="033a11de5e3d19ea25c9302d11224e1a1898fe5abd23c61c7c360c25195e3eb1", url="https://pypi.org/packages/42/a9/d1785c85ebf9b7dfacd08938dd028209c34a0ea3b1bcdb895208bd40a67d/python-Levenshtein-0.12.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-levenshtein@0.25:", when="@0.25:")
        depends_on("py-levenshtein@0.24", when="@0.24")
        depends_on("py-levenshtein@0.23", when="@0.23")
        depends_on("py-levenshtein@0.22", when="@0.22")
        depends_on("py-levenshtein@0.21.1:0.21", when="@0.21.1:0.21")
        depends_on("py-levenshtein@0.21:0.21.0", when="@0.21:0.21.0")
        depends_on("py-levenshtein@0.20.9:0.20", when="@0.20.9:0.20")
        depends_on("py-levenshtein@0.20.8", when="@0.20.8")
        depends_on("py-levenshtein@0.20.7", when="@0.20.7")
        depends_on("py-levenshtein@0.20.6", when="@0.20.6")
    # END DEPENDENCIES

