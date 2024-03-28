# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRich(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("13.7.1", sha256="4edbae314f59eb482f54e9e30bf00d33350aaa94f4bfcd4e9e3110e64d0d7222", url="https://pypi.org/packages/87/67/a37f6214d0e9fe57f6ae54b2956d550ca8365857f42a1ce0392bb21d9410/rich-13.7.1-py3-none-any.whl")
    version("13.7.0", sha256="6da14c108c4866ee9520bbffa71f6fe3962e193b7da68720583850cd4548e235", url="https://pypi.org/packages/be/be/1520178fa01eabe014b16e72a952b9f900631142ccd03dc36cf93e30c1ce/rich-13.7.0-py3-none-any.whl")
    version("13.6.0", sha256="2b38e2fe9ca72c9a00170a1a2d20c63c790d0e10ef1fe35eba76e1e7b1d7d245", url="https://pypi.org/packages/be/2a/4e62ff633612f746f88618852a626bbe24226eba5e7ac90e91dcfd6a414e/rich-13.6.0-py3-none-any.whl")
    version("13.5.3", sha256="9257b468badc3d347e146a4faa268ff229039d4c2d176ab0cffb4c4fbc73d5d9", url="https://pypi.org/packages/c1/d1/23ba6235ed82883bb416f57179d1db2c05f3fb8e5d83c18660f9ab6f09c9/rich-13.5.3-py3-none-any.whl")
    version("13.5.2", sha256="146a90b3b6b47cac4a73c12866a499e9817426423f57c5a66949c086191a8808", url="https://pypi.org/packages/8d/5f/21a93b2ec205f4b79853ff6e838e3c99064d5dbe85ec6b05967506f14af0/rich-13.5.2-py3-none-any.whl")
    version("13.5.1", sha256="b97381b204a206e1be618f5e1215a57174a1a7732490b3bf6668cf41d30bc72d", url="https://pypi.org/packages/83/d5/311cc7acdc4dfb146e419c5975c23ffca4e3023a6f41588af35d19718e0c/rich-13.5.1-py3-none-any.whl")
    version("13.5.0", sha256="996670a7618ccce27c55ba6fc0142e6e343773e11d34c96566a17b71b0e6f179", url="https://pypi.org/packages/cf/2c/aa1418e8fafb5489c6fbfb36ba6afc1be72b196419bdea0c501487743740/rich-13.5.0-py3-none-any.whl")
    version("13.4.2", sha256="8f87bc7ee54675732fa66a05ebfe489e27264caeeff3728c945d25971b6485ec", url="https://pypi.org/packages/fc/1e/482e5eec0b89b593e81d78f819a9412849814e22225842b598908e7ac560/rich-13.4.2-py3-none-any.whl")
    version("13.4.1", sha256="d204aadb50b936bf6b1a695385429d192bc1fdaf3e8b907e8e26f4c4e4b5bf75", url="https://pypi.org/packages/ea/93/c68645c689d10a035010e3ae314b6b2855d040ce0d11fdfdfbb8be416581/rich-13.4.1-py3-none-any.whl")
    version("13.4.0", sha256="db8c367c0fbe39f72334452ecfdd708e8f2a6b8d16b2c94f451775d6c86e3965", url="https://pypi.org/packages/79/2c/165e0916c5488f0662637f49507480b7e9fc47428b478be2cc0d57664914/rich-13.4.0-py3-none-any.whl")
    version("12.5.1", sha256="2eb4e6894cde1e017976d2975ac210ef515d7548bc595ba20e195fb9628acdeb", url="https://pypi.org/packages/f6/39/4cb526e0d505464376e3c47a812df6e6638363ebe66e6a63618831fe47ad/rich-12.5.1-py3-none-any.whl")
    version("10.14.0", sha256="ab9cbfd7a3802d8c6f0fa91e974630e2a69447972dcbb9dfe9b01016dd95e38e", url="https://pypi.org/packages/37/51/0e3e0adf12839a7ae73956942e5d47cb246566c8b9223851569369d4da34/rich-10.14.0-py3-none-any.whl")
    version("10.9.0", sha256="2c84d9b3459c16bf413fe0f9644c7ae1791971e0bb944dfae56e7c7634b187ab", url="https://pypi.org/packages/e9/c4/ea9a6e34dd5c4c3049b0a86c49feb7f38c9f5e901ffb6eeb832e89dfa540/rich-10.9.0-py3-none-any.whl")
    version("10.0.0", sha256="01b3fcc305ae71b9ade4a645b6e371d395c6cd9ba52dcf180bfba69ef05c13b5", url="https://pypi.org/packages/5c/94/435b820f6be96a650a3d00025efb9955a6b4e1e6f070ca18c3c134289b76/rich-10.0.0-py3-none-any.whl")
    version("9.9.0", sha256="d376396cb3793a042f6167cd613a31a370ea2c5ec1bbdf76a5c9e9c588ccff12", url="https://pypi.org/packages/cb/dc/bee6fdd474ecc0456dcf176b40c95108978e9a6ec027a031dfe9a8520455/rich-9.9.0-py3-none-any.whl")
    version("9.8.2", sha256="d7732d12dfa91a2c06f89fa2b630a068ba12d39ad22a2078b477ef1948b38f3f", url="https://pypi.org/packages/b9/2b/5ff334698e7b246dae1bdc672963b872faf9e74ffa8121305e9c0f0c018b/rich-9.8.2-py3-none-any.whl")
    version("9.8.1", sha256="7e594114b109dfcf4c242a5ae1b2767dbc49d0abc9c5f082eb7e558dd622bc90", url="https://pypi.org/packages/20/d3/802735641e249bffa5dc650d21ec871cc8a34d49216385e457da61e222e0/rich-9.8.1-py3-none-any.whl")
    version("9.8.0", sha256="812a911cd85d32f484325f501fb8f84270b8e0a7af739d4bf1d3df42643e93a6", url="https://pypi.org/packages/e6/1a/3d2d4e6ac7178cd9e1accfefef502eebec930e0a1d59bce83b4685044be3/rich-9.8.0-py3-none-any.whl")
    version("9.7.0", sha256="f1967aa6c91dc700c322b54165b35a38785e0e666c1522f9f9a876073b68831b", url="https://pypi.org/packages/e5/30/4361eeb72b551262ee5ef415ea61b9e5ad2c6028649c63321d23f02c69fb/rich-9.7.0-py3-none-any.whl")
    version("9.6.2", sha256="e0efd2ba715dcfb78e57986e15c6d70a3beb98a7015471ca9dd511571a8a9882", url="https://pypi.org/packages/37/61/d25e97f11b712fbbdbaff37d963197e6d218a94b4e0f8882da63bdb21613/rich-9.6.2-py3-none-any.whl")
    version("9.6.1", sha256="064814e6cfbc61ff1f82b1e950667c5dc3bf3ec3ed9ca6f62a29007d1bc5ed4c", url="https://pypi.org/packages/40/b4/ff5ef4691df6d947bc9ce2f4bc3c12196f714048b5e2e401b22746e77634/rich-9.6.1-py3-none-any.whl")
    version("9.6.0", sha256="85d9d67f25ab2d676666c9895bdbfa064f9e68791977637f03b49b290cf4e3ac", url="https://pypi.org/packages/f0/ea/e37495b286215f6fd41c68faf162f0933eb5106d7e3cef37015fc7dc49bd/rich-9.6.0-py3-none-any.whl")
    version("9.5.1", sha256="0f4359df97670c1981599690458c4c9ede02c56f59ae3a648b7154cdba21b0cc", url="https://pypi.org/packages/e4/65/2376e6510efc51a3e7ead4012c6ade4742634cd89127bd5368a380d23454/rich-9.5.1-py3-none-any.whl")
    version("9.5.0", sha256="7a768215cc1175218223079fbfaa452b080529cac6439079bb70684e698281ce", url="https://pypi.org/packages/76/8a/00f666183508da511f7f03dde9f05d708dd4a43ba1d2b6d96adc96f021c2/rich-9.5.0-py3-none-any.whl")
    version("9.4.0", sha256="dfc1d6a394f97674163b2b2c24d12e15f85752ce5451043c4d3ce77dad16a07d", url="https://pypi.org/packages/f9/a0/875fd1285885fd491540380a10f22834f3648ff5a3c3a0ed3c2013888e72/rich-9.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama@0.4:", when="@1.0.1:11")
        depends_on("py-commonmark@0.9:", when="@0.4:13.1")
        depends_on("py-markdown-it-py@2.2:", when="@13.4.2:")
        depends_on("py-markdown-it-py@2.2:2", when="@13.3.2:13.4.1")
        depends_on("py-pygments@2.13:", when="@13.3.2:")
        depends_on("py-pygments@2.6:", when="@1.0.1:13.2")
        depends_on("py-typing-extensions@4:", when="@12.2: ^python@:3.8")
        depends_on("py-typing-extensions@3.7.4:3", when="@0.2:10.1")
    # END DEPENDENCIES

