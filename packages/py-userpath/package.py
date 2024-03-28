# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUserpath(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.9.2", sha256="2cbf01a23d655a1ff8fc166dfb78da1b641d1ceabf0fe5f970767d380b14e89d", url="https://pypi.org/packages/43/99/3ec6335ded5b88c2f7ed25c56ffd952546f7ed007ffb1e1539dc3b57015a/userpath-1.9.2-py3-none-any.whl")
    version("1.9.1", sha256="e085053e5161f82558793c41d60375289efceb4b77d96033ea9c84fc0893f772", url="https://pypi.org/packages/a2/28/20c7dcdb12681b2e12224184a8a158e5df51feb0c68116cb4b1b991a4aab/userpath-1.9.1-py3-none-any.whl")
    version("1.9.0", sha256="8069f754d31edfbdb2c3b2e9abada057ce7518290838dac35d1c8cee1b4cc7b0", url="https://pypi.org/packages/54/e4/5a33b7d5d2a7387ad7d5cf11cab2b832fd36ace778597e365595c5a12041/userpath-1.9.0-py3-none-any.whl")
    version("1.8.0", sha256="f133b534a8c0b73511fc6fa40be68f070d9474de1b5aada9cded58cdf23fb557", url="https://pypi.org/packages/45/72/e8cf3e440a4719253cf114c091ae84e7a07394dbb44983f3a561f40f80b6/userpath-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="4c3d3b611706a8b0c6309510c8b1a774c54eb491cafe7df58dc5571c0bee30e2", url="https://pypi.org/packages/78/26/50fe9e5003ccd28bba6dcca47dabf43470292ce9199f42f0c4c5d354cffa/userpath-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="43569129eeecec6c567bcbd47120c161a43344712417de013b754191961426db", url="https://pypi.org/packages/36/ba/311896660f318a46e586a170a6eb487ce15ffeb2c2af666af6d2aa4be255/userpath-1.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click")
    # END DEPENDENCIES

