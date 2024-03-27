##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLatexcodec(PythonPackage):
    version("3.0.0", sha256="6f3477ad5e61a0a99bd31a6a370c34e88733a6bad9c921a3ffcfacada12f41a7", url="https://pypi.org/packages/b0/bf/ea8887e9f31a8f93ca306699d11909c6140151393a4216f0d9f85a004077/latexcodec-3.0.0-py3-none-any.whl")
    version("2.0.1", sha256="c277a193638dc7683c4c30f6684e3db728a06efb0dc9cf346db8bd0aa6c5d271", url="https://pypi.org/packages/0a/76/9552dfc6b74c2d6c3f199e927d41998dc1e561b7cbe4af7e7247388e17e8/latexcodec-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="05d9ba4b2340bc9e71487719ca31c48db3b6685524322590448b8b96bcc98af6", url="https://pypi.org/packages/8e/4f/6e7353dce0cfde419995117705035c4a0433a08aa7c49219ee589767766a/latexcodec-2.0.0-py2.py3-none-any.whl")
    version("1.0.7", sha256="c937f0de93e077079da33684aee877d3cf7d9388740d3f4ffaa073cd5cdfb328", url="https://pypi.org/packages/c1/3b/3098d07abf8eb39d6714466d5ff41cdee30356f35c3e796b760fbb55e2fd/latexcodec-1.0.7-py2.py3-none-any.whl")
    version("1.0.6", sha256="860eaa2cd8a2461d19c128361524248a42d456e6f1f58a17e2fd200bccd43a2b", url="https://pypi.org/packages/b3/49/50f2dfc56cb08c51acd10b928b8c940fca7e86504e5a1d500ca6ef25103d/latexcodec-1.0.6-py2.py3-none-any.whl")
    version("1.0.5", sha256="9607d9d260654eb607c54a8b8c991e4406008605c383ded4f4034522dc0bad7d", url="https://pypi.org/packages/b8/04/a0011d86eafe6a31bf2d0b235a0d3b48bec61db4c76830bc6ded296e6931/latexcodec-1.0.5.tar.gz")
    version("1.0.4", sha256="62bf8a3ee298f169a4d014dad5522bc1325b54dc98789a453fd338620387cb6c", url="https://pypi.org/packages/3e/a3/d86746a4fbafd8126a0e5c497179be8820a78a40321634dcef3994a73e80/latexcodec-1.0.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.4.1:", when="@1.0.6:2")

