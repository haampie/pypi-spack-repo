# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrometheusClient(PythonPackage):
    # BEGIN VERSIONS
    version("0.20.0", sha256="cde524a85bce83ca359cc837f28b8c0db5cac7aa653a588fd7e84ba061c329e7", url="https://pypi.org/packages/c7/98/745b810d822103adca2df8decd4c0bbe839ba7ad3511af3f0d09692fc0f0/prometheus_client-0.20.0-py3-none-any.whl")
    version("0.19.0", sha256="c88b1e6ecf6b41cd8fb5731c7ae919bf66df6ec6fafa555cd6c0e16ca169ae92", url="https://pypi.org/packages/bb/9f/ad934418c48d01269fc2af02229ff64bcf793fd5d7f8f82dc5e7ea7ef149/prometheus_client-0.19.0-py3-none-any.whl")
    version("0.18.0", sha256="8de3ae2755f890826f4b6479e5571d4f74ac17a81345fe69a6778fdb92579184", url="https://pypi.org/packages/aa/84/8b11274c61f81376ee06dfb5b60b176097b58166f095d55014f033632f46/prometheus_client-0.18.0-py3-none-any.whl")
    version("0.17.1", sha256="e537f37160f6807b8202a6fc4764cdd19bac5480ddd3e0d463c3002b34462101", url="https://pypi.org/packages/ad/b3/6e18c89bf6bd120590ea538a62cae16dc763ff2745b18377c4be5495c4aa/prometheus_client-0.17.1-py3-none-any.whl")
    version("0.17.0", sha256="a77b708cf083f4d1a3fb3ce5c95b4afa32b9c521ae363354a4a910204ea095ce", url="https://pypi.org/packages/5b/62/75fc6f255e214ff0a8bd3267a0bd337521dd24f76cd593c10795e488f41b/prometheus_client-0.17.0-py3-none-any.whl")
    version("0.16.0", sha256="0836af6eb2c8f4fed712b2f279f6c0a8bbab29f9f4aa15276b91c7cb0d1616ab", url="https://pypi.org/packages/5b/8e/6a546e439b4366ab9eab0a736876eb1e1916dd93b4a1fa560ef711d24f8c/prometheus_client-0.16.0-py3-none-any.whl")
    version("0.15.0", sha256="db7c05cbd13a0f79975592d112320f2605a325969b270a94b71dcabc47b931d2", url="https://pypi.org/packages/2e/5e/4225463cdac1098aac718b1d8adf8f9dc3d6aaea55f4f85a2f7d572b4f7c/prometheus_client-0.15.0-py3-none-any.whl")
    version("0.14.1", sha256="522fded625282822a89e2773452f42df14b5a8e84a86433e3f8a189c1d54dc01", url="https://pypi.org/packages/19/e5/7d4b4b3b0d8d2fdc55395cdb4271c6dbfde3c3ff7d6a6dbe63d19c4e2288/prometheus_client-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="f4aba3fdd1735852049f537c1f0ab177159b7ab76f271ecc4d2f45aa2a1d01f2", url="https://pypi.org/packages/f7/81/bad2d4def4d010535c08459d4882c927968af12a9651d995aa4534f892b1/prometheus_client-0.14.0-py3-none-any.whl")
    version("0.13.1", sha256="357a447fd2359b0a1d2e9b311a0c5778c330cfbe186d880ad5a6b39884652316", url="https://pypi.org/packages/53/d2/b64e76fc5df129db7cee2c071ba129ce090b2f6e7fb4c734aa9d2fc1d262/prometheus_client-0.13.1-py3-none-any.whl")
    version("0.12.0", sha256="317453ebabff0a1b02df7f708efbab21e3489e7072b61cb6957230dd004a0af0", url="https://pypi.org/packages/df/6c/6c5f9404977f8f9caa30c1a408f6cc5ea6e0c1949761f24d0a33239b49c5/prometheus_client-0.12.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="71cd24a2b3eb335cb800c7159f423df1bd4dcd5171b234be15e3f31ec9f622da", url="https://pypi.org/packages/b3/23/41a5a24b502d35a4ad50a5bb7202a5e1d9a0364d0c12f56db3dbf7aca76d/prometheus_client-0.7.1.tar.gz")
    version("0.7.0", sha256="ee0c90350595e4a9f36591f291e6f9933246ea67d7cd7d1d6139a9781b14eaae", url="https://pypi.org/packages/36/ae/99d3bfdb9b4eec8de1ef0abf28c833689f8884f192d97e2b9e72f8774f31/prometheus_client-0.7.0.tar.gz")
    version("0.5.0", sha256="e8c11ff5ca53de6c3d91e1510500611cafd1d247a937ec6c588a0a7cc3bef93c", url="https://pypi.org/packages/bc/e1/3cddac03c8992815519c5f50493097f6508fa153d067b494db8ab5e9c4ce/prometheus_client-0.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("twisted", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-twisted", when="@0.8:+twisted")
    # END DEPENDENCIES

