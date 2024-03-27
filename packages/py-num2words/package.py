##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNum2words(PythonPackage):
    version("0.5.13", sha256="39e662c663f0a7e15415431ea68eb3dc711b49e3b776d93403e1da0a219ca4ee", url="https://pypi.org/packages/8f/f0/ca1228af2bcbce2fdf2b23d58643c84253b88a3c1cd9dba391ca683c4b21/num2words-0.5.13-py3-none-any.whl")
    version("0.5.12", sha256="9eeef488658226ab36818c06d7aeb956d19b530fb62030596b6802fb4659f30e", url="https://pypi.org/packages/eb/09/b14d798bc02411b1e5a9896d680f8f417cadc53232bbf7ae9d30263dcf45/num2words-0.5.12-py3-none-any.whl")
    version("0.5.11", sha256="0cabf605a9a0161282affc98ed682c32559963f73b05a23fd5f049b6fa8a2603", url="https://pypi.org/packages/6c/e5/9ee14acf01cfb3dd49bb220abb2bc231203ad6a50d44455f52e710ab01ef/num2words-0.5.11-py3-none-any.whl")
    version("0.5.10", sha256="0b6e5f53f11d3005787e206d9c03382f459ef048a43c544e3db3b1e05a961548", url="https://pypi.org/packages/eb/a2/ea800689730732e27711c41beed4b2a129b34974435bdc450377ec407738/num2words-0.5.10-py3-none-any.whl")
    version("0.5.9", sha256="f2f561a8ee02b57e7f17837198d353f05ea1199792c4860da57322f7aa86d171", url="https://pypi.org/packages/97/59/daea20448b3bf3cc07694f393a2a9d06439e4c9a96f83734d9d2c5231703/num2words-0.5.9-py3-none-any.whl")
    version("0.5.8", sha256="f923a5877abba82b916acd92432720e09a95d507d620c01fabd0143f7460a4d7", url="https://pypi.org/packages/7d/2c/72bc7baabd7bc25f08a9dbc0ee8c56bb8f26a4d96c35786081b5217640d3/num2words-0.5.8-py3-none-any.whl")
    version("0.5.7", sha256="ac4b5971b427611bc565c395e95289ba09b3b1c0fb041ad2538786dde816d664", url="https://pypi.org/packages/bc/9a/31a9151abd891ab7387d8d74cb0d84c4e77674735dbf85a63dfeb8eed6a6/num2words-0.5.7.tar.gz")
    version("0.5.6", sha256="529017394eef84daf63bb57e837fe2fb81363d1b06f6114e86608dae7ceb11ee", url="https://pypi.org/packages/aa/6e/6d026d15d1b0fd37a9dd42ecf559f36871cee67158aff5ba652d3130e8b9/num2words-0.5.6-py2.py3-none-any.whl")
    version("0.5.5", sha256="84e3ef9a7539135c67b1642156ffb22dc14946b342d1f0a9503e1f31374c37e2", url="https://pypi.org/packages/5f/d8/1c1fb47cce56ff2cc1f5eb2740f2679045769778a746fbf9ebff1d70a63e/num2words-0.5.5-py2.py3-none-any.whl")
    version("0.5.4", sha256="9c15ee58b2e23804c17d7fcf9864601b89ef54f85c5db600f1eb2b2b2709be86", url="https://pypi.org/packages/8f/27/98c9acd3629aa9269aa746dde13b5e34529e1ddbada7e3c9b166d2101b54/num2words-0.5.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-docopt@0.6.2:", when="@0.5.8:")

