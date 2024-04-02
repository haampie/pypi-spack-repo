# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrometheusClient(PythonPackage):
    # BEGIN VERSIONS
    version("0.17.0", sha256="a77b708cf083f4d1a3fb3ce5c95b4afa32b9c521ae363354a4a910204ea095ce", url="https://pypi.org/packages/5b/62/75fc6f255e214ff0a8bd3267a0bd337521dd24f76cd593c10795e488f41b/prometheus_client-0.17.0-py3-none-any.whl")
    version("0.14.1", sha256="522fded625282822a89e2773452f42df14b5a8e84a86433e3f8a189c1d54dc01", url="https://pypi.org/packages/19/e5/7d4b4b3b0d8d2fdc55395cdb4271c6dbfde3c3ff7d6a6dbe63d19c4e2288/prometheus_client-0.14.1-py3-none-any.whl")
    version("0.12.0", sha256="317453ebabff0a1b02df7f708efbab21e3489e7072b61cb6957230dd004a0af0", url="https://pypi.org/packages/df/6c/6c5f9404977f8f9caa30c1a408f6cc5ea6e0c1949761f24d0a33239b49c5/prometheus_client-0.12.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="71cd24a2b3eb335cb800c7159f423df1bd4dcd5171b234be15e3f31ec9f622da", url="https://pypi.org/packages/b3/23/41a5a24b502d35a4ad50a5bb7202a5e1d9a0364d0c12f56db3dbf7aca76d/prometheus_client-0.7.1.tar.gz")
    version("0.7.0", sha256="ee0c90350595e4a9f36591f291e6f9933246ea67d7cd7d1d6139a9781b14eaae", url="https://pypi.org/packages/36/ae/99d3bfdb9b4eec8de1ef0abf28c833689f8884f192d97e2b9e72f8774f31/prometheus_client-0.7.0.tar.gz")
    version("0.5.0", sha256="e8c11ff5ca53de6c3d91e1510500611cafd1d247a937ec6c588a0a7cc3bef93c", url="https://pypi.org/packages/bc/e1/3cddac03c8992815519c5f50493097f6508fa153d067b494db8ab5e9c4ce/prometheus_client-0.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("twisted", default=False, description="twisted")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-twisted", when="@0.8:+twisted")
    # END DEPENDENCIES

