##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFsspec(PythonPackage):
    version("2024.3.1", sha256="918d18d41bf73f0e2b261824baeb1b124bcf771767e3a26425cd7dec3332f512", url="https://pypi.org/packages/93/6d/66d48b03460768f523da62a57a7e14e5e95fdf339d79e996ce3cecda2cdb/fsspec-2024.3.1-py3-none-any.whl")
    version("2024.3.0", sha256="779001bd0122c9c4975cf03827d5e86c3afb914a3ae27040f15d341ab506a693", url="https://pypi.org/packages/60/be/ba7cf9660a7f566fe6b63eab725e962d23ffc340324ba1eb837833e4b90a/fsspec-2024.3.0-py3-none-any.whl")
    version("2024.2.0", sha256="817f969556fa5916bc682e02ca2045f96ff7f586d45110fcb76022063ad2c7d8", url="https://pypi.org/packages/ad/30/2281c062222dc39328843bd1ddd30ff3005ef8e30b2fd09c4d2792766061/fsspec-2024.2.0-py3-none-any.whl")
    version("2023.12.2", sha256="d800d87f72189a745fa3d6b033b9dc4a34ad069f60ca60b943a63599f5501960", url="https://pypi.org/packages/70/25/fab23259a52ece5670dcb8452e1af34b89e6135ecc17cd4b54b4b479eac6/fsspec-2023.12.2-py3-none-any.whl")
    version("2023.12.1", sha256="6271f1d3075a378bfe432f6f42bf7e1d2a6ba74f78dd9b512385474c579146a0", url="https://pypi.org/packages/96/0e/2be9b5a2e3f736577e749bbdf27a1e7e965041e1c908d49dedf56eeb2b8a/fsspec-2023.12.1-py3-none-any.whl")
    version("2023.12.0", sha256="f807252ee2018f2223760315beb87a2166c2b9532786eeca9e6548dfcf2cfac9", url="https://pypi.org/packages/67/32/9276db0647d8142da3d9ec1af536522081813005a9d7aaebbdba082967c1/fsspec-2023.12.0-py3-none-any.whl")
    version("2023.10.0", sha256="346a8f024efeb749d2a5fca7ba8854474b1ff9af7c3faaf636a4548781136529", url="https://pypi.org/packages/e8/f6/3eccfb530aac90ad1301c582da228e4763f19e719ac8200752a4841b0b2d/fsspec-2023.10.0-py3-none-any.whl")
    version("2023.9.2", sha256="603dbc52c75b84da501b9b2ec8c11e1f61c25984c4a0dda1f129ef391fbfc9b4", url="https://pypi.org/packages/fe/d3/e1aa96437d944fbb9cc95d0316e25583886e9cd9e6adc07baad943524eda/fsspec-2023.9.2-py3-none-any.whl")
    version("2023.9.1", sha256="99a974063b6cced36cfaa61aa8efb05439c6fea2dafe65930e7ab46f9d2f8930", url="https://pypi.org/packages/6a/af/c673e8c663e17bd4fb201a6f029153ad5d7023aa4442d81c7987743db379/fsspec-2023.9.1-py3-none-any.whl")
    version("2023.9.0", sha256="d55b9ab2a4c1f2b759888ae9f93e40c2aa72c0808132e87e282b549f9e6c4254", url="https://pypi.org/packages/3a/9f/b40e8e5be886143379000af5fc0c675352d59e82fd869d24bf784161dc77/fsspec-2023.9.0-py3-none-any.whl")
    version("2023.6.0", sha256="1cbad1faef3e391fba6dc005ae9b5bdcbf43005c9167ce78c915549c352c869a", url="https://pypi.org/packages/e3/bd/4c0a4619494188a9db5d77e2100ab7d544a42e76b2447869d8e124e981d8/fsspec-2023.6.0-py3-none-any.whl")
    version("2023.5.0", sha256="51a4ad01a5bb66fcc58036e288c0d53d3975a0df2a5dc59a93b59bade0391f2a", url="https://pypi.org/packages/ec/4e/397b234a369df06ec782666fcdf9791d125ca6de48729814b381af8c6c03/fsspec-2023.5.0-py3-none-any.whl")
    version("2023.4.0", sha256="f398de9b49b14e9d84d2c2d11b7b67121bc072fe97b930c4e5668ac3917d8307", url="https://pypi.org/packages/d6/30/db3078afe553e9a07c87534cbfb87a8c8ebb083fa0a8847ca5bdc86b51a7/fsspec-2023.4.0-py3-none-any.whl")
    version("2023.3.0", sha256="bf57215e19dbfa4fe7edae53040cc1deef825e3b1605cca9a8d2c2fadd2328a0", url="https://pypi.org/packages/4f/65/887925f1549fcb6ac3abb23a747c10f5ab083e8471fe568768b18bdb15b2/fsspec-2023.3.0-py3-none-any.whl")
    version("2023.1.0", sha256="b833e2e541e9e8cde0ab549414187871243177feb3d344f9d27b25a93f5d8139", url="https://pypi.org/packages/bd/64/f0d369ede0ca54fdd520bdee5086dbaf0af81dac53a2ce847bd1ec6e0bf1/fsspec-2023.1.0-py3-none-any.whl")
    version("2022.11.0", sha256="d6e462003e3dcdcb8c7aa84c73a228f8227e72453cd22570e2363e8844edfe7b", url="https://pypi.org/packages/37/57/eb7c3c10b187d3b8565946772ce0229c79e3c623010eda0aeb5032ff56f4/fsspec-2022.11.0-py3-none-any.whl")
    version("2022.1.0", sha256="256e2be44e62430c9ca8dac2e480384b00a3c52aef4e2b0b7204163fdc861d37", url="https://pypi.org/packages/f6/90/32e53b96067954c2f916667f5a11634aeabef8ed70e83133ed8037b8111b/fsspec-2022.1.0-py3-none-any.whl")
    version("2021.7.0", sha256="86822ccf367da99957f49db64f7d5fd3d8d21444fac4dfdc8ebc38ee93d478c6", url="https://pypi.org/packages/40/e1/7111d8afc76ee3171f4f99592cd29bac9d233ae1aa34623011506f955434/fsspec-2021.7.0-py3-none-any.whl")
    version("2021.4.0", sha256="70dae1d8d51072c4a1196acb9ba1bf8f5b9cdd83c4bb67e8a31dac604a49594b", url="https://pypi.org/packages/e9/91/2ef649137816850fa4f4c97c6f2eabb1a79bf0aa2c8ed198e387e373455e/fsspec-2021.4.0-py3-none-any.whl")
    version("0.9.0", sha256="7e98ea66f3f0156601e126fb2799e5d0ed87c3108b519f64c834b4284509fc82", url="https://pypi.org/packages/62/11/f7689b996f85e45f718745c899f6747ee5edb4878cadac0a41ab146828fa/fsspec-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="ce109f41ffe62853d5de84888f3e455c39f2a0796c05b558474c77156e19b570", url="https://pypi.org/packages/d3/66/974e01194980d9780cc09724315111f9cccba26b4351552fdb4d97eb842e/fsspec-0.8.0-py3-none-any.whl")
    version("0.7.3", sha256="9f0e3f4915b463b94c5788afa37b89d2c29c696f0d4da7d05f9cb5b17c8c84f7", url="https://pypi.org/packages/e9/fa/51b4b5630d6c8ce08aac7370989949d534052fb0e80a749fe8980b1d86d9/fsspec-0.7.3-py3-none-any.whl")
    version("0.4.4", sha256="97697a46e8bf8be34461c2520d6fc4bfca0ed749b22bb2b7c21939fd450a7d63", url="https://pypi.org/packages/44/99/39445aabe009d2327a369e74dea98178a5d757023e214ee478fdbec5844d/fsspec-0.4.4.tar.gz")

    variant("http", default=False)

    with default_args(type="run"):
        depends_on("py-aiohttp@:3", when="@2022.8:+http")
        depends_on("py-aiohttp", when="@0.8.1:2022.7+http")
        depends_on("py-requests", when="@0.8.1:2023+http")

