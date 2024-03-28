# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColorspacious(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="c78befa603cea5dccb332464e7dd29e96469eebf6cd5133029153d1e69e3fd6f", url="https://pypi.org/packages/ab/a1/318b9aeca7b9856410ededa4f52d6f82174d1a41e64bdd70d951e532675a/colorspacious-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="33317422e348a7814cce43153d33e60e64d07b4f8ba8836f4442fe41a7e74789", url="https://pypi.org/packages/44/fc/6d36b0af326fc39af9426417baf3aa9e835ca393d23e847fa3df42101b59/colorspacious-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="fc5cb7a93a2d5c4b2b9d5cc2ccc7b62d85d63c55ccd2635447f9d534806bd03e", url="https://pypi.org/packages/06/86/1a81bead5516fdd92df61ed272e6ae3993d4d7f9e6c805df60c9cea28699/colorspacious-1.1.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="55d17d5d08081ca2fcfe6a98323c1ca7ccec32e05f160b26e615746d32798afd", url="https://pypi.org/packages/c7/fc/8a470549f47af35dc97bce6b4ca21ecb490f4b0656ffbcdc56adccc7e0e8/colorspacious-1.0.0-py2.py3-none-any.whl")
    version("0.1.0", sha256="a4a9965d73ba07273268b5c104b5b14d13d0155a34f68d6f648d7fc1bbad59bc", url="https://pypi.org/packages/ba/ed/14efa57e558d69f37d0e7d426bcffff7a2628b7a6b2fbc3ce6c9fd83c2fe/colorspacious-0.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1:")
    # END DEPENDENCIES

