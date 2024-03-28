# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyct(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="a4038a8885059ab8cac6f946ea30e0b5e6bdbe0b92b6723f06737035f9d65e8c", url="https://pypi.org/packages/75/e7/c7c1e9e1b6b23ca1db7af3c6826d57d8da883021f751edcc9c82143b127a/pyct-0.5.0-py2.py3-none-any.whl")
    version("0.5.0-rc1", sha256="5fe6515618c400e3b8b0cf59b6dd442ec709dfd943cc1f61a7fd126556bdfab2", url="https://pypi.org/packages/6e/b5/fff73e8f93af701510188af73fc56c9b04c4777708af6cd8be04f417752a/pyct-0.5.0rc1-py2.py3-none-any.whl")
    version("0.4.8", sha256="222e104d561b28cfdb56667d2ba10e5290b4466db66d0af38ab935577af85390", url="https://pypi.org/packages/71/76/52ce7aec26b0171939d3b3843acd011f8eb297b2a569e992691bb2964185/pyct-0.4.8-py2.py3-none-any.whl")
    version("0.4.7", sha256="cbccd93c8f9b3d179e6b8b137e8c376dbb6026d5f3ae48aef324477ca7fabccb", url="https://pypi.org/packages/7d/20/d47832b891090cc190631aebd467c61ac6ca3e545f42437b6e0b66368b73/pyct-0.4.7-py2.py3-none-any.whl")
    version("0.4.6", sha256="359eab8c91e63c705f838ccdd56548258f013de0bd3481c99775552ee2ab9de6", url="https://pypi.org/packages/eb/76/cdf8ba7edc7be2a26d418ff8d1ff695a7ac024761bda1ad6f8e269a90434/pyct-0.4.6-py2.py3-none-any.whl")
    version("0.4.5", sha256="be0603e20805daabbf773318fbe09d9006cd7e8563b964befd51980a0e4466d6", url="https://pypi.org/packages/83/bc/bf8174c75364432b51fb349701a395a85eac0ab114bc8efdfff6d98fcc7c/pyct-0.4.5-py2.py3-none-any.whl")
    version("0.4.4", sha256="c313c6b34155b9ba5073f5998039524ad1e0694d4b2fc53cb34ab8bda76eac85", url="https://pypi.org/packages/b7/50/65bf69c8bfb01752239e89a528ccd8273a121d5289d735053f28775ea091/pyct-0.4.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-param@1.7:", when="@0.4.4:")
        depends_on("py-pyyaml", when="@0.2.3,0.4:0.4.3")
        depends_on("py-requests", when="@0.4:0.4.3")
    # END DEPENDENCIES

