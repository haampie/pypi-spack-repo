# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQdarkstyle(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.3", sha256="ea980ee426d594909cf1058306832af71ff6cbad6f69237b036d1550635aefbc", url="https://pypi.org/packages/93/7d/c3c10498430dadcea4def5faddf71cd199e577d20a125e7ef1e9d7bdbbfa/QDarkStyle-3.2.3-py2.py3-none-any.whl")
    version("3.2.2", sha256="de14201998b344d988c20d16891cde4b18d914f29f5959d93f533805a0225ea9", url="https://pypi.org/packages/5a/5a/685b0d4e1040f60150e0c6779635a1eb570f0ee30edd33fb3dee3bf2e621/QDarkStyle-3.2.2-py2.py3-none-any.whl")
    version("3.2.1", sha256="44bea76ba8ff60bba1741c618b1f9836158e2fde5fc292ebfc7cdde04f3d4eca", url="https://pypi.org/packages/d1/a1/1a27f494131109cf3feabcb21739137e8abc7d617881f36243b1f508991a/QDarkStyle-3.2.1-py2.py3-none-any.whl")
    version("3.2", sha256="71fc0e22648f943014fdeb8d958ac8ae95d35f90054ef8123cd10a1acd46cdaa", url="https://pypi.org/packages/eb/f1/dc9042a9ea932638a60215ab6ba427433a9d5e8ea1233334dc2448f0e0e8/QDarkStyle-3.2-py2.py3-none-any.whl")
    version("3.1", sha256="679a38fcd040de9fac8b8cae483310302fdb12c8d912845249c41dc54974a9b2", url="https://pypi.org/packages/48/59/01f454d0eacb6670c77add68611b7a572455ae69ba902d270ed761869f87/QDarkStyle-3.1-py2.py3-none-any.whl")
    version("3.0.3", sha256="ebccb129275dba637a112f0b7fa1040ea51e95938eb332a9f653d963c63aa915", url="https://pypi.org/packages/e9/89/4efa30bc9891a48b055877b2386bc33f13c7a3d9c8a41b6ccd76b82c8f5d/QDarkStyle-3.0.3-py2.py3-none-any.whl")
    version("3.0.2", sha256="7c791535cc20b3cc1e8e1bf6b88dabe53cb0615983df702be83597e73ada2558", url="https://pypi.org/packages/42/3c/b4a755f5cf9e5b9ce735dcd650810a20dd21ab5de4b23c3410e40aac6a45/QDarkStyle-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="70346f9a09f0246374489c64526cba0b6b361e3c4d487a314bd1477c0640287a", url="https://pypi.org/packages/41/4c/bcba237b21d58ea2f6b4770c37756c902bbc05f624161e29a2fec7dacdf4/QDarkStyle-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="f021f6e293c5fd8ef084a9d4f4f9f88abb08c46629060bcac7d0ce71b1c15903", url="https://pypi.org/packages/b4/33/f5146d02ddb4144cddd01a4ed8a969fdd2b93415f0693d42512d3ab77454/QDarkStyle-3.0.0-py2.py3-none-any.whl")
    version("2.8.1", sha256="7cead57817a8a1f38b48d76ef38986b6cc397d0315c0dd0431fcd06749556947", url="https://pypi.org/packages/e8/8e/cf0f5444b2389d860578292a811f5a9de3d2c0841df3ffe45a6a8e8f77c3/QDarkStyle-2.8.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-helpdev@0.6.10:", when="@2.8.1:2")
        depends_on("py-qtpy@2:", when="@3.2:")
        depends_on("py-qtpy@1.9:", when="@2.8.1:3.1")
    # END DEPENDENCIES

