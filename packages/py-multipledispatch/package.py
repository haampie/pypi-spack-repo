# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultipledispatch(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.0", sha256="0c53cd8b077546da4e48869f49b13164bebafd0c2a5afceb6bb6a316e7fb46e4", url="https://pypi.org/packages/51/c0/00c9809d8b9346eb238a6bbd5f83e846a4ce4503da94a4c08cb7284c325b/multipledispatch-1.0.0-py3-none-any.whl")
    version("0.6.0", sha256="407e6d8c5fa27075968ba07c4db3ef5f02bea4e871e959570eeb69ee39a6565b", url="https://pypi.org/packages/3d/a3/3638c2232eb513a9f876bb96e2e400f18d2f5bdc2e7abe84194c8bd38c2d/multipledispatch-0.6.0-py2-none-any.whl")
    version("0.5.0", sha256="58803e7a748ccf551ea2a7886183248093f5f78df48c71417401f17d63208dfa", url="https://pypi.org/packages/d1/0d/0d51971308af74de1a3a66e52cb518cb14c3fa9b0c6736105eacf77d2d09/multipledispatch-0.5.0-py2.py3-none-any.whl")
    version("0.4.9", sha256="e3be277f524f1fdcd2d6a23056e7f3101744f340327e88595afdc5af6d91de5b", url="https://pypi.org/packages/4c/b2/43d4944b102c8e8d1f2491dca85fea52982ee5dcf27312df1ef9ee7efb82/multipledispatch-0.4.9-py2.py3-none-any.whl")
    version("0.4.8", sha256="07d41fb3ed25e8424536e48a8566f88a0f9926ca4b6174bff6aa16c98251b92e", url="https://pypi.org/packages/ff/03/31f284e8b9ae2793ada14b62489292db89a4ce814ea19c90770236a933b5/multipledispatch-0.4.8.tar.gz")
    version("0.4.7", sha256="401bb875cdbd85359f01029e60ef7610bf1172b5052474285daf4102b109496d", url="https://pypi.org/packages/5d/49/1126b975b71b836c8ab1017f4b03f7734f88fc182fed33a664ea7a54b5a5/multipledispatch-0.4.7.tar.gz")
    version("0.4.6", sha256="9974135f46af8f22096f0517afede26a9b2e015aed9e154c4f5e3173a447162c", url="https://pypi.org/packages/ad/66/942782061db31ea90b293c65f8fec2c5f8b4d7e89c38dc0a5598afbb7b03/multipledispatch-0.4.6.tar.gz")
    version("0.4.5", sha256="aeb5974860656de5ea488c641a86adcb965b354d1bcddf8c0a07713619ee0237", url="https://pypi.org/packages/48/35/1872b05e183df33b2360715cbdf9234c0e4b9d07fa4bb0a343a5343684a9/multipledispatch-0.4.5.tar.gz")
    version("0.4.4", sha256="891f0786937536ac84d1f60bbafe4c365eafedc4d9eb3a20dd5d4b907f953614", url="https://pypi.org/packages/f3/03/698f91095a2c4a745a5da46972942d329dbcf5e5584d4af9fe65a7554fac/multipledispatch-0.4.4.tar.gz")
    version("0.4.3", sha256="9d8c20ffe7f3530c9b49529ab56ec65a4759c42e19f005693bc8a188c7427255", url="https://pypi.org/packages/bb/ee/33b8ce5248cfbd31b75d779c3f8d3b671db015b6eaf83244acd5bf553791/multipledispatch-0.4.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@0.6:0")
    # END DEPENDENCIES

