##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWasabi(PythonPackage):
    version("1.1.2", sha256="0a3f933c4bf0ed3f93071132c1b87549733256d6c8de6473c5f7ed2e171b5cf9", url="https://pypi.org/packages/8f/69/26cbf0bad11703241cb84d5324d868097f7a8faf2f1888354dac8883f3fc/wasabi-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="32e44649d99a64e08e40c1c96cddb69fad460bd0cc33802a53cab6714dfb73f8", url="https://pypi.org/packages/58/5f/1f2833d59abf53e24dbadc21b0565fe10c64545da8705faed8eff3b14745/wasabi-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="e4be528edf13d25656f676bf8a1b8a54d2b18c1c20bd2ca608b0405d10b290a3", url="https://pypi.org/packages/d4/6e/fdf8d3d4d4e5a08b2fa732f7835c5c0214880de2bf99e4f0584791ba44d6/wasabi-1.1.0-py3-none-any.whl")
    version("0.10.1", sha256="fe862cc24034fbc9f04717cd312ab884f71f51a8ecabebc3449b751c2a649d83", url="https://pypi.org/packages/34/74/bd566f876c2de097e75d525c2696fb9829009987a0d93a4fb3576778a0a8/wasabi-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="62d26d6f095779e08f05fbe598d0863c3c3119ea5c478e6b70b80667d84f423c", url="https://pypi.org/packages/d1/f2/1be789e54f5fc473368124d8abd0772263d1cf580ba7d71bc12c99d52e1c/wasabi-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="217edcb2850993c7931399e7419afccde13539d589e333bc85f9053cf0bb1772", url="https://pypi.org/packages/f6/77/736fa303d2efb5b640aad8abad323c23c83c184ce95c4df25e8a8e435d2e/wasabi-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="f40f317981d019903db5b69eb2bf78519c9e165c1dfdbd0452e4ca81ff9a31d2", url="https://pypi.org/packages/da/96/1f8e7a9d5cd48251b84991657ba3aeab9463a9e897ff105f70e103946348/wasabi-0.9.0-py3-none-any.whl")
    version("0.8.2", sha256="a493e09d86109ec6d9e70d040472f9facc44634d4ae6327182f94091ca73a490", url="https://pypi.org/packages/a6/1d/d281571b4c3b20fff183b485c6673c62878727119a849c7932651a8b5060/wasabi-0.8.2-py3-none-any.whl")
    version("0.8.1", sha256="62284f46cac06607508395aa75fb716eb61944f79b39bc894891e3c7351f3e09", url="https://pypi.org/packages/74/44/9e2823d9afe04e36c71dd62f24912dd5fb31bf81b7d7b6ab059575b45087/wasabi-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="98bc9c492c6aa8628303a02961a5cfa7b0c7fa6d2b397abdeb0adc4b39397c49", url="https://pypi.org/packages/1b/10/55f3cf6b52cc89107b3e1b88fcf39719392b377a3d78ca61da85934d0d10/wasabi-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="ee3809f4ce00e1e7f424b1572c753cff0dcaca2ca684e67e31f985033a9f070b", url="https://pypi.org/packages/4e/d1/a23917773a5759b36d1dc8433d15fb40700ca29d5ba924d6350c38a8ef8e/wasabi-0.7.1.tar.gz")
    version("0.7.0", sha256="e875f11d7126a2796999ff7f092195f24005edbd90b32b2df16dde5d392ecc8c", url="https://pypi.org/packages/04/e5/aa1892776a8ed6f6d552ba1be0640e6403f07e850d36e79f475f1e605aa9/wasabi-0.7.0.tar.gz")
    version("0.6.0", sha256="da1f100e0025fe1e50fd67fa5b0b05df902187d5c65c86dc110974ab856d1f05", url="https://pypi.org/packages/21/e1/e4e7b754e6be3a79c400eb766fb34924a6d278c43bb828f94233e0124a21/wasabi-0.6.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-colorama@0.4.6:", when="@1: platform=windows")

