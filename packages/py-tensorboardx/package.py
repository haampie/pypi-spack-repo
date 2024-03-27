##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorboardx(PythonPackage):
    version("2.6.2.2", sha256="160025acbf759ede23fd3526ae9d9bfbfd8b68eb16c38a010ebe326dc6395db8", url="https://pypi.org/packages/44/71/f3e7c9b2ab67e28c572ab4e9d5fa3499e0d252650f96d8a3a03e26677f53/tensorboardX-2.6.2.2-py2.py3-none-any.whl")
    version("2.6.2.1", sha256="391ee8dc123e5c19c5a565d36e1fe98ddc9f727e1fd71f3e076658e6228ca36d", url="https://pypi.org/packages/f7/94/63570a1a408077217ed086056bcaf5a50c20fcb26b50152ed59e55ec5cab/tensorboardX-2.6.2.1-py2.py3-none-any.whl")
    version("2.6.2", sha256="951260a78c63dc97a89b1e6756c2bfc4c7dfd70782382e5b8b3a65e396a14149", url="https://pypi.org/packages/44/7b/eee50dcadcee4c674353ca207fdcd53a5b1f382021af1ed1797f9c0c45d2/tensorboardX-2.6.2-py2.py3-none-any.whl")
    version("2.6.1", sha256="4960feb79b1b84fd2b020885b09fd70962caec277d4bc194f338a6c203cd78ca", url="https://pypi.org/packages/02/bd/673947dde6b3a43f4ffc3abaf103947c4fb574ac8b7c32747f2421f1f7c9/tensorboardX-2.6.1-py2.py3-none-any.whl")
    version("2.6", sha256="24a7cd076488de1e9d15ef25371b8ebf90c4f8f622af2477c611198f03f4a606", url="https://pypi.org/packages/60/9f/d532d37f10ac7af136d4c2ba71e1fe7af0f3cc0cc076dfc05826171e9737/tensorboardX-2.6-py2.py3-none-any.whl")
    version("2.5.1", sha256="8808133ccca673cd04076f6f2a85cf2d39bb2d0393a0f20d0f9cbb06d472b57e", url="https://pypi.org/packages/96/47/9004f6b182920e921b6937a345019c9317fda4cbfcbeeb2af618b3b7a53e/tensorboardX-2.5.1-py2.py3-none-any.whl")
    version("2.5", sha256="b1d8903f8106e2f4484640a293f9680f9757d5f7d2e699e0672bb2382d988e07", url="https://pypi.org/packages/8b/6e/1a997fbf7f10aa80ea7c70d44c69724bf9dd6823a5d60f6cb6a4a246114e/tensorboardX-2.5-py2.py3-none-any.whl")
    version("2.4.1", sha256="209770034b87e99bfa36ecb471462c3bcce6544324b0c891958b65523348c277", url="https://pypi.org/packages/98/88/977b2f03fd0f8a2490fc7a1ad691d5e44cee5f1dc90c57078c5c168e2e70/tensorboardX-2.4.1-py2.py3-none-any.whl")
    version("2.4", sha256="2742b1ac3fdef2b938b1110b503c6986b7100a3250394a5a44ef12784b563b55", url="https://pypi.org/packages/99/0b/a26bbe92667c549d39c40b80c5ddec638fbae9521f04aeef26560e07e504/tensorboardX-2.4-py2.py3-none-any.whl")
    version("2.3", sha256="829e9548635c67aafd6bcdc8dc61fda93fa40e92fe06103c5c8645ea2cf54b59", url="https://pypi.org/packages/42/36/2b147652c40c3a858efa0afbf7b8236fae968e88ff530511a4cfa299a506/tensorboardX-2.3-py2.py3-none-any.whl")
    version("2.1", sha256="2d81c10d9e3225dcd9bb5fb277588610bdf45317603e7682f6953d83b5b38f6a", url="https://pypi.org/packages/af/0c/4f41bcd45db376e6fe5c619c01100e9b7531c55791b7244815bac6eac32c/tensorboardX-2.1-py2.py3-none-any.whl")
    version("2.0", sha256="8e336103a66b1b97a663057cc13d1db4419f7a12f332b8364386dbf8635031d9", url="https://pypi.org/packages/35/f1/5843425495765c8c2dd0784a851a93ef204d314fc87bcc2bbb9f662a3ad1/tensorboardX-2.0-py2.py3-none-any.whl")
    version("1.9", sha256="3d6706fc0d0b2d4afbb9ec8bfc2aa9b7c2abff7d4dc3e1cb92cf180c9cfaf1d6", url="https://pypi.org/packages/a6/5c/e918d9f190baab8d55bad52840d8091dd5114cc99f03eaa6d72d404503cc/tensorboardX-1.9-py2.py3-none-any.whl")
    version("1.8", sha256="f52e59b38b4cdf83384f3fce067bcaf2d2847619f9f533394df0de3b5a71ab8e", url="https://pypi.org/packages/c3/12/dcaf67e1312475b26db9e45e7bb6f32b540671a9ee120b3a72d9e09bc517/tensorboardX-1.8-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-packaging", when="@2.6:")
        depends_on("py-protobuf@3.20.0:", when="@2.6.2.2:")
        depends_on("py-protobuf", when="@2.6.2:2.6.2.1")
        depends_on("py-protobuf@4.22.3:", when="@2.6.1")
        depends_on("py-protobuf@3.8.0:3", when="@2.6:2.6.0")
        depends_on("py-protobuf@3.8.0:3.20.1", when="@2.5.1:2.5")
        depends_on("py-protobuf@3.8.0:", when="@1.9:2.5.0")
        depends_on("py-protobuf@3.2.0:", when="@1.4:1.8")
        depends_on("py-six", when="@:2.1,2.5:2.5.0")

