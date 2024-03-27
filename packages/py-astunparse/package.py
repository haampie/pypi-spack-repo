##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstunparse(PythonPackage):
    version("1.6.3", sha256="c2652417f2c8b5bb325c885ae329bdf3f86424075c4fd1a128674bc6fba4b8e8", url="https://pypi.org/packages/2b/03/13dde6512ad7b4557eb792fbcf0c653af6076b81e5941d36ec61f7ce6028/astunparse-1.6.3-py2.py3-none-any.whl")
    version("1.6.2", sha256="271fb1f3d7a2e3c66eab41000298860f046253d22ec96e4f024cfaf266805a8e", url="https://pypi.org/packages/2e/37/5dd0dd89b87bb5f0f32a7e775458412c52d78f230ab8d0c65df6aabc4479/astunparse-1.6.2-py2.py3-none-any.whl")
    version("1.6.1", sha256="dd4b33f553f5c3ec7a507a62c7111c65ae8e7ce330d0efc83d7f45fce3aad897", url="https://pypi.org/packages/0d/9d/1576217f67e7420f5945c15c6afd7045178c4850b148741bdbdbdabbf40e/astunparse-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="a9701ec06a8be16978141b901d99609f86f479781a5bfc4a98139aceaffb85f9", url="https://pypi.org/packages/0a/c3/7994a969a543a11d12a69e451ddf2b4efc9c89d1bebb0db858e39264c8fe/astunparse-1.6.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="699911dd43824de7444624a6731a258689702e008b2e344b98df5c480800ede3", url="https://pypi.org/packages/8b/ea/d38686f1718e307d83673d905dcffd142640a31a217e4e76d1de78f21b20/astunparse-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="0b7bb5d97da357eae4a81b6df8ee0c962e0c509d56a2523cdfeceafd59e05ccb", url="https://pypi.org/packages/79/16/ee6a5100f0a13e9adfc7737aa7aeda199bae954bc2c7fcccac44e0c2da58/astunparse-1.4.0.tar.gz")
    version("1.3.0", sha256="9ee11b7cfdc24c4068d1d2748a434a96d6acdcf8c12ae207ce53c94b427bd4ed", url="https://pypi.org/packages/14/80/c48ae086cd947f0b0d18086d7d76cedc5b2422339ff0c78adc95648b6c73/astunparse-1.3.0.tar.gz")
    version("1.2.2", sha256="2290514dab07a69078176beceda146c82afc0fc8fb294fbccf9f23bbfafc2e13", url="https://pypi.org/packages/a8/0b/0a413dd4781abc0c088ec3a2c4fd3526ad382f796d8040cdf779c5a3446e/astunparse-1.2.2.tar.gz")
    version("1.2.1", sha256="bb8bd1c9606ce23d0acfe5ee197cea1bb8613fefa3dc7aa5e58e21cceb0eb11b", url="https://pypi.org/packages/a3/29/be0ab59e92bfa785037ebd72d40ecf9182ad59f05fe6de7797edab66d00e/astunparse-1.2.1.tar.gz")
    version("1.2.0", sha256="38824c348888b9c5490ac86a50a29484a4a3b3642a0c13328dd0c988f6f3d3f5", url="https://pypi.org/packages/6c/31/5f707422451033ca303efc0a77cddeff5898d0854dfd754a74c6f647798b/astunparse-1.2.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.6.1:", when="@1.5:")
        depends_on("py-wheel@0.23:", when="@1.5:")

