# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDunamai(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.19.2", sha256="bc126b17571a44d68ed826cec596e0f61dc01edca8b21486f70014936a5d44f2", url="https://pypi.org/packages/ab/ca/6747d43753dddea1e12e22a8de6287af5ddaf5e9e763ba0f9544b4885118/dunamai-1.19.2-py3-none-any.whl")
    version("1.19.1", sha256="a6aa0ae3bdb01a12d6f219555d6e230ec02663afb43a7bd37933e6c4fecefc9b", url="https://pypi.org/packages/2a/5c/82252ed6046a78dbb274067b1589e9e5df4d86db5d450fcb4e0576e8e348/dunamai-1.19.1-py3-none-any.whl")
    version("1.19.0", sha256="1ed948676bbf0812bfaafe315a134634f8d6eb67138513c75aa66e747404b9c6", url="https://pypi.org/packages/c5/56/40dc7bcfdc2105ec170a8264f849782a1fccb3a577ba904da22900bb6d4b/dunamai-1.19.0-py3-none-any.whl")
    version("1.18.1", sha256="ee7b042f7a687fa04fc383258eb93bd819c7bd8aec62e0974f3c69747e5958f2", url="https://pypi.org/packages/19/87/d097cc1f44cfd5757ed3a09c05cd7e934cb2ad313dd541d2ad0710f7152c/dunamai-1.18.1-py3-none-any.whl")
    version("1.18.0", sha256="f9284a9f4048f0b809d11539896e78bde94c05b091b966a04a44ab4c48df03ce", url="https://pypi.org/packages/4f/7c/1f3e504c627c81f58b1e6120618266df3c1a52a6ee9170c6e3ab265376bc/dunamai-1.18.0-py3-none-any.whl")
    version("1.17.0", sha256="5aa4ac1085de10691269af021b10497261a5dd644f277e2a21822212604d877b", url="https://pypi.org/packages/15/8e/ab699ce8c856edada5c7b4b79188caa478406c4f5ed4be99d703ca2c6827/dunamai-1.17.0-py3-none-any.whl")
    version("1.16.1", sha256="b9f169183147f6f1d3a5b3d913ffdd67247d90948006e205cbc499fe98d45554", url="https://pypi.org/packages/f9/4a/24dc20c208a9f74feca3b7fb841e182657aa416f8b3fc73b46ec4fd8c019/dunamai-1.16.1-py3-none-any.whl")
    version("1.16.0", sha256="dc92d817f3bc155e8b129e8c705c36bb15a7e950e2698a93aea142732a888e98", url="https://pypi.org/packages/02/13/ceeef025eeb3dafc6f709b68c35f126f4e9bb940ed8e6b11a899c4fd6b22/dunamai-1.16.0-py3-none-any.whl")
    version("1.15.0", sha256="646d7a6c07d0ec8412ac43c1a3546f1d1b52f3ed918f4bfbefe32439b49dec7e", url="https://pypi.org/packages/6a/62/048c060adc4c51561957efd7c15054b82d4b6e3418d7fcd29b5e5d57d910/dunamai-1.15.0-py3-none-any.whl")
    version("1.14.1", sha256="6486738116c7c8db8f23b9f166ff2f7b0846a3f577fde2616e91bb62dc9686c4", url="https://pypi.org/packages/b9/dd/7f72f6994f15c77fc50918adf0393d9b156dd24bd5cf56f64f0fbf9714eb/dunamai-1.14.1-py3-none-any.whl")
    version("1.13.1", sha256="f23d31fd3e7df1c16f018f4f0c408df7feda8cba9516f7c9822a29fa3ed665cd", url="https://pypi.org/packages/13/ed/cbc61cd53954bbdab845886b416a6343014710d0ef821e2a6aadc4b81f05/dunamai-1.13.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging@20.9:", when="@1.7:")
    # END DEPENDENCIES

