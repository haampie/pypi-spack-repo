# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAniso8601(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("9.0.1", sha256="1d2b7ef82963909e93c4f24ce48d4de9e66009a21bf1c1e1c85bdd0812fe412f", url="https://pypi.org/packages/e3/04/e97c12dc034791d7b504860acfcdd2963fa21ae61eaca1c9d31245f812c3/aniso8601-9.0.1-py2.py3-none-any.whl")
    version("9.0.0", sha256="36b8db7035ae3e1308e56550d586f6c7c58cbc6f33357e76dd8dd3c138fbaa3b", url="https://pypi.org/packages/ae/16/db3a1a970e0a7dc89204d07cff6401760380a9ab90a9dc399a8e7df3b430/aniso8601-9.0.0-py2.py3-none-any.whl")
    version("8.1.1", sha256="f59914762c5049ffd956cad037aa82fe0cabf8baf51900e2af24026761090b0b", url="https://pypi.org/packages/2c/09/c26ecac7a5e187db69380e66cbad27f8d53ae98b3d5188af08fdd5e34d9f/aniso8601-8.1.1-py2.py3-none-any.whl")
    version("8.1.0", sha256="51047d4fb51d7b8afd522b70f2d21a1b2487cbb7f7bd84ea852e9aa7808e7704", url="https://pypi.org/packages/93/4e/760c0aaf32034e2da98e1ac6d83b6ffc6d1301132af54c3950ee07785bfa/aniso8601-8.1.0-py2.py3-none-any.whl")
    version("8.0.0", sha256="c033f63d028b9a58e3ab0c2c7d0532ab4bfa7452bfc788fbfe3ddabd327b181a", url="https://pypi.org/packages/eb/e4/787e104b58eadc1a710738d4e418d7e599e4e778e52cb8e5d5ef6ddd5833/aniso8601-8.0.0-py2.py3-none-any.whl")
    version("7.0.0", sha256="d10a4bf949f619f719b227ef5386e31f49a2b6d453004b21f02661ccc8670c7b", url="https://pypi.org/packages/45/a4/b4fcadbdab46c2ec2d2f6f8b4ab3f64fd0040789ac7f065eba82119cd602/aniso8601-7.0.0-py2.py3-none-any.whl")
    version("6.0.0", sha256="bb167645c79f7a438f9dfab6161af9bed75508c645b1f07d1158240841d22673", url="https://pypi.org/packages/85/58/1e804d6d53435b1b2241036056360575640b69a332e7ead086a04bd5ad95/aniso8601-6.0.0-py2.py3-none-any.whl")
    version("5.1.0", sha256="a5c7595bb65d3919a9944a759d907b57c4d050abaa0e5cf845e84c26cdfd1218", url="https://pypi.org/packages/5d/0d/ca7f24d2f87163f03044315c13edc300010d898ba712c972f4a3a827a5ab/aniso8601-5.1.0-py2.py3-none-any.whl")
    version("5.0.1", sha256="c9ecb8eb5429a7dd188fae86ac504a7c3d9091f63f1598970b866d5e6ccb3074", url="https://pypi.org/packages/e8/4d/110b532eb3280f1880c2561034a7aa86541ff73ec278e62a2b5a05dccd74/aniso8601-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="60f4c1cba7760d910d92efbbd6850e586b7559aaf53110650b37403d57f41554", url="https://pypi.org/packages/82/63/24b5bb126f83749f895f8cd3ed45975df2fcd469e17f598bf424c4eed31f/aniso8601-5.0.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="ac30cceff24aec920c37b8d74d7d8a5dd37b1f62a90b4f268a6234cabe147080", url="https://pypi.org/packages/8c/1d/6fdba7c6e28a53fea0cb13171829fb1812c400eb0d4d9d1de25ec5d81f0f/aniso8601-4.1.0-py2.py3-none-any.whl")
    version("4.0.1", sha256="547e7bc88c19742e519fb4ca39f4b8113fdfb8fca322e325f16a8bfc6cfc553c", url="https://pypi.org/packages/69/9b/f2ae61c0c90181b62e15ca09d283d2aab42c7c2c3bbd7c548dd0cfd8bf3e/aniso8601-4.0.1-py2.py3-none-any.whl")
    version("4.0.0", sha256="41e649cf0a8b4f5642f0a2acf557a072a024a991b4693e775ebb9febd3a19f9f", url="https://pypi.org/packages/56/93/c29b08cc9cc583863d607324325f5b665627eac1827d4033aae8f4ee0af6/aniso8601-4.0.0-py2.py3-none-any.whl")
    version("3.0.2", sha256="94f90871fcd314a458a3d4eca1c84448efbd200e86f55fe4c733c7a40149ef50", url="https://pypi.org/packages/17/13/eecdcc638c0ea3b105ebb62ff4e76914a744ef1b6f308651dbed368c6c01/aniso8601-3.0.2-py2.py3-none-any.whl")
    version("3.0.0", sha256="f7052eb342bf2000c6264a253acedb362513bf9270800be2bc8e3e229fe08b5a", url="https://pypi.org/packages/ba/8c/4cd25b3facc5f443cb083f4582483e8c8e7901380c71c44aff6eeda4dc54/aniso8601-3.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-relativetimebuilder@0.2:", when="@5.1:5")
    # END DEPENDENCIES

