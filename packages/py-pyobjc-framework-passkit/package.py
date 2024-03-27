##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPasskit(PythonPackage):
    version("10.2", sha256="0c879d632f0f0bf586161a7abbbba3dad9ba9894a3edbce06f4160491c2c134c", url="https://pypi.org/packages/49/2a/29810f864770d8e1430f5f982fa8094c31c45907249eef1a80b4244d39fa/pyobjc-framework-PassKit-10.2.tar.gz")
    version("10.1", sha256="bc19a46fad004137f207a5a9643d3f9a3602ea3f1d75c57841de986019a3c805", url="https://pypi.org/packages/8d/65/2455458940a565daeedd017dd1ab1ab941c7ee626dfe35bf60e3f11156f9/pyobjc-framework-PassKit-10.1.tar.gz")
    version("10.0", sha256="da2c5b12c341e2e826b5345798854219966c7bef4bfdb8df306816877df22abb", url="https://pypi.org/packages/ba/c7/89a0688efd86cd03ecb1e76c09486f1c729fe20bd0eff036d9cbc8b7361a/pyobjc-framework-PassKit-10.0.tar.gz")
    version("9.2", sha256="5411c6cf332960eda180b28131d5c46dded38e5bf93be973e5c1db2bc062b8b7", url="https://pypi.org/packages/00/1c/9db06d9f0308cffebed44315b5e86825ed9438c451bf4eddc9feba37eead/pyobjc-framework-PassKit-9.2.tar.gz")
    version("9.1.1", sha256="62bb923aa3beab0d12d0eb5d5372c52f90ebb986858dd3bda606a68eab8a4723", url="https://pypi.org/packages/3c/a1/b45433d87fd6f1968c9a1d63dfcc2930f71ccc4af4d3e92ecf1a280f9c07/pyobjc-framework-PassKit-9.1.1.tar.gz")
    version("9.1", sha256="5dd630a6f039746d8e7f78586f2ad00ef6abc5d1bb46e5b7e0729c2cf52b9cbd", url="https://pypi.org/packages/42/21/d796ac174ddc963d276ebbdc8220fe422b5c2fe08f9eebcd0ee6184f8e7e/pyobjc-framework-PassKit-9.1.tar.gz")
    version("9.0.1", sha256="3d422c41465baa6a9e7f0f4e85cb8dc773103dcbee1d284ca90ce49d036540ae", url="https://pypi.org/packages/ed/d5/44b795225cecfc4c6d1aa21584884c1c6f613d962b271d41b41548dd8df8/pyobjc-framework-PassKit-9.0.1.tar.gz")
    version("9.0", sha256="4a26b96d471a6002a2f628e652bea308013afc34e6b20adc24d85dbf43c9d02e", url="https://pypi.org/packages/88/63/8a5b27706d944a6cb15caacf59e144287700f126aca77910d9d19d81d675/pyobjc-framework-PassKit-9.0.tar.gz")
    version("8.5.1", sha256="fe4b7ecdb49b4a9b78729d6df23de862997ce62a7d60f74a29060165d721a874", url="https://pypi.org/packages/d3/14/941ed8986bc114ce3c135b7e158e71ad6341a69dabdd6e58abe2446aa368/pyobjc-framework-PassKit-8.5.1.tar.gz")
    version("8.5", sha256="ec3bc9daf0a8289630df95fe78bc3c6b985f6711fca12d2f4289e5c6932aea86", url="https://pypi.org/packages/40/b2/f91947f593330ac71fc0b31a3f8488f4557c1fbef9d7f924b6a8b55dc100/pyobjc-framework-PassKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

