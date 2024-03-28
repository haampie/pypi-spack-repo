# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFixtures(PythonPackage):
    # BEGIN VERSIONS
    version("4.1.0", sha256="a43a55da406c37651aa86dd1ba6c3983a09d36d60fe5f72242872c8a4eeeb710", url="https://pypi.org/packages/db/ab/3259874efafdbaa9d25dd8fa99c999621c6539eacd03c95b64a34bd5acd1/fixtures-4.1.0-py3-none-any.whl")
    version("4.0.1", sha256="d2758826400d095b79666cf93a32a84f50ff8cd179831927efb48cd1e3ca7466", url="https://pypi.org/packages/3c/3d/f106b3278ba50067e9cd397f836d33d141aa790853152dbb3512aaee19f3/fixtures-4.0.1.tar.gz")
    version("4.0.0", sha256="c579191f96a088b16095eb60e21d3eb6334f006a93e248f4decdcb6bfef238d8", url="https://pypi.org/packages/9e/e7/58f53ed1cf81bec87e79558df62a9a8650e11ac5230734a8e75c689a3980/fixtures-4.0.0-py3-none-any.whl")
    version("3.0.0", sha256="2a551b0421101de112d9497fb5f6fd25e5019391c0fbec9bad591ecae981420d", url="https://pypi.org/packages/a8/28/7eed6bf76792f418029a18d5b2ace87ce7562927cdd00f1cefe481cd148f/fixtures-3.0.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="de4582925a49aaa46c6bc810eaac74a96014c719630ff0e47c4cd361dfd9d7d9", url="https://pypi.org/packages/df/a5/31505ab93b7433022eab2a6305d8f320012176eda465528771be49765123/fixtures-2.0.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="c7944a31a4b81758e41c163e7b2ab87b505df66bc2cabbacede15bfab619ca16", url="https://pypi.org/packages/b4/b6/4409d6bef30805cfe2bacc38040e34165244d3babcf3e3d289a68096ddb6/fixtures-1.4.0-py2.py3-none-any.whl")
    version("1.3.2.dev6", sha256="64918b2497904b515ca45e0a4a791b96bdbc53c504aee98ae22f2d0e2072d8f6", url="https://pypi.org/packages/e2/6f/21952dfb7fe7aadd6630f2be951ef564c18f4deb82f15795ea929e2ab2c4/fixtures-1.3.2.dev6.tar.gz")
    version("1.3.1", sha256="4603391f62aec34f06a64c50bee558ae723506a1a7224d13f692e05ec53859bb", url="https://pypi.org/packages/e5/10/ab3ef83597e367e233dd688421ba5b8428683db08233d87f2db9636ccf26/fixtures-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="34c2d10e7482e55f7ff754510232f96a8be0b25002b77b33a32a2c01e1b1ac31", url="https://pypi.org/packages/9f/54/ef98dcf2a3c511ed99b86cbf10c973a11c6615a8a4c937179bcf1b82509b/fixtures-1.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pbr@5.7:", when="@4:4.0.0,4.1:")
        depends_on("py-testtools@2.5:", when="@4:4.0.0")
    # END DEPENDENCIES

