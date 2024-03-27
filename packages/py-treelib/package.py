##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTreelib(PythonPackage):
    version("1.7.0", sha256="c37795eaba19f73f3e1a905ef3f4f0cab660dc7617126e8ae99391e25c755416", url="https://pypi.org/packages/74/93/0944bb5ade972a5ef2dd9211a20730081ed2833024239171807d7a9bd4b0/treelib-1.7.0-py3-none-any.whl")
    version("1.6.4", sha256="4218f7dded2448dfa6a335888bf68a28430660163e7faf18c6128ec4477d34c0", url="https://pypi.org/packages/99/36/0d5a284d58dee33a738c1a77cf032a93cb978a7382497fb54f31baa0dc1a/treelib-1.6.4-py3-none-any.whl")
    version("1.6.3", sha256="2a7096d6b7e711bbc1e67f942430be7d7882e8c45b197bd1cbfb5cd35705b0cc", url="https://pypi.org/packages/89/9c/785a06eba694dac22aeae08e177da148474e49f1c8ecc521619a9a68bfc6/treelib-1.6.3-py3-none-any.whl")
    version("1.6.1", sha256="1cbfffb2d2b75ccac27d0200cee0507b6fbb0726e0afb9fae017ade5d2ce8788", url="https://pypi.org/packages/04/b0/2269c328abffbb63979f7143351a24a066776b87526d79956aea5018b80a/treelib-1.6.1.tar.gz")
    version("1.5.5", sha256="44695f7048b0bd82b45a4fe976611f9fb52902506249d84db255976a5e8738e0", url="https://pypi.org/packages/17/47/0a8e745a1982ca82ef2149903fc77d5bbf08c4d566f8d238dca7eaf59837/treelib-1.5.5.tar.gz")
    version("1.5.3", sha256="3e4ee4ea22ec9e6e5fe5df4f4d6189a9b2c6c6604bd835d692419466e0312f0a", url="https://pypi.org/packages/cf/4f/f6dc76341c438a84672386a5db57c1a49b3d79a642a09328c7c3f72db144/treelib-1.5.3.tar.gz")
    version("1.5.1", sha256="5f781a48eef400d09b5d57e786b1e1ac5e5127cd33f1399e7fd8066f1858e0e4", url="https://pypi.org/packages/f1/11/19621205d33cbd45a28740eee35754d0d28aba5d829ad20d1d1d2162bcb3/treelib-1.5.1.tar.gz")
    version("1.5.0", sha256="74638bc7976d2f19b0da05a047e9b85f26f9ac8381f99af3e2f765b2e878b1db", url="https://pypi.org/packages/54/7d/efcf36cb10e2abda33afde87035802df10183e23b15a22806f8812d7652f/treelib-1.5.0.tar.gz")
    version("1.4.0", sha256="726f7b7445ee74e62af8e4a063467d6f305eae6cfe2f2756066370a8a7618a42", url="https://pypi.org/packages/7f/4a/8599679d437b2e33405269b2f0ce4f4610ef8a36e740a6ec83ef45a35c71/treelib-1.4.0.tar.gz")
    version("1.3.7", sha256="157dfefcafaca41ed0605ae2ba4432fbec80f6bcfd5bb0c14fb756b24809329f", url="https://pypi.org/packages/1d/61/df5914a50c7501f2fd4de82803cde26bf785fcc59dcec44673704a4d87a8/treelib-1.3.7.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@1.6.3:")

