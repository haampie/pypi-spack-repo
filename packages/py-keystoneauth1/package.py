##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKeystoneauth1(PythonPackage):
    version("5.6.0", sha256="d740843afcf9c159fb929004eee1eecf46573236901e9d8ca2dca5694733a379", url="https://pypi.org/packages/2f/14/dfc5af6ec3918aacaac8ce1bbdca034351538617e104ae7a5e38754e2e55/keystoneauth1-5.6.0-py3-none-any.whl")
    version("5.5.0", sha256="af944cecf3634fca3fffe5426ddf925e2b671653e03f54482876a9df25c03296", url="https://pypi.org/packages/fc/c7/a73d5581ef4655e35e24047396f4b378a0cb505a6aec3d9c5fb8524cfc44/keystoneauth1-5.5.0-py3-none-any.whl")
    version("5.4.0", sha256="125c70dc7a2a6d8906d436d0e853a75c022505007422b98970a1e693a2002c6e", url="https://pypi.org/packages/b1/69/822db60e8f93473faa486c52b376f33bad40d0fe705236fa61cd664e28b5/keystoneauth1-5.4.0-py3-none-any.whl")
    version("5.3.0", sha256="174407998ecdee31234b6f84bef2fd440949b0ad66a49ddcbe978952589485d5", url="https://pypi.org/packages/4d/6d/848bd88ec530df8f46cacd82f2e3de2cb8226000b36db73f4dbf6a0c6750/keystoneauth1-5.3.0-py3-none-any.whl")
    version("5.2.1", sha256="d2fcfdcfe347df8d92390e0806b4969289d884cd9ec3519e4c5aec53e66d0767", url="https://pypi.org/packages/78/36/f71f4a9eff65e7164963af7f53e1be3987b49e41f885e93ae3fbd14826de/keystoneauth1-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="84feba003301c2042693eb9366b0008eabd47b221c65f8106f0049f54eba989d", url="https://pypi.org/packages/c7/37/58353e4e1e08508d55c2c8ff67da1abe42c7ac8b136024899d5051d3aa8f/keystoneauth1-5.2.0-py3-none-any.whl")
    version("5.1.2", sha256="dc71d6a5d22bbf69b024d7dc7ca1e1213cbcc91a3a7d437a68cb3013a53d1633", url="https://pypi.org/packages/29/d6/c7cdfc9e0e0a4a6e9261002006f03b8ca4665e3cca24f38f2fcc7a6a2435/keystoneauth1-5.1.2-py3-none-any.whl")
    version("5.1.1", sha256="7fd532490ce4cf3f41d7b3a5804bf293fc58e2d88b8365d4cad90c0faf95f68f", url="https://pypi.org/packages/db/54/a73c38ded20fce781db3d3a43e1db27849c3950a973061478bf6cb8402ce/keystoneauth1-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="5f7a60efff415bd74ce57f3ceb21612deae940746bbb69e36b7b350390d7f5dc", url="https://pypi.org/packages/78/83/6437bcc3a46baf98b75d4afa024a9025842f32f7fb162f70106c90b238b4/keystoneauth1-5.1.0-py3-none-any.whl")
    version("5.0.1", sha256="a75fa94d38e2848ea300a3f64f48b74b435ca91e60f4c2b9eefe36f3fa3b53e1", url="https://pypi.org/packages/fe/e7/8298d6fe0017031244e28345a0dde4254b5ddad9c7f8b5e2c5bb03942a49/keystoneauth1-5.0.1-py3-none-any.whl")
    version("4.3.1", sha256="c4a80b79bc3e0412eb127fa761e80912614f8563646ca34b62bcd9d533f93077", url="https://pypi.org/packages/7a/1b/8c5d1fd19b9e08d3a3b64492d078039c7ddd166c3cf029154f1c5f0439f7/keystoneauth1-4.3.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-iso8601@0.1.11:", when="@2.7:")
        depends_on("py-os-service-types@1.2:", when="@3.6:")
        depends_on("py-pbr@2:2.0,3:", when="@2.20:")
        depends_on("py-requests@2.14.2:", when="@3:")
        depends_on("py-six@1.10:", when="@3.3:5.1")
        depends_on("py-stevedore@1.20:", when="@2.19:")

