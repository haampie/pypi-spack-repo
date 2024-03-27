##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCalendarstore(PythonPackage):
    version("10.2", sha256="e289236df651953a41be8ee4ce548f477a6ab8e90aa8bbd73f46ad29032ff13f", url="https://pypi.org/packages/12/d8/0937fa3f1e0130490f41d81a415d9f38dc18a4ab2ae1e709600b0d37ca04/pyobjc_framework_CalendarStore-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="cbd8ec495d9b13cc986b018d8740e25a4e18a25732ee19de1311f0c30ab53120", url="https://pypi.org/packages/fd/40/3bb184054817ca142f9d901d8215af1060cc82364e3c20040deb68d0b625/pyobjc_framework_CalendarStore-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="1e0da82b7d1a0d1f34991795d1f7dc8e186f79faf9a4b0ef5fe1a74112ac70a4", url="https://pypi.org/packages/58/7e/4efa910e49ff7bb544b7d4dff49bd8485bdf7f56f5f7ff0794e5b24933c4/pyobjc_framework_CalendarStore-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="83d064b61b22afa4cd35a78d939f72a097a4a9fd7b9dccd8050fb43389db6e50", url="https://pypi.org/packages/4d/16/5c36f3462a9d53ee339882136d7d0a29d18703f2a653bd54920d3f71fdb7/pyobjc_framework_CalendarStore-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="d949a965e0c4e218d3363d2ef9ebcbfebf9cfef5d704ce066cc057c329c19974", url="https://pypi.org/packages/14/56/7c2ee4f07c04c470cf44c26b8ad7b17f2d9272b4efaafe879af67f273b15/pyobjc_framework_CalendarStore-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="474a3e94902944c7cb76d72fc7a75ba8451ac209d3f92da02903a6b63cacdcdf", url="https://pypi.org/packages/f0/02/56cb5d4bcaa4951d4dee53b897a3cdbaf7c8b32d7ab676f8d087f78207b2/pyobjc_framework_CalendarStore-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="ddb62bc90fbd772dfc233ebefe06075b59de5735110979c5efff599159d30d40", url="https://pypi.org/packages/02/a4/4e300e2ed093e1276d360d5ec95111f19442e392ea094a6ac2c1403c5c7d/pyobjc_framework_CalendarStore-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="87a56635ddac4350e0e15fc03cef849cabe21fa1b0816e097be8b14414d2949d", url="https://pypi.org/packages/34/07/fbaadf8926a9ba7957e80c0944a7d8c9557db7a0f1d93df3ce7c3cded8c3/pyobjc_framework_CalendarStore-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="8ebf85ef0daa0c8ab631d46467698a9d26d0a4364c1fc236068408a6b1b85d0f", url="https://pypi.org/packages/b6/b5/2e17e7b0869263be8ef5a0d11f571d990f92236434fe852b97c088ace52d/pyobjc_framework_CalendarStore-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="efdbd64154e351e5383aaea38cd37a8ac49963baf70d51c17edb80e95c5daa9f", url="https://pypi.org/packages/2d/a3/c863c037d7f96de9e685df3454dd8cbd48c48f56bae30afd39722f99e1ab/pyobjc_framework_CalendarStore-8.5-py2.py3-none-any.whl")

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

