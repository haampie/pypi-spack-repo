##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpyparallel(PythonPackage):
    version("8.7.0", sha256="7748d0ca42b5ac04374316846df4858bd8f495fff58536d91d988ed367eb1c3c", url="https://pypi.org/packages/32/97/29b4090f8dd4735be31ac7b30855b48661f74d67655d74cf58e3946bd68c/ipyparallel-8.7.0-py3-none-any.whl")
    version("8.6.1", sha256="39324d481759f74c9be4fb0deb025d446de6246f08fb81490443c9f55e2f056c", url="https://pypi.org/packages/93/7a/39cfad289aef9f7b32617e078f30b4cc7d7a04d2063e60b613c8d3c7fad3/ipyparallel-8.6.1-py3-none-any.whl")
    version("8.6.0", sha256="820bc1c035192b5a80e6d9e8d4daeb5023b07ab6e1795f3f2eb9b4e56d3ce4e1", url="https://pypi.org/packages/43/ac/66b3c14e4a69a1c9f013eaef655890d8f748f508b21d03a2c5d81893c497/ipyparallel-8.6.0-py3-none-any.whl")
    version("8.5.1", sha256="84b9a3567f40d5afcc67b6176944f51633b61cd0c92387d8b5fc0fbe584f0b07", url="https://pypi.org/packages/16/8e/82b620b794131b2688960fc88d760873ec1e3916666f066257047a738b42/ipyparallel-8.5.1-py3-none-any.whl")
    version("8.5.0", sha256="296ebefe8a3d60e2efc59670d3a62f1488c4094df60cde1101ffbd880cca5a99", url="https://pypi.org/packages/97/3a/154be475a96ca40c0fce2291279cec49e01e36c2ef544ebe68b61835a5c1/ipyparallel-8.5.0-py3-none-any.whl")
    version("8.4.1", sha256="ecce5fc3c2717cc94ed7593eaf95419fb528f7f70abff3c7038f70a33fea1e6b", url="https://pypi.org/packages/e2/80/7f01a9a4fd4c3e1d2addd7696335cc07c5b990a11c579f44b417cf316ca4/ipyparallel-8.4.1-py3-none-any.whl")
    version("8.4.0", sha256="0ab40787d2e2b6833332eb84c9fe12d32a94bbc1e12fbb5411af8f42b9996b96", url="https://pypi.org/packages/18/b6/7900afa3552518a527cb0b8d03a9a532b03aacef7de16bbc2b27dd3614d5/ipyparallel-8.4.0-py3-none-any.whl")
    version("8.3.0", sha256="7f9e1e390522fc2ec20a80c2d621f7b7b85de3dd8c602c7f09c7760590bf1a40", url="https://pypi.org/packages/89/56/5ea1ae2d0c805f58dca8f041d61886c367fe5f18f541adcd168b216214ae/ipyparallel-8.3.0-py3-none-any.whl")
    version("8.2.1", sha256="8509448670cdc3c3961e29a827c6bdacbee29ee9c9e8c50f70032c8714f731fb", url="https://pypi.org/packages/4c/7e/7683845c9cabfd062f4f94aa0257737cc1d70c054eaeecacb4157c7703d4/ipyparallel-8.2.1-py3-none-any.whl")
    version("8.2.0", sha256="1fdedc8b83e537e67789d76d9c14684f5dde0e559d31b3dc5584232c4e33c1ab", url="https://pypi.org/packages/58/70/63bff3c813941777529988b8b940c0de282e87f1acd863b5ecbe05669cb3/ipyparallel-8.2.0-py3-none-any.whl")
    version("8.0.0", sha256="3365f8020baa2a675b5c7e42b6fe1c03b20e95de7af3330fa5557265ac07451a", url="https://pypi.org/packages/62/e6/2aaddc081158cd6bedeed86047ed4609b38fcd0e44ddf0fe002bd8f9f7a6/ipyparallel-8.0.0-py3-none-any.whl")
    version("7.1.0", sha256="d72496c1e75e6d26636117b33d3770b66d46b99c2421412676656ca957933ee3", url="https://pypi.org/packages/8d/c5/39e862edc26bbaf6973575c20a243705788156d3b1a5657a16eb565ebe54/ipyparallel-7.1.0-py3-none-any.whl")
    version("6.3.0", sha256="61013af22cbcbefcaa9ba7b118a6ea1538491a82ef95b0adfd157924777c1df9", url="https://pypi.org/packages/3b/e9/03a9189eb39276396309faf28bf833b4328befe4513bbf375b811a36a076/ipyparallel-6.3.0-py3-none-any.whl")
    version("6.2.5", sha256="4d11a85c420bfc15bfba74190513227d52b38263a8b2855e0e0eacc6cea27c68", url="https://pypi.org/packages/d5/45/abc77804b90034c75f4798df90833d9b61df8928d2358559471fddbfd413/ipyparallel-6.2.5-py2.py3-none-any.whl")
    version("6.2.4", sha256="2acbffcbd6da955b47ec7befb320dcad1788cc146cfc7abfa6d1c74436d74d38", url="https://pypi.org/packages/3f/82/aaa7a357845a98d4028f27c799f0d3bb2fe55fc1247c73dc712b4ae2344c/ipyparallel-6.2.4-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-decorator", when="@:2,5:")
        depends_on("py-entrypoints", when="@:2,7.0.0-beta1:")
        depends_on("py-ipykernel@4.4:", when="@:2,6.2.3:")
        depends_on("py-ipython@4.0.0:", when="@:2,5:")
        depends_on("py-ipython-genutils", when="@5:7.0.0-beta2")
        depends_on("py-jupyter-client", when="@:2,5:")
        depends_on("py-psutil", when="@:2,7.0.0-alpha4:")
        depends_on("py-python-dateutil@2:", when="@:2,6:")
        depends_on("py-pyzmq@13:", when="@5:7.0.0-alpha1")
        depends_on("py-pyzmq@18:", when="@:2,7.0.0-alpha3:")
        depends_on("py-tornado@4:", when="@5:6")
        depends_on("py-tornado@5.1:", when="@:2,7:")
        depends_on("py-tqdm", when="@:2,7.0.0-alpha3:")
        depends_on("py-traitlets@4.3.0:", when="@:2,6.1:")

