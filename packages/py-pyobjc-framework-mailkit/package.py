##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMailkit(PythonPackage):
    version("10.2", sha256="d8bc9e6649e7e500d2d4d4ab288304846d9bfa06952ebeee621fe095dc2f51eb", url="https://pypi.org/packages/c6/24/4be9142fa1b01d7507a335d3c15d6ab61097a93e0cd6bb4629a227df194f/pyobjc_framework_MailKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="498d743e56d876d6d128970e6c0674470d9a4bcf9c021f0b115aa0c6ade1f5ae", url="https://pypi.org/packages/f3/7e/69b0be0549242ed49a18b47e3c025ac913043f9610adf8fca2bf22b65ec4/pyobjc_framework_MailKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="b95f61745c01d41b2548ff6b6d0efc1476b718874a115fe0f17c06b5b3a1d300", url="https://pypi.org/packages/45/f0/dd6c7a2d68a6929dd9badeb76638bf88b8fdc4352616419fd74e2575c185/pyobjc_framework_MailKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="8d0b8820cd34701d7da0e494ac2bc66c0dd70aad881325d3e24a5364d864c49c", url="https://pypi.org/packages/15/47/623cc87ab9bb0757b50c154587cc60c7730d9f08a2240edaff51262371ff/pyobjc_framework_MailKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="232ca4f233a59df2a4652884fbf56f87a93486ed3843863da8d6211dfac39e63", url="https://pypi.org/packages/87/67/46e83b66ef1007484f7c7491dec3eb9a5e58dfaeb04c244e4ac837febc8a/pyobjc_framework_MailKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="ba218ca5b2d055d1fb52b8212b587cd159fed5674d7342606ba0047184e054e5", url="https://pypi.org/packages/96/dc/5f7262f25654fc2da6f7fc0c624098fcba08350aaccaca914e31a353eccd/pyobjc_framework_MailKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="65803da7e051e5bd7cae8c0eb76f0098a73ffdb2d288f9e59af578bb8ac7a15d", url="https://pypi.org/packages/9d/37/782adb8767c62822a61449eb95e1f9804ef38f17d4bbda857566cdfe4161/pyobjc_framework_MailKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="7a4ff16a37d8be8a508cfce4c26c4615ebb547087a87b45fed82e0e724cba455", url="https://pypi.org/packages/fe/50/bf0afb69c0f18c90098c9d1980c4882225eb4526b85cb00366f129ee42f1/pyobjc_framework_MailKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="c18134dd01c35aa8a21ddf36294820f4f1b8fd815406905c61c7a52b4a3bb120", url="https://pypi.org/packages/c8/df/2855915fc42a8956b3b92d3ecc61de0e471032fc219b1f2a35570e20c3a7/pyobjc_framework_MailKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="2fb79f64cf54672ba8a3aadc80cc1c25285a7bb263e3f4b57e8b7b7cd7c01f43", url="https://pypi.org/packages/e1/4a/660c0baff789f36556063706d5bd2b662fa71b1c5bd531fee62b985ff62e/pyobjc_framework_MailKit-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

