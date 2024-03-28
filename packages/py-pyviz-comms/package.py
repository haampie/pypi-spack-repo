# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvizComms(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.2", sha256="31541b976a21b7738557c3ea23bd8e44e94e736b9ed269570dcc28db4449d7e3", url="https://pypi.org/packages/6b/09/9163cfdd2b2440bb283f48e2e6f2bdacdbd3afeedcb48b06fa24a78d3b1f/pyviz_comms-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="0130e952b942906a0eb5fcbcc750262a8e4f565a9b06b3c0d8d631f33b61b78e", url="https://pypi.org/packages/88/e1/a877ce6f15fcf51da1ef0a253266c3f321bec7ed6f93cc82e8a8296c8618/pyviz_comms-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="91c967151b1e4d436c458c147a31991a42fbe7567e49176e4eb5b8dc8e20f1ff", url="https://pypi.org/packages/67/bc/f698554d2a179c3ae40adba328db1bc552c0ea5832101503200ab1904dd8/pyviz_comms-3.0.0-py3-none-any.whl")
    version("2.3.2", sha256="2e9f6574409ef6c44331b41ff254cbde05fffca140aca8ac47ca13d9223b4499", url="https://pypi.org/packages/9b/cb/9a8860b75c8cc7fe6852329c7d1e1a1e89457d16a759039bd3b017118f6e/pyviz_comms-2.3.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="33d096820e6547eb120dd2dd43242ecccfbc62f3db86eda0781cadd05ad25c99", url="https://pypi.org/packages/64/2a/8b2815cb43fdc8ee4d2643853f2c8a65feafb67a661068641181a1213df0/pyviz_comms-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="955c87c59f565dae30a46edfea5c8b93bf6a86caf3f90e096f7923f6d4dc19a1", url="https://pypi.org/packages/a6/ed/29bad395a07b401bfa8af5a8298cb9c6b73509b38e65e357f3d644b0a715/pyviz_comms-2.3.0-py2.py3-none-any.whl")
    version("2.2.1", sha256="aba28430cf28b39f2605acb48f7fddf0e3025394a8286adfeb40d74b0ae0f4f9", url="https://pypi.org/packages/2f/78/72bec6805be44a11dc80e949752fcaacc21661c3423e26623263d19a73d1/pyviz_comms-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="c11837635ae47d7001d001d87cf8bf3ae417b4bbf6f493c376114207b7efcd77", url="https://pypi.org/packages/be/65/84b7520204dcbd9aae2d6e173ffc86a70743953e37722beb6bcf5f1d7927/pyviz_comms-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="6ff14e4180107782088be17d565415dcb02375aa34e4626f481e52adb7324676", url="https://pypi.org/packages/7c/cb/513487e3f724d30dc58d654c32db3ee9c2bbe4aad49954830b724a43ab70/pyviz_comms-2.1.0-py2.py3-none-any.whl")
    version("2.0.2", sha256="0ed42ffd0dd2182edc7a331100c72d9923a027120f4225dbbc33663eadddba8e", url="https://pypi.org/packages/0f/e6/45913dbdd90dbb3ebb408721e2f0dc22150868182ac70627be4dcf8bbdf2/pyviz_comms-2.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-param", when="@0.7.2:")
    # END DEPENDENCIES

