##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestForked(PythonPackage):
    version("1.6.0", sha256="810958f66a91afb1a1e2ae83089d8dc1cd2437ac96b12963042fbb9fb4d16af0", url="https://pypi.org/packages/f4/af/9c0bda43e486a3c9bf1e0f876d0f241bc3f229d7d65d09331a0868db9629/pytest_forked-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="fe43952a8483d7e4dac3c3a6c4568095d5d35a42407c4e5c3f0917d2a038cafb", url="https://pypi.org/packages/69/86/8b2c57e67af19e8c1c01f9daf7b70ac25f0d9a298fb09f891945eb121876/pytest_forked-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="bbbb6717efc886b9d64537b41fb1497cfaf3c9601276be8da2cccfea5a3c8ad8", url="https://pypi.org/packages/0c/36/c56ef2aea73912190cdbcc39aaa860db8c07c1a5ce8566994ec9425453db/pytest_forked-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="dc4147784048e70ef5d437951728825a131b81714b398d5d52f17c7c144d8815", url="https://pypi.org/packages/9d/88/77eeb091b4fa79f28c08718f6e6ebff5827d9d1c1dd9974218ddfbe031ee/pytest_forked-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="42a438336731465c5bd76ab38e1645647ac55914a08b507efbabe8783a08aa6c", url="https://pypi.org/packages/cb/9e/042a670001fb67f4e454cab96fef5fe65eed8d196e705c01461aeee33dab/pytest_forked-1.2.0-py2.py3-none-any.whl")
    version("1.1.3", sha256="1ae25dba8ee2e56fb47311c9638f9e58552691da87e82d25b0ce0e4bf52b7d87", url="https://pypi.org/packages/03/1e/81235e1fcfed57a4e679d34794d60c01a1e9a29ef5b9844d797716111d80/pytest_forked-1.1.3-py2.py3-none-any.whl")
    version("1.1.2", sha256="6d1c9052f5dd766a7cb2f8947fef7d32b6bbaf9aaea8cd971a1f84d257253498", url="https://pypi.org/packages/35/57/f027e004e3db19c038c12dd96c8f28ee52561c9a7edfe4e893660dd62de9/pytest-forked-1.1.2.tar.gz")
    version("1.1.1", sha256="e2d46f319c8063a3a0536b18f9cdea6eea3bc9fe2cb16c94e1d6fad3abc37300", url="https://pypi.org/packages/ae/9c/8f0c51c98ee5165ff575f196662a4a314ff07c9d3de64a94580c982edcee/pytest-forked-1.1.1.tar.gz")
    version("1.1.0", sha256="37d5b1c16f3f0e9910265168cf91e6510009714d8a11a671c9c2f9408a76d560", url="https://pypi.org/packages/29/1c/bec803938ecd9fa35d2425e48fe9d6792d7ce18769ad2866becaa3b87df8/pytest-forked-1.1.0.tar.gz")
    version("1.0.2", sha256="5fe33fbd07d7b1302c95310803a5e5726a4ff7f19d5a542b7ce57c76fed8135f", url="https://pypi.org/packages/3f/55/ef92c340e723495dbee91d749903d2b7950b49c501943296257246d7d880/pytest_forked-1.0.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-py", when="@1.3:")
        depends_on("py-pytest@3.10:", when="@1.3:")
        depends_on("py-pytest@3.1:", when="@1:1.0.1,1.1.3:1.2")

