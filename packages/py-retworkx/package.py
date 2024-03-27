##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRetworkx(PythonPackage):
    version("0.14.2", sha256="9c36ac96f3c0b44b2793dc701d03914031badddf8649eae4ccef73f06457908b", url="https://pypi.org/packages/0c/e9/763c9fb623315ba50b4c3fc2cef987b158eb30669c1bc1d767d822f3287a/retworkx-0.14.2-py3-none-any.whl")
    version("0.14.1", sha256="ab725fd6fba1e089e5579e74adc07c7d28084fa599cfb0f5665de588a69ff49a", url="https://pypi.org/packages/11/14/bb0c282ff25e1f5ba7ede3fd2b67cb6ae3500f90c626ccce4f45314c6d96/retworkx-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="7e3721d99547cae81eae3b240c1dd251e63073dd85444a29bb7477b55f9a726d", url="https://pypi.org/packages/c3/05/3d6daf85db4d8bd81935baaabd74cdfcdaab04ac1e33fcd3e1d57315d56f/retworkx-0.14.0-py3-none-any.whl")
    version("0.13.2", sha256="693336a1f1f04c5017258ddff78f018e06cfd55b8e16b1e2d8dd98fe1e752e18", url="https://pypi.org/packages/01/65/3f52d88a2218a8fa85c0a79184038ba27baef9fa2d4454169536f2f3c249/retworkx-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="ab610c29ff1c784d8493ac3d2292809336453c39d7b7e7eed76b5d35c3279074", url="https://pypi.org/packages/96/e4/3fbaf64d7a891cff6bf0761546fedb0551b2a0efe132459984f85fcc4fa0/retworkx-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="cefe0565e9fff27cc995c8cbd0258e648be1395e863c333f1a9ea2b2174071aa", url="https://pypi.org/packages/33/17/1eadbba5e138960d42b6c97a55d2c3a2b98e73392af7eddb331f1cf3f50c/retworkx-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="b8f9b9953fcb1569154dc06383b213e5e2e2fd18ad5e5aa932341106101d1010", url="https://pypi.org/packages/cb/70/213c1626c9b4ab39dac71250fadb953eef839b6f2948c381a7838bbfe25b/retworkx-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="2914e02b7a3c56a9095c01c605beb8e66c932fd24521f6c92758ab634781ad47", url="https://pypi.org/packages/78/71/2335ce2739fb92545e2fa26602835f55f1ab419a88f828e1c3ee55620bf5/retworkx-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="a4c2a5ad3f8402493d41ad20ad91a03777ea214a3636c290272bbfaf36161161", url="https://pypi.org/packages/39/ca/e370819a445d152661464d87e77de9e9045cc626fb41726717aeeed81a93/retworkx-0.11.0.tar.gz")
    version("0.10.2", sha256="ba81cb527de7ff338575905bb6fcbebdf2ab18ae800169a77ab863f855bf0951", url="https://pypi.org/packages/1e/23/f51ae67c2902d910091d8dd6dc8b32af48d609e96ef7d552c77eac3c9881/retworkx-0.10.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.16.0:1", when="@0.14:")
        depends_on("py-numpy@1.16.0:", when="@0.12:0.13")
        depends_on("py-rustworkx@0.14.2:", when="@0.14.2:")
        depends_on("py-rustworkx@0.14.1", when="@0.14.1")
        depends_on("py-rustworkx@0.14:0.14.0", when="@0.14:0.14.0")
        depends_on("py-rustworkx@0.13.2:0.13", when="@0.13.2:0.13")
        depends_on("py-rustworkx@0.13.1", when="@0.13.1")
        depends_on("py-rustworkx@0.13:0.13.0", when="@0.13:0.13.0")
        depends_on("py-rustworkx@0.12.1:0.12", when="@0.12.1:0.12")
        depends_on("py-rustworkx@:0.12.0", when="@0.12:0.12.0")

