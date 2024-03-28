# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuart(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.19.4", sha256="959da9371b44b6f48d952661863f8f64e68a893481ef3f2ef45b177629dc0928", url="https://pypi.org/packages/9a/2c/681b4fcecefd98627a90dd5aecdc6b57ba18c9ce07e173d86a0b1274f20b/quart-0.19.4-py3-none-any.whl")
    version("0.19.3", sha256="3bfb433bb4edfcb13eb908096e579cb99eaae0b57ef05a3edfde797a2b12518a", url="https://pypi.org/packages/6b/5b/b12ae796a9e6ebaa75f7a9adcf31a685908d72efb8c1a71231bdb36d982a/quart-0.19.3-py3-none-any.whl")
    version("0.19.2", sha256="f450de888fa1435261ec0b6ed72e1174920df6a38d0e9a62fa5a78d62c9687a0", url="https://pypi.org/packages/e0/02/2bf05e33a377ef0f775e24f2752114b5d6397f1cb9b41182e93e038f6af3/quart-0.19.2-py3-none-any.whl")
    version("0.19.1", sha256="b3c5ebbb6f6c932f9ffa53ebb67039bb419e08f40172dad81a4bd7b82e11ba0c", url="https://pypi.org/packages/c9/36/481af69e2cbe21bffbefa180cc278e34b5a9b49659d6266f907cfc7b9a51/quart-0.19.1-py3-none-any.whl")
    version("0.19.0", sha256="c8198e798e3dd5d3396872687522cbf45d63e90b21265c9fcf9542a66b950c30", url="https://pypi.org/packages/43/39/58d4a45850c93807cc885d2eb871499af9bb91df166e152f82f76fb9cf4b/quart-0.19.0-py3-none-any.whl")
    version("0.18.4", sha256="578a466bcd8c58b947b384ca3517c2a2f3bfeec8f58f4ff5038d4506ffee6be7", url="https://pypi.org/packages/8f/79/ccd45c2374711b632647aad3dc27af4341c96a852049603493e33c288762/quart-0.18.4-py3-none-any.whl")
    version("0.18.3", sha256="c221a7deb83a014dee040108d654b6141fe37f59e249c5caa0fdcf6506caf50b", url="https://pypi.org/packages/5c/05/64e318eaf6dbeb8db79402cb71d6ecda676c9510f382b9243efe67b9ba50/Quart-0.18.3-py3-none-any.whl")
    version("0.18.2", sha256="17503c36e78f1dde8ea9dbdd23ae8ec2d2972c2f3e2e56d0d6d3d943d1de5387", url="https://pypi.org/packages/84/09/77f9d571ab1d28e5080e8db02373a1c035a60465f1c1a4850f859890e5dd/Quart-0.18.2-py3-none-any.whl")
    version("0.18.1", sha256="2069dd9822c58582441b04ef5141277308a058668368b39e386b8392f28b2421", url="https://pypi.org/packages/57/78/9497fdbf18615cbe6351fe375493cd99aecb76226ca409d0934a730722ab/Quart-0.18.1-py3-none-any.whl")
    version("0.18.0", sha256="5bef6711d25e379ce8a1ed3f7d3ec72eae4159d116e8d480d1cab59c8bb6f44d", url="https://pypi.org/packages/e2/ef/b66ea886347443067adab9c4e9708d630a0de45dcbd63c6acb6cdf6b7c5e/Quart-0.18.0-py3-none-any.whl")
    version("0.16.3", sha256="556d07f24a8789db3b2dca78e0fe764c5a97a75ca800b1b7e5c4cfb7c3da2ea1", url="https://pypi.org/packages/30/41/2405163b533eb53a7563e899d13ad5b62bfa11a7ea6b066b9f3d0a04f797/Quart-0.16.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiofiles", when="@0.2:")
        depends_on("py-blinker@1.6:", when="@0.19:")
        depends_on("py-blinker@:1.5", when="@0.18.4:0.18")
        depends_on("py-blinker", when="@0.2:0.18.3")
        depends_on("py-click@8.0.0:", when="@0.18.1:")
        depends_on("py-click", when="@0.4:0.18.0")
        depends_on("py-flask@3:", when="@0.19:")
        depends_on("py-hypercorn@0.11.2:", when="@0.15,0.16.1:")
        depends_on("py-importlib-metadata", when="@0.18: ^python@:3.9")
        depends_on("py-itsdangerous", when="@0.2:")
        depends_on("py-jinja2", when="@0.2:")
        depends_on("py-markupsafe", when="@0.17:")
        depends_on("py-toml", when="@0.11:0.17")
        depends_on("py-typing-extensions", when="@0.19: ^python@:3.9")
        depends_on("py-werkzeug@3:", when="@0.19:")
        depends_on("py-werkzeug@2.2.0:", when="@0.18")
        depends_on("py-werkzeug@2.0.0:", when="@0.15,0.16.1:0.17")
    # END DEPENDENCIES

