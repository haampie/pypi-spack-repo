##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonBioformats(PythonPackage):
    version("4.0.7", sha256="1d272e9e080a05e06c143f84934fa59589383b998bcaf6bd47d3be49e776f0ff", url="https://pypi.org/packages/6b/f4/bdb811d751cd7c02d49e7753d4387f4ba10ed78acec91ba40caf3128a06a/python_bioformats-4.0.7-py3-none-any.whl")
    version("4.0.6", sha256="6696454b4920c54b9997560cfacedab129b375673ff26e2c825ebf476f547a54", url="https://pypi.org/packages/26/b4/1be675f9a239090f9accbd4ddede704a7b66573e936941a6de20cb924c9a/python_bioformats-4.0.6-py3-none-any.whl")
    version("4.0.5", sha256="9c5cc32dd78c7b6e891513f0dc897c4c74a8fd4d9e9afb69d40edd0eb481320f", url="https://pypi.org/packages/5d/48/0873186982a2800060e63095cfd6b299e815e866ab0fa8bfe2a9cb1d8a08/python_bioformats-4.0.5-py3-none-any.whl")
    version("4.0.4", sha256="8c5458f3ad58016fcc71da763fcc029e3258ecc02b8c99098331eeb044946444", url="https://pypi.org/packages/b3/ec/6d9f2d6baf911881c27d30f385181d002146c830ff1e2f407014d863764d/python_bioformats-4.0.4-py3-none-any.whl")
    version("4.0.3", sha256="e195be72adcacdb5142a9e850520e6724397813224c1f643b455a1c050b58eae", url="https://pypi.org/packages/7f/d0/a51de9e7478196fd88df924ae591462f2e3c437718176e8ab6e2ee835010/python-bioformats-4.0.3.tar.gz")
    version("4.0.2", sha256="09e21b16d880c8159a89ae6f44faa494abd32f19c604da19d3e9e092ef555249", url="https://pypi.org/packages/5f/5c/ea252273130843996b17ede65c15d1db313754cf7d9245f7507d8ead177f/python-bioformats-4.0.2.tar.gz")
    version("4.0.1", sha256="4c0f7041c81c8bdd1ccf1c5c595ddbe8fbb8f1f0001b1d6270107438fb759462", url="https://pypi.org/packages/f7/8c/3a767188398d7249ccab64dc2d10a7f016eb92cfd8a42bec4273f6d7d0d6/python-bioformats-4.0.1.macosx-10.15-x86_64.tar.gz")
    version("4.0.0", sha256="53056361d217be870e6071a1d96fecd1519c4a3a3d7c2733b65883e6f124c8d7", url="https://pypi.org/packages/61/64/de0a193af35e7052563a5a7af50461e060780f2a9dc7311504eefe921bb1/python_bioformats-4.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-boto3@1.14.23:", when="@4.0.0,4.0.4:")
        depends_on("py-future@0.18.2:", when="@4.0.0,4.0.4:")
        depends_on("py-python-javabridge@4.0.3:", when="@4.0.4:")
        depends_on("py-python-javabridge@4.0.0", when="@4.0.0")

