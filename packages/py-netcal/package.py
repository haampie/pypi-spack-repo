##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetcal(PythonPackage):
    version("1.3.5", sha256="3c3ae5ea35786878c3a979ad5a0f7192d89e7c53d0b3ab76ed27e227dd18d6cd", url="https://pypi.org/packages/12/a6/fd7aa37d5d613216637976f4f121270bc1781d1ad4ac3bf981f34a45b1c0/netcal-1.3.5-py3-none-any.whl")
    version("1.3.4", sha256="9434b68d21e9a7339f23d6337f97c2fd1d9b24def54f2670f73e407905a010e4", url="https://pypi.org/packages/6a/65/00da9f31a799aca85a40958439d45262e370fae249292a828176d70728cb/netcal-1.3.4-py3-none-any.whl")
    version("1.3.3", sha256="e57dc17f37c5786d1f696ce0fae6cd9de8a6ed20e6b980797e2f0ed5182c91ce", url="https://pypi.org/packages/7a/fe/a768b2681d26eb89bbecbea4b937a59b0c54f88eaded3611623b8094ab1c/netcal-1.3.3-py3-none-any.whl")
    version("1.3.2", sha256="ea0164686df0460adca61697434d6d07186386bab1f811c64638ffcc59534efa", url="https://pypi.org/packages/14/d0/9c9bab45096064895d8872f4bf8a52a795567ecb26891428f23d370d62b8/netcal-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="bdbb1603d5bcb1d73538f3b4a1d3428480f4dac1c329a26dbc4d9116118938c0", url="https://pypi.org/packages/c2/1e/4f4cf66aee3806112a317d69fc501ee3997c42ec0be6ff8245c8a0bb27fd/netcal-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="fb6a9ebed683fe7d12ef5cf0e41f909ac01f9eda71aaea26b6ccb55e86399906", url="https://pypi.org/packages/1e/10/dc067eb049fe3d0488ce5dc1b2bb7f979aaa58f84a8eaf393ebc700e5e9a/netcal-1.3.0-py3-none-any.whl")
    version("1.2.1", sha256="bcf1d5fc93f4688be1bf4abc360dcaba239ef49e24095b9718574fcbb1714849", url="https://pypi.org/packages/13/9b/31ba043ba2035b2007a8f1deaeb7e77a6b4a425adc694df1f0e0f1cff6ae/netcal-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="dcfde0dc34bcb6a06a17cfe59abcbe05c13278c21bdf651b837d45db4807173d", url="https://pypi.org/packages/41/b3/49110ef149a8b71d871eba86a0e78e8f6ea5c32157d066dacdc91b76c5e9/netcal-1.2.0-py3-none-any.whl")
    version("1.1.3", sha256="fbf930f489d6175ccc58061400ae26c0cabad2a0258e77ed5e3ea7c2a61ecf42", url="https://pypi.org/packages/d0/15/afddb1da638254dec469e7564a920ef311da5012b67522e8cbf837f9f1b9/netcal-1.1.3-py3-none-any.whl")
    version("1.1.2", sha256="e24637782f0ace5022212224deb3b675f83da7a6729b1f24965e6afd39192d31", url="https://pypi.org/packages/a8/a0/03ea56958564127b5b0bdf7b4cbaa1d3291c2a6ddb37735517f4906d202b/netcal-1.1.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-gpytorch@1.5.1:", when="@1.3:")
        depends_on("py-matplotlib@3.3.0:", when="@1.3:")
        depends_on("py-matplotlib@3.1.0:", when="@:1.2")
        depends_on("py-numpy@1.18.0:", when="@1.3:")
        depends_on("py-numpy@1.17.0:", when="@1.1.3:1.2")
        depends_on("py-numpy@1.15.0:", when="@:1.1.2")
        depends_on("py-pyro-ppl@1.8:", when="@1.3:")
        depends_on("py-pyro-ppl@1.3:", when="@1.2")
        depends_on("py-scikit-learn@0.24.0:", when="@1.3:")
        depends_on("py-scikit-learn@0.21.0:", when="@1.2")
        depends_on("py-scikit-learn@0.20.0:", when="@:1.1")
        depends_on("py-scipy@1.4.0:", when="@1.3:")
        depends_on("py-scipy@1.3.0:", when="@1.1:1.2")
        depends_on("py-tensorboard@2.2:", when="@1.2:")
        depends_on("py-tikzplotlib@0.9.8", when="@1.3:")
        depends_on("py-tikzplotlib@0.9.8:", when="@1.2")
        depends_on("py-torch@1.9:", when="@1.3:")
        depends_on("py-torch@1.4:", when="@1.2")
        depends_on("py-torch@1.1:", when="@1.1")
        depends_on("py-torchvision@0.10:", when="@1.3:")
        depends_on("py-torchvision@0.5:", when="@1.2")
        depends_on("py-tqdm@4.40:", when="@1.2:")
        depends_on("py-tqdm", when="@1.1")

