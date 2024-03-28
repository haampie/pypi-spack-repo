# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsToolbelt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0", sha256="cccfdd665f0a24fcf4726e690f65639d272bb0637b9b92dfd91a5568ccf6bd06", url="https://pypi.org/packages/3f/51/d4db610ef29373b879047326cbf6fa98b6c1969d6f6dc423279de2b1be2c/requests_toolbelt-1.0.0-py2.py3-none-any.whl")
    version("0.10.1", sha256="18565aa58116d9951ac39baa288d3adb5b3ff975c4f25eee78555d89e8f247f7", url="https://pypi.org/packages/05/d3/bf87a36bff1cb88fd30a509fd366c70ec30676517ee791b2f77e0e29817a/requests_toolbelt-0.10.1-py2.py3-none-any.whl")
    version("0.10.0", sha256="64c6b8c51b515d123f9f708a29743f44eb70c4479440641ed2df8c4dea56d985", url="https://pypi.org/packages/a7/c5/cdf6f0e54d15a3f3440d26c9f962b58a3b2ff8d76692408251ed4831b68d/requests_toolbelt-0.10.0-py2.py3-none-any.whl")
    version("0.9.1", sha256="380606e1d10dc85c3bd47bf5a6095f815ec007be7a8b69c878507068df059e6f", url="https://pypi.org/packages/60/ef/7681134338fc097acef8d9b2f8abe0458e4d87559c689a8c306d0957ece5/requests_toolbelt-0.9.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="a582006f08e12d871fcaa746c4a0ff16313312d18964a2f42a8ba9c8b3ece571", url="https://pypi.org/packages/05/3b/facf65bc2173e3fa014f13ce7096b15577ae0e1244a3fd185804c4e3db5d/requests_toolbelt-0.9.0-py2.py3-none-any.whl")
    version("0.8.0", sha256="42c9c170abc2cacb78b8ab23ac957945c7716249206f90874651971a4acff237", url="https://pypi.org/packages/97/8a/d710f792d6f6ecc089c5e55b66e66c3f2f35516a1ede5a8f54c13350ffb0/requests_toolbelt-0.8.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="17077c6876338ba4101b6e9ab6ba925da970387a7a7eab91d28eed8d25da01f0", url="https://pypi.org/packages/dd/85/519354e995d8a926ce3121034dc2144a5ae70435dad3e1155a19bbde8011/requests_toolbelt-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="a0432b1124e6b33151ecf694497b4808690dd94ce68c6648c1daa63b771278c4", url="https://pypi.org/packages/57/60/cc85ca45c85585191e70e21687aeaa74ec4e555a1404628ba77b8af7d92e/requests_toolbelt-0.7.0-py2.py3-none-any.whl")
    version("0.6.2", sha256="a252f66501663d655ab6c5be83a08c82afc3932931cc0af54b315a58e34d0a3c", url="https://pypi.org/packages/c0/06/d198c065f25815e43b6fb4acdeb88ffcffe7a383c888bb8da80edc546dbc/requests_toolbelt-0.6.2-py2.py3-none-any.whl")
    version("0.6.1", sha256="11798328e3e897fcf1548227c24230c4950e1c12ddaf33911a768a8d80d56ac4", url="https://pypi.org/packages/92/31/718557078c85f902dc5b0310875a8e64f1bd0ad3b9c4b53154d6015d5c87/requests_toolbelt-0.6.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="f19762fc818a71444198abdf5d6bd4cade5f154d3b0df3e59010c430d3ab6fa8", url="https://pypi.org/packages/44/b3/f6e0e1756c3a22c47a4b5ce9fde7f64fd844f3579a80c9c3a5655ac78959/requests_toolbelt-0.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@2.0.1:", when="@0.4:")
    # END DEPENDENCIES

