# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUhi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="c7e82826314c66b8e7fee7869b75eb038f500b034f5371ef928def41c8db70bc", url="https://pypi.org/packages/2a/9a/d5de1ec139e24f0f8d9e1b9cfdf6b3ade0d0d204f99b20ff921472206b91/uhi-0.4.0-py3-none-any.whl")
    version("0.3.3", sha256="4805a4194550310ee2a58aa8c777e6ab80f8896c96469d7c16fd2436aef4c9c3", url="https://pypi.org/packages/70/e7/599c0589e0fcb3f330ea6cc13b3fde9d3f0a65fe939f9b5634c50dde6349/uhi-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="427d7d54f1ac072a52f3b476457732ecd3767da00b2a8b6fdc38dd6820db107e", url="https://pypi.org/packages/ad/36/fbc93bc03270b16fd80d7e870fb459289aaaa6b1077bc8cd12836b4b751f/uhi-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="5c2f7ceceacd349f906104a7776859812e0926936273667eadf56762133d6d5e", url="https://pypi.org/packages/67/03/b2731129bba0ed39f3dbb5e5cea557491efb82f34cf2d7a9fbaee2be4a83/uhi-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="20fe823e7e34f8f0a5a223ba3c22c164b43cb8fc2b2f9b4ed2e2cd6fceea583e", url="https://pypi.org/packages/94/af/227bc7260a770fafe939e9c663ae348f6869f2964e58b1065cf9c312046b/uhi-0.3.0-py3-none-any.whl")
    version("0.2.1", sha256="387f66cd0e89fdc3105fa15e96eddea16fe062dcd8b33b5c1e4971c966f9efe5", url="https://pypi.org/packages/9c/30/7046fd215607e8af7b3360553ecadd37543251557186d0a584b7d83f6bca/uhi-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="b8cd4ab4b6c0f926eee17ea00e029fd18d934bceabedaf5d6f57d1730b24253a", url="https://pypi.org/packages/02/76/d37cf82c0f5e18cb7049247ac36a713d6334250b423c500b573393268fd0/uhi-0.2.0-py3-none-any.whl")
    version("0.1.2", sha256="543997ad2194a75cc69219e1fbaf16b341e16da392ae6e837d6d85d2d5cde8f1", url="https://pypi.org/packages/a8/2f/375c06d8844f1b149df8901b6b3581faa2fce4660c84d19ae810be356534/uhi-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="c1be1ed6d7f4f0f64fffc42239a7415cca21bedd888aa4835be7d2daee27c957", url="https://pypi.org/packages/2d/cb/a129ef52cd7ae64ba85b16b99adcee8d1597c32c6331cfd1f599e13a0c6e/uhi-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="3aa19f2362fc8daf79edc0259adafcdd6784ec5a7f8ca703e8bf152bca9e1ce1", url="https://pypi.org/packages/12/47/119a5f7213950195842c62cba41308662705adef356061bc580e995405be/uhi-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.13.3:", when="@0.2:")
    # END DEPENDENCIES

