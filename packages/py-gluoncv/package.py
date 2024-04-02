# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGluoncv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.5.post0", sha256="93318cfda39ac3ac0fae3226f425f86b5edeafa581323e4f24927655538929ee", url="https://pypi.org/packages/8b/48/5564159e0ee638353bedfcdaf7a95f260d24969489444fab4cb01d1efe9d/gluoncv-0.10.5.post0-py2.py3-none-any.whl")
    version("0.6.0", sha256="7a169a546af47c2fa2aef41e772f5fc36710c48b3c4e51ef4dbe8cc7ad9d4288", url="https://pypi.org/packages/69/4d/d9d6b9261af8f7251977bb97be669a3908f72bdec9d3597e527712d384c2/gluoncv-0.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-autocfg", when="@0.9.0-beta20201105:")
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-opencv-python", when="@0.9.0-beta20201105:")
        depends_on("py-pandas", when="@0.9.0-beta20201105:")
        depends_on("py-pillow")
        depends_on("py-portalocker")
        depends_on("py-pyyaml", when="@0.9.0-beta20201105:")
        depends_on("py-requests")
        depends_on("py-scipy")
        depends_on("py-tqdm")
        depends_on("py-yacs", when="@0.9.0-beta20201105:")
    # END DEPENDENCIES

