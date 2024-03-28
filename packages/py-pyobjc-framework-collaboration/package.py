# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCollaboration(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="239a0505d702d49b5c3f0a3524531f9be63d599ea2cd3cbb5953147b34dbdcc1", url="https://pypi.org/packages/10/59/bbf60e22415dc3eb24a37d469d63bb37eff1b56f0a01161358276772a3c3/pyobjc_framework_Collaboration-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="9a2137aaed1ad71bf6c92c7c275253c2dc6f0062af9d2d8a1590d00bf30c1ecb", url="https://pypi.org/packages/35/7b/5dce629a2b8c30d98e3468a803b1bbf29ee35ce038068b819e20f7848dbb/pyobjc_framework_Collaboration-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="971e75adb91bc3f39750ce3f5332e72500f82d04f6e95cb1e8dd1dc468826530", url="https://pypi.org/packages/71/f6/50fefc316747f60a25414cfb772ea77553b05faddc46906355e9ac1f11f0/pyobjc_framework_Collaboration-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="f82564db198d0f0766dbb76660f62e086b63ad9eb8b4fe54f53779f1b616a9ad", url="https://pypi.org/packages/46/7f/fd4b1ffa95c3d088681f14b496f7d5a0395d43a0f39b88ba3e92afb8488c/pyobjc_framework_Collaboration-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="09b0f474101b55fee825c79f7abdb36eaf20ff63af4775076a3f3bfa3c5837ec", url="https://pypi.org/packages/b8/f8/b2061599c0bf1b828556faa737a4a781b7f8427eabe874e1a34bcf52e9c1/pyobjc_framework_Collaboration-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="1d6595c6621741a88a03212f3cd2893a376211adad4b55e6c412d802bed157f4", url="https://pypi.org/packages/7f/00/9cfae3f93041c98d7e17c0780a91261fc3364a8e4bbf270643502d4d1aba/pyobjc_framework_Collaboration-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="7496248e3013d43cf609a8ba0612f4bdc069105e6bd2dd1b8363125bb1ec277d", url="https://pypi.org/packages/58/14/9289ec541a5c9b83da93c6252e5015c01ccdf7fbb2318be7487580dfbdfd/pyobjc_framework_Collaboration-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="5ec6ddf1c4654633fd3037a6894f4ef50ff2dec9c8560e35584e0194bf6b1845", url="https://pypi.org/packages/f7/c7/b9c31e5aff40743d318e5538e1985d39f41d3c65848fe59d20900b230dfd/pyobjc_framework_Collaboration-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="8f266165bf2a362966126e0a7d207caae814fe7f78071dd278ee49ee8d661301", url="https://pypi.org/packages/79/83/124c6ce45f5382b0648c6f1c4410dd23fa5fd94c2b995c58b62799e1a3f9/pyobjc_framework_Collaboration-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="7cda382202199ae599bddeda136503e82de453f2790400caf8ec2be41962e17b", url="https://pypi.org/packages/0e/31/e39f3e3c5182251ea04b650147f01676586544f9b04146bbcdfe79d29c5a/pyobjc_framework_Collaboration-8.5-py2.py3-none-any.whl")
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

