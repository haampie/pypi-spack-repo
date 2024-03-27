##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskBabel(PythonPackage):
    version("4.0.0", sha256="638194cf91f8b301380f36d70e2034c77ee25b98cb5d80a1626820df9a6d4625", url="https://pypi.org/packages/14/c2/e0ab5abe37882e118482884f2ec660cd06da644ddfbceccf5f88f546b574/flask_babel-4.0.0-py3-none-any.whl")
    version("3.1.0", sha256="deb3ee272d5adf97f5974ed09ab501243d63e7fb4a047501a00de4bd4aca4830", url="https://pypi.org/packages/5e/b2/ec77c54dcc31acef7fb75c5730f35714ab4fe4742b41d99fc932eefe6ca1/flask_babel-3.1.0-py3-none-any.whl")
    version("3.0.1", sha256="ceb8c82039954a6b29da33ec5deb84878b78069d1ea628b21cac3f8233e9189c", url="https://pypi.org/packages/c9/f7/7574f62f4fe299155f85b327afa24d20fc22c3e6dd25ad121a7db959f79f/flask_babel-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="a5615f2305a9a2911a7cac79bcfdb05feeb6ac359abbc6e002a1c7854b7fc190", url="https://pypi.org/packages/b7/f8/43ceaa332545452f085703e9e11193ff8a29f8c4d782a3429cfeb55c92d2/flask_babel-3.0.0-py3-none-any.whl")
    version("2.0.0", sha256="e6820a052a8d344e178cdd36dd4bb8aea09b4bda3d5f9fa9f008df2c7f2f5468", url="https://pypi.org/packages/ab/3e/02331179ffab8b79e0383606a028b6a60fb1b4419b84935edd43223406a0/Flask_Babel-2.0.0-py3-none-any.whl")
    version("1.0.0", sha256="247f4ec34cf605d03781f480bccb1a5acb719df1d1a2a743c091ab3db5d5fde2", url="https://pypi.org/packages/76/a4/0115c7c520125853037fc1d6b3da132a526949640e27a699a13e05ec7593/Flask_Babel-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-babel@2.12:", when="@3.1:")
        depends_on("py-babel@2.11:", when="@3:3.0")
        depends_on("py-babel@2.3:", when="@1:2")
        depends_on("py-flask@2.0.0:", when="@3.1:")
        depends_on("py-flask@2.0.0:2", when="@3:3.0")
        depends_on("py-flask", when="@1:2")
        depends_on("py-jinja2@3.1:", when="@3.1:")
        depends_on("py-jinja2@3.1.2:", when="@3:3.0")
        depends_on("py-jinja2@2.5:", when="@1:2")
        depends_on("py-pytz@2022.7:", when="@3.1:")
        depends_on("py-pytz@2022.7:2022", when="@3:3.0")
        depends_on("py-pytz", when="@1:2")

