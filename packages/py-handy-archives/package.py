# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHandyArchives(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="8495e08f3cd1c452fe65570db1869db07f709149f85c7e9cd8f3f461df436318", url="https://pypi.org/packages/f9/e5/23451e1cee169259fbc98d2b2ed7b1c3711b707355896c9c3761325ddb01/handy_archives-0.2.0-py3-none-any.whl")
    version("0.1.4", sha256="0c5db273e338a197e7cb00cf4f652d2c06c7a545751a791a0f33a584f2c3eaef", url="https://pypi.org/packages/5f/ea/b832254da91afaf4502ccbe56d7cebd77689afeeb17c9ebf9269fd69874f/handy_archives-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="b530bc42870b3e06cff0ba4b64e5263c892bed76f9367b5e0ab21cd8e7ebdb5a", url="https://pypi.org/packages/61/b5/c77204e2f9583ab98e2f6cc0366e7723ecef90cd7b4610804951b8ab63b6/handy_archives-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="f5ee79152fc24d8b4ed3cbed6b335f190d10f06dcf7c005d8f232959f029d72e", url="https://pypi.org/packages/68/4d/042c3b44f249158b4ff00e3281f4bb54c2b0144b20bb244129feca179f94/handy_archives-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="0e3d5c0876eecf64e93f395965e96be3fd3a8228817e59040782929d8d112605", url="https://pypi.org/packages/c3/69/d3e44455b1eaecb933dd9fa2cd5a6882b26417c07fd6451b7adc9b09b990/handy_archives-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="0407437ad712b3ed3579b60abb5729d4886a2c5ed5260007b79c56fbaa040c62", url="https://pypi.org/packages/63/29/6e9c59583db7728967cd9b16559982d08c0c855af1814a15133a3a14f73b/handy_archives-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@3.1:", when="@:0.1.3")
    # END DEPENDENCIES

