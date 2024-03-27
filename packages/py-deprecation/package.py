##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeprecation(PythonPackage):
    version("2.1.0", sha256="a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a", url="https://pypi.org/packages/02/c3/253a89ee03fc9b9682f1541728eb66db7db22148cd94f89ab22528cd1e1b/deprecation-2.1.0-py2.py3-none-any.whl")
    version("2.0.7", sha256="dc9b4f252b7aca8165ce2764a71da92a653b5ffbf7a389461d7a640f6536ecb2", url="https://pypi.org/packages/b9/2a/d5084a8781398cea745c01237b95d9762c382697c63760a95cc6a814ad3a/deprecation-2.0.7-py2.py3-none-any.whl")
    version("2.0.6", sha256="fecd0f05024126466ba7e5309b905f09fce7d25d67e4648f7ec5488f9e764310", url="https://pypi.org/packages/32/e9/01ffbaf3540ad54476cd7066439d629f1dd73b851cc5c0993ce2c12e1cdd/deprecation-2.0.6-py2.py3-none-any.whl")
    version("2.0.5", sha256="cbe7d15006bc339709be5e02b14884ecc479639c1a3714a908de3a8ca13b5ca9", url="https://pypi.org/packages/dd/06/aed49f13984c4acfcd67d699b2a0e96fefd2f9c700ce88a43120eb0363e2/deprecation-2.0.5.tar.gz")
    version("2.0.4", sha256="fc08ca4e9cb7543187206d45a02a6f25f10e079d9bbde2822e1d15f3581dc97a", url="https://pypi.org/packages/8a/87/5924d68ff9cdfbbbdfbcd95562005c9ddc0ee3b9d745b810ab237a955ae9/deprecation-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="b2b152634372dd845503b50f6738ef5bb03e736ad2a2470577b0e33060e089e9", url="https://pypi.org/packages/00/47/6b2c094aafd289aa941b53ecf33276cec7573d5f389fcb1dfd29ac1a2bdc/deprecation-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="0ea3d6f95a5b08fe0e14ba728d4baafd79bfd5e2aaa40b779230cf4af62d1128", url="https://pypi.org/packages/64/10/3d60a4c42efa31a63f6b23b1960d3f79010c71620f7ba9568c48c395e6b7/deprecation-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="bd68dcbe067fece343520c7eb78b4c333304b081472c56cc191b8ad926d1361d", url="https://pypi.org/packages/bc/ef/b3d75763320122b8b965ece1316d5aab77b099c4d000b512dedc439cfa4f/deprecation-2.0.1-py3-none-any.whl")
    version("2.0", sha256="492b1ff401242ddb33c4d0ee6a27b98b6cef825453f1a1339315d861503ce012", url="https://pypi.org/packages/f1/68/f28dcab6411a2b09831b14bc936f2ab627b07b411098bbbfbc1c86f32cf4/deprecation-2.0.tar.gz")
    version("1.2", sha256="f3290b162abfe234d8a6b14dcff276efc513a5a324f0a51ac57dec7a718ae541", url="https://pypi.org/packages/5e/5f/260bfcec67f3a202e6ddd65911f3407e937387512509bf89252d64f1612e/deprecation-1.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-packaging", when="@2.0.1:")
        depends_on("py-unittest2", when="@2.0.3")

