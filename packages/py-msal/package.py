# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMsal(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.28.0", sha256="3064f80221a21cd535ad8c3fafbb3a3582cd9c7e9af0bb789ae14f726a0ca99b", url="https://pypi.org/packages/40/41/646c00154efa437bf01b30444421285fb29ef624e86b2446e71eff50b7a9/msal-1.28.0-py3-none-any.whl")
    version("1.27.0", sha256="572d07149b83e7343a85a3bcef8e581167b4ac76befcbbb6eef0c0e19643cdc0", url="https://pypi.org/packages/c0/a3/46ebb1d55aa65c1983f0b96739c84957fbb5be3c55ce34ecbab69afd4242/msal-1.27.0-py2.py3-none-any.whl")
    version("1.27.0-beta2", sha256="44da52f87ac006a28af0768639811e55b4138bcfb11abab0882027ba99fc5832", url="https://pypi.org/packages/a2/86/8a080897128f483498cf72b6f7b09c17f1b1aa5f8fa845f08942039f3c5d/msal-1.27.0b2-py2.py3-none-any.whl")
    version("1.26.0", sha256="be77ba6a8f49c9ff598bbcdc5dfcf1c9842f3044300109af738e8c3e371065b5", url="https://pypi.org/packages/b7/61/2756b963e84db6946e4b93a8e288595106286fc11c7129fcb869267ead67/msal-1.26.0-py2.py3-none-any.whl")
    version("1.25.0", sha256="386df621becb506bc315a713ec3d4d5b5d6163116955c7dde23622f156b81af6", url="https://pypi.org/packages/2a/45/d80a35ce701c1b3b53ab57a585813636acba39f3a8ed87ac01e0f1dfa3c1/msal-1.25.0-py2.py3-none-any.whl")
    version("1.24.1", sha256="ce4320688f95c301ee74a4d0e9dbcfe029a63663a8cc61756f40d0d0d36574ad", url="https://pypi.org/packages/35/33/0fd933b627879a9855d02a83a57929b45d0bdbeb050ddd63109cc404fbf6/msal-1.24.1-py2.py3-none-any.whl")
    version("1.24.0", sha256="a7f2f342b80ba3fe168218003b6798cc81b83c9745284bf63fb8d4ec8e2dbc50", url="https://pypi.org/packages/8f/71/5c385d104814fede34da5e10102bc0f4a0d05ef42eae052dac787381b2bc/msal-1.24.0-py2.py3-none-any.whl")
    version("1.23.0", sha256="3342e0837a047007f9d479e814b559c3219767453d57920dc40a31986862048b", url="https://pypi.org/packages/6f/cd/c5d31dc262c139763dbee91ac91d12ced729a529e59877d150705e60832e/msal-1.23.0-py2.py3-none-any.whl")
    version("1.22.0", sha256="9120b7eafdf061c92f7b3d744e5f325fca35873445fa8ffebb40b1086a13dd58", url="https://pypi.org/packages/5a/0d/5e21072561e8cbf13f938da854804cde984475e9b3d125922962e46487b8/msal-1.22.0-py2.py3-none-any.whl")
    version("1.21.0", sha256="e8444617c1eccdff7bb73f5d4f94036002accea4a2c05f8f39c9efb5bd2b0c6a", url="https://pypi.org/packages/cc/86/9900755d4be6e36b48603f9056ffca341d42139297df6f7e143fa96e6ed7/msal-1.21.0-py2.py3-none-any.whl")
    version("1.20.0", sha256="d2f1c26368ecdc28c8657d457352faa0b81b1845a7b889d8676787721ba86792", url="https://pypi.org/packages/53/51/b0874200ae0b926d83e402a5689b81310f49743b78e6457dbab85d0b354f/msal-1.20.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="a620afb65c468b78ce26d7a724c7ebc5d350ffcb57e1d18dc722e5ca1244673b", url="https://pypi.org/packages/8a/0c/b88d529caf2fa8658cae9b616d27b4ecba203c15981c29c89ef9e57b71b4/msal-1.3.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="c944b833bf686dfbc973e9affdef94b77e616cb52ab397e76cde82e26b8a3373", url="https://pypi.org/packages/a9/7c/bc473b3fe76d466362e5b84b4b165b18a427604a9582a9bca61c1545d872/msal-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@0.6:", when="@1.23:")
        depends_on("py-cryptography@0.6:42", when="@1.22")
        depends_on("py-cryptography@0.6:40", when="@1.19,1.20.0:1.21")
        depends_on("py-pyjwt@1:+crypto", when="@1.9:")
        depends_on("py-pyjwt@1+crypto", when="@:1.8")
        depends_on("py-requests@2:")
    # END DEPENDENCIES

