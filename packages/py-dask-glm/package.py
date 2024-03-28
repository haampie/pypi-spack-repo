# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDaskGlm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.2", sha256="649e55f24e5e0d91a51e0d8d45a9b005dde3c3e6b6480e1290422adec91d4da6", url="https://pypi.org/packages/8a/8e/cd1502dd2d00d54fb3e10880d4c8cb6699320a239da7a39c9f55044afdee/dask_glm-0.3.2-py2.py3-none-any.whl")
    version("0.3.1", sha256="a019113b8b3d169a99e8778e1894709756dc53dc423313958459b5f73bc3db9f", url="https://pypi.org/packages/7f/42/e7ba5c1d4cc60e14fae817152411a19e722f87d28097fc83ba16fdbf9645/dask_glm-0.3.1-py2.py3-none-any.whl")
    version("0.3.0", sha256="0ab973efed61d852e518d3bc6a08e2c4a17aa392a40fa40b21415a90b3281068", url="https://pypi.org/packages/4f/73/ad1a7b3a11fa37db0807a9f521dfaeefedc728a2d8cae3d2b071ad4136f3/dask_glm-0.3.0-py2.py3-none-any.whl")
    version("0.2.0", sha256="a116c36a830cc20660c0815c4c8d67239814931952e8695d784604cb4839ea51", url="https://pypi.org/packages/cb/ee/36c6e0e7b51e08406e5c3bb036f35adb77bd0a89335437b2e6f03c948f1a/dask_glm-0.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cloudpickle@0.2.2:")
        depends_on("py-dask+array")
        depends_on("py-distributed", when="@0.3:")
        depends_on("py-multipledispatch@0.4.9:")
        depends_on("py-scikit-learn@0.18:")
        depends_on("py-scipy@0.18.1:")
        depends_on("py-sparse@0.7:", when="@0.3:")
    # END DEPENDENCIES

