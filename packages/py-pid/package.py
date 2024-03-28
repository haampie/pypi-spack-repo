# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPid(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.3", sha256="16a57105bd9a270d7f686899abe5f36a558489ee2e85f512a227b92f31ec69f2", url="https://pypi.org/packages/2f/1f/8004ef8a56dfb97fa21ba9d017a00ea3999d99a19a463d0a006f97fac3c2/pid-3.0.3-py2.py3-none-any.whl")
    version("3.0.2", sha256="717fec62e7bf2221502ddf81b8760c39fb4049c389057a722faa5500eabcff9b", url="https://pypi.org/packages/05/57/538b6f6e5fa141f0680b7ba78fc7e68706bc041b7330e6e3e05345fac1ec/pid-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="c68936d54f38f6c45edcbc83c877cb08973cf972d6ac42a9479b0a82d9fd59c8", url="https://pypi.org/packages/f8/9a/0928469f5ec2bef9f034751484c8deacc0dc3979ed885444d427bb9145a7/pid-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="4737d23a054f0ff2250668d7c23c438c5afdda003f63e3c875937e012effa9d6", url="https://pypi.org/packages/af/fd/943f2e011d3a71e4937063ac29981e97a6a5bf7c3998bc4731e16ba991fc/pid-3.0.0-py2.py3-none-any.whl")
    version("2.2.5", sha256="fe1ac2fd0617b091e7afd7b90f7af65ffb2339b57586215500e965462bb3cf0b", url="https://pypi.org/packages/82/bc/3633e94577c0f64864684be5a73251f194fd8673fb7c1f095597ef34dbc2/pid-2.2.5-py2.py3-none-any.whl")
    version("2.2.4", sha256="db621fbab1faf5f68bdecc2a8cad0a56a2f0362c05fe416c861c27db837def96", url="https://pypi.org/packages/6b/d3/c6b5d1f1565e226a89779f1ffeeb55351059702f327fd0a301c3bb4e731a/pid-2.2.4-py2.py3-none-any.whl")
    version("2.2.3", sha256="077da788630394adce075c88f4a087bcdb27d98cab67eb9046ebcfeedfc1194d", url="https://pypi.org/packages/b4/e7/333cec100e4f6a52c3f3ff730d1adc50dd2aae32398ef38aaa38de9548ec/pid-2.2.3.tar.gz")
    version("2.2.2", sha256="daa52ff1aa4f3e21cee0df5d8862be5db96dde6e5abf7613964a626a78eca5f8", url="https://pypi.org/packages/d7/33/e80d9a457668fa7daedd6538b487e175719085771325c7544fff2f2badd7/pid-2.2.2.tar.gz")
    version("2.2.1", sha256="636cb4743a6e6fb1d89efcfd772e6deb5a058590f3531703595d776507098d7b", url="https://pypi.org/packages/6e/da/8bc87f0171d45b98a15acb2324cd3e61e37938d717c0506f873ac3e69b1b/pid-2.2.1.tar.gz")
    version("2.2.0", sha256="b71dd3ce0bd56eb5021a84a2feddaa180328869ead002d980a26f815767baf50", url="https://pypi.org/packages/80/fb/8f4e402e940493c11c3cc808a5b53abaaefc8643b69d74013f41a7fd6f7d/pid-2.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-psutil@5.4.8:", when="@3: platform=windows")
    # END DEPENDENCIES

