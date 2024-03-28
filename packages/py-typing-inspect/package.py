# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypingInspect(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.0", sha256="9ee6fc59062311ef8547596ab6b955e1b8aa46242d854bfc78f4f6b0eff35f9f", url="https://pypi.org/packages/65/f3/107a22063bf27bdccf2024833d3445f4eea42b2e598abfbd46f6a63b6cb0/typing_inspect-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="5fbf9c1e65d4fa01e701fe12a5bca6c6e08a4ffd5bc60bfac028253a447c5188", url="https://pypi.org/packages/be/01/59b743dca816c4b6ca891b9e0f84d20513cd61bdbbaa8615de8f5aab68c1/typing_inspect-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="3cd7d4563e997719a710a3bfe7ffb544c6b72069b6812a02e9b414a8fa3aaa6b", url="https://pypi.org/packages/ad/fa/77565f652ce57ed56d3a63d537c885a18e4451cf2d56d944991aeb3c82bd/typing_inspect-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="118ebe93e4702647200ef946ea8bfd4508b4e5ff2cc8ed6e85a21f5c554dd660", url="https://pypi.org/packages/93/16/d23fd6b4663825df2d929ef4040e15fc7d5a2f2c99842791573eb5943f05/typing_inspect-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="3b98390df4d999a28cf5b35d8b333425af5da2ece8a4ea9e98f71e7591347b4f", url="https://pypi.org/packages/42/1c/66402db44184904a2f14722d317a4da0b5c8c78acfc3faf74362566635c5/typing_inspect-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="c6ed1cd34860857c53c146a6704a96da12e1661087828ce350f34addc6e5eee3", url="https://pypi.org/packages/f8/f7/4f9f37898a36ddc36d26fe50993617a82dfdd7f173984b2f20830e86f211/typing_inspect-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="a7cb36c4a47d034766a67ea6467b39bd995cd00db8d4db1aa40001bf2d674a9b", url="https://pypi.org/packages/ea/48/46ba0aff9c6ea0f6db6a0a62559298a9fe448316d06b797200595d77d0c0/typing_inspect-0.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mypy-extensions@0.3:", when="@0.3.1:")
        depends_on("py-typing-extensions@3.7.4:", when="@0.5:")
    # END DEPENDENCIES

