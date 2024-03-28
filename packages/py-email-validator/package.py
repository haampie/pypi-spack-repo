# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEmailValidator(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.1", sha256="97d882d174e2a65732fb43bfce81a3a834cbc1bde8bf419e30ef5ea976370a05", url="https://pypi.org/packages/e4/60/b02cb0f5ee0be88bd4fbfdd9cc91e43ec2dfcc47fe064e7c70587ff58a94/email_validator-2.1.1-py3-none-any.whl")
    version("2.1.0.post1", sha256="c973053efbeddfef924dc0bd93f6e77a1ea7ee0fce935aea7103c7a3d6d2d637", url="https://pypi.org/packages/09/68/d237a603d524ba052e292d71c89939bfa70e3ec7963b255cc3ef7a8770a0/email_validator-2.1.0.post1-py3-none-any.whl")
    version("2.1.0", sha256="4496ecc949b51e42d1c9e6159d57cd04ef017af57d2e366ed7fd998f1bf8af69", url="https://pypi.org/packages/90/41/4767ff64e422734487a06384a66e62615b1f5cf9cf3b23295e22d3ecf711/email_validator-2.1.0-py3-none-any.whl")
    version("2.0.0.post2", sha256="2466ba57cda361fb7309fd3d5a225723c788ca4bbad32a0ebd5373b99730285c", url="https://pypi.org/packages/b3/f1/1645adf5a12df4889bebc77701f2b44ba37409e7db92be9eef7dded2d04c/email_validator-2.0.0.post2-py3-none-any.whl")
    version("2.0.0.post1", sha256="26efa040ae50e65cc130667080fa0f372f0ac3d852923a76166a54cf6a0ee780", url="https://pypi.org/packages/ef/c7/92211f9a4678757e605fef6fcde9ffc1508adf34b894c476c4be02c99d10/email_validator-2.0.0.post1-py3-none-any.whl")
    version("2.0.0", sha256="07c61b62ee446e39274b18204afa8e422baf64570776045272b04d10c02f64f6", url="https://pypi.org/packages/6d/5b/bfecbb5d1ca9784f38ce8eba1c33a752a5cab505ef68f0566ebcc6f96d84/email_validator-2.0.0-py3-none-any.whl")
    version("1.3.1", sha256="49a72f5fa6ed26be1c964f0567d931d10bf3fdeeacdf97bc26ef1cd2a44e0bda", url="https://pypi.org/packages/ba/ec/adc595d04e795b04bb0028fc6b067713fdb4a7e8cec44b428f7144fc432e/email_validator-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="816073f2a7cffef786b29928f58ec16cdac42710a53bb18aa94317e3e145ec5c", url="https://pypi.org/packages/e7/d3/88997ca4903c70fb6eec2e29501a35f84aaf34790f207febdf188e374377/email_validator-1.3.0-py2.py3-none-any.whl")
    version("1.2.1", sha256="c8589e691cf73eb99eed8d10ce0e9cbb05a0886ba920c8bcb7c82873f4c5789c", url="https://pypi.org/packages/6b/d2/c587a9cd8473041fd138b213fa12581a4e039d260cf24dfa07f5c9de78e4/email_validator-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="2323219d19b82f887b64f2a84c6d73f451431bdf87744022c54b1b5bd0bde1bd", url="https://pypi.org/packages/8a/e0/27e88c86fc1b2adebb967c5f29a7f6eb3c5baf0e75dbe716d2c0b4d2fa0d/email_validator-1.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dnspython@2.0.0:", when="@2:")
        depends_on("py-dnspython@1.15:", when="@1.0.3:1")
        depends_on("py-idna@2:", when="@1.0.3:")
    # END DEPENDENCIES

