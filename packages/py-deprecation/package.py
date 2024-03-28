# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeprecation(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.0", sha256="a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a", url="https://pypi.org/packages/02/c3/253a89ee03fc9b9682f1541728eb66db7db22148cd94f89ab22528cd1e1b/deprecation-2.1.0-py2.py3-none-any.whl")
    version("2.0.7", sha256="dc9b4f252b7aca8165ce2764a71da92a653b5ffbf7a389461d7a640f6536ecb2", url="https://pypi.org/packages/b9/2a/d5084a8781398cea745c01237b95d9762c382697c63760a95cc6a814ad3a/deprecation-2.0.7-py2.py3-none-any.whl")
    version("2.0.6", sha256="fecd0f05024126466ba7e5309b905f09fce7d25d67e4648f7ec5488f9e764310", url="https://pypi.org/packages/32/e9/01ffbaf3540ad54476cd7066439d629f1dd73b851cc5c0993ce2c12e1cdd/deprecation-2.0.6-py2.py3-none-any.whl")
    version("2.0.5", sha256="65a105244df7e43025218751da6c83389cc1dda12a5b7919b23e5fde7c481ec3", url="https://pypi.org/packages/9e/87/2e497672bf5157740f36233a8d2d59266dd083887ccdc5f3b6979e8c3a46/deprecation-2.0.5-py2-none-any.whl")
    version("2.0.4", sha256="fc08ca4e9cb7543187206d45a02a6f25f10e079d9bbde2822e1d15f3581dc97a", url="https://pypi.org/packages/8a/87/5924d68ff9cdfbbbdfbcd95562005c9ddc0ee3b9d745b810ab237a955ae9/deprecation-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="b2b152634372dd845503b50f6738ef5bb03e736ad2a2470577b0e33060e089e9", url="https://pypi.org/packages/00/47/6b2c094aafd289aa941b53ecf33276cec7573d5f389fcb1dfd29ac1a2bdc/deprecation-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="0ea3d6f95a5b08fe0e14ba728d4baafd79bfd5e2aaa40b779230cf4af62d1128", url="https://pypi.org/packages/64/10/3d60a4c42efa31a63f6b23b1960d3f79010c71620f7ba9568c48c395e6b7/deprecation-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="bd68dcbe067fece343520c7eb78b4c333304b081472c56cc191b8ad926d1361d", url="https://pypi.org/packages/bc/ef/b3d75763320122b8b965ece1316d5aab77b099c4d000b512dedc439cfa4f/deprecation-2.0.1-py3-none-any.whl")
    version("2.0", sha256="28162cbd79e8f3107cccb867c3902e3e7d2bb1f8c5dcb60b1c2b71cd6a3077ab", url="https://pypi.org/packages/2e/d0/73324198fe5c499a979f91d09493831f821027e43106f1dd3b434da4f740/deprecation-2.0-py3-none-any.whl")
    version("1.2", sha256="fa5d6c28b6f4cec8eb6c1a40d327bb2a5eb7f0e57e17f1be29e2623362c055eb", url="https://pypi.org/packages/39/a1/fe7d2021cbc9da5a6ad60fb3a014e787bf83893c1c710d5f071700cc4835/deprecation-1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@2.0.1:")
        depends_on("py-unittest2", when="@2.0.3")
    # END DEPENDENCIES

