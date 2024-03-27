##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKombu(PythonPackage):
    version("5.3.5", sha256="0eac1bbb464afe6fb0924b21bf79460416d25d8abc52546d4f16cad94f789488", url="https://pypi.org/packages/f7/88/daca086d72832c74a7e239558ad484644c8cda0b9ae8a690f247bf13c268/kombu-5.3.5-py3-none-any.whl")
    version("5.3.4", sha256="63bb093fc9bb80cfb3a0972336a5cec1fa7ac5f9ef7e8237c6bf8dda9469313e", url="https://pypi.org/packages/a8/cc/24160d61e8c44bd76a775017c0859a403db471ddbd701e725fdf2becafa6/kombu-5.3.4-py3-none-any.whl")
    version("5.3.3", sha256="6cd5c5d5ef77538434b8f81f3e265c414269418645dbb47dbf130a8a05c3e357", url="https://pypi.org/packages/c4/05/0504dce43327e610cbe05c223691992bdb0212202bb830f105d57641665f/kombu-5.3.3-py3-none-any.whl")
    version("5.3.2", sha256="b753c9cfc9b1e976e637a7cbc1a65d446a22e45546cd996ea28f932082b7dc9e", url="https://pypi.org/packages/86/dc/8a252a772d3a18008fab6fd3ec1bed16a6c3351260a1023c8e8f95759454/kombu-5.3.2-py3-none-any.whl")
    version("5.3.1", sha256="48ee589e8833126fd01ceaa08f8a2041334e9f5894e5763c8486a550454551e9", url="https://pypi.org/packages/63/58/b23b9c1ffb30d8b5cdfc7bdecb17bfd7ea20c619e86e515297b496177144/kombu-5.3.1-py3-none-any.whl")
    version("5.3.0", sha256="fa9be55281bb351ba9da582b2a74e3dd5015b8d075b287e4d16f0b2f25fefcc2", url="https://pypi.org/packages/7d/a4/09517596299ee8b7f27e39ac0867949bd2f6f6025aa02fcdc17a2c2a5885/kombu-5.3.0-py3-none-any.whl")
    version("5.3.0-rc2", sha256="10f17896f9d5dc28b80a882badbd333931c77c82aaa45cd4b84fcdc74398ff2b", url="https://pypi.org/packages/b1/07/b9a5b27445f481e6ea80647d95624719fd81e6f6a2932c8fed05a4706178/kombu-5.3.0rc2-py3-none-any.whl")
    version("5.3.0-rc1", sha256="1d565fd1aad51f7bca86ba35dee7857303007de64a4500b8a86d83634380c487", url="https://pypi.org/packages/8c/6a/254262fbc68548a8a6051ce329c16ed84996c12afeef9c48e9d3943e36e1/kombu-5.3.0rc1-py3-none-any.whl")
    version("5.2.4", sha256="8b213b24293d3417bcf0d2f5537b7f756079e3ea232a8386dcc89a59fd2361a4", url="https://pypi.org/packages/d9/f3/62d12dd7ebad710319f0877c1c33bca379fc7d28069daae890fa2fa444c8/kombu-5.2.4-py3-none-any.whl")
    version("5.2.3", sha256="eeaeb8024f3a5cfc71c9250e45cddb8493f269d74ada2f74909a93c59c4b4179", url="https://pypi.org/packages/6b/e6/79f5fc77b8f54de7e3d8bdf382b2ca23e85ed35095801851003e70028f2f/kombu-5.2.3-py3-none-any.whl")
    version("5.0.2", sha256="6dc509178ac4269b0e66ab4881f70a2035c33d3a622e20585f965986a5182006", url="https://pypi.org/packages/22/6e/69bc1061633a88aa47beaa8bbecff1c3c555a005603cfbebcec4aa37f183/kombu-5.0.2-py2.py3-none-any.whl")
    version("4.6.11", sha256="be48cdffb54a2194d93ad6533d73f69408486483d189fe9f5990ee24255b0e0a", url="https://pypi.org/packages/9e/34/3eea6a3a9ff81b0c7ddbdceb22a1ffc1b5907d863f27ca19a68777d2211d/kombu-4.6.11-py2.py3-none-any.whl")
    version("4.6.6", sha256="e7465aa85a1db889116819f08c5de29520d2fa103324dcdca5e90af345f01771", url="https://pypi.org/packages/f7/86/496db94e44c6d0a16a52a1b539b5315d98e8aa59d14a8d4f1009d4eab6c2/kombu-4.6.6-py2.py3-none-any.whl")
    version("4.5.0", sha256="7b92303af381ef02fad6899fd5f5a9a96031d781356cd8e505fa54ae5ddee181", url="https://pypi.org/packages/b7/af/1914e93314f1b98756d5c5e366193124a0ffaab0e6d0e51e0f6f65fa851d/kombu-4.5.0-py2.py3-none-any.whl")
    version("4.3.0", sha256="7a2cbed551103db9a4e2efafe9b63222e012a61a18a881160ad797b9d4e1d0a1", url="https://pypi.org/packages/29/48/c709a54c8533ed46fd868e593782c6743da33614f8134b82bc0955455031/kombu-4.3.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-amqp@5.1.1:", when="@5.3:")
        depends_on("py-amqp@5.0.9:", when="@5.2.3:5.2")
        depends_on("py-amqp@5.0.0:", when="@5.0.2:5.0")
        depends_on("py-amqp@2.6:2", when="@4.6.9:5.0.1")
        depends_on("py-amqp@2.5.2:2.5", when="@4.6.6:4.6.8")
        depends_on("py-amqp@2.4:2", when="@4.3:4.5")
        depends_on("py-backports-zoneinfo@0.2.1:+tzdata", when="@5.3.0: ^python@:3.8")
        depends_on("py-backports-zoneinfo@0.2.1:", when="@5.3.0-rc2 ^python@:3.8")
        depends_on("py-importlib-metadata@0.18:", when="@4.6.4:4.6.6")
        depends_on("py-typing-extensions", when="@5.3: ^python@:3.9")
        depends_on("py-vine", when="@5.1:")

