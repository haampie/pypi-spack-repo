##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXanaduCloudClient(PythonPackage):
    version("0.3.2", sha256="120d8567329c249afe00ff29b1be842cce6eed74caaf0d7aecc554043a0810f1", url="https://pypi.org/packages/76/a4/f56b02aae6223ed789ae121ea2b10cde6ac947c0c24a739e187026231cf6/xanadu_cloud_client-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="3b4c7dfb99e953f19b0cd048633fdf81dabb29f5719e73edc9b42f829f9a730d", url="https://pypi.org/packages/34/07/fbf2214cad027874aef0e69ba47d0abd534cbde6ddaae505e22ee3699437/xanadu_cloud_client-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="f96a7a4ef6b0bfe08f21a83c572524fda561f9fbec2b805639f6aa452909d230", url="https://pypi.org/packages/51/d7/3c8505a9583ac42d29946f1d46a2fc52c8a4bc2dbd0ebd05a121295c7b1b/xanadu_cloud_client-0.3.0-py3-none-any.whl")
    version("0.2.1", sha256="bbc4c05a1b05a94494c414f6dff4177ad0089364cd8c62c2608c3b639cbf357c", url="https://pypi.org/packages/45/57/e43a59a34728db29222e5e0362b81ac90329f939041c068af6882b9a154d/xanadu_cloud_client-0.2.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-appdirs")
        depends_on("py-fire")
        depends_on("py-numpy")
        depends_on("py-pydantic@2.0:", when="@0.3.2:")
        depends_on("py-pydantic@:1+dotenv", when="@0.3.1")
        depends_on("py-pydantic+dotenv", when="@:0.3.0")
        depends_on("py-pydantic-settings", when="@0.3.2:")
        depends_on("py-python-dateutil")
        depends_on("py-python-dotenv", when="@0.3.2:")
        depends_on("py-requests")

