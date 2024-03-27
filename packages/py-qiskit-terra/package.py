##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQiskitTerra(PythonPackage):
    version("0.46.1", sha256="9fe20d23cb59cefcda66f9d2b9c3e6c6d532887637568bbc80b2c1d36bff3c0f", url="https://pypi.org/packages/9e/cf/705649e70856f7a2f5856a7ae6e1fdd713987991cfb18c0a3609e79a2cc1/qiskit-terra-0.46.1.tar.gz")
    version("0.46.0", sha256="49ba03cfe49b38b81a9e3144637bf036a82d38f97333f3871dee7b72a5f1f094", url="https://pypi.org/packages/d5/1b/677ba8b534203d660fe0616cd68e9d08622b4056b8ace4fcf325566cfddc/qiskit-terra-0.46.0.tar.gz")
    version("0.45.3", sha256="fa3c5d9f54abd5f38fa79c1b1490ff984358377a2d6ed3c17ad2f06fd94243f8", url="https://pypi.org/packages/a5/63/70fedee4c584f6262b23f09286af239317d8b0e8b0032db6db288872ec89/qiskit-terra-0.45.3.tar.gz")
    version("0.45.2", sha256="bf089871c60406beea90ec5e31a1776308d4aa7ec0defdd08afeaf192f452175", url="https://pypi.org/packages/a4/d4/63a36cf542af5a8f3afacb7573267e8dde6dd96099841f44792dc2e3c980/qiskit-terra-0.45.2.tar.gz")
    version("0.45.1", sha256="4ed0cf0d5f275276a27135b9d02f599d0c59c0c1c4286c2392314558481ed736", url="https://pypi.org/packages/e4/4c/2569d4b34d5213c1f88b3cb61098e074592855d88e4a5f6960dd46eafd7b/qiskit-terra-0.45.1.tar.gz")
    version("0.45.0", sha256="fe58d2fb123395853b426e7bd3747cdba4152573c7c3be1f19b5cd20bef92664", url="https://pypi.org/packages/22/ef/22cd225697087a5c5bbcc2ad55e4dbf76ce7906d5321d5566591d15b06a7/qiskit-terra-0.45.0.tar.gz")
    version("0.25.3", sha256="1540a63d9771021724d0587975bd6b9fe0210852f4d96df7ec86305e0b09608c", url="https://pypi.org/packages/9b/12/30aad118262028899d1cb0b552c1e24a0c2dc1f472990bab44097fab64a2/qiskit-terra-0.25.3.tar.gz")
    version("0.25.2.1", sha256="d3af3e01a4a58996fd065a7aa59bc46c4ea3559acd2164bf8725b58522fbafc4", url="https://pypi.org/packages/89/e9/ce1d5eaf1b8f7f8aac12e2ddc65792f261af0ef334e4a95977dac9a044a2/qiskit-terra-0.25.2.1.tar.gz")
    version("0.25.2", sha256="b865af9696a71aeca17c2e926c262a9160191aa247c98c3d75860d3ff34bdc67", url="https://pypi.org/packages/39/06/3825f83417dc0403af3a02cb01f8e4873569a593a91eca31be3c1f002dcf/qiskit-terra-0.25.2.tar.gz")
    version("0.25.1", sha256="1ea5981800377af5cc8beefd5ca62e18196b918058de8382a129abc921fa3c8b", url="https://pypi.org/packages/da/a4/a5c3aaa98467c0c27bad3c657002e4aca06119be9769bf4288025fcd87eb/qiskit-terra-0.25.1.tar.gz")
    version("0.23.3", sha256="8f2f61622c28ad38db95d9bbacb03b9743923581545df08eb5047fa86f4de198", url="https://pypi.org/packages/9b/ca/18eaef015cab6042e8d3f0241961a45810362ecb01f86b4b0fea8a85d4a4/qiskit-terra-0.23.3.tar.gz")
    version("0.22.2", sha256="efd212cd98479ebedc8cc1f93d4eb8039f21c07bd39a62065b584e02d72e632d", url="https://pypi.org/packages/63/c3/90b54d3d673e0e65d7867a0040fe16dd9c28b20a2f91bb25c3243a0cd0f5/qiskit-terra-0.22.2.tar.gz")
    version("0.18.3", sha256="8737c8f1f4c6f29ec2fb02d73023f4854a396c33f78f4629a861a3e48fc789cc", url="https://pypi.org/packages/3a/60/8bb779e14af93f70e525d4cc04c01ff465ef93579e5cbb6320d5ce17f291/qiskit-terra-0.18.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-dill@0.3:", when="@0.25.3:")
        depends_on("py-numpy@1.17.0:1", when="@0.45:")
        depends_on("py-numpy@1.17.0:", when="@0.25.3:0.25")
        depends_on("py-pillow@4.2.1:", when="@:0.8")
        depends_on("py-ply@3.10:", when="@:0.10,0.25.3:")
        depends_on("py-psutil@5:", when="@:0.10,0.25.3:")
        depends_on("py-pylatexenc@1.4:", when="@0.8")
        depends_on("py-python-dateutil@2.8:", when="@0.25.3:")
        depends_on("py-rustworkx@0.13:", when="@0.25.3:")
        depends_on("py-scipy@1.5.0:", when="@0.25.3:")
        depends_on("py-stevedore@3:", when="@0.25.3:")
        depends_on("py-sympy@1.3:", when="@:0.10,0.25.3:")
        depends_on("py-typing-extensions", when="@0.25.3: ^python@:3.10")

        # marker: platform_machine == "x86_64" or platform_machine == "aarch64" or platform_machine == "ppc64le" or platform_machine == "amd64" or platform_machine == "arm64"
        # depends_on("py-symengine@0.11:", when="@0.46:")
        # depends_on("py-symengine@0.9,0.11:", when="@0.45.1:0.45")
        # depends_on("py-symengine@0.9", when="@0.25.3:0.45.0")

