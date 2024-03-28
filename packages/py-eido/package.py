# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEido(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2", sha256="01af095ec4c3ea081a917dbcd3be1308f0043e167a4b6dc15a75c99b85159293", url="https://pypi.org/packages/83/2f/a4c453d8151bbd1a0b3e6e005f784013da415c16a0655ed649d2613069f6/eido-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="e177ace8f524220a4757d1c015ed182e08679702504505be2baa3eee2f68d937", url="https://pypi.org/packages/d2/8f/07e4eb3c0f45b0aab600b24ca5f6f02e3501bc447fa2b8a3b64374dba616/eido-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="2c939686470ccc7e6933424f3975e920301667b90775de12e14deca67d849fca", url="https://pypi.org/packages/58/50/8a45f95b8a789781574553357d0dd64facdb4d06d70dbcf61dee35caa279/eido-0.2.0-py3-none-any.whl")
    version("0.1.9", sha256="a40e3c83c7d4370f6604feaf867f2daa2b36997ad01052b3589db7f73f743e26", url="https://pypi.org/packages/d7/94/89d9384b4328def500175ca19478073ecefa9e1d463d5c6db72ff797d945/eido-0.1.9-py3-none-any.whl")
    version("0.1.8", sha256="4b4676762f73d7668af03e70e93dd0807d005d822eae664730a9b6669e39870c", url="https://pypi.org/packages/06/6b/b43f60d38c7a65ddfded8181513a40f3568da955fa181ec0fdac94a13dfb/eido-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="2cc94078d3bfc36a7b8bac4a84c87fd2b180101e3f7a97fd235530d607a50409", url="https://pypi.org/packages/2c/e7/d64bcc7856577b11b3a3c1ede7305210d2272730eb0d176e637836aa13ef/eido-0.1.7-py3-none-any.whl")
    version("0.1.6", sha256="fffbde8116992e23999696b7ae2f2824fcabf3e982f7699f349aac737cd1650a", url="https://pypi.org/packages/f4/4b/6fcdc7fe2d61a5216ec6414ac64e3c0a38e7ad696cec7bf24f58868cd234/eido-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="fbe48eba95ccc1795dc8b1c025bf1c16498b63fcf43f5821d58dcc1528aafb3d", url="https://pypi.org/packages/d6/d7/503873565d84f9cbe7dea89f259a331aeb17cf70acf9419ed3cbc8d8b195/eido-0.1.5-py3-none-any.whl")
    version("0.1.4", sha256="f8d283943e5aacf764d50353a280446426ea6600c07ee655d2702caca2b6736e", url="https://pypi.org/packages/6c/24/71022e299cb51be9431ef0011da8c987cfd2556d73e2cd80c1db97aa29c9/eido-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="0a369649d52f3e169f50706a5ab8f579258ce9d2cb458368263d00a52662a7c2", url="https://pypi.org/packages/62/b7/d96ce178fabb415f9053000b053b50722f726e96b73eb6d2ddc0afc06f6e/eido-0.1.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jsonschema@3.0.1:", when="@0.1.2:")
        depends_on("py-logmuse@0.2.5:", when="@0.1.2:")
        depends_on("py-pandas", when="@0.1.3:")
        depends_on("py-peppy@0.35.7:", when="@0.2.2:")
        depends_on("py-peppy@0.35.5:", when="@0.2:0.2.1")
        depends_on("py-peppy@0.32:", when="@0.1.6:0.1")
        depends_on("py-peppy@0.31.1:", when="@0.1.5")
        depends_on("py-peppy@0.31:", when="@0.1.3:0.1.4")
        depends_on("py-ubiquerg@0.5.2:", when="@0.1.2:")
        depends_on("py-yacman@0.6.7:", when="@0.1.2:0.1.4")
    # END DEPENDENCIES

