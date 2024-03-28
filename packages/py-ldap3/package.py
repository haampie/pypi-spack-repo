# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLdap3(PythonPackage):
    # BEGIN VERSIONS
    version("2.9.1", sha256="5869596fc4948797020d3f03b7939da938778a0f9e2009f7a072ccf92b8e8d70", url="https://pypi.org/packages/4e/f6/71d6ec9f18da0b2201287ce9db6afb1a1f637dedb3f0703409558981c723/ldap3-2.9.1-py2.py3-none-any.whl")
    version("2.9", sha256="c1df41d89459be6f304e0ceec4b00fdea533dbbcd83c802b1272dcdb94620b57", url="https://pypi.org/packages/3f/fb/00547465dc9d02cc1ceab8b5700dd4aebce53759ee26c7cf8d91bf3cf3e3/ldap3-2.9-py2.py3-none-any.whl")
    version("2.8.1", sha256="7c3738570766f5e5e74a56fade15470f339d5c436d821cf476ef27da0a4de8b0", url="https://pypi.org/packages/01/e7/5f51c1f0261483b999da07b93d67a8dc073eee246b2b3508da521b6af0b0/ldap3-2.8.1-py2.py3-none-any.whl")
    version("2.8", sha256="df27407f4991f25bd669b5bb1bc8cb9ddf44a3e713ff6b3afeb3b3c26502f88f", url="https://pypi.org/packages/f8/ab/0c9d57b052f67c93ac2dab75a28be06222cfe73df37cd464e16f4d60b776/ldap3-2.8-py2.py3-none-any.whl")
    version("2.7", sha256="81df4ac8b6df10fb1f05b17c18d0cb8c4c344d5a03083c382824960ed959cf5b", url="https://pypi.org/packages/7e/22/c942210f4ad383ccf9e4b0980a2922f0af7452be811c56d585748b9a5a01/ldap3-2.7-py2.py3-none-any.whl")
    version("2.6.1", sha256="1898194d872539670a2f36d4b56fe5a35d4b9ead28103bec78f05a8993e8122f", url="https://pypi.org/packages/06/a8/d53156e4c465b7a0dd57585e66473e4036e3bd9484a301fbd78383b57a28/ldap3-2.6.1-py2.py3-none-any.whl")
    version("2.6", sha256="a92e380a0265963dc5507580ecd51eb84677e00c3d7800517b6442ef046f6ece", url="https://pypi.org/packages/b5/3c/57f87ba620248f003e36cbc2f7b163d9a865bcfe13a82272b0543f72a09b/ldap3-2.6-py2.py3-none-any.whl")
    version("2.5.2", sha256="dd9be8ea27773c4ffc18ede0b95c3ca1eb12513a184590b9f8ae423db3f71eb9", url="https://pypi.org/packages/54/93/55d4de43abf3af1b60befa648811538b49701237e5cbda456608384b25ac/ldap3-2.5.2-py2.py3-none-any.whl")
    version("2.5.1", sha256="cc09951809678cfb693a13a6011dd2d48ada60a52bd80cb4bd7dcc55ee7c02fd", url="https://pypi.org/packages/86/ff/439de3a80632ba187511dbdcac43c9d8e1649271f5af5e997d9ed1410291/ldap3-2.5.1.tar.gz")
    version("2.5", sha256="5a25d825de9c2e9f9bb1eeb8a96822fd1d4739ee00e797beb400f45e497a502e", url="https://pypi.org/packages/f6/d9/a9db559375543af5ff950198a433bbc34bf7e8afbd32ab22231d0959710a/ldap3-2.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyasn1@0.4.6:", when="@2.8:")
        depends_on("py-pyasn1@0.1.8:", when="@:1,2.1.1:2.5.0,2.5.2:2.7")
    # END DEPENDENCIES

