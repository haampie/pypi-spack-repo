##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSystemextensions(PythonPackage):
    version("10.2", sha256="883c41cb257fb2b5baadafa4213dc0f0fffc97edb35ebaf6ed95a185a786eb85", url="https://pypi.org/packages/5b/a8/0f785b4667671a918967f660e2a42961b00f78ad494629481816b89133fa/pyobjc-framework-SystemExtensions-10.2.tar.gz")
    version("10.1", sha256="3eb7ad8f1a6901294b02cd6d6581bd6960a48fcfd82475f5970d1c909f12670d", url="https://pypi.org/packages/d3/3a/3f800d6cab6b99c64572ab11de004c8782fb10fdb542f26847101ead23dd/pyobjc-framework-SystemExtensions-10.1.tar.gz")
    version("10.0", sha256="0c71c2d3db048fd55d931137402e9d0550178f65aacc6597538d4c1c9debb729", url="https://pypi.org/packages/1d/2b/2ff0a9e29f8da4bf9fcc20bcca90cba67a7a40f885648b462b9bcb46d87d/pyobjc-framework-SystemExtensions-10.0.tar.gz")
    version("9.2", sha256="1de1cb60f7ed1ec8fd19777422534ce81892834ccc903ea5e8e3e0bc85045650", url="https://pypi.org/packages/f3/b3/3768a7415aa04429df7f9254bb772bf05a999d77a8b8916303d6b38a5868/pyobjc-framework-SystemExtensions-9.2.tar.gz")
    version("9.1.1", sha256="d39c6f89805434d5d214f028bad31be4b711996ab1d83518a7a4f07a4f9dcf08", url="https://pypi.org/packages/48/bd/963b93a373b678ba729bcc83f02064465df6d88cf931da1c6644a78982d7/pyobjc-framework-SystemExtensions-9.1.1.tar.gz")
    version("9.1", sha256="73b32121c0eb4aaf9889ab8d8800a5cc4a0bce891f9e0834ff257b54d0a0495e", url="https://pypi.org/packages/9a/83/5c129c1efa7c0487e8240ac494b23f6adba335821671432942c25597f687/pyobjc-framework-SystemExtensions-9.1.tar.gz")
    version("9.0.1", sha256="0b95decfa84f863d5418c6ab341285b1f4c7344566c2cb6dbc62b6380a8d39ba", url="https://pypi.org/packages/bf/79/78910eb0e899fffd558e8756e43318f1f6cbd47ef1a6995130ce575fa299/pyobjc-framework-SystemExtensions-9.0.1.tar.gz")
    version("9.0", sha256="1bef25c14dd9083bd09a5cf301001e60c7a6093d9ad3a204db3b739c72d844a8", url="https://pypi.org/packages/6c/1d/6af5b76a53489ecfbad0e4fa3cde676da17db7b657ceb911df7fb6301184/pyobjc-framework-SystemExtensions-9.0.tar.gz")
    version("8.5.1", sha256="fb2e2892cf5cf613c06c0316bcdd8f6c5d3a576b2b059145c9c01e3f71793cf9", url="https://pypi.org/packages/22/72/77291d8e1aad12bb8b73e8f3bcb9f5a549d36c93eaeded9365012f89c595/pyobjc-framework-SystemExtensions-8.5.1.tar.gz")
    version("8.5", sha256="fdc61bb91a91e8a3335b7675b939fb2f63dc636de0676f4c344d0f43d21de413", url="https://pypi.org/packages/15/95/e3142a449676698b6b3c3966684e29d0371daf91b16ae3776efc1dcb35a1/pyobjc-framework-SystemExtensions-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

