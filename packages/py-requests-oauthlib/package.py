# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsOauthlib(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.1", sha256="2577c501a2fb8d05a304c09d090d6e47c306fef15809d102b327cf8364bddab5", url="https://pypi.org/packages/6f/bb/5deac77a9af870143c684ab46a7934038a53eb4aa975bc0687ed6ca2c610/requests_oauthlib-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="7f71572defaecd16372f9006f33c2ec8c077c3cfa6f5911a9a90202beb513f3d", url="https://pypi.org/packages/a3/12/b92740d845ab62ea4edf04d2f4164d82532b5a0b03836d4d4e71c6f3d379/requests_oauthlib-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="d3ed0c8f2e3bbc6b344fa63d6f933745ab394469da38db16bdddb461c7e25140", url="https://pypi.org/packages/c2/e2/9fd03d55ffb70fe51f587f20bcf407a6927eb121de86928b34d162f0b1ac/requests_oauthlib-1.2.0-py2.py3-none-any.whl")
    version("0.3.3", sha256="37557b4de3eef50d2a4c65dc9382148b8331f04b1c637c414b3355feb0f007e9", url="https://pypi.org/packages/0f/8a/a7afc508dd7cf6883fb318bdf0c2a0fd65443e396ccd27977c6f146040a3/requests-oauthlib-0.3.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-oauthlib@3:", when="@1.3.1:")
        depends_on("py-requests@2:", when="@0.6.2:1.0,1.3.1:")
    # END DEPENDENCIES

