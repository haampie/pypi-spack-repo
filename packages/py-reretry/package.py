# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReretry(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.8", sha256="5ec1084cd9644271ee386d34cd5dd24bdb3e91d55961b076d1a31d585ad68a79", url="https://pypi.org/packages/66/11/e295e07d4ae500144177f875a8de11daa4d86b8246ab41c76a98ce9280ca/reretry-0.11.8-py2.py3-none-any.whl")
    version("0.11.7", sha256="118e0e430f4e10aefdc44227ec0a56bad985620c04394e182f31c39f895a669a", url="https://pypi.org/packages/27/ee/b82982bba89ef5c4ccc3941c18fba528692353059e5f15756102d95776ee/reretry-0.11.7-py2.py3-none-any.whl")
    version("0.11.1", sha256="54ecdd41b5ead5bc65a65cdeccf10cb3450f884168c08f4a9e0e089583890d10", url="https://pypi.org/packages/eb/75/592a6dabe116d0e54e95052aafaa703c1737c6a2d8c3a7f99cc6d1eeb5b8/reretry-0.11.1-py2.py3-none-any.whl")
    version("0.11.0", sha256="81730c0081fa50ecd0c4f688b2c8c4a6e8f72b16565ba644a566d4e27fd0d26a", url="https://pypi.org/packages/69/a6/bb2bc460fcee54504d36b5380e2bab501018a534d653c5ba9854cf7e9768/reretry-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="a37d92681e8398097579b4449d122cf471dc821bab11590bca7ac7fb09e12829", url="https://pypi.org/packages/24/96/12c464de685f5ad87b52e8231873b8af011a96a016c4e46a2ae6ad6bcfcc/reretry-0.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-decorator@3.4.2:", when="@:0.11.0")
        depends_on("py-py@1.4.26:", when="@:0.11.0")
    # END DEPENDENCIES

