##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydanticSettings(PythonPackage):
    version("2.2.1", sha256="0235391d26db4d2190cb9b31051c4b46882d28a51533f97440867f012d4da091", url="https://pypi.org/packages/99/ee/24ec87e3a91426497c5a2b9880662d19cfd640342d477334ebc60fc2c276/pydantic_settings-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="5f7bcaf9ad4419559dc5ac155c0324a9aeb2547c60471ee7c7d026f467a6b515", url="https://pypi.org/packages/b1/06/ec58f4deef618541f8285bb722bc888d152f4a92a54443d8c9b808661020/pydantic_settings-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="7621c0cb5d90d1140d2f0ef557bdf03573aac7035948109adf2574770b77605a", url="https://pypi.org/packages/5d/c9/8042368e9a1e6e229b5ec5d88449441a3ee8f8afe09988faeb190af30248/pydantic_settings-2.1.0-py3-none-any.whl")
    version("2.0.3", sha256="ddd907b066622bd67603b75e2ff791875540dc485b7307c4fffc015719da8625", url="https://pypi.org/packages/46/92/918ef6b14d54c6a4fccdecd65b3ee15360ca2b4aa52d5c9c4f39f99b4c56/pydantic_settings-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="6183a2abeab465d5a3ab69758e9a22d38b0cc2ba193f0b85f6971a252ea630f6", url="https://pypi.org/packages/9c/3e/3311eeab406db6116e7f2d4ed9b05c2811282143efa55feb12cc513a8b84/pydantic_settings-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="579bbcbec3501e62bab73867b097ae10218201950e897463c98a182ffe7ed104", url="https://pypi.org/packages/05/fe/ed5f64a49b72af12244dec414e85cb006b5e011325e1ae7e373128a33444/pydantic_settings-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="11179e6f1837a129bd7854bcce21006cbcb7e8a988f8ae7239a09a28d2ad35fd", url="https://pypi.org/packages/24/3e/a7733506319a483c04f88719b817c4b6f2c5c22be9ff2c27b1fa89d670de/pydantic_settings-2.0.0-py3-none-any.whl")
    version("2.0-beta2", sha256="f30630781bba8bec76d679e3a6eedeee7ea345546fd57de7dc27acfe16bce074", url="https://pypi.org/packages/e3/33/629b53e9c3b7fd27f25fc6f19cc60d688251afc9332e358a68330dd3bb87/pydantic_settings-2.0b2-py3-none-any.whl")
    version("1.99", sha256="2bd45d80b0b5597e1252288e073742f48ba13b57ad604cc6e2fce40bf131a4c4", url="https://pypi.org/packages/eb/37/1a0ebb6a69be0f8c2419d67ae363d6672d1aab841f0f35672597d00fc15f/pydantic_settings-1.99-py3-none-any.whl")
    version("0.2.5", sha256="347991a2d96674dc9a412b6306d2fa1d84605e16d5180b04763ec4280116dbee", url="https://pypi.org/packages/ab/8e/ec99b1a4731fc4dc0aa683f6ca8d124a17206883f67ca2eeeb4fa98f9f78/pydantic_settings-0.2.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-attrs@19", when="@:0")
        depends_on("py-class-doc@0.2:0.2.0", when="@0.2:0")
        depends_on("py-pydantic@2.5:", when="@2.1:")
        depends_on("py-pydantic@2.0.1:", when="@2.0.1:2.0")
        depends_on("py-pydantic@2.0-beta3:", when="@2.0-beta2:2.0.0")
        depends_on("py-pydantic@2.0-alpha3", when="@1:2.0-alpha4")
        depends_on("py-pydantic", when="@0.1.2-beta0:0")
        depends_on("py-python-dotenv@0.21:", when="@1:")
        depends_on("py-pyyaml@5.1.2:5", when="@:0")
        depends_on("py-tomlkit@0.5.5:0.5", when="@:0")
        depends_on("py-typing-extensions@3.7.4:3", when="@:0")

