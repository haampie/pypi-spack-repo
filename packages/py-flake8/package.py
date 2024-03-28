# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlake8(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.0.0", sha256="a6dfbb75e03252917f2473ea9653f7cd799c3064e54d4c8140044c5c065f53c3", url="https://pypi.org/packages/e3/01/cc8cdec7b61db0315c2ab62d80677a138ef06832ec17f04d87e6ef858f7f/flake8-7.0.0-py2.py3-none-any.whl")
    version("6.1.0", sha256="ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5", url="https://pypi.org/packages/b0/24/bbf7175ffc47cb3d3e1eb523ddb23272968359dfcf2e1294707a2bf12fc4/flake8-6.1.0-py2.py3-none-any.whl")
    version("6.0.0", sha256="3833794e27ff64ea4e9cf5d410082a8b97ff1a06c16aa3d2027339cd0f1195c7", url="https://pypi.org/packages/d9/6a/bb0122ebe280476c924470779d2595f1403878cafe3c8a343ac56a5a9c0e/flake8-6.0.0-py2.py3-none-any.whl")
    version("5.0.4", sha256="7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248", url="https://pypi.org/packages/cf/a0/b881b63a17a59d9d07f5c0cc91a29182c8e8a9aa2bde5b3b2b16519c02f4/flake8-5.0.4-py2.py3-none-any.whl")
    version("5.0.3", sha256="93aa565ae2f0316b95bb57a354f2b2d55ee8508e1fe1cb13b77b9c195b4a2537", url="https://pypi.org/packages/ed/be/d1705b8bab0452b5682f5a7c4de6c01e998da2ae4bdeece2425f9d59ad87/flake8-5.0.3-py2.py3-none-any.whl")
    version("5.0.2", sha256="a7926e0b6d23c0991245b60279e774d2596dfecd9b158525d1f8c050a61eae5a", url="https://pypi.org/packages/6b/c0/b468ca1fb44acb7c054008e6edc0171e4209dd527bdb4f5836667102f36d/flake8-5.0.2-py2.py3-none-any.whl")
    version("5.0.1", sha256="44e3ecd719bba1cb2ae65d1b54212cc9df4f5db15ac271f8856e5e6c2eebefed", url="https://pypi.org/packages/4f/24/5396113ca4621c0bcc924a2e9ceb7bf03e141ebbfcc89c724284f55225c7/flake8-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="f44e470195849d0596cb488c7bd769086fcbe987c10cc9daae9a13b4136abb24", url="https://pypi.org/packages/ad/b5/27d1c9553cfd5282e5f94fe0306b231890d42d86506fb7f623bc638e741e/flake8-5.0.0-py2.py3-none-any.whl")
    version("4.0.1", sha256="479b1304f72536a55948cb40a32dce8bb0ffe3501e26eaf292c7e60eb5e0428d", url="https://pypi.org/packages/34/39/cde2c8a227abb4f9ce62fe55586b920f438f1d2903a1a22514d0b982c333/flake8-4.0.1-py2.py3-none-any.whl")
    version("4.0.0", sha256="124554bfd067e04d891258c0208a764b512ca3a94c8a3c06bea56af539dd74db", url="https://pypi.org/packages/0f/cc/931e8fd88a7730d66ee3b962f954eef1efc9959d618d01574cebf6905dae/flake8-4.0.0-py2.py3-none-any.whl")
    version("3.9.2", sha256="bf8fd333346d844f616e8d47905ef3a3384edae6b4e9beb0c5101e25e3110907", url="https://pypi.org/packages/fc/80/35a0716e5d5101e643404dabd20f07f5528a21f3ef4032d31a49c913237b/flake8-3.9.2-py2.py3-none-any.whl")
    version("3.9.1", sha256="3b9f848952dddccf635be78098ca75010f073bfe14d2c6bda867154bea728d2a", url="https://pypi.org/packages/a0/b0/3b5820728d687f2c000476216a3fccc7a03baac1034afc0284ccde25e26d/flake8-3.9.1-py2.py3-none-any.whl")
    version("3.9.0", sha256="12d05ab02614b6aee8df7c36b97d1a3b2372761222b19b58621355e82acddcff", url="https://pypi.org/packages/2a/cb/cd92e789442e234b8701bf6e886a55fbc83b7fd6e529b047e20b9cf196e8/flake8-3.9.0-py2.py3-none-any.whl")
    version("3.8.4", sha256="749dbbd6bfd0cf1318af27bf97a14e28e5ff548ef8e5b1566ccfb25a11e7c839", url="https://pypi.org/packages/d4/ca/3971802ee6251da1abead1a22831d7f4743781e2f743bd266bdd2f46c19b/flake8-3.8.4-py2.py3-none-any.whl")
    version("3.8.3", sha256="15e351d19611c887e482fb960eae4d44845013cc142d42896e9862f775d8cf5c", url="https://pypi.org/packages/6c/20/6326a9a0c6f0527612bae748c4c03df5cd69cf06dfb2cf59d85c6e165a6a/flake8-3.8.3-py2.py3-none-any.whl")
    version("3.8.2", sha256="ccaa799ef9893cebe69fdfefed76865aeaefbb94cb8545617b2298786a4de9a5", url="https://pypi.org/packages/ea/35/dcf9a3393305bfc61854b764b5aeb79a72493e77991eead133c189d7868e/flake8-3.8.2-py2.py3-none-any.whl")
    version("3.8.1", sha256="6c1193b0c3f853ef763969238f6c81e9e63ace9d024518edc020d5f1d6d93195", url="https://pypi.org/packages/bf/47/36e51603431e1a5289eb41636199d2c225fcb1ca286e29c02d219c8e6e88/flake8-3.8.1-py2.py3-none-any.whl")
    version("3.8.0", sha256="bcf5163890bb01f11f04f0f444f01004d0f9ad5fab10c51104f770acf532008f", url="https://pypi.org/packages/f8/42/91c9c3fee57d0cc662b00a2b69ab7d0fcdc341207e4de5f70dba864e5968/flake8-3.8.0-py2.py3-none-any.whl")
    version("3.7.9", sha256="49356e766643ad15072a789a20915d3c91dc89fd313ccd71802303fd67e4deca", url="https://pypi.org/packages/f8/1f/7ea40d1e4146ea55dbab41cda1376db092a75794914169aabd7e8d7a7def/flake8-3.7.9-py2.py3-none-any.whl")
    version("3.7.8", sha256="8e9dfa3cecb2400b3738a42c54c3043e821682b9c840b0448c0503f781130696", url="https://pypi.org/packages/26/de/3f815a99d86eb10464ea7bd6059c0172c7ca97d4bdcfca41051b388a653b/flake8-3.7.8-py2.py3-none-any.whl")
    version("3.7.7", sha256="a796a115208f5c03b18f332f7c11729812c8c3ded6c46319c59b53efd3819da8", url="https://pypi.org/packages/e9/76/b915bd28976068a9843bf836b789794aa4a8eb13338b23581005cd9177c0/flake8-3.7.7-py2.py3-none-any.whl")
    version("3.7.6", sha256="6eab21c6e34df2c05416faa40d0c59963008fff29b6f0ccfe8fa28152ab3e383", url="https://pypi.org/packages/54/a7/adf0c095af5b6c33d560780404504e9d58d9a1999253834f2b2d141098d8/flake8-3.7.6-py2.py3-none-any.whl")
    version("3.7.5", sha256="c3ba1e130c813191db95c431a18cb4d20a468e98af7a77e2181b68574481ad36", url="https://pypi.org/packages/5a/d8/1377549a9b77ad6d3c8161c741e2186bc698150f639fe08123bfe53e7a27/flake8-3.7.5-py2.py3-none-any.whl")
    version("3.7.4", sha256="e0f8cd519cfc0072c0ee31add5def09d2b3ef6040b34dc426445c3af9b02163c", url="https://pypi.org/packages/bf/ee/e0c4e08b94f80df6e8a852f7bb6da6d6a7094248206d1657389a32e83fe3/flake8-3.7.4-py2.py3-none-any.whl")
    version("3.7.3", sha256="806ec5785af23b4d9f3224a47cdd73714528923fccc95cc13cb1b74ba19c1820", url="https://pypi.org/packages/62/ca/01eb596aa0752b76b02a77cab6272f7c132575e63f6f87a7dc9480683a28/flake8-3.7.3-py2.py3-none-any.whl")
    version("3.7.2", sha256="0323db2e3a72faa2c4cdd61ea87594b9cb343fc4dfa5c24d6b43059d7ba29d0e", url="https://pypi.org/packages/69/3b/59284a25e5f087347125d35596c6775c574b8933722f71e0cdfff92cecab/flake8-3.7.2-py2.py3-none-any.whl")
    version("3.7.1", sha256="545c8faa8425cafcd9800538b4fa324a543cdec0ac273cf698ddd6a954123401", url="https://pypi.org/packages/69/5f/abf3fb57fcb9e0dac0e5215dcb84c792cc353c7c5361fb613d4b81102873/flake8-3.7.1-py2.py3-none-any.whl")
    version("3.7.0", sha256="7eda8e5c29ac9e0d3c0fd44649298c29768efc79a9b872b41c8f05ca5f502c83", url="https://pypi.org/packages/c9/17/b05f0910ef5e3d275f56d4bfc6bf4048cba779635cc1e61d7c07404d04d5/flake8-3.7.0-py2.py3-none-any.whl")
    version("3.5.0", sha256="c7841163e2b576d435799169b78703ad6ac1bbb0f199994fc05f700b2a90ea37", url="https://pypi.org/packages/b9/dc/14e9d94c770b8c4ef584e906c7583e74864786a58d47de101f2767d50c0b/flake8-3.5.0-py2.py3-none-any.whl")
    version("3.0.4", sha256="603a3ae7c8030219fee084728ca02a8bbd3a51829cacf97b445172a46cb04662", url="https://pypi.org/packages/70/fd/93266c6af1a23ea4d8b9a557b1fa02e6bdb43702b817c9151da5a3af3aa7/flake8-3.0.4-py2.py3-none-any.whl")
    version("2.6.2", sha256="7ac3bbaac27174d95bc4734ed23a07de567ffbcf4fc7e316854b4f3015d4fd15", url="https://pypi.org/packages/70/a9/9b66f22d038de51e05f92d5e677fd89d8f9c980db0b8a130621baad052f5/flake8-2.6.2-py2.py3-none-any.whl")
    version("2.6.1", sha256="32722c10e925b6bf75543269f5a022169578e5489a399f578cd6b1509736934f", url="https://pypi.org/packages/46/14/457b85bea74649f6d086c494c42d5e8dc8780ac98822e8030a6f261e9c9b/flake8-2.6.1-py2.py3-none-any.whl")
    version("2.6.0", sha256="d37bae8d6c836ea9f29a670f870b1652ff08d9b52b371fe1b7a53eb95e335f29", url="https://pypi.org/packages/aa/68/9882a69953b1f87a2661611660a4766e0c15c211c48981b371ed2a995494/flake8-2.6.0-py2.py3-none-any.whl")
    version("2.5.4", sha256="fb5a67af4024622287a76abf6b7fe4fb3cfacf765a790976ce64f52c44c88e4a", url="https://pypi.org/packages/e1/16/fba9e558dd7215b9a54abfc65a7032c5239c983cbb4f9eac9abf0e8f399b/flake8-2.5.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@6:")
        depends_on("py-entrypoints@0.3", when="@3.7")
        depends_on("py-mccabe@0.7:", when="@5:")
        depends_on("py-mccabe@0.6", when="@3.3:4")
        depends_on("py-mccabe@0.5", when="@3:3.2")
        depends_on("py-mccabe@0.2.1:0.5", when="@2.6:2")
        depends_on("py-mccabe@0.2.1:0.4", when="@2.5.2:2.5")
        depends_on("py-pep8@1.5.7:1.5,1.7:", when="@2.4.1:2.5")
        depends_on("py-pycodestyle@2.11:", when="@6.1:")
        depends_on("py-pycodestyle@2.10", when="@6:6.0")
        depends_on("py-pycodestyle@2.9", when="@5")
        depends_on("py-pycodestyle@2.8", when="@4")
        depends_on("py-pycodestyle@2.7", when="@3.9:3")
        depends_on("py-pycodestyle@2.6", when="@3.8")
        depends_on("py-pycodestyle@2.5", when="@3.7")
        depends_on("py-pycodestyle@2.0.0:2.3", when="@3.3:3.3.0.0,3.4:3.5")
        depends_on("py-pycodestyle@2.0.0:2.0", when="@2.6:3.1.0")
        depends_on("py-pyflakes@3.2:", when="@7:")
        depends_on("py-pyflakes@3.1", when="@6.1:6")
        depends_on("py-pyflakes@3:3.0", when="@6:6.0")
        depends_on("py-pyflakes@2.5:2", when="@5")
        depends_on("py-pyflakes@2.4", when="@4")
        depends_on("py-pyflakes@2.3", when="@3.9:3")
        depends_on("py-pyflakes@2.2", when="@3.8")
        depends_on("py-pyflakes@2.1", when="@3.7")
        depends_on("py-pyflakes@1.5:1", when="@3.5")
        depends_on("py-pyflakes@0.8.1:1.1,1.2.3:1.2", when="@2.6:3.1.0")
        depends_on("py-pyflakes@0.8.1:1.0", when="@2.5")
    # END DEPENDENCIES

