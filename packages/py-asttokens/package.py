##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsttokens(PythonPackage):
    version("2.4.1", sha256="051ed49c3dcae8913ea7cd08e46a606dba30b79993209636c4875bc1d637bc24", url="https://pypi.org/packages/45/86/4736ac618d82a20d87d2f92ae19441ebc7ac9e7a581d7e58bbe79233b24a/asttokens-2.4.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="cf8fc9e61a86461aa9fb161a14a0841a03c405fa829ac6b202670b3495d2ce69", url="https://pypi.org/packages/4f/25/adda9979586d9606300415c89ad0e4c5b53d72b92d2747a3c634701a6a02/asttokens-2.4.0-py2.py3-none-any.whl")
    version("2.3.0", sha256="bef1a51bc256d349e9f94e7e40e44b705ed1162f55294220dd561d24583d9877", url="https://pypi.org/packages/bd/4a/84cb4c859de8cc90b36d16605d976b61749532644dc79593c3287e6b9e01/asttokens-2.3.0-py2.py3-none-any.whl")
    version("2.2.1", sha256="6b0ac9e93fb0335014d382b8fa9b3afa7df546984258005da0b9e7095b3deb1c", url="https://pypi.org/packages/f3/e1/64679d9d0759db5b182222c81ff322c2fe2c31e156a59afd6e9208c960e5/asttokens-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="c56caef774a929923696f09ceea0eadcb95c94b30e8ee4f9fc4f5867096caaeb", url="https://pypi.org/packages/c5/28/c6cf14c78126cb7ae65ee81ad28f74bff0fb7b9e0ea773d543ce73904718/asttokens-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="1b28ed85e254b724439afc783d4bee767f780b936c3fe8b3275332f42cf5f561", url="https://pypi.org/packages/23/f7/19e20888d0b1e44b40c2795894a05e7be1f631c09949f7e0b177df1ab7a2/asttokens-2.1.0-py2.py3-none-any.whl")
    version("2.0.8", sha256="e3305297c744ae53ffa032c45dc347286165e4ffce6875dc662b205db0623d86", url="https://pypi.org/packages/2d/1b/fdbdf82b86e07ca90985740ac160a1dd4ab09cb81071ec12d71c701e1138/asttokens-2.0.8-py2.py3-none-any.whl")
    version("2.0.7", sha256="f5589ef8518f73dd82c15e1c19f795d8a62c133485e557c04443d4a1a730cf9f", url="https://pypi.org/packages/ad/a8/1f7eed0f3f775937025dc3813fa5b8f1e00ddfacc6084bc48debb885ee7b/asttokens-2.0.7-py2.py3-none-any.whl")
    version("2.0.6", sha256="d74743b486968525b02d6f5497b106c051b7ee1d8eb554cdfc2adddef48bc717", url="https://pypi.org/packages/01/ea/12c8a917e6148cf14a178f5ee18fb9ed88da4a827924b89e986490f23f48/asttokens-2.0.6-py2.py3-none-any.whl")
    version("2.0.5", sha256="0844691e88552595a6f4a4281a9f7f79b8dd45ca4ccea82e5e05b4bbdb76705c", url="https://pypi.org/packages/16/d5/b0ad240c22bba2f4591693b0ca43aae94fbd77fb1e2b107d54fff1462b6f/asttokens-2.0.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six@1.12:", when="@2.3:")
        depends_on("py-six", when="@:2.2")

