# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnirf(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.42", sha256="be7b02fdc2b0a3bb1e4a6196967026a41a6bf8d32da056b8467685f96960df1f", url="https://pypi.org/packages/44/b3/abccb0a0a6a3757c0410383347f1716e099970af582fcc22020daac6742e/snirf-0.7.42-py2.py3-none-any.whl")
    version("0.7.4", sha256="eba3f80c2e6fa35341147c519d31c7460ebdc9af7f5a659afc4c8ac6aab65324", url="https://pypi.org/packages/75/1b/3f41beca581312e95492fcc3987e80ff2198fe2f79e5dcc03a3045b3e072/snirf-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="9386e429d6c5a70e1f9ed56eec71ffd41e958ce8af4802b6899b7d00aabddac7", url="https://pypi.org/packages/4e/cd/72eef26f2a285924218be18983f9b9773c89ac03ae8de86ce5a61b3b580f/snirf-0.7.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama")
        depends_on("py-h5py@3.1:")
        depends_on("py-numpy")
        depends_on("py-pip")
        depends_on("py-setuptools")
        depends_on("py-termcolor")
    # END DEPENDENCIES

