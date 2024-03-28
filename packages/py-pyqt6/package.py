# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt6(PythonPackage):
    # BEGIN VERSIONS
    version("6.6.1", sha256="9f158aa29d205142c56f0f35d07784b8df0be28378d20a97bcda8bd64ffd0379", url="https://pypi.org/packages/8c/2b/6fe0409501798abc780a70cab48c39599742ab5a8168e682107eaab78fca/PyQt6-6.6.1.tar.gz")
    version("6.6.0", sha256="d41512d66044c2df9c5f515a56a922170d68a37b3406ffddc8b4adc57181b576", url="https://pypi.org/packages/17/dc/969e2da415597b328e6a73dc233f9bb4f2b312889180e9bbe48470c957e7/PyQt6-6.6.0.tar.gz")
    version("6.5.3", sha256="bcbbf9511b038b4924298ca10999aa36eb37a0a38d0638f895f9bba6025c0a77", url="https://pypi.org/packages/18/b8/74667c8108d8481b87f8d87e6d962b64eb53ea21432cdbfbfeee4d2b4430/PyQt6-6.5.3.tar.gz")
    version("6.5.2", sha256="1487ee7350f9ffb66d60ab4176519252c2b371762cbe8f8340fd951f63801280", url="https://pypi.org/packages/34/da/e03b7264b1e88cd553ff62a71c0c19f55690e08928130f4aae613723e535/PyQt6-6.5.2.tar.gz")
    version("6.5.1", sha256="e166a0568c27bcc8db00271a5043936226690b6a4a74ce0a5caeb408040a97c3", url="https://pypi.org/packages/1c/77/3b14889ac1e677bd5a284e0d003cac873689046e328401d92a927c9cc921/PyQt6-6.5.1.tar.gz")
    version("6.5.0", sha256="b97cb4be9b2c8997904ea668cf3b0a4ae5822196f7792590d05ecde6216a9fbc", url="https://pypi.org/packages/28/01/9e4b91cb0c1023934b1dc654c5bbfc29cbabcbf6092f936b74aee46dd637/PyQt6-6.5.0.tar.gz")
    version("6.4.2", sha256="740244f608fe15ee1d89695c43f31a14caeca41c4f02ac36c86dfba4a5d5813d", url="https://pypi.org/packages/c3/e0/e1b592a6253712721612e2e64a323930a724e1f5cf297ed5ec6d6c86dda1/PyQt6-6.4.2.tar.gz")
    version("6.4.1", sha256="0c1dcadf161331cfdbde0906c05f7f8048dc4907d717647c33bbc4404146f59f", url="https://pypi.org/packages/8a/a6/12565a8b14faaeb3ecf3edb5bc1e6bcb622dab776c23ea4eb4c369176c75/PyQt6-6.4.1.tar.gz")
    version("6.4.0", sha256="91392469be1f491905fa9e78fa4e4059a89ab616ddf2ecfd525bc1d65c26bb93", url="https://pypi.org/packages/b2/c9/266b12a9826452e387f0ff4f0b4bbd29e11d2de81a5f60c0975933b34e7f/PyQt6-6.4.0.tar.gz")
    version("6.3.1", sha256="8cc6e21dbaf7047d1fc897e396ccd9710a12f2ef976563dad65f06017d2c9757", url="https://pypi.org/packages/a3/ab/c5989de70eceed91abf5f828d99817462ff75f41558e9f5a6f5213f0932c/PyQt6-6.3.1.tar.gz")
    version("6.3.0", sha256="4fd85dcb15ea4e734b6e4e216fe9a6246779761edaf2cf7c0cce1a2303a8d31b", url="https://pypi.org/packages/1a/54/793f2a2408fd7774361faf99ecf1e276e787e0cbc3062161e2c54d94df33/PyQt6-6.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyqt6-sip@13.6:", when="@6.5.3:")
        depends_on("py-pyqt6-sip@13.4:", when="@6.3.1:6.5.2")
        depends_on("py-pyqt6-sip@13.2:", when="@6.2.2:6.3.0")
    # END DEPENDENCIES

