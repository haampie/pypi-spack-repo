##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrometheusFlaskExporter(PythonPackage):
    version("0.23.0", sha256="7a026b4fdd54ebeddb77589333efe3a1ec43c7c717468825b0b3e9b6c33f7e9e", url="https://pypi.org/packages/2c/f7/ad9ad5bdab5af0bc2dca568687234f0bac5484dcb3666c5d9da43e46b93d/prometheus_flask_exporter-0.23.0-py3-none-any.whl")
    version("0.22.4", sha256="e130179c26d5a9b903c12c0d8826127ae491b04b298cae0b92b98677dcf2c06f", url="https://pypi.org/packages/2d/48/cdb895f4926d562d6669d47a5315615677d76a39bed732f2a87e8e97aed2/prometheus_flask_exporter-0.22.4-py3-none-any.whl")
    version("0.22.3", sha256="16e6a3a7ce0089fc7c78a6956cdf28c184c3ac518e2b46a2a8e410b68d3a84a3", url="https://pypi.org/packages/ef/82/a794f15bdeb1ac8b9cc6548bce06001042d3489288f8ba294d1e65a62043/prometheus_flask_exporter-0.22.3-py3-none-any.whl")
    version("0.22.2", sha256="299c53dc068afe8c5510e17a8d2e50cfe22ae9cfe6c0755556ebd6fd9d0b3bd4", url="https://pypi.org/packages/a6/cd/7ff75a0602e24adaf8cfdd31986e531f93c53a32ba171eb04eb58bd65993/prometheus_flask_exporter-0.22.2-py3-none-any.whl")
    version("0.22.1", sha256="d4a0c7e237cef36162638c3a0ba5e17264ca916fddda1546bc8567a631e5e0b8", url="https://pypi.org/packages/42/17/1870051d1d95a06f735409d636e5c70351b7cd9f43e76e48760942ff56b8/prometheus_flask_exporter-0.22.1-py3-none-any.whl")
    version("0.22.0", sha256="03c0682bd343e0ab1961acf7348f69488a8a101fd5c5c35cd10a508c51d3ff83", url="https://pypi.org/packages/7a/89/90663f449fad0811098478b9bae770294e824b5a1bd7f69155795652608b/prometheus_flask_exporter-0.22.0-py3-none-any.whl")
    version("0.21.0", sha256="6dc4a010c299d1ed94b6151d91f129c4513fb8aa04310db00be4ccb0006de400", url="https://pypi.org/packages/55/fa/09ee59e31dca1b2d9db3e8a85e8cda7d7174af09b52dc8dd370bfb1aa535/prometheus_flask_exporter-0.21.0-py3-none-any.whl")
    version("0.20.3", sha256="8e38ada61a24543c4ce65672db9694d0b3d0d20d4516e2f30d6ba85304cd6031", url="https://pypi.org/packages/c0/e0/37e98fa277989d5b62f49f9ade0c2d238e7107032046a78403ac6b8ada2c/prometheus_flask_exporter-0.20.3-py3-none-any.whl")
    version("0.20.2", sha256="946f8d631430258b9bf76c037a9f51a1d51f369cff84c8decc7e142e38d41197", url="https://pypi.org/packages/c0/aa/e3e828c9c5bee692a884fc775200b1bf15f9c92c4fffa3394ae49a6d163f/prometheus_flask_exporter-0.20.2-py3-none-any.whl")
    version("0.20.1", sha256="83f2c2b2744650658addf1cf15e54d1be4fc1bd86cfb37660f3f352b09fd2c57", url="https://pypi.org/packages/0b/4f/b21b6b132bc6915b157964d8823c78e286b6e4d11ce373fcdcd5a81f8034/prometheus_flask_exporter-0.20.1-py3-none-any.whl")
    version("0.18.2", sha256="fc487e385d95cb5efd045d6a315c4ecf68c42661e7bfde0526af75ed3c4f8c1b", url="https://pypi.org/packages/f3/c1/2cc385fadf18dc75fe24c18899269eda4dcc60221d61eff7da4a6cc5c01d/prometheus_flask_exporter-0.18.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-flask", when="@0.18.3:")
        depends_on("py-prometheus-client", when="@0.18.3:")

