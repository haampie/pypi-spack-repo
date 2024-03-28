# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLxml(PythonPackage):
    # BEGIN VERSIONS
    version("5.1.0", sha256="3eea6ed6e6c918e468e693c41ef07f3c3acc310b70ddd9cc72d9ef84bc9564ca", url="https://pypi.org/packages/2b/b4/bbccb250adbee490553b6a52712c46c20ea1ba533a643f1424b27ffc6845/lxml-5.1.0.tar.gz")
    version("5.0.1", sha256="4432a1d89a9b340bc6bd1201aef3ba03112f151d3f340d9218247dc0c85028ab", url="https://pypi.org/packages/83/18/1d0c7cf3df839cc2827a0deee2e4b42f4048bc4c1c15612271e2db3928e5/lxml-5.0.1.tar.gz")
    version("5.0.0", sha256="2219cbf790e701acf9a21a31ead75f983e73daf0eceb9da6990212e4d20ebefe", url="https://pypi.org/packages/80/2c/076fafd979728858829fb9ce2e13fa6367b6be9acc4da0cff6367aa6a1ce/lxml-5.0.0.zip")
    version("4.9.4", sha256="b1541e50b78e15fa06a2670157a1962ef06591d4c998b998047fff5e3236880e", url="https://pypi.org/packages/84/14/c2070b5e37c650198de8328467dd3d1681e80986f81ba0fea04fc4ec9883/lxml-4.9.4.tar.gz")
    version("4.9.3", sha256="48628bd53a426c9eb9bc066a923acaa0878d1e86129fd5359aee99285f4eed9c", url="https://pypi.org/packages/30/39/7305428d1c4f28282a4f5bdbef24e0f905d351f34cf351ceb131f5cddf78/lxml-4.9.3.tar.gz")
    version("4.9.2", sha256="2455cfaeb7ac70338b3257f41e21f0724f4b5b0c0e7702da67ee6c3640835b67", url="https://pypi.org/packages/06/5a/e11cad7b79f2cf3dd2ff8f81fa8ca667e7591d3d8451768589996b65dec1/lxml-4.9.2.tar.gz")
    version("4.9.1", sha256="fe749b052bb7233fe5d072fcb549221a8cb1a16725c47c37e42b0b9cb3ff2c3f", url="https://pypi.org/packages/70/bb/7a2c7b4f8f434aa1ee801704bf08f1e53d7b5feba3d5313ab17003477808/lxml-4.9.1.tar.gz")
    version("4.9.0", sha256="520461c36727268a989790aef08884347cd41f2d8ae855489ccf40b50321d8d7", url="https://pypi.org/packages/aa/23/bda4e9881090f0f5e33e2efe89aacfa0668eb6e1ab2de28591e2912d78d4/lxml-4.9.0.tar.gz")
    version("4.8.0", sha256="f63f62fc60e6228a4ca9abae28228f35e1bd3ce675013d1dfb828688d50c6e23", url="https://pypi.org/packages/3b/94/e2b1b3bad91d15526c7e38918795883cee18b93f6785ea8ecf13f8ffa01e/lxml-4.8.0.tar.gz")
    version("4.7.1", sha256="a1613838aa6b89af4ba10a0f3a972836128801ed008078f8c1244e65958f1b24", url="https://pypi.org/packages/84/74/4a97db45381316cd6e7d4b1eb707d7f60d38cb2985b5dfd7251a340404da/lxml-4.7.1.tar.gz")
    version("4.6.4", sha256="daf9bd1fee31f1c7a5928b3e1059e09a8d683ea58fb3ffc773b6c88cb8d1399c", url="https://pypi.org/packages/fe/4c/a4dbb4e389f75e69dbfb623462dfe0d0e652107a95481d40084830d29b37/lxml-4.6.4.tar.gz")
    version("4.6.3", sha256="39b78571b3b30645ac77b95f7c69d1bffc4cf8c3b157c435a34da72e78c82468", url="https://pypi.org/packages/e5/21/a2e4517e3d216f0051687eea3d3317557bde68736f038a3b105ac3809247/lxml-4.6.3.tar.gz")
    version("4.6.1", sha256="c152b2e93b639d1f36ec5a8ca24cde4a8eefb2b6b83668fcd8e83a67badcb367", url="https://pypi.org/packages/c5/2f/a0d8aa3eee6d53d5723d89e1fc32eee11e76801b424e30b55c7aa6302b01/lxml-4.6.1.tar.gz")
    version("4.5.2", sha256="cdc13a1682b2a6241080745b1953719e7fe0850b40a5c71ca574f090a1391df6", url="https://pypi.org/packages/2c/4d/3ec1ea8512a7fbf57f02dee3035e2cce2d63d0e9c0ab8e4e376e01452597/lxml-4.5.2.tar.gz")
    version("4.4.2", sha256="eff69ddbf3ad86375c344339371168640951c302450c5d3e9936e98d6459db06", url="https://pypi.org/packages/e4/19/8dfeef50623892577dc05245093e090bb2bab4c8aed5cad5b03208959563/lxml-4.4.2.tar.gz")
    version("4.4.1", sha256="c81cb40bff373ab7a7446d6bbca0190bccc5be3448b47b51d729e37799bb5692", url="https://pypi.org/packages/c4/43/3f1e7d742e2a7925be180b6af5e0f67d38de2f37560365ac1a0b9a04c015/lxml-4.4.1.tar.gz")
    version("4.3.3", sha256="4a03dd682f8e35a10234904e0b9508d705ff98cf962c5851ed052e9340df3d90", url="https://pypi.org/packages/7d/29/174d70f303016c58bd790c6c86e6e86a9d18239fac314d55a9b7be501943/lxml-4.3.3.tar.gz")
    version("4.2.5", sha256="36720698c29e7a9626a0dc802ef8885f8f0239bfd1689628ecd459a061f2807f", url="https://pypi.org/packages/4b/20/ddf5eb3bd5c57582d2b4652b4bbcf8da301bdfe5d805cb94e805f4d7464d/lxml-4.2.5.tar.gz")
    version("3.7.3", sha256="aa502d78a51ee7d127b4824ff96500f0181d3c7826e6ee7b800d068be79361c7", url="https://pypi.org/packages/39/e8/a8e0b1fa65dd021d48fe21464f71783655f39a41f218293c1c590d54eb82/lxml-3.7.3.tar.gz")
    version("2.3", sha256="eea1b8d29532739c1383cb4794c5eacd6176f0972b59e8d29348335b87ff2e66", url="https://pypi.org/packages/ea/f8/c62f5857ca8274d89932696cb0876dab40385e2293a709a359f92793141e/lxml-2.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cssselect", default=False)
    variant("html5", default=False)
    variant("htmlsoup", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-beautifulsoup4", when="@4.2.2,4.2.4:4.5,4.9.4:+htmlsoup")
        depends_on("py-cssselect@0.7:", when="@4.2.2,4.2.4:4.5,4.9.4:+cssselect")
        depends_on("py-html5lib", when="@4.2.2,4.2.4:4.5,4.9.4:+html5")
    # END DEPENDENCIES

