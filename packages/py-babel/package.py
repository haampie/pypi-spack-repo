##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBabel(PythonPackage):
    version("2.14.0", sha256="efb1a25b7118e67ce3a259bed20545c29cb68be8ad2c784c83689981b7a57287", url="https://pypi.org/packages/0d/35/4196b21041e29a42dc4f05866d0c94fa26c9da88ce12c38c2265e42c82fb/Babel-2.14.0-py3-none-any.whl")
    version("2.13.1", sha256="7077a4984b02b6727ac10f1f7294484f737443d7e2e66c5e4380e41a3ae0b4ed", url="https://pypi.org/packages/86/14/5dc2eb02b7cc87b2f95930310a2cc5229198414919a116b564832c747bc1/Babel-2.13.1-py3-none-any.whl")
    version("2.13.0", sha256="fbfcae1575ff78e26c7449136f1abbefc3c13ce542eeb13d43d50d8b047216ec", url="https://pypi.org/packages/ff/37/b0241795c3a320a3def948cd0d06daf70310e7fea1d8fda312629bc22ea9/Babel-2.13.0-py3-none-any.whl")
    version("2.12.1", sha256="b4246fb7677d3b98f501a39d43396d3cafdc8eadb045f4a31be01863f655c610", url="https://pypi.org/packages/df/c4/1088865e0246d7ecf56d819a233ab2b72f7d6ab043965ef327d0731b5434/Babel-2.12.1-py3-none-any.whl")
    version("2.12.0", sha256="8f8b752c803e9f9e03ff219b644aceb0dbcf081c55a88ea11f86291e60a7bb68", url="https://pypi.org/packages/28/d8/74b2d68dea0eb112af778093a25f0e87f0a549deced0293cb782837cb99e/Babel-2.12.0-py3-none-any.whl")
    version("2.11.0", sha256="1ad3eca1c885218f6dce2ab67291178944f810a10a9b5f3cb8382a5a232b64fe", url="https://pypi.org/packages/92/f7/86301a69926e11cd52f73396d169554d09b20b1723a040c2dcc1559ef588/Babel-2.11.0-py3-none-any.whl")
    version("2.10.3", sha256="ff56f4892c1c4bf0d814575ea23471c230d544203c7748e8c68f0089478d48eb", url="https://pypi.org/packages/2e/57/a4177e24f8ed700c037e1eca7620097fdfbb1c9b358601e40169adf6d364/Babel-2.10.3-py3-none-any.whl")
    version("2.10.2", sha256="81a3beca4d0cd40a9cfb9e2adb2cf39261c2f959b92e7a74750befe5d79afd7b", url="https://pypi.org/packages/a0/cf/def13a69e80ba635b476b7532f56e33b5c780744567d6ca92151a5b5386f/Babel-2.10.2-py3-none-any.whl")
    version("2.10.1", sha256="3f349e85ad3154559ac4930c3918247d319f21910d5ce4b25d439ed8693b98d2", url="https://pypi.org/packages/c5/7b/2c9fc1e18cb97676c7bedaa872447eb720e0c6e0e48190b4fba7eccdc1a8/Babel-2.10.1-py3-none-any.whl")
    version("2.10.0", sha256="92c9313a278c2920e39c8ac6373eb397b540798830fa0fcb8968192f908e2eef", url="https://pypi.org/packages/de/2d/e47819e2e7160b91f79a09951f9578d214c7bc34c62c0ba9686ff05335fe/Babel-2.10.0-py2.py3-none-any.whl")
    version("2.9.1", sha256="ab49e12b91d937cd11f0b67cb259a57ab4ad2b59ac7a3b41d6c06c0ac5b0def9", url="https://pypi.org/packages/aa/96/4ba93c5f40459dc850d25f9ba93f869a623e77aaecc7a9344e19c01942cf/Babel-2.9.1-py2.py3-none-any.whl")
    version("2.7.0", sha256="af92e6106cb7c55286b25b38ad7695f8b4efb36a90ba483d7f7a6628c46158ab", url="https://pypi.org/packages/2c/60/f2af68eb046c5de5b1fe6dd4743bf42c074f7141fe7b2737d3061533b093/Babel-2.7.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="6778d85147d5d85345c14a26aada5e478ab04e39b078b0745ee6870c2b5cf669", url="https://pypi.org/packages/b8/ad/c6f60602d3ee3d92fbed87675b6fb6a6f9a38c223343ababdb44ba201f10/Babel-2.6.0-py2.py3-none-any.whl")
    version("2.4.0", sha256="e86ca5a3a6bb64b9bbb62b9dac37225ec0ab5dfaae3c2492ebd648266468042f", url="https://pypi.org/packages/5f/cf/17935db603f7044d188ce3e3a6545c4b4500dbaa8835d50da2934b738111/Babel-2.4.0-py2.py3-none-any.whl")
    version("2.3.4", sha256="3318ed2960240d61cbc6558858ee00c10eed77a6508c4d1ed8e6f7f48399c975", url="https://pypi.org/packages/b4/ec/acd307eac2e23f9cab1c8bdbe29b3b1d43215e31c32f8aa91b3a97925b5b/Babel-2.3.4-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pytz@2015.7:", when="@2.12: ^python@:3.8")
        depends_on("py-pytz@2015.7:", when="@2.7:2.11")
        depends_on("py-pytz", when="@2.1:2.6")
        depends_on("py-setuptools", when="@2.13.1:2.13 ^python@3.12:")

