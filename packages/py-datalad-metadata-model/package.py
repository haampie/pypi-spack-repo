##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladMetadataModel(PythonPackage):
    version("0.3.11", sha256="c9e9b4a1d0c57e4bc57cd6c73335fda4f4c57ece7e193031784ab64f7fff57b9", url="https://pypi.org/packages/ba/6b/d67f36f90effd0729cba9bec8d7f47f1c1484fa87614a6f8a274720cb946/datalad_metadata_model-0.3.11-py3-none-any.whl")
    version("0.3.10", sha256="13c186aebfd5f9367850eb54e63bf4f21fbd80d72b951949c072d7411469ab95", url="https://pypi.org/packages/9d/69/e1ae4839a98b880b6ee28fd9cd01db62dfa316748cca392e7908425312ab/datalad_metadata_model-0.3.10-py3-none-any.whl")
    version("0.3.9", sha256="2685af15d96ad5cf1bcb6f6fa8b68f29c9435e5de5fc0ebe1dc9cc9e3999f1e3", url="https://pypi.org/packages/85/00/0f33af00571689e22389951e1480ce5dafe81c63c28f55fd461eaa610156/datalad_metadata_model-0.3.9-py3-none-any.whl")
    version("0.3.8", sha256="1e9439433824591d5d9acdd3ac3c8b5c539b01b6ba58f2ca60bc41a1dfddf237", url="https://pypi.org/packages/e6/2e/a940e5c56eb024a5ffdee814889421166a49275427fd0d17e4819b8199ef/datalad_metadata_model-0.3.8-py3-none-any.whl")
    version("0.3.7", sha256="118d0201e10a16432e05ae28e77ece4c705d298b242c8201c788c7456d18bfa8", url="https://pypi.org/packages/db/ce/a4be16c93a8ada38a9fb2459d5e5c6ea0c953769920a1135ec09ed3fe359/datalad_metadata_model-0.3.7-py3-none-any.whl")
    version("0.3.6", sha256="3e7f2cb00878221905a1c404668a9c6acf2257cfc348d1a4b9f7c24bde489de9", url="https://pypi.org/packages/7f/19/89d2caae87598795b3d247744f5734ab685625697757578947fd9d98347a/datalad_metadata_model-0.3.6-py3-none-any.whl")
    version("0.3.5", sha256="b550e16508b6d21bbc7a3c6a28fb0b470799361a46aafbd28f6a152503b5fc15", url="https://pypi.org/packages/0e/b8/0f87fdb1f1b37ecec1367e337d3c70ed351a7ef4e48295bf66ecbae2280e/datalad_metadata_model-0.3.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-appdirs", when="@0.1.0-rc3:")
        depends_on("py-click", when="@0.1.0-rc3:")
        depends_on("py-fasteners", when="@0.1.0-rc3:")

