# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEmoji(PythonPackage):
    # BEGIN VERSIONS
    version("2.10.1", sha256="11fb369ea79d20c14efa4362c732d67126df294a7959a2c98bfd7447c12a218e", url="https://pypi.org/packages/98/00/00d56e704d69cee4a92b1d517676579b4af5f2f8bc72946c464a504705b2/emoji-2.10.1-py2.py3-none-any.whl")
    version("2.10.0", sha256="aed4332caa23553a7218f032c08b0a325ae53b010f7fb98ad272c0f7841bc1d3", url="https://pypi.org/packages/8d/97/fbe537350214b0489e6c7052b9e8928a85ed5febb621a82cc5437dbf17e7/emoji-2.10.0-py2.py3-none-any.whl")
    version("2.9.0", sha256="17b0d53e1d9f787307a4c65aa19badb0a1ffdbc89b3a3cd851fc77821cdaced2", url="https://pypi.org/packages/03/40/91d0c9fe5a0b494c0fdbcacda4d203aea39f8293e69c70129389308ca928/emoji-2.9.0-py2.py3-none-any.whl")
    version("2.8.0", sha256="a8468fd836b7ecb6d1eac054c9a591701ce0ccd6c6f7779ad71b66f76664df90", url="https://pypi.org/packages/96/c6/0114b2040a96561fd1b44c75df749bbd3c898bf8047fb5ce8d7590d2dee6/emoji-2.8.0-py2.py3-none-any.whl")
    version("2.7.0", sha256="375cc08589704266099846c553b6572ec5be591374b4d2cd1623b8343d5c9abb", url="https://pypi.org/packages/97/15/97a951a9befc0f17fb24685f06bdf17487a2d922593d8fe12934612523a6/emoji-2.7.0.tar.gz")
    version("2.6.0", sha256="39ad95c9ba270cdfbd141d20c2ebcfc4e295d010b605de66908a098a3ba63a3c", url="https://pypi.org/packages/de/e6/4a7eb9de0d78022cb759994c8cf517d19eb3fd12720cdf8ec4d92773c91e/emoji-2.6.0.tar.gz")
    version("2.5.1", sha256="8e5ec80f56dd1fe38f4c4847b9ea6f18d4ad94d0b8dd135b0b2355ddf56d6d62", url="https://pypi.org/packages/05/73/0b381e376dbd396717bd2963eda0f674ff8d1af840faa83e7020c2fc55f9/emoji-2.5.1.tar.gz")
    version("2.5.0", sha256="0e048dd540a0644bd30790b540466492f1487a3788528422fe196a939a7a3ac0", url="https://pypi.org/packages/97/32/76ad03dfe94ca7753986974f914b31150323608339c2eafbc4c068bc3049/emoji-2.5.0.tar.gz")
    version("2.4.0", sha256="72b918412f7059f57b0f0b0c27f3458802c4c97a2f039f4732610c2582b6c9e4", url="https://pypi.org/packages/8e/a6/37e16414bb538ed3e45d7e8ab1e3ba975c058b3a14a2e9a2094fa370a909/emoji-2.4.0.tar.gz")
    version("2.3.0", sha256="bb51b176ac80fb147b20198e961d4d872fb39650a62df941ca2b51f30f63c466", url="https://pypi.org/packages/7e/45/4d31fde618eb51ee804220aad413c4c8610c87341a31249c090f48f56e2f/emoji-2.3.0.tar.gz")
    version("1.7.0", sha256="65c54533ea3c78f30d0729288998715f418d7467de89ec258a31c0ce8660a1d1", url="https://pypi.org/packages/68/8a/b08dd0b946f0843cba782e3784cd979c33f144e5e7c37fb0162dc47acd43/emoji-1.7.0.tar.gz")
    version("1.6.3", sha256="cc28bdc1010b1c03c241f69c7af1e8715144ef45a273bfadc14dc89319ba26d0", url="https://pypi.org/packages/83/db/beeea7a485754d0841935bb7b2ad22816b2a71d3472b5eca55dce83b5d6f/emoji-1.6.3.tar.gz")
    version("1.6.1", sha256="53d61a8e4c025f6c295ab99c842302c66d47952199c4fde66dd060dee3ad4324", url="https://pypi.org/packages/17/f0/7db2f4d8651951ff4a51ee77f0ffe0b3d015cd963c941c7390b3ba9fb302/emoji-1.6.1.tar.gz")
    version("1.6.0", sha256="379610aeeb10c62876d89472e6ed514971512a51224d4845c117681258eda845", url="https://pypi.org/packages/f9/93/3d26f850b2dcb750dd07b0305d3ac7a916e161c4f9a2263edb02a66dbfc1/emoji-1.6.0.tar.gz")
    version("1.5.0", sha256="2eddd062f940924fb25a3108d84d77dc571927d91a419b4c30f37e253c791b19", url="https://pypi.org/packages/04/f1/efe9360dbbdcf045620d8fb2fb79df36468a0a616578e907ccf0c71b52d7/emoji-1.5.0.tar.gz")
    version("1.4.2", sha256="21257f311e24468031e85685867c00b87249dc7612b82dc763a771ba5fb00c01", url="https://pypi.org/packages/75/eb/e09f7986f83c4bd711f0c81482f12a48742b9a7473a7ac0a97b8bcc9dd4b/emoji-1.4.2.tar.gz")
    version("1.4.1", sha256="6b539615c0b31b4274e10db949672c9cd1e6d3d8eb835ef421d11db3f46066d8", url="https://pypi.org/packages/1a/88/790b944f1769cfcd7e84f745ac2a0d543fede42442ca100931e6466d01b0/emoji-1.4.1.tar.gz")
    version("1.4.0", sha256="272d38308a949d8d8ca4ee7d033469201496465495b07d91a3ee32e8fe99dd65", url="https://pypi.org/packages/08/8f/c6cad83e6261114a612870a21832e4700f05fcacff8bd7e362a0af3c5acf/emoji-1.4.0.tar.gz")
    version("1.2.0", sha256="6b19b65da8d6f30551eead1705539cc0eadcd9e33a6ecbc421a29b87f96287eb", url="https://pypi.org/packages/24/fa/b3368f41b95a286f8d300e323449ab4e86b85334c2e0b477e94422b8ed0f/emoji-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="153fbf06eb5a111ca2b0c04f6f14ec3be434946a302f7892bf4c30446e050381", url="https://pypi.org/packages/79/0d/c06a34f306a219fd32b9d0297d999e3551d0ecee8190dce921602db4094c/emoji-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

