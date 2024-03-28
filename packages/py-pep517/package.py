# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPep517(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.1", sha256="31b206f67165b3536dd577c5c3f1518e8fbaf38cbc57efff8369a392feff1721", url="https://pypi.org/packages/25/6e/ca4a5434eb0e502210f591b97537d322546e4833dcb4d470a48c375c5540/pep517-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b", url="https://pypi.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl")
    version("0.12.0", sha256="dd884c326898e2c6e11f9e0b64940606a93eb10ea022a2e067959f3a110cf161", url="https://pypi.org/packages/f4/67/846c08e18fefb265a66e6fd5a34269d649b779718d9bf59622085dabd370/pep517-0.12.0-py2.py3-none-any.whl")
    version("0.11.1", sha256="12a811fec422deae52821771113f804ddf4ae86a6ae743afd107ccef0677188d", url="https://pypi.org/packages/ef/72/b82f78c44937fdb8de21133c3e8f87c223e5ef01b13645cf2742b3ab309e/pep517-0.11.1-py2.py3-none-any.whl")
    version("0.11.0", sha256="3fa6b85b9def7ba4de99fb7f96fe3f02e2d630df8aa2720a5cf3b183f087a738", url="https://pypi.org/packages/3b/da/bfa8de153f54df0b04ca634a4489d28758ab56b394931588627fcb49f44b/pep517-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="eba39d201ef937584ad3343df3581069085bacc95454c80188291d5b3ac7a249", url="https://pypi.org/packages/2f/5b/9afe177c8cc801ad9342488f8509c3e237f7c9ec161b7fccb1d61d6d0716/pep517-0.10.0-py2.py3-none-any.whl")
    version("0.9.1", sha256="3985b91ebf576883efe5fa501f42a16de2607684f3797ddba7202b71b7d0da51", url="https://pypi.org/packages/66/f5/2411973d0032f62629908612fb961eb2987212e071dba6a0d9f86d20820e/pep517-0.9.1-py2.py3-none-any.whl")
    version("0.8.2", sha256="576c480be81f3e1a70a16182c762311eb80d1f8a7b0d11971e5234967d7a342c", url="https://pypi.org/packages/43/f6/4af3567c136e8e1620f6fcff665f9a478e68d06f9c990d0f2717cf9a2b8c/pep517-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="882e2eeeffe39ccd6be6122d98300df18d80950cb5f449766d64149c94c5614a", url="https://pypi.org/packages/f4/9b/82910c0f01f29c7bdd8fc4306ed03e1742256612e2cfca8f05ebb21958ab/pep517-0.8.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="fac83aa4c3b73adc84cb2a295f1f5bd5b9a13946ebd1339ba3b33ce287165c88", url="https://pypi.org/packages/21/44/ead783bf40d0e8242ef16ecd056a28fa177808ac6aece525663571a5c55c/pep517-0.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.6:0.7")
        depends_on("py-toml", when="@0.7:0.10")
        depends_on("py-tomli@1.1:", when="@0.13: ^python@:3.10")
        depends_on("py-tomli@1.1:", when="@0.11.1:0.12")
        depends_on("py-tomli", when="@0.11:0.11.0")
        depends_on("py-zipp", when="@0.6:0.7")
    # END DEPENDENCIES

