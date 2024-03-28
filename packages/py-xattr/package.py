# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXattr(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.1", sha256="c12e7d81ffaa0605b3ac8c22c2994a8e18a9cf1c59287a1b7722a2289c952ec5", url="https://pypi.org/packages/a0/19/dfb42dd6e6749c6e6dde55b12ee44b3c8247c3cfa5b85180a60902722538/xattr-0.10.1.tar.gz")
    version("0.9.9", sha256="09cb7e1efb3aa1b4991d6be4eb25b73dc518b4fe894f0915f5b0dcede972f346", url="https://pypi.org/packages/91/ac/5898d1811abc88c3710317243168feff61ce12be220b9c92ee045ecd66c4/xattr-0.9.9.tar.gz")
    version("0.9.8", sha256="bf11c8c857215e3ef60b031e7807264f30af4348d7565a7e9b8dca70593753c7", url="https://pypi.org/packages/22/ac/25763ab6c7ad651370b2f05c42c113160db4f63789791da42b13ea19b145/xattr-0.9.8.tar.gz")
    version("0.9.7", sha256="b0bbca828e04ef2d484a6522ae7b3a7ccad5e43fa1c6f54d78e24bb870f49d44", url="https://pypi.org/packages/c1/74/1ff659d6deb1d2d6babb9483171edfa330264ae2cbf005035bb7a77b07d2/xattr-0.9.7.tar.gz")
    version("0.9.6", sha256="7cb1b28eeab4fe99cc4350e831434142fce658f7d03f173ff7722144e6a47458", url="https://pypi.org/packages/60/80/a1f35bfd3c7ffb78791b2a6a15c233584a102a20547fd96d48933ec453e7/xattr-0.9.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cffi@1:", when="@0.9.3:0.9.7")
    # END DEPENDENCIES

