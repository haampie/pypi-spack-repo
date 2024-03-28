# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCoverage(PythonPackage):
    # BEGIN VERSIONS
    version("7.2.6", sha256="2025f913f2edb0272ef15d00b1f335ff8908c921c8eb2013536fcaf61f5a683d", url="https://pypi.org/packages/fc/6d/e8658433ce675a34ac82167ce8b890b1c020dcb6bacc7a0e4505af82bfaa/coverage-7.2.6.tar.gz")
    version("6.4.4", sha256="e16c45b726acb780e1e6f88b286d3c10b3914ab03438f32117c4aa52d7f30d58", url="https://pypi.org/packages/79/f3/8c1af7233f874b5df281397e2b96bedf58dc440bd8c6fdbf93a4436c517a/coverage-6.4.4.tar.gz")
    version("6.3.1", sha256="6c3f6158b02ac403868eea390930ae64e9a9a2a5bbfafefbb920d29258d9f2f8", url="https://pypi.org/packages/4f/9c/fd040e3291e6b123fb35474c8c685b9afa8f14abd4efba3fe2fa2b71ea2c/coverage-6.3.1.tar.gz")
    version("6.1.2", sha256="d9a635114b88c0ab462e0355472d00a180a5fbfd8511e7f18e4ac32652e7d972", url="https://pypi.org/packages/56/45/6917f6de0b18a4d3b465c5b35c95df4cf1e440de37c7584275412f11f637/coverage-6.1.2.tar.gz")
    version("5.5", sha256="ebe78fe9a0e874362175b02371bdfbee64d8edc42a044253ddf4ee7d3c15212c", url="https://pypi.org/packages/38/df/d5e67851e83948def768d7fb1a0fd373665b20f56ff63ed220c6cd16cb11/coverage-5.5.tar.gz")
    version("5.3", sha256="280baa8ec489c4f542f8940f9c4c2181f0306a8ee1a54eceba071a449fb870a0", url="https://pypi.org/packages/da/50/4c0c93ea67c8b42aa700cfbdedd64ea5ac5e7108ba14e3e744f57309304b/coverage-5.3.tar.gz")
    version("5.0.4", sha256="1b60a95fc995649464e0cd48cecc8288bac5f4198f21d04b8229dc4097d76823", url="https://pypi.org/packages/d1/7d/ac53d7350a5178c1f59ddf0f17552bf68e4bb3a202543f9a30bbaa46cf80/coverage-5.0.4.tar.gz")
    version("4.5.4", sha256="e07d9f1a23e9e93ab5c62902833bf3e4b1f65502927379148b6622686223125c", url="https://pypi.org/packages/85/d5/818d0e603685c4a613d56f065a721013e942088047ff1027a632948bdae6/coverage-4.5.4.tar.gz")
    version("4.5.3", sha256="9de60893fb447d1e797f6bf08fdf0dbcda0c1e34c1b06c92bd3a363c0ea8c609", url="https://pypi.org/packages/82/70/2280b5b29a0352519bb95ab0ef1ea942d40466ca71c53a2085bdeff7b0eb/coverage-4.5.3.tar.gz")
    version("4.3.4", sha256="eaaefe0f6aa33de5a65f48dd0040d7fe08cac9ac6c35a56d0a7db109c3e733df", url="https://pypi.org/packages/6e/33/01cb50da2d0582c077299651038371dba988248058e03c7a7c4be0c84c40/coverage-4.3.4.tar.gz")
    version("4.0-alpha6", sha256="afb4e6f0795c3ca233ba8130921b18b1d169427ced80f1240135d3b711230fa1", url="https://pypi.org/packages/d1/4c/87136ba38cc99e188e6288de24c4065cf96e3998453e13158c9965aaf43b/coverage-4.0a6.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("toml", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-toml", when="@5.0-beta1:5.2.0+toml")
    # END DEPENDENCIES

