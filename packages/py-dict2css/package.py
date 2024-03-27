##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDict2css(PythonPackage):
    version("0.3.0.post1", sha256="f006a6b774c3e31869015122ae82c491fd25e7de4a75607a62aa3e798f837e0d", url="https://pypi.org/packages/fe/47/290daabcf91628f4fc0e17c75a1690b354ba067066cd14407712600e609f/dict2css-0.3.0.post1-py3-none-any.whl")
    version("0.3.0", sha256="ef934ce73a225fdd5f811b484fe9e2dd768f7ef14a89fc8f4eb5672597131d00", url="https://pypi.org/packages/ff/1c/5c108f07fc0818bef046fd1d6cdd84ba081833d59b1adbc3a112a0f741cd/dict2css-0.3.0-py3-none-any.whl")
    version("0.2.4", sha256="afaad026895d2d738a4ccc4e119d36c2d58d533d184af9ee749f308c16218eed", url="https://pypi.org/packages/46/fd/07ceefdf488355a0bddd765f68db56223bb0b183fc6059873126ed337951/dict2css-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="41206b3e71b975eb5fbc4433be0ab19515fd81127c9fcdee6dcde4e76a106c7b", url="https://pypi.org/packages/ac/7a/4aacde73cb8847a40b1c6b7d803d98a73f08db632e98d37a8f2a79843c9b/dict2css-0.2.3-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-css-parser@1.0.6", when="@:0.2")
        depends_on("py-cssutils@2.2:", when="@0.3:")
        depends_on("py-domdf-python-tools@2.2:")

