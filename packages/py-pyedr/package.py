##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyedr(PythonPackage):
    version("0.8.0", sha256="3e61705d4460bae9fd1f4245a11bdd433ac7fc6084ebd0ab8b8f5b6bcfeb5ad0", url="https://pypi.org/packages/26/77/33237d2e9f19e32774704555f8efbd4c336d82b1bcf4dab712d5a8c2a9d5/pyedr-0.8.0-py3-none-any.whl")
    version("0.7.2", sha256="c5f024973f69ec32a3234eb4033b69044dbd3a73a9c96ed59f2b0f9962fb63ed", url="https://pypi.org/packages/35/63/02ea8cef64bdead4c65d6e80f1f92f82b6db7438d285fa30ee4484102485/pyedr-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="7914ec210abb17a72684b4a8f042c5cfcf19042d3afa3bce2b3f0a2c9d22affa", url="https://pypi.org/packages/64/76/5b1a485afba2cbaa5634a49eed716d12dcf92fcc548c2ea531f4bc2f4fc6/pyedr-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="2600fac964ad74b0892f172b6119f5d09625429e5fe9ed69b1b2b102b674d366", url="https://pypi.org/packages/6d/39/d13d6715c1606d46d3ed604c9c8253ebeba557aa9e96f6189d8b29ab202f/pyedr-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="6dbef7f1e890bfe1401fc1884db1f49669a2715406766469c8c7f51a99d99d71", url="https://pypi.org/packages/2a/09/fa49661051a93813512e593f8d9629c62ba2b53465b4e95b6af985b6095f/pyedr-0.6.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.8:")
        depends_on("py-mda-xdrlib", when="@0.7.2:")
        depends_on("py-numpy", when="@0.8:")
        depends_on("py-numpy@1.19.0:", when="@:0.7")
        depends_on("py-pbr", when="@:0.7")
        depends_on("py-tqdm", when="@0.7.1:")

