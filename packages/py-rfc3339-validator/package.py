##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRfc3339Validator(PythonPackage):
    version("0.1.4", sha256="24f6ec1eda14ef823da9e36ec7113124b39c04d50a4d3d3a3c2859577e7791fa", url="https://pypi.org/packages/7b/44/4e421b96b67b2daff264473f7465db72fbdf36a07e05494f50300cc7b0c6/rfc3339_validator-0.1.4-py2.py3-none-any.whl")
    version("0.1.3", sha256="bf86bab55fd90bf5fa42c84d63066053345e675efcd351d1266d6d20b46ca86e", url="https://pypi.org/packages/4c/90/312d90e3a5b824731ca778205b35694c48d5ba8c84f86cccafb987be2208/rfc3339_validator-0.1.3-py2.py3-none-any.whl")
    version("0.1.2", sha256="ce04632ad50bd8cead747a17baabbf720dc0203adc7eee9e66b702a24265dc35", url="https://pypi.org/packages/c2/e7/e18d6cfd3262d48159cd8095eb8f002b5f4e4015e194daffbe0fb706154b/rfc3339_validator-0.1.2-py2.py3-none-any.whl")
    version("0.1.1", sha256="6642ad0521fed9789f1d19d6adc793936bb0ef58912643d1f421fdda9fb37d0f", url="https://pypi.org/packages/9c/9b/69ce82e96c8dfd92cba2678526d8e3466272c56c292b09393e4bf65cf0e1/rfc3339_validator-0.1.1-py2.py3-none-any.whl")
    version("0.1.0", sha256="3ec3d4f3683e66cc774dc0b43551aeb090d0d370afcaa3e2c08cfa566bc66891", url="https://pypi.org/packages/b4/b5/9fc5efaea74570f2fd4ee1ec633077ef314af21bf965c9c0faa7a4abb0fa/rfc3339_validator-0.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six")

