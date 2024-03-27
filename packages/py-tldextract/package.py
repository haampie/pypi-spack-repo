##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTldextract(PythonPackage):
    version("5.1.2", sha256="4dfc4c277b6b97fa053899fcdb892d2dc27295851ab5fac4e07797b6a21b2e46", url="https://pypi.org/packages/fc/6d/8eaafb735b39c4ab3bb8fe4324ef8f0f0af27a7df9bb4cd503927bd5475d/tldextract-5.1.2-py3-none-any.whl")
    version("5.1.1", sha256="b9c4510a8766d377033b6bace7e9f1f17a891383ced3c5d50c150f181e9e1cc2", url="https://pypi.org/packages/d0/de/3f37b2568115c7ebeae39508dc1092f04f3dc286f22ef30171baca9c9cf2/tldextract-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="c8eecb15f556b43db6eebd21667640fb6fba9bc9539b48707432014913a78d13", url="https://pypi.org/packages/55/c8/43abd77a03143c7be1474df13d08118e1c37e7868e13d7bbc4a9a7d849eb/tldextract-5.1.0-py3-none-any.whl")
    version("5.0.1", sha256="8322fa2b73d9572c6bde31e96f66b694abb86d85b32ed6082593da806a6d33b4", url="https://pypi.org/packages/75/c0/038a9529d1b3cf10ab682bb66e2e253530e5380c2b656205703d9f618b30/tldextract-5.0.1-py3-none-any.whl")
    version("5.0.0", sha256="1f4938a58ea6aa3fc5b374e22c9477ed43159a26c61a5c51a0bf0fdd694fd5e1", url="https://pypi.org/packages/3d/c3/e743f2a39cd38b0ea5af0d7833ba18bd73f79ea5348826d2a08d8b3ba5e4/tldextract-5.0.0-py3-none-any.whl")
    version("4.0.0", sha256="9950afba41f7dfda3ef3fcc8fdc12790c22a662c5b4e6d1d796eff32bf7048dc", url="https://pypi.org/packages/38/38/ef579e09695b406075370265e3f74030a6190556351e3af23c2f402c9a41/tldextract-4.0.0-py3-none-any.whl")
    version("3.6.0", sha256="30a492de80f4de215aa998588ba5c2e625ee74ace3a2705cfb52b0021053bcbe", url="https://pypi.org/packages/76/a6/adc68851ae4a7fd6a02ad5c1c2f4533d5811c64558bfaa583a61b0e312b5/tldextract-3.6.0-py3-none-any.whl")
    version("3.5.0", sha256="2cb271ca8d06ea1630a1361b58edad14e0cf81f34ce3c90b052854528fe2a281", url="https://pypi.org/packages/e4/6b/2e0c1449c0768f25ea8054476a991152a59507ac019a5647d92e44540a73/tldextract-3.5.0-py3-none-any.whl")
    version("3.4.4", sha256="581e7dbefc90e7bb857bb6f768d25c811a3c5f0892ed56a9a2999ddb7b1b70c2", url="https://pypi.org/packages/7e/83/8ab4b0505086a92bda25d81b39cfbfc4e90f432a3dd7b0d2725579e7998a/tldextract-3.4.4-py3-none-any.whl")
    version("3.4.3", sha256="5ed3fd01df4e78b8b378bdff94397cd8cdb130b54d2681c40d254beadd50f69f", url="https://pypi.org/packages/ce/d5/fd274ffb00ace49387b3de13eb8346f7003ee23b01c2bc8c2737a9e856f4/tldextract-3.4.3-py3-none-any.whl")
    version("3.4.1", sha256="26f646987b01ae2946e7491cce4aaf54129f3489a196a274e6c843ec72968313", url="https://pypi.org/packages/fb/21/dad9eaedad757362458f92f9345307cc847956ab9775ee9ab5a0fcb912cf/tldextract-3.4.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-filelock@3.0.8:", when="@3:")
        depends_on("py-idna", when="@2.2.1:")
        depends_on("py-requests@2.1:", when="@2.2.1:")
        depends_on("py-requests-file@1.4:", when="@2.2.1:")

