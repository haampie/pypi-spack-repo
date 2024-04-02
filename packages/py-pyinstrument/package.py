# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyinstrument(PythonPackage):
    # BEGIN VERSIONS
    version("4.4.0", sha256="be34a2e8118c14a616a64538e02430d9099d5d67d8a370f2888e4ac71e52bbb7", url="https://pypi.org/packages/9a/f8/1feae9239316e073dcdc53e6d1ffbd3d02bb2e0d3a755bc61439a6264221/pyinstrument-4.4.0.tar.gz")
    version("4.0.3", sha256="08caf41d21ae8f24afe79c664a34af1ed1e17aa5d4441cd9b1dc15f87bbbac95", url="https://pypi.org/packages/70/40/f0fcd90f3128c43d9e20ae3e37b166e26885c5250e8386a7abf4b6b5dc05/pyinstrument-4.0.3.tar.gz")
    version("3.1.3", sha256="aca49f1b04097ddfa03da1c0f73856cd61bd20fda18fe60b907593c0581ff9dc", url="https://pypi.org/packages/1f/0d/fd53567bff37bd87b211f71329dd74f87e559dc2136fdcb6abfea8ebee48/pyinstrument-3.1.3-py2.py3-none-any.whl")
    version("3.1.0", sha256="1f8a11be6e61df23b09ea411b98eb888336d6468c172b81c5d42d47a48cddef6", url="https://pypi.org/packages/89/59/1174e1a8294021e2d62f85e010701f0b3825e67e18ba2d6382cd41972cc3/pyinstrument-3.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("jupyter", default=False, description="jupyter")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@4:")
        depends_on("py-pyinstrument-cext@0.2.2:", when="@3.0.3:3")
    # END DEPENDENCIES

