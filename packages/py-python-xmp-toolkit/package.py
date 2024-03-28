# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonXmpToolkit(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.2", sha256="dad1c2dcf5392459ecf2d0e368a7bbcab099cac7ef9f75fa53612db4efbcda8a", url="https://pypi.org/packages/c4/d0/d94b7150333ea5092992dbbcfdd27d338276ad5df4796cafe4d43febf552/python_xmp_toolkit-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="ad7869810687b594d21901ed101906ae4291b270ce09af5ea6886be49202e186", url="https://pypi.org/packages/8d/be/1f64e6e9c4e6b6b4689ec9bbc2e3804ac70227c5e3040a86c9afc21402bb/python_xmp_toolkit-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="1c44d1c5d997c834cd46daf9d9fe7378451ada7a219e42adad558db5f30d661f", url="https://pypi.org/packages/31/2d/7b91a52472cf6d3d09d97d05576034424b039832de11d8b7e7da7ec98aad/python-xmp-toolkit-2.0.0.tar.gz")
    version("1.0.2", sha256="0c545d41a84c45ba0a06f7b5ff7378d1522c3c721a9bd35fb6e49d66d16ddd24", url="https://pypi.org/packages/20/c8/edc7df21f56ac08f5db8aa35ea22d2222a2d4f2f7e1814e80286426e6089/python-xmp-toolkit-1.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytz", when="@2.0.1:")
    # END DEPENDENCIES

