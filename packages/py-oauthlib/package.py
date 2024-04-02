# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOauthlib(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.2", sha256="8139f29aac13e25d502680e9e19963e83f16838d48a0d71c287fe40e7067fbca", url="https://pypi.org/packages/7e/80/cab10959dc1faead58dc8384a781dfbf93cb4d33d50988f7a69f1b7c9bbe/oauthlib-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="88e912ca1ad915e1dcc1c06fc9259d19de8deacd6fd17cc2df266decc2e49066", url="https://pypi.org/packages/92/bb/d669baf53d4ffe081dab80aad93c5c79f84eeac885dd31507c8c055a98d5/oauthlib-3.2.1-py3-none-any.whl")
    version("3.1.1", sha256="42bf6354c2ed8c6acb54d971fce6f88193d97297e18602a3a886603f9d7730cc", url="https://pypi.org/packages/e8/5d/9dd1c29e5a786525f6342f6c1d812ed2e37edc653ad297048c1668988053/oauthlib-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="df884cd6cbe20e32633f1db1072e9356f53638e4361bef4e8b03c9127c9328ea", url="https://pypi.org/packages/05/57/ce2e7a8fa7c0afb54a0581b14a65b56e62b5759dbc98e80627142b8a3704/oauthlib-3.1.0-py2.py3-none-any.whl")
    version("3.0.1", sha256="3e1e14f6cde7e5475128d30e97edc3bfb4dc857cb884d8714ec161fdbb3b358e", url="https://pypi.org/packages/16/95/699466b05b72b94a41f662dc9edf87fda4289e3602ecd42d27fcaddf7b56/oauthlib-3.0.1-py2.py3-none-any.whl")
    version("2.0.2", sha256="b3b9b47f2a263fe249b5b48c4e25a5bce882ff20a0ac34d553ce43cff55b53ac", url="https://pypi.org/packages/fa/2e/25f25e6c69d97cf921f0a8f7d520e0ef336dd3deca0142c0b634b0236a90/oauthlib-2.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("extras", default=False, description="extras")
    variant("rsa", default=False, description="rsa")
    variant("signals", default=False, description="signals")
    variant("signedtoken", default=False, description="signedtoken")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-blinker@1.4:", when="@3.1.1:+signals")
        depends_on("py-blinker", when="@2.0.7:3.1.0+signals")
        depends_on("py-cryptography@3:", when="@3.2:+signedtoken")
        depends_on("py-cryptography@3:", when="@3.2:+rsa")
        depends_on("py-cryptography@3", when="@3.1.1:3.1+signedtoken")
        depends_on("py-cryptography@3", when="@3.1.1:3.1+rsa")
        depends_on("py-cryptography", when="@2.0.7:3.1.0+signedtoken")
        depends_on("py-cryptography", when="@2.0.7:3.1.0+rsa")
        depends_on("py-pyjwt@2.0.0:", when="@3.1.1:+signedtoken")
        depends_on("py-pyjwt@1:", when="@2.0.7:3.1.0+signedtoken")
    # END DEPENDENCIES

