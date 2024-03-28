# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPortend(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.0", sha256="8b3fe3f78779df906559a21d9eaa6e21c8fa5a7a8cc76362cbbe1e16777399cf", url="https://pypi.org/packages/a3/c5/7041b39bcad182a37ec6ea92e7e478a460db6277c542e6d417e34246bdac/portend-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="9e735cee3a5c1961f09e3f3ba6dc498198c2d70b473d98d0d1504b8d1e7a3d61", url="https://pypi.org/packages/5e/d5/55f51adaa23038c8533cde602c79e314edd6525d1f7f6a15a1995abec91e/portend-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="4c5a5a05fb31e5df7b73e08e96d55928d8a7f4ae6b4724de3777b06d0e8de693", url="https://pypi.org/packages/4a/c3/4714b8eaf7f4c375e307f1d1a49628cc3f421d5a4112148b69933183ad2d/portend-3.0.0-py3-none-any.whl")
    version("2.7.2", sha256="35a5bfbdb763d11aa701c3c2fa56d05399625ac2ee18220a429d0107936a465c", url="https://pypi.org/packages/e3/68/f91e5e8c89eb55732bbd55055bd65c1ac012f66402cec825e363fe2e4608/portend-2.7.2-py3-none-any.whl")
    version("2.7.1", sha256="add53a9e65d4022885f97de7895da583d0ed57df3eadb0b4d2ada594268cc0e6", url="https://pypi.org/packages/b8/a1/fd29409cced540facdd29abb986d988cb1f22c8170d10022ea73af77fa55/portend-2.7.1-py3-none-any.whl")
    version("2.7.0", sha256="f101c1aa58ef0718dcf591017adecbdcb54cf528721ecc5a138421511b80a285", url="https://pypi.org/packages/71/72/25a9f466c3672e09fbfb2dcf87cbf688976de4d4ad6e5fe48cf5afd85690/portend-2.7.0-py3-none-any.whl")
    version("2.6", sha256="62dd00b94a6a55fbf0320365fbdeba37f0d1fe14d613841037dc4780bedfda8f", url="https://pypi.org/packages/d7/79/eee70a512bffe5ceb5008f8e3326581948f50ca393c3bcb4d557e4818bd1/portend-2.6-py2.py3-none-any.whl")
    version("2.5", sha256="d2dca12e585ce29fc357b31ce424a27c16e2d485029252bbf8ddcc9696207976", url="https://pypi.org/packages/0a/f5/0e5fe0bba1450034f023519aed3ca326bc42981475a93e3645ab868f351c/portend-2.5-py2.py3-none-any.whl")
    version("2.4", sha256="853d69e61d86aa1bc7a4976cb2f67efe1c92d3b41c47a5e6b8771d3c51b5bfd3", url="https://pypi.org/packages/54/18/d288ef3cfcaac40c9c3674d92ef8313bf137deeced810d60d9722c0a327a/portend-2.4-py2.py3-none-any.whl")
    version("2.3", sha256="f5c99a1aa1655733736bb0283fee6a1e115e18db500332bec8e24c43f320d8e8", url="https://pypi.org/packages/81/43/21afd5914b74d4271184ee76f4093b45aa6a580dc6627d72dfc33664c6ac/portend-2.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-tempora@1.8:", when="@2:")
    # END DEPENDENCIES

