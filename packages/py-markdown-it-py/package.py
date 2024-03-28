# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkdownItPy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.0", sha256="355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", url="https://pypi.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl")
    version("2.2.0", sha256="5a35f8d1870171d9acc47b99612dc146129b631baf04970128b568f190d0cc30", url="https://pypi.org/packages/bf/25/2d88e8feee8e055d015343f9b86e370a1ccbec546f2865c98397aaef24af/markdown_it_py-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="93de681e5c021a432c63147656fe21790bc01231e0cd2da73626f1aa3ac0fe27", url="https://pypi.org/packages/f9/3f/ecd1b708973b9a3e4574b43cffc1ce8eb98696da34f1a1c44a68c3c0d737/markdown_it_py-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="31974138ca8cafbcb62213f4974b29571b940e78364584729233f59b8dfdb8bd", url="https://pypi.org/packages/76/76/8e186ed000240e4ed46fc51637e00b30c08490ac9f5e5ed43c0713c68b45/markdown_it_py-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="15cc69c5b7c493ba8603722b710e39ce3fab2961994179fb4fa1c99b070d2059", url="https://pypi.org/packages/cf/2e/1a8564f14f84b085e9cb52c7d634e88461c071123d7855fef16b0737b4e4/markdown_it_py-2.0.0-py3-none-any.whl")
    version("1.1.0", sha256="98080fc0bc34c4f2bcf0846a096a9429acbd9d5d8e67ed34026c03c61c464389", url="https://pypi.org/packages/08/6b/33c40781e26c76e26825528f417f5414c501807f1f7fced82119c29aa832/markdown_it_py-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="ac9e0f051ffd2aabecdd83b41b8fb71d7ab24005a3e0e63f192138dd699a6932", url="https://pypi.org/packages/a4/59/fd21c64e4c547416fb6975bcd5b23a8332a5e190c963f7a7336266e347aa/markdown_it_py-1.0.0-py3-none-any.whl")
    version("1.0.0-beta3", sha256="226d2221d1eae6618e42a870bd58674a5f6682e358b7f38abb7e26a01a0cace2", url="https://pypi.org/packages/e1/f6/ba0ea7fe2fb0aa61e8ef3402741bb225640077863d718b820f1343ac25c1/markdown_it_py-1.0.0b3-py3-none-any.whl")
    version("1.0.0-beta2", sha256="53945d3a8ae52611f20eefef3e2bf70093491a31c7fe2087ea81632c8d447ba1", url="https://pypi.org/packages/8f/66/3952dd02ea7831a03964b8b79273f007d66897b2c22442d4462b45fa3f2d/markdown_it_py-1.0.0b2-py3-none-any.whl")
    version("1.0.0-beta1", sha256="051e9c076e922b83160b33722f791882059d8ec6ce7d8f6b810301df49516e3e", url="https://pypi.org/packages/e0/1d/308126ff30a2bf87fa0326f3245b85491dfc7c271266e2175b600a0a0a6f/markdown_it_py-1.0.0b1-py3-none-any.whl")
    version("0.6.2", sha256="30b3e9f8198dc82a5df0dcb73fd31d56cd9a43bf8a747feb10b2ba74f962bcb1", url="https://pypi.org/packages/2e/cb/8493188845d26599170268bb0e0a63e75584d5e7f130488c641e96449cd7/markdown_it_py-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="f22808fed0fd5c006c5c1626ea4e6c68123d5af54eb54712af77a4c57ad34ebc", url="https://pypi.org/packages/36/54/4e983048843a5adb6baf58412ab5c4272a412b5fb837fad7e2093576564e/markdown_it_py-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="f90912a0ff1ac328627d1551bd5a17bce0ef1d483df222d460336e59213c6d29", url="https://pypi.org/packages/41/e2/bc095d382e451f72f2e2b18bbdbb1389975fbec98a1240a0cba3a9559d85/markdown_it_py-0.6.0-py3-none-any.whl")
    version("0.5.8", sha256="d71989a540588875bb60919feb4ce83989beb2d4dd018f7a6ed475d4cf0c76ff", url="https://pypi.org/packages/f8/1b/0e24960d9f6553f3ea170f5fe56bb0230943a968c2a6fbcca7ed49b9cd6e/markdown_it_py-0.5.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("linkify", default=False)
    variant("plugins", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19:21", when="@1.1:2.0")
        depends_on("py-attrs@19:20", when="@0.5.1:1.0")
        depends_on("py-linkify-it-py@1:", when="@2.2:+linkify")
        depends_on("py-linkify-it-py@1", when="@0.5.8:2.1+linkify")
        depends_on("py-mdit-py-plugins", when="@1.0.0-beta2:+plugins")
        depends_on("py-mdit-py-plugins@0.2.6:0.2", when="@1:1.0.0-beta1")
        depends_on("py-mdit-py-plugins@0.2.1:0.2", when="@0.6:0")
        depends_on("py-mdurl@0.1:", when="@2:")
    # END DEPENDENCIES

