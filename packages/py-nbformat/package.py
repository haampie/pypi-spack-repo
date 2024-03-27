##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbformat(PythonPackage):
    version("5.10.3", sha256="d9476ca28676799af85385f409b49d95e199951477a159a576ef2a675151e5e8", url="https://pypi.org/packages/b0/4c/20b6c8b6d7cc17b0481eb49c18f23b76f913ab3e6580a57515cd9727ca43/nbformat-5.10.3-py3-none-any.whl")
    version("5.10.2", sha256="7381189a0d537586b3f18bae5dbad347d7dd0a7cf0276b09cdcd5c24d38edd99", url="https://pypi.org/packages/2f/5c/982c01957e937007fb86f452af5409800bd9b725a0d43c5a4898a6657a10/nbformat-5.10.2-py3-none-any.whl")
    version("5.10.1", sha256="32667779ed07f5f141b8b72d785fbc84c9b9f4f0cc75377d6da81762ad27cfaf", url="https://pypi.org/packages/c1/2f/f65380687035a25dbfa9b76a6630c58986fb5e022e39377ab7dddd25e022/nbformat-5.10.1-py3-none-any.whl")
    version("5.10.0", sha256="a6611be71a95840ea7e8fedd58cbe37ebf0cbf1d3d230936d963392f13be5e54", url="https://pypi.org/packages/d1/a1/9a87b5e0cd21af32f8fa4b4a2a9ea7455cc1e70ec3c4bb53ed4577210a5f/nbformat-5.10.0-py3-none-any.whl")
    version("5.9.2", sha256="1c5172d786a41b82bcfd0c23f9e6b6f072e8fb49c39250219e4acfff1efe89e9", url="https://pypi.org/packages/f4/e7/ef30a90b70eba39e675689b9eaaa92530a71d7435ab8f9cae520814e0caf/nbformat-5.9.2-py3-none-any.whl")
    version("5.9.1", sha256="b7968ebf4811178a4108ee837eae1442e3f054132100f0359219e9ed1ce3ca45", url="https://pypi.org/packages/01/e5/322b31448ba6b0ed6de740306367e85d8da2af0d91e67f7a2860bdf87f72/nbformat-5.9.1-py3-none-any.whl")
    version("5.9.0", sha256="8c8fa16d6d05062c26177754bfbfac22de644888e2ef69d27ad2a334cf2576e5", url="https://pypi.org/packages/e1/ce/7f0f454b4e7f1cb31345f9f977bdce7486033a1c08b5945b17ea95c4afbc/nbformat-5.9.0-py3-none-any.whl")
    version("5.8.0", sha256="d910082bd3e0bffcf07eabf3683ed7dda0727a326c446eeb2922abe102e65162", url="https://pypi.org/packages/1d/f6/38f4694b5035306a8c2685e9e6ea7bf46ea344c03422d7131442ac9677c1/nbformat-5.8.0-py3-none-any.whl")
    version("5.7.3", sha256="22a98a6516ca216002b0a34591af5bcb8072ca6c63910baffc901cfa07fefbf0", url="https://pypi.org/packages/21/ad/020fed74bfde983a3b70cc95843d6adbe59171aa9a3da5aab403aa722a17/nbformat-5.7.3-py3-none-any.whl")
    version("5.7.2", sha256="36340fa5c0bbcbf3fec3473414e6ca7eb872df83a80bc108d2875afd6af99586", url="https://pypi.org/packages/64/16/9a60c6d61a21fb64897ed58caf53686d218a104c38cc2e25b296509dbf98/nbformat-5.7.2-py3-none-any.whl")
    version("5.7.0", sha256="1b05ec2c552c2f1adc745f4eddce1eac8ca9ffd59bb9fd859e827eaa031319f9", url="https://pypi.org/packages/5c/9f/957655d02f43b8bff77e6da08c94472b1229c13e7455bbd662163c9b78c0/nbformat-5.7.0-py3-none-any.whl")
    version("5.4.0", sha256="0d6072aaec95dddc39735c144ee8bbc6589c383fb462e4058abc855348152dad", url="https://pypi.org/packages/2f/9a/97151abb954af0cc5d0e3ff2eb7b6d96704a317ac2c0ce0cc76cef003991/nbformat-5.4.0-py3-none-any.whl")
    version("5.1.3", sha256="eb8447edd7127d043361bc17f2f5a807626bc8e878c7709a1c647abda28a9171", url="https://pypi.org/packages/e7/c7/dd50978c637a7af8234909277c4e7ec1b71310c13fb3135f3c8f5b6e045f/nbformat-5.1.3-py3-none-any.whl")
    version("5.0.7", sha256="ea55c9b817855e2dfcd3f66d74857342612a60b1f09653440f4a5845e6e3523f", url="https://pypi.org/packages/4d/d1/b568bd35f95321f152f594b3647cd080e96d3347843ff2fa34dce871b8bf/nbformat-5.0.7-py3-none-any.whl")
    version("4.4.0", sha256="b9a0dbdbd45bb034f4f8893cafd6f652ea08c8c1674ba83f2dc55d3955743b0b", url="https://pypi.org/packages/da/27/9a654d2b6cc1eaa517d1c5a4405166c7f6d72f04f6e7eea41855fe808a46/nbformat-4.4.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="02f3474203248214f7a34ad0955d75490462dc0e328f9920d1ea8aa795ae3399", url="https://pypi.org/packages/d6/4c/8058f1170dbdbe5a66e9431489f85d2d3e5a8e6314dd7ed1f7b10d864a70/nbformat-4.1.0-py2.py3-none-any.whl")
    version("4.0.1", sha256="dc875e80f2a170b3691907e0485047027dd17d76aac95050673eca6655809ceb", url="https://pypi.org/packages/c5/9d/7cc4a5e291ac24cfa5f02612f43c056f62575357fcf381ec70adcc7ebd02/nbformat-4.0.1.zip")
    version("4.0.0", sha256="e16eac24ad493244dee77a8f4f2dca8fe203a4c74c1382b134858b2e1f438435", url="https://pypi.org/packages/0a/38/5c2b242f2d7b047261c795d960be804abb91866b4e4eee71ba105241eecb/nbformat-4.0.0.zip")

    with default_args(type="run"):
        depends_on("py-fastjsonschema", when="@5.3:")
        depends_on("py-ipython-genutils", when="@4.1:5.1")
        depends_on("py-jsonschema@2.6:", when="@5.3:")
        depends_on("py-jsonschema@2.4,2.5.1:", when="@4.2:5.2")
        depends_on("py-jsonschema@2:2.4,2.5.1:", when="@4.1")
        depends_on("py-jupyter-core", when="@4.1:")
        depends_on("py-traitlets@5.1:", when="@5.4:")
        depends_on("py-traitlets@4.1.0:", when="@4.2:5.3")
        depends_on("py-traitlets", when="@4.1")

