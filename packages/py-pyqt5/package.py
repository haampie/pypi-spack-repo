##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt5(PythonPackage):
    version("5.15.10", sha256="d46b7804b1b10a4ff91753f8113e5b5580d2b4462f3226288e2d84497334898a", url="https://pypi.org/packages/4d/5d/b8b6e26956ec113ad3f566e02abd12ac3a56b103fcc7e0735e27ee4a1df3/PyQt5-5.15.10.tar.gz")
    version("5.15.9", sha256="dc41e8401a90dc3e2b692b411bd5492ab559ae27a27424eed4bd3915564ec4c0", url="https://pypi.org/packages/5c/46/b4b6eae1e24d9432905ef1d4e7c28b6610e28252527cdc38f2a75997d8b5/PyQt5-5.15.9.tar.gz")
    version("5.15.8", sha256="bc85e3efb9135c56c8b88157c8825005fb7cd0f14babd93976778aae82eda360", url="https://pypi.org/packages/c1/c3/76c52be757e2e07e2f76dfda0e89546a14c1b97004cc7e126851764370b3/PyQt5-5.15.8.tar.gz")
    version("5.15.7", sha256="755121a52b3a08cb07275c10ebb96576d36e320e572591db16cfdbc558101594", url="https://pypi.org/packages/e1/57/2023316578646e1adab903caab714708422f83a57f97eb34a5d13510f4e1/PyQt5-5.15.7.tar.gz")
    version("5.15.6", sha256="80343bcab95ffba619f2ed2467fd828ffeb0a251ad7225be5fc06dcc333af452", url="https://pypi.org/packages/3b/27/fd81188a35f37be9b3b4c2db1654d9439d1418823916fe702ac3658c9c41/PyQt5-5.15.6.tar.gz")
    version("5.15.5", sha256="b411b7a8fa03901c9feb1dcbac7ea1fc3ce20b9ae682762b777cd5398749ca2b", url="https://pypi.org/packages/72/bf/4e7c66eefa9ede1ec01d065d220373667f4ca3285a83a6430eefc254904c/PyQt5-5.15.5.tar.gz")
    version("5.15.4", sha256="2a69597e0dd11caabe75fae133feca66387819fc9bc050f547e5551bce97e5be", url="https://pypi.org/packages/8e/a4/d5e4bf99dd50134c88b95e926d7b81aad2473b47fde5e3e4eac2c69a8942/PyQt5-5.15.4.tar.gz")
    version("5.15.3", sha256="965ba50e7029b37f218a54ace24e87c77db3e5a9f0b83baeb21fb57b4154b838", url="https://pypi.org/packages/6e/86/d715e71771cece0e060f2ebab20f3ded067b08a0927dfb3143530cae8098/PyQt5-5.15.3.tar.gz")
    version("5.15.2", sha256="372b08dc9321d1201e4690182697c5e7ffb2e0770e6b4a45519025134b12e4fc", url="https://pypi.org/packages/28/6c/640e3f5c734c296a7193079a86842a789edb7988dca39eab44579088a1d1/PyQt5-5.15.2.tar.gz")
    version("5.15.1", sha256="d9a76b850246d08da9863189ecb98f6c2aa9b4d97a3e85e29330a264aed0f9a1", url="https://pypi.org/packages/1d/31/896dc3dfb6c81c70164019a6cbba6ab037e3af7653d9ca60ccc874ee4c27/PyQt5-5.15.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyqt5-qt", when="@5.15.3")
        depends_on("py-pyqt5-sip@12.13:", when="@5.15.10:")
        depends_on("py-pyqt5-sip@12.11:", when="@5.15.7:5.15.9")
        depends_on("py-pyqt5-sip@12.8:", when="@5.15:5.15.1")

