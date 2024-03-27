##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleAuthOauthlib(PythonPackage):
    version("1.2.0", sha256="297c1ce4cb13a99b5834c74a1fe03252e1e499716718b190f56bcb9c4abc4faf", url="https://pypi.org/packages/71/bf/9e125754d1adb3bc4bd206c4e5df756513b1d23675ac06caa471278d1f3f/google_auth_oauthlib-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="089c6e587d36f4803ac7e0720c045c6a8b1fd1790088b8424975b90d0ee61c12", url="https://pypi.org/packages/ce/33/a907b4b67245647746dde8d61e1643ef5d210c88e090d491efd89eff9f95/google_auth_oauthlib-1.1.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="95880ca704928c300f48194d1770cf5b1462835b6e49db61445a520f793fd5fb", url="https://pypi.org/packages/4a/07/8d9a8186e6768b55dfffeb57c719bc03770cf8a970a074616ae6f9e26a57/google_auth_oauthlib-1.0.0-py2.py3-none-any.whl")
    version("0.8.0", sha256="40cc612a13c3336d5433e94e2adb42a0c88f6feb6c55769e44500fc70043a576", url="https://pypi.org/packages/98/0e/bfc3d7de5d1788871d1be3e6862fe3e56d92b446909b7b032c373fc4ecab/google_auth_oauthlib-0.8.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="860e54c4b58b2664116c9cb44325bc0ec92bcd93e8211698ceea911b1b873b86", url="https://pypi.org/packages/c9/fd/8cf240372179c101bddd01f7cb9d25bb29e92baf21dec2c622a8940c519f/google_auth_oauthlib-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="53019edbde83e08ff0740eefc5bded7e26a289941d12e7ae1f0f5bacf2faa031", url="https://pypi.org/packages/08/1a/08edf0cbcf3b1f0772c7cb7346b80dabb3b27953bfee1a827f3a06a75725/google_auth_oauthlib-0.7.0-py2.py3-none-any.whl")
    version("0.6.0", sha256="69112d0890c075e6ab03950cd9b8e1b953d6e89ba51de5f393e939fb3bc68284", url="https://pypi.org/packages/4d/d1/79277a5c507df72cc22ee2c3949ae384c4af8110bc0b472f0c49fcdcba3b/google_auth_oauthlib-0.6.0-py2.py3-none-any.whl")
    version("0.5.3", sha256="9e8ff4ed2b21c174a2d6cc2172c698dbf0b1f686509774c663a83c495091fe09", url="https://pypi.org/packages/04/74/8a2664dc7b5494ebef67f876467d7a2336810affcd0b9f7cf325631314ac/google_auth_oauthlib-0.5.3-py2.py3-none-any.whl")
    version("0.5.2", sha256="6d6161d0ec0a62e2abf2207c6071c117ec5897b300823c4bb2d963ee86e20e4f", url="https://pypi.org/packages/f8/93/aa9e5c46c955758ec9f08779e78838f7e041cbef8338ac9e490465aa4947/google_auth_oauthlib-0.5.2-py2.py3-none-any.whl")
    version("0.5.1", sha256="24f67735513c4c7134dbde2f1dee5a1deb6acc8dfcb577d7bff30d213a28e7b0", url="https://pypi.org/packages/ee/43/2160e91ab8bd0182378656ca4ef977ba43aa5ac96ff6b09f3c193513d1e4/google_auth_oauthlib-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="8b7ff4d2fe81e3bd034306aa665444360b3c67195b9dea582dddc7dfb8d89d34", url="https://pypi.org/packages/77/62/be9811606c4163068e8e5076864356881d3456b5c192997dee4e9a23acd6/google_auth_oauthlib-0.5.0-py2.py3-none-any.whl")
    version("0.4.6", sha256="3f2a6e802eebbb6fb736a370fbf3b055edcb6b52878bf2f26330b5e041316c73", url="https://pypi.org/packages/b1/0e/0636cc1448a7abc444fb1b3a63655e294e0d2d49092dc3de05241be6d43c/google_auth_oauthlib-0.4.6-py2.py3-none-any.whl")
    version("0.4.5", sha256="b5a1ce7c617d247ccb2dfbba9d4bfc734b41096803d854a2c52592ae80150a67", url="https://pypi.org/packages/45/d9/df4019fc28b3aed8218e1bfca38158b90b70a3583c15f568ca669564dc24/google_auth_oauthlib-0.4.5-py2.py3-none-any.whl")
    version("0.4.4", sha256="0e92aacacfb94978de3b7972cf4b0f204c3cd206f74ddd0dc0b31e91164e6317", url="https://pypi.org/packages/9d/d3/7541e89f1fc456eef157224f597a8bba22589db6369a03eaba68c11f07a0/google_auth_oauthlib-0.4.4-py2.py3-none-any.whl")
    version("0.4.3", sha256="dabffbf594a6be2fd6d054060846d1201569252efb10dfb749b504a7591f8af0", url="https://pypi.org/packages/cb/f5/6e656a95ca0b432c5f090239962f618c3b45447037d21e1c049123521f53/google_auth_oauthlib-0.4.3-py2.py3-none-any.whl")
    version("0.4.2", sha256="d4d98c831ea21d574699978827490a41b94f05d565c617fe1b420e88f1fc8d8d", url="https://pypi.org/packages/81/67/e2c34bb0628984c7ce71cce6ba6964cb29c418873847fc285f826e032e6e/google_auth_oauthlib-0.4.2-py2.py3-none-any.whl")
    version("0.4.1", sha256="a92a0f6f41a0fb6138454fbc02674e64f89d82a244ea32f98471733c8ef0e0e1", url="https://pypi.org/packages/7b/b8/88def36e74bee9fce511c9519571f4e485e890093ab7442284f4ffaef60b/google_auth_oauthlib-0.4.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-auth@2.15:", when="@0.8:")
        depends_on("py-google-auth@2.14:", when="@0.7.1:0.7")
        depends_on("py-google-auth@2.13:", when="@0.7:0.7.0")
        depends_on("py-google-auth@1:", when="@0.4.3:0.6")
        depends_on("py-google-auth", when="@:0.4.2")
        depends_on("py-requests-oauthlib@0.7:")

