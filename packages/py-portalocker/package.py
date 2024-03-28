# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPortalocker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.2", sha256="cfb86acc09b9aa7c3b43594e19be1345b9d16af3feb08bf92f23d4dce513a28e", url="https://pypi.org/packages/17/9e/87671efcca80ba6203811540ed1f9c0462c1609d2281d7b7f53cef05da3d/portalocker-2.8.2-py3-none-any.whl")
    version("2.8.1", sha256="d13c79617e5644356e1a01e791e41c4b50eb4eed957567b3e9403219decd9d39", url="https://pypi.org/packages/21/1f/20af121f4f878c5d66cd29f342180becec56c435f153a920749daeb7b0c8/portalocker-2.8.1-py3-none-any.whl")
    version("2.8.0", sha256="5ea10654e42178182c63c16f608774e2a8914dc0afbdcce9879d6ef6f6845fe2", url="https://pypi.org/packages/a8/a8/b6bcc90951971cf29f3bc66d892b70071000ebb9aafeb2409809094fe4e8/portalocker-2.8.0-py3-none-any.whl")
    version("2.7.0", sha256="769c394f934f3459fab9f0989c17aa8158334f1898b9bb8407432bdc3f44be6d", url="https://pypi.org/packages/db/1e/07ab791977f4c5a6f30c74a10c3e38360cf6dea228ceda89d83a97c0c6f6/portalocker-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="102ed1f2badd8dec9af3d732ef70e94b215b85ba45a8d7ff3c0003f19b442f4e", url="https://pypi.org/packages/2a/59/dab72d0b8859a410a83dcaffb84781ffc467651b79c827a435c8945add05/portalocker-2.6.0-py2.py3-none-any.whl")
    version("2.5.1", sha256="400bae275366e7b840d4baad0654c6ec5994e07c40c423d78e9e1340279b8352", url="https://pypi.org/packages/a9/0a/21422dc681e3e59ce5ec4051015de4c2074bd0e6759099c018471f3dc4e3/portalocker-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="931db460f729d6088fe7bec43a57a0d024ea927f963d9ab8d09caa7843a4239f", url="https://pypi.org/packages/e6/87/7f6218b2f9be1f123803689c6888cf904eab6c02418d8c8788c520456dbf/portalocker-2.5.0-py2.py3-none-any.whl")
    version("2.4.0", sha256="b092f48e1e30a234ab3dd1cfd44f2f235e8a41f4e310e463fc8d6798d1c3c235", url="https://pypi.org/packages/f1/4e/1030afbf2e64e676e968bbbc82014ce4ddf1cc1ed0b492585958768cf79a/portalocker-2.4.0-py2.py3-none-any.whl")
    version("2.3.2", sha256="d8c9f7c542e768dbef006a3e49875046ca170d2d41ca712080719110bd066cc4", url="https://pypi.org/packages/63/eb/f84872af6e9312ea2f345b218015a41191cfd37eeba4a4fd228f241c2a75/portalocker-2.3.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="4277c7ff2ba170b0e207f8e4b367fb5bb73653a765924543a4ca2c4896a6ab4d", url="https://pypi.org/packages/cf/37/7adb2876d7a423ab7119222f1ad5740ffc2c424b975eed23e71e5927ee61/portalocker-2.3.1-py2.py3-none-any.whl")
    version("1.7.1", sha256="34cb36c618d88bcd9079beb36dcdc1848a3e3d92ac4eac59055bdeafc39f9d4a", url="https://pypi.org/packages/3b/e7/ceef002a300a98a208232fab593183249b6964b306ee7dabb29908419cca/portalocker-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="874d6063c6ceb185fe4771da41b01872d2c56d292db746698f8ad7bf1833c905", url="https://pypi.org/packages/53/84/7b3146ec6378d28abc73ab484f09f47dfa008ad6f03f33d90a369f880e25/portalocker-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="094bd1e4b2bccdfcb586fe4ccf0f3229cb08f6ec66418bef541c69103265c3ed", url="https://pypi.org/packages/64/03/9abfb3374d67838daf24f1a388528714bec1debb1d13749f0abd7fb07cfb/portalocker-1.6.0-py2.py3-none-any.whl")
    version("1.5.2", sha256="6f57aabb25ba176462dc7c63b86c42ad6a9b5bd3d679a9d776d0536bfb803d54", url="https://pypi.org/packages/91/db/7bc703c0760df726839e0699b7f78a4d8217fdc9c7fcb1b51b39c5a22a4e/portalocker-1.5.2-py2.py3-none-any.whl")
    version("1.5.1", sha256="934a848531ecd03b78d780402ddbf57e518172c67f0b4b9fbe2ea253fdaf6c3f", url="https://pypi.org/packages/60/ec/836a494dbaa72541f691ec4e66f29fdc8db9bcc7f49e1c2d457ba13ced42/portalocker-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="40477dff70ba7e6ffa0b272da6e9cdd2ab8b9b54b90f71ea362bea69d2d6c09d", url="https://pypi.org/packages/c4/4a/940f5184098d054804605e73258d57707b1df087fc532111593e6110be13/portalocker-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="d98cdcdbd8c590ee4c93fb4149b2e76030ea6c36d6fdfec122e6656ebf90086f", url="https://pypi.org/packages/eb/48/bf5e330d7d6d57d92157480db9ccad84da86efd045205f7133a53b29aace/portalocker-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="e6b3fdca1f232504da1a79dbe6230dfce241bac77698bd713883527c53db09ad", url="https://pypi.org/packages/e4/b5/3766a38c77707232e0800b1f2e970002020b687d626f52386c255ae7c63a/portalocker-1.3.0-py2.py3-none-any.whl")
    version("1.2.1", sha256="95ec72fd36c230b92634dcffde65686e585a9a8569b9ba806dff41f56e255fbf", url="https://pypi.org/packages/57/41/05e79e5516db1cc0c967b3202388cde729f871c871b0a07bf24ff11adfcf/portalocker-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="d6dfb262b0167c1a603cb8ebdb53cac61eef81d8885074ee69c3bf73c9cb422d", url="https://pypi.org/packages/0a/22/6a54021b020dd085d6cc03bf2243bbb7cf8808ac23be2db716780e7935c1/portalocker-1.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pywin32@226:", when="@2.4: platform=windows")
    # END DEPENDENCIES

