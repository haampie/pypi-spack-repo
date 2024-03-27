##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTomlkit(PythonPackage):
    version("0.12.4", sha256="5cd82d48a3dd89dee1f9d64420aa20ae65cfbd00668d6f094d7578a78efbb77b", url="https://pypi.org/packages/07/fa/c96545d741f2fd47f565e4e06bfef0962add790cb9c2289d900102b55eca/tomlkit-0.12.4-py3-none-any.whl")
    version("0.12.3", sha256="b0a645a9156dc7cb5d3a1f0d4bab66db287fcb8e0430bdd4664a095ea16414ba", url="https://pypi.org/packages/6e/43/159750d32481f16e34cc60090b53bc0a14314ad0c1f67a9bb64f3f3a0551/tomlkit-0.12.3-py3-none-any.whl")
    version("0.12.2", sha256="eeea7ac7563faeab0a1ed8fe12c2e5a51c61f933f2502f7e9db0241a65163ad0", url="https://pypi.org/packages/15/27/c53c6505ae6c94b7e11521e19855d7838396b9da09a519cf5f107df359a4/tomlkit-0.12.2-py3-none-any.whl")
    version("0.12.1", sha256="712cbd236609acc6a3e2e97253dfc52d4c2082982a88f61b640ecf0817eab899", url="https://pypi.org/packages/a0/6d/808775ed618e51edaa7bbe6759e22e1c7eafe359af6e084700c6d39d3455/tomlkit-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="926f1f37a1587c7a4f6c7484dae538f1345d96d793d9adab5d3675957b1d0766", url="https://pypi.org/packages/68/4f/12207897848a653d03ebbf6775a29d949408ded5f99b2d87198bc5c93508/tomlkit-0.12.0-py3-none-any.whl")
    version("0.11.8", sha256="8c726c4c202bdb148667835f68d68780b9a003a9ec34167b6c673b38eff2a171", url="https://pypi.org/packages/ef/a8/b1c193be753c02e2a94af6e37ee45d3378a74d44fe778c2434a63af92731/tomlkit-0.11.8-py3-none-any.whl")
    version("0.11.7", sha256="5325463a7da2ef0c6bbfefb62a3dc883aebe679984709aee32a317907d0a8d3c", url="https://pypi.org/packages/c0/83/eb757ef200543637c40f136e370ef05158d4079ad61da2cf455fe34c508d/tomlkit-0.11.7-py3-none-any.whl")
    version("0.11.6", sha256="07de26b0d8cfc18f871aec595fda24d95b08fef89d147caa861939f37230bf4b", url="https://pypi.org/packages/2b/df/971fa5db3250bb022105d17f340339370f73d502e65e687a94ca1a4c4b1f/tomlkit-0.11.6-py3-none-any.whl")
    version("0.11.5", sha256="f2ef9da9cef846ee027947dc99a45d6b68a63b0ebc21944649505bf2e8bc5fe7", url="https://pypi.org/packages/df/b6/310fe14933403413f7352be0c8e75b7ed23db2170d769ed69e40f40130a3/tomlkit-0.11.5-py3-none-any.whl")
    version("0.11.4", sha256="25d4e2e446c453be6360c67ddfb88838cfc42026322770ba13d1fbd403a93a5c", url="https://pypi.org/packages/18/31/2a87f292f752d39c6c207f9e44137e3e1d4250da880a9fbc0bbf630138e0/tomlkit-0.11.4-py3-none-any.whl")
    version("0.11.0", sha256="0f4050db66fd445b885778900ce4dd9aea8c90c4721141fde0d6ade893820ef1", url="https://pypi.org/packages/96/6b/67e390f8efdd095c4fce0fa648ad711eb795fef2d954a01c289238e39076/tomlkit-0.11.0-py3-none-any.whl")
    version("0.7.2", sha256="173ad840fa5d2aac140528ca1933c29791b79a374a0861a80347f42ec9328117", url="https://pypi.org/packages/eb/ef/5bd27c1a8040874cc863c263bf38857b5607017b656943c6c93b29bc8f42/tomlkit-0.7.2-py2.py3-none-any.whl")
    version("0.7.0", sha256="6babbd33b17d5c9691896b0e68159215a9387ebfa938aa3ac42f4a4beeb2b831", url="https://pypi.org/packages/bc/01/a0ee34fe37dd54f795e8f8a820af57c9a94d7358276acf6cdc21ae8d9533/tomlkit-0.7.0-py2.py3-none-any.whl")
    version("0.5.11", sha256="4e1bd6c9197d984528f9ff0cc9db667c317d8881288db50db20eeeb0f6b0380b", url="https://pypi.org/packages/7d/8c/c3ee9cd41b2df781b2dc39c31209724b4f04a3110b46531de2e661ace186/tomlkit-0.5.11-py2.py3-none-any.whl")
    version("0.5.10", sha256="5ca7863ebd6046256147198ced158266cdb1ad6679df61ba77d2533386b8367a", url="https://pypi.org/packages/e1/91/3a2f6fcd9baa59b516a3e11cec7209d57287268562e43998e1455bb8c48e/tomlkit-0.5.10-py2.py3-none-any.whl")
    version("0.5.9", sha256="ef2063736ab48a4504597c6e134d7d8e3adb604b2d34dbdb7eb7a238bbce2813", url="https://pypi.org/packages/d5/0d/a8149aece3dbd7bd1cb3e7a8f955ef98806cede5d6bf3f25ef51d0bcb602/tomlkit-0.5.9-py2.py3-none-any.whl")
    version("0.5.8", sha256="96e6369288571799a3052c1ef93b9de440e1ab751aa045f435b55e9d3bcd0690", url="https://pypi.org/packages/3e/30/7c2693fc50bd466285ec22bf02ee344be1bde3e2e8267e302fdc82d11f2d/tomlkit-0.5.8-py2.py3-none-any.whl")
    version("0.5.7", sha256="6c1c8af5d98468e9d2b07db2060ae2bc6fe204bda7f32f46a6255b50fe78a71c", url="https://pypi.org/packages/7a/16/0d282673450911053452f3166c79580f0280ac82fe85f44e0c3bb7af427d/tomlkit-0.5.7-py2.py3-none-any.whl")
    version("0.5.6", sha256="18f488e4d65db8159e09f0eabe27b039bbaa2e3b55195e47ad9e8dd8d3ebb27a", url="https://pypi.org/packages/97/c2/533e295eb072098b48886b6f4dca640c72b04abf3d8eaa201417bc37a933/tomlkit-0.5.6-py2.py3-none-any.whl")
    version("0.5.5", sha256="c6b0c11b85e888c12330c7605d43c1446aa148cd421163f90ca46ea813f2c336", url="https://pypi.org/packages/29/22/716eb55bb154d2519752a2d91cf7e91d58dd24e8150c47aaaa67aae75aa6/tomlkit-0.5.5-py2.py3-none-any.whl")


