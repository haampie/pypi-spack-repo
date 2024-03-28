# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTokenizeRt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.2.0", sha256="b79d41a65cfec71285433511b50271b05da3584a1da144a0752e9c621a285289", url="https://pypi.org/packages/8d/35/78f03aa48cfebd13646707f64477bc7eacf1081edcdcd1b4d57cb1b5d0a8/tokenize_rt-5.2.0-py2.py3-none-any.whl")
    version("5.1.0", sha256="9b7bb843e77dd6ed0be5564bfaaba200083911e0497841cd3e9235a6a9794d74", url="https://pypi.org/packages/33/60/8fe577a3d0c7697df3701ad46300d967791d29a0a5225d9f11e84759ba26/tokenize_rt-5.1.0-py2.py3-none-any.whl")
    version("5.0.0", sha256="c67772c662c6b3dc65edf66808577968fb10badfc2042e3027196bed4daf9e5a", url="https://pypi.org/packages/8d/12/4c7495f25b4c9131706f3aaffb185d4de32c02a6ee49d875e929c5b7c919/tokenize_rt-5.0.0-py2.py3-none-any.whl")
    version("4.2.1", sha256="08a27fa032a81cf45e8858d0ac706004fcd523e8463415ddf1442be38e204ea8", url="https://pypi.org/packages/2f/e2/654a25ad594df2eb07f76e405f6f261d8fa9b5c06eb1e78549a086245455/tokenize_rt-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="b479c08878a914c67fb5b3345754071c6aa3ca5a06d854d75672f04b8213aa63", url="https://pypi.org/packages/c6/46/4cfc6275a1bba037790800ec3fc1021cb05645e077d23795e66b8540b391/tokenize_rt-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="b37251fa28c21e8cce2e42f7769a35fba2dd2ecafb297208f9a9a8add3ca7793", url="https://pypi.org/packages/13/24/49368436ba6fad56f4b2677350ecc5e88127663e57f278c6fbb86ffe7135/tokenize_rt-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="c47d3bd00857c24edefccdd6dc99c19d4ceed77c5971a3e2fac007fb0c02e39d", url="https://pypi.org/packages/ff/74/181593e69eaa6ae3173221cf94421770a8911efb25af1467c5fe276b44f4/tokenize_rt-4.0.0-py2.py3-none-any.whl")
    version("3.2.0", sha256="53f5c22d36e5c6f8e3fdbc6cb4dd151d1b3d38cea1b85b5fef6268f153733899", url="https://pypi.org/packages/a9/50/1983329a9b82496326627bfb44d2f2604913311fe6d9aa426aa4261351ea/tokenize_rt-3.2.0-py2.py3-none-any.whl")
    version("3.1.0", sha256="862442a55cd21b24c62adbdf0ae7fa178f1fd289e532fe9f5ab902d227317b42", url="https://pypi.org/packages/87/88/edfba9ab2a34bc9ab557a7241e82aafec767d850852cce7a7f9425d8b47d/tokenize_rt-3.1.0-py2.py3-none-any.whl")
    version("3.0.1", sha256="c65559bd0574447e10348f0f18710e870f862e168d673157f9b5eb43fb1b7eff", url="https://pypi.org/packages/ec/77/e37131d747e1b6be9c2279f0fa6312397cdfe45cf9741b25d1a5087fd4bb/tokenize_rt-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="0ad773efe3325971ebb06231879166d63d0f64acbc224a78c91e3f5b5ec34c0a", url="https://pypi.org/packages/95/e6/3d487dc522a442f88e5730538a3b9a380d04a331c305251e44f9e5ddabd5/tokenize_rt-3.0.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="6b845036b52d430d395b02981fa4adaeb279c6914b57d8019be0d7d0a98b8a03", url="https://pypi.org/packages/43/4b/c5df89ff5b38afffc04fb208c9b1fce30c1426788a368d7039b4cbcf524e/tokenize_rt-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="608b26913b74e00d16f5eee36ea2975423be1684ac5bdf68480ba04d488513d4", url="https://pypi.org/packages/76/82/0e6a9dda45dd76be22d74211443e199a330ac7e428b8dbbc5d116651be03/tokenize_rt-2.1.0-py2.py3-none-any.whl")
    version("2.0.1", sha256="2310f462de4f57c0d4d2ee0b4e5c589f06a7ef25cdfc73e6531f815ba099b065", url="https://pypi.org/packages/04/59/092aa671d0e19a7b14419e12c518288c563d4532ce7d42da5b3a1dffc49e/tokenize_rt-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="0d26a18e00fde31bb3c85ac3f3f3b5e9d3276853222bb8c8dcd210f7b3de5601", url="https://pypi.org/packages/30/d9/a02454b29e8cc7f39bff2620cbe8e1ecce377886e8956c7994a7a09e358e/tokenize_rt-2.0.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="d4ee182772f863c2279ba335bd1e00b048ed2405a4c374ef62df036b9dfdb847", url="https://pypi.org/packages/87/11/419e1935bc0cd7bd4287d5c21269f8108d80435779eadaa5c15a1f1e3f75/tokenize_rt-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

