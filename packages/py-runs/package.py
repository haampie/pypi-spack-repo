# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRuns(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.2", sha256="0980dcbc25aba1505f307ac4f0e9e92cbd0be2a15a1e983ee86c24c87b839dfd", url="https://pypi.org/packages/86/d6/17caf2e4af1dec288477a0cbbe4a96fbc9b8a28457dce3f1f452630ce216/runs-1.2.2-py3-none-any.whl")
    version("1.2.1", sha256="f103386deb84983d445e61b56de48a006691289a17f80214fe593e858d193a12", url="https://pypi.org/packages/d7/74/cb1ca09152bcca9ebed1a9a3cd8c66639d68bee528233e84c7db1c94c99d/runs-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="ec6fe3b24dfa20c5c4e5c4806d3b35bb880aad0e787a8610913c665c5a7cc07c", url="https://pypi.org/packages/81/2f/0bc8ca6f42ea647afcb056efe3546341bd75dc40892a68a65414d668fba0/runs-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="702a31bec6d3336175ab6dcadd605ebd39b75d792a98303202b090d4556883e3", url="https://pypi.org/packages/bc/12/3cd1e484a2276271c6b365a7213e10274f8da5b53b300738c7585936e003/runs-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="14cf2636c580fef79077de5e4afe693cdf92fc52344fd9cb994cc2b1566d788a", url="https://pypi.org/packages/95/11/cfa0b0ce7688c5d24356883340c7395b75a65da811b0f006805fe5bd8032/runs-1.0.0-py3-none-any.whl")
    version("0.3.2", sha256="c64216397bd1e255ed56f22b9cefe507e75e8c3c76946c2e869488593b6bd767", url="https://pypi.org/packages/74/d7/45404df2c373a971c475faa3ba84c879da32516d16f32472b24a8ca086bf/runs-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="b5839315f80a752427284f460c2f092a7d2841248316cb883a6e6ebb17915913", url="https://pypi.org/packages/2d/d3/4473b639b6df03db1eeeda063b7848b168f0f80c182f9bd22e2ccf965d11/runs-0.3.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-xmod")
    # END DEPENDENCIES

