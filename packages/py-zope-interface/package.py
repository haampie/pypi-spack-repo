# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZopeInterface(PythonPackage):
    # BEGIN VERSIONS
    version("6.2", sha256="3b6c62813c63c543a06394a636978b22dffa8c5410affc9331ce6cdb5bfa8565", url="https://pypi.org/packages/cd/37/1b003190ba7148226a8212d98ff8074e212fef30c82e616bdb818ae1f838/zope.interface-6.2.tar.gz")
    version("6.1", sha256="2fdc7ccbd6eb6b7df5353012fbed6c3c5d04ceaca0038f75e601060e95345309", url="https://pypi.org/packages/87/03/6b85c1df2dca1b9acca38b423d1e226d8ffdf30ebd78bcb398c511de8b54/zope.interface-6.1.tar.gz")
    version("6.0", sha256="aab584725afd10c710b8f1e6e208dbee2d0ad009f57d674cb9d1b3964037275d", url="https://pypi.org/packages/7a/62/f0d012151af1e8cc0a6c97db74b78141143425dcdf81bc7960c498e28960/zope.interface-6.0.tar.gz")
    version("5.5.2", sha256="bfee1f3ff62143819499e348f5b8a7f3aa0259f9aca5e0ddae7391d059dce671", url="https://pypi.org/packages/38/6f/fbfb7dde38be7e5644bb342c4c7cdc444cd5e2ffbd70d091263b3858a8cb/zope.interface-5.5.2.tar.gz")
    version("5.5.1", sha256="6d678475fdeb11394dc9aaa5c564213a1567cc663082e0ee85d52f78d1fbaab2", url="https://pypi.org/packages/c5/ec/3e116b5c3c54f1fb7296a686c110c14d1242bbea17286c487892075d9858/zope.interface-5.5.1.tar.gz")
    version("5.5.0", sha256="700ebf9662cf8df70e2f0cb4988e078c53f65ee3eefd5c9d80cf988c4175c8e3", url="https://pypi.org/packages/62/ba/e517891d44208f2a6cf493109dfff59134bb922a9c8bd2a896da7d9a82a1/zope.interface-5.5.0.tar.gz")
    version("5.4.0", sha256="5dba5f530fec3f0988d83b78cc591b58c0b6eb8431a85edd1569a0539a8a5a0e", url="https://pypi.org/packages/ae/58/e0877f58daa69126a5fb325d6df92b20b77431cd281e189c5ec42b722f58/zope.interface-5.4.0.tar.gz")
    version("5.3.0", sha256="b18a855f8504743e0a2d8b75d008c7720d44e4c76687e13f959e35d9a13eb397", url="https://pypi.org/packages/b1/f8/aa59109d5345ece4820e8e7a05a97203ef21a0ac2c0460c6c929ea5be889/zope.interface-5.3.0.tar.gz")
    version("5.2.0", sha256="8251f06a77985a2729a8bdbefbae79ee78567dddc3acbd499b87e705ca59fe24", url="https://pypi.org/packages/84/21/80cdc749908ebf2719a9063eddcc02b668fbc62d200c1f1a4d92aaaba76b/zope.interface-5.2.0.tar.gz")
    version("5.1.2", sha256="c9c8e53a5472b77f6a391b515c771105011f4b40740ce53af8428d1c8ca20004", url="https://pypi.org/packages/e5/4f/86e90a34419df9c32a6e88b06f18233cffe93a236f7d2690f707c816fbe6/zope.interface-5.1.2.tar.gz")
    version("5.1.0", sha256="40e4c42bd27ed3c11b2c983fecfb03356fae1209de10686d03c02c8696a1d90e", url="https://pypi.org/packages/af/d2/9675302d7ced7ec721481f4bbecd28a390a8db4ff753d28c64057b975396/zope.interface-5.1.0.tar.gz")
    version("4.5.0", sha256="57c38470d9f57e37afb460c399eb254e7193ac7fb8042bd09bdc001981a9c74c", url="https://pypi.org/packages/ac/8a/657532df378c2cd2a1fe6b12be3b4097521570769d4852ec02c24bd3594e/zope.interface-4.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@4.4.2,4.6,6.1:")
    # END DEPENDENCIES

