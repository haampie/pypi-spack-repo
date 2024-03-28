# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGitdb2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.3.post1", sha256="f4c17cc3389772557b624e0208ed7cb854c6d7e95962da81e3a3ccd32f7c4b2e", url="https://pypi.org/packages/90/f4/7adc5862e6f094216c9e2d0c72dffadd89877c1626255ad1742495491ab6/gitdb2-3.0.3.post1-py2.py3-none-any.whl")
    version("3.0.3", sha256="d3000288f8799606e15aff2707ddd3ebb60335e9b106ca620328ba2985413c68", url="https://pypi.org/packages/18/bb/cc9d6877d95c536ea9d2fa3670b72df09fd0005957d5dbaca1adf1207fe0/gitdb2-3.0.3-py2.py3-none-any.whl")
    version("3.0.2", sha256="b2b3a67090c17dc61f8407ca485e79ae811225ab5ebcd98ac5ee01448e8987b5", url="https://pypi.org/packages/18/a8/370c8767e9d4133cdb1192ac42f377d09975bd0494e6a896b21462cc4679/gitdb2-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="6e46b9a55fc23d444b1dd984247df81a98c7b55b84a45ce14f3aa3c77b152118", url="https://pypi.org/packages/73/a2/35eaf268ee43884fcec35979be80ea23eac70c9a20ddea5de588a1d450ac/gitdb2-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="0a84c85d07166cefaf10fa4b728a8a1b847a7f0d081e2fbe083185462158c126", url="https://pypi.org/packages/17/5e/4ec98f192bbf783917c0d68f23fb588a8f394fed67b90197786bdb30d0c7/gitdb2-3.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-smmap2@2", when="@3.0.3:3")
        depends_on("py-smmap2@2:", when="@:3.0.2")
    # END DEPENDENCIES

