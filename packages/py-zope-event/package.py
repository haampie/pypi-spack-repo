##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZopeEvent(PythonPackage):
    version("5.0", sha256="2832e95014f4db26c47a13fdaef84cef2f4df37e66b59d8f1f4a8f319a632c26", url="https://pypi.org/packages/fe/42/f8dbc2b9ad59e927940325a22d6d3931d630c3644dae7e2369ef5d9ba230/zope.event-5.0-py3-none-any.whl")
    version("4.6", sha256="73d9e3ef750cca14816a9c322c7250b0d7c9dbc337df5d1b807ff8d3d0b9e97c", url="https://pypi.org/packages/8b/a8/3ab9648dc08d2ab7543145ec174a2d982d08fb996d50d9a4d3e057da7132/zope.event-4.6-py2.py3-none-any.whl")
    version("4.5.1", sha256="8cca6074a2bbca140d32704694e74098d5621f2c75ea6e3a9458240a3b5382a9", url="https://pypi.org/packages/29/ee/ade65f9bce824800c55e4aba8822ff949a61f6be35ab291fda62a9db4698/zope.event-4.5.1-py2.py3-none-any.whl")
    version("4.5.0", sha256="2666401939cdaa5f4e0c08cf7f20c9b21423b95e88f4675b1443973bdb080c42", url="https://pypi.org/packages/9e/85/b45408c64f3b888976f1d5b37eed8d746b8d5729a66a49ec846fda27d371/zope.event-4.5.0-py2.py3-none-any.whl")
    version("4.4", sha256="d8e97d165fd5a0997b45f5303ae11ea3338becfe68c401dd88ffd2113fe5cae7", url="https://pypi.org/packages/c5/96/361edb421a077a4c208b4a5c212737d78ae03ce67fbbcd01621c49f332d1/zope.event-4.4-py2.py3-none-any.whl")
    version("4.3.0", sha256="57b5fefd1d92774a7c26d7307b7ad9d0eac2181fd320b2061e69216e2a3b3a07", url="https://pypi.org/packages/03/62/bb2d843b59f62bac43d071e2d3543ffc63d35fcc515a5796c759b62de49b/zope.event-4.3.0-py2.py3-none-any.whl")
    version("4.2.0", sha256="ce11004217863a4827ea1a67a31730bddab9073832bdb3b9be85869259118758", url="https://pypi.org/packages/cd/a5/4927363244aaa7fd8a696d32005ea8214c4811550d35edea27797ebbd4fd/zope.event-4.2.0.tar.gz")
    version("4.1.0", sha256="dc7a59a2fd91730d3793131a5d261b29e93ec4e2a97f1bc487ce8defee2fe786", url="https://pypi.org/packages/0e/87/75e3d62a3506953c2e56d15a150de31e5d92310e87db2c8b102dc01b0b8e/zope.event-4.1.0.tar.gz")
    version("4.0.3", sha256="f5fdf6ca5716f714023358b212f7f435539dea11771603cd90eebf3ad34405f1", url="https://pypi.org/packages/c1/29/91ba884d7d6d96691df592e9e9c2bfa57a47040ec1ff47eff18c85137152/zope.event-4.0.3.tar.gz")
    version("4.0.2", sha256="f19691a70cf1a1394b3886fc5fd54e48644cf54943b50995dc90c2e514e5662b", url="https://pypi.org/packages/0c/64/f8ae73e8173e1210a89b4410ba0d1244f373cfe0ea3f58c6fecf97eaa5f2/zope.event-4.0.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-setuptools", when="@4.3:")

