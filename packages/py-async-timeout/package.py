##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsyncTimeout(PythonPackage):
    version("4.0.3", sha256="7405140ff1230c310e51dc27b3145b9092d659ce68ff733fb0cefe3ee42be028", url="https://pypi.org/packages/a7/fa/e01228c2938de91d47b307831c62ab9e4001e747789d0b05baf779a6488c/async_timeout-4.0.3-py3-none-any.whl")
    version("4.0.2", sha256="8ca1e4fcf50d07413d66d1a5e416e42cfdf5851c981d679a09851a6853383b3c", url="https://pypi.org/packages/d6/c1/8991e7c5385b897b8c020cdaad718c5b087a6626d1d11a23e1ea87e325a7/async_timeout-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="a22c0b311af23337eb05fcf05a8b51c3ea53729d46fb5460af62bee033cec690", url="https://pypi.org/packages/41/4a/2ca8802045b6df8dd25a0f8f7c216808e9e3bff2809efe4a36cc99d35cca/async_timeout-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="f3303dddf6cafa748a92747ab6c2ecf60e0aeca769aee4c151adfce243a05d9b", url="https://pypi.org/packages/53/a9/cd484af830e5c525553da1a585ff4fe6f1d91a12f0131c736a3ef0d99cce/async_timeout-4.0.0-py3-none-any.whl")
    version("4.0.0-alpha3", sha256="b57eb8bc4e9693d4be1c97d93ccf8225908903dcc6440e1f8bf0b785c1ac2478", url="https://pypi.org/packages/b8/95/caf486ee569cad74c95d4dfaeeb4e09cccb338238e7650e27d4c3a4b0262/async_timeout-4.0.0a3-py3-none-any.whl")
    version("4.0.0-alpha2", sha256="0b0e3079aaca061347d171961953782c97f7b9c5eb29310eb8e5150f7931dcba", url="https://pypi.org/packages/c3/2b/18a2d8d215ae4f0445c8ec640557195d5453b8bb4c0bbbaee7f3e459a8be/async_timeout-4.0.0a2-py3-none-any.whl")
    version("4.0.0-alpha1", sha256="3d4af2e9e059ec21e0e574e53a7488fb56c992166b49435ab0eb15062e254f4c", url="https://pypi.org/packages/65/b0/80595f272668ba6f5a7d153c67f3fadd6ea76b761c91387329b67f64531d/async_timeout-4.0.0a1-py3-none-any.whl")
    version("4.0.0-alpha0", sha256="933801327e45710045d0822476725b5a399af4560f96e1d3650a77db594f20a4", url="https://pypi.org/packages/2f/1b/8a8183d457fc4c7fb2015be0a0ae26cb64dc576558b1cc9f0ac830d08295/async_timeout-4.0.0a0-py3-none-any.whl")
    version("3.0.1", sha256="4291ca197d287d274d0b6cb5d6f8f8f82d434ed288f962539ff18cc9012f9ea3", url="https://pypi.org/packages/e1/1e/5a4441be21b0726c4464f3f23c8b19628372f606755a9d2e46c187e65ec4/async_timeout-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="474d4bc64cee20603e225eb1ece15e248962958b45a3648a9f5cc29e827a610c", url="https://pypi.org/packages/96/0f/e6357458c87fb4ed8f3df215773f3caad40968f10e05552cbd8bd28415e4/async_timeout-3.0.0-py3-none-any.whl")
    version("2.0.1", sha256="9093db5b8ddbe4b8f6885d1a6e0ad84ae3155464cbf6877c387605244c285f3c", url="https://pypi.org/packages/1d/b9/213521db2918b5b7f7df333a33ea3d38ba70ba705d9db6c29f0343c213ea/async_timeout-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="d3a195a827b0f4068d1616ae2da04aac62e365d14f2b13dbc071f9feed9db4e2", url="https://pypi.org/packages/16/6c/9a34c589658d63bb331db5a4a745f0f9814860a3ddadd10376965eb97ac0/async_timeout-2.0.0-py3-none-any.whl")
    version("1.4.0", sha256="5b5c855783f65dfda72fc15ca538070188776ece811408867e64dd3cce53371d", url="https://pypi.org/packages/d3/29/294a79872545bdd4765a6e1afd04bbc4c5ee4efb5baa2094794abe5dc46b/async_timeout-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="087a26de8b926d41087c56bb7f70d9b5480c119e4b56589d431206d24508a131", url="https://pypi.org/packages/90/bb/2dc6e9a9c2e9958c4f2028b4d391734a63209da03d15cca72dd70063c4f5/async_timeout-1.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-typing-extensions@3.6.5:", when="@4.0.0-alpha2:4.0.1")

