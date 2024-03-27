##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyResponses(PythonPackage):
    version("0.18.0", sha256="15c63ad16de13ee8e7182d99c9334f64fd81f1ee79f90748d527c28f7ca9dd51", url="https://pypi.org/packages/79/f3/2b3a6dc5986303b3dd1bbbcf482022acb2583c428cd23f0b6d37b1a1a519/responses-0.18.0-py3-none-any.whl")
    version("0.17.0", sha256="e4fc472fb7374fb8f84fcefa51c515ca4351f198852b4eb7fc88223780b472ea", url="https://pypi.org/packages/3c/f7/3925be6f7c251b331095d3e7302fdf3c7599284b5a616bd4c90fca7ace45/responses-0.17.0-py2.py3-none-any.whl")
    version("0.16.0", sha256="f358ef75e8bf431b0aa203cc62625c3a1c80a600dbe9de91b944bf4e9c600b92", url="https://pypi.org/packages/32/17/f231fbca0c5021507409a3cdd91574a9128c9171366f692276176496164a/responses-0.16.0-py2.py3-none-any.whl")
    version("0.15.0", sha256="5955ad3468fe8eb5fb736cdab4943457b7768f8670fa3624b4e26ff52dfe20c0", url="https://pypi.org/packages/55/03/bf9b983e68724fc83942666454f6f7a9b024203ff15d0065e4ea482542ef/responses-0.15.0-py2.py3-none-any.whl")
    version("0.14.0", sha256="57bab4e9d4d65f31ea5caf9de62095032c4d81f591a8fac2f5858f7777b8567b", url="https://pypi.org/packages/7b/9b/d4f61d21bf2c9a653d02bf5ef8910c03e0cbc876db5eebae358421261b4c/responses-0.14.0-py2.py3-none-any.whl")
    version("0.13.4", sha256="d8d0f655710c46fd3513b9202a7f0dcedd02ca0f8cf4976f27fa8ab5b81e656d", url="https://pypi.org/packages/d6/8c/a985395210c54d8a3b849cbe8d9212906550020ba35fd3514ef463906c2f/responses-0.13.4-py2.py3-none-any.whl")
    version("0.13.3", sha256="b54067596f331786f5ed094ff21e8d79e6a1c68ef625180a7d34808d6f36c11b", url="https://pypi.org/packages/ba/00/0e63b7024c2d873bf57411ab0ed77eeafd5f44bace7cbf1d56bca8ab3be2/responses-0.13.3-py2.py3-none-any.whl")
    version("0.13.2", sha256="75529f9bea08276cea43545dcb6129f137c299d6a12269485a753785c869e0e2", url="https://pypi.org/packages/a8/ba/03b4c978708510c2ab52a75804530edfd96647f3de44abe1cf25d16150ad/responses-0.13.2-py2.py3-none-any.whl")
    version("0.13.1", sha256="3b1ea9cf026edaaf25e853abc4d3b2687d25467e9d8d41e77ee525cad0673f3e", url="https://pypi.org/packages/b1/a1/162c90162e0f4539534b6ce6d723c4c07be8ad38c1cb975d7c63128502e0/responses-0.13.1-py2.py3-none-any.whl")
    version("0.13.0", sha256="a4a90c8244006c01f4246aecf532fbb5429c4031df4adcc7638061f0f3ce4ceb", url="https://pypi.org/packages/b1/54/1107e50648b975bbc2d10388b83a6782bbe25db0f552dfbb669fb478d958/responses-0.13.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-requests@2:", when="@0.7:0.8,0.10.1:0.21")
        depends_on("py-six", when="@0.7:0.8,0.10.1:0.17")
        depends_on("py-urllib3@1.25.10:", when="@0.10.16:0.23.1")

