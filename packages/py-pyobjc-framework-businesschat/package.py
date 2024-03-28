# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkBusinesschat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="aa51d4d0b3b3eb050242e0d0e48b29e020ccfeb82a39c0d3a2289512734f53e4", url="https://pypi.org/packages/97/35/0cedf1bba964b7fc92680d65463365e2e4954584316355671d4cc60e1e59/pyobjc_framework_BusinessChat-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="60df5660a9a90a461c68a6cb49326c25e81f3412e951e84be7ccc98b62eb5404", url="https://pypi.org/packages/a5/99/c86cbd34f466ea9f00e8d0902f463a37a2e757702c1226fdb0ecd7d10882/pyobjc_framework_BusinessChat-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="2eb35f6f3585302c32cab1af13501b13f97badd13c0ed885c4ecd66ed24add15", url="https://pypi.org/packages/e9/22/52303092efde25a233088344eee747ca2be8ba51968b97481778937c217a/pyobjc_framework_BusinessChat-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="c60553568212687de415c542bf6bc490fae2cf9b2ae55b0f5335c814f27d6bab", url="https://pypi.org/packages/e6/6b/9ff1a8829cb17be1c4bba6a80e8f34207c410d50958c4f21866d2b5a7dae/pyobjc_framework_BusinessChat-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="f23b576f0cf336dc2820705138c2ace08edd8eb5f0043f34a579c26b1b6ec80b", url="https://pypi.org/packages/83/d3/3086d991ff5a9e8575e41d41643d77d28e172946d5540c3eb70b038beb8c/pyobjc_framework_BusinessChat-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="f47a20f2bccfe58e5d4cc72af721b67b9d5dd568ecbab179f51d8269027f6810", url="https://pypi.org/packages/ae/29/7ec4478e6085648c6bfd435c4159ea2bdb3d2fbbfc7ed506c9874ab3c7ac/pyobjc_framework_BusinessChat-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="f1f853e715b7ee6b90e01c42481cbb0bef50942bed8af9ad908914fb5f0e782e", url="https://pypi.org/packages/0b/a8/1ff33659fb567e70bbcf33b132db4eb81e978785663c4da9c84956052d45/pyobjc_framework_BusinessChat-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="90fb99a3c11210d36bc8c683ef93b8b09e0af94aadcc53e9e3bd7ed1b40383a2", url="https://pypi.org/packages/f4/37/6964c6ee3f17ff8d772cc5dc8248f058f43465774435316084e32d9f8356/pyobjc_framework_BusinessChat-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="f2a82452444df68999aea48ed5ce71cb485f48104ed58cad6561888ccb328781", url="https://pypi.org/packages/c4/43/a3e7eeaab441b79496095724348ea48e394a69d8f01d162fe6d301102c76/pyobjc_framework_BusinessChat-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="c2be517d75370d8fe0bc00a0ef182d8c79b5628f619b0922efe03a3358256781", url="https://pypi.org/packages/0e/c9/3413f20d405cfaca8e35c4a929c53dd1030c4c706eca53b35687a927d25d/pyobjc_framework_BusinessChat-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

