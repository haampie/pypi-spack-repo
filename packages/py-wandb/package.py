##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWandb(PythonPackage):
    version("0.16.5", sha256="023b6c72a6ef13085c9a970f6714548eca64f56d3d8698e42372764950dfd004", url="https://pypi.org/packages/53/7c/f3656d1ce3b916ea35f454c6a32b56342168c08baf09a0683df240ca2dce/wandb-0.16.5-py3-none-any.whl")
    version("0.16.4", sha256="bb9eb5aa2c2c85e11c76040c4271366f54d4975167aa6320ba86c3f2d97fe5fa", url="https://pypi.org/packages/97/c9/5af930be59487ab6c7e76dc1ffa31f7f035be2e50cb17cc56b87ba47ff8f/wandb-0.16.4-py3-none-any.whl")
    version("0.16.3", sha256="b8907ddd775c27dc6c12687386a86b5d6acf291060f9ae680bbc61cc8fc03237", url="https://pypi.org/packages/c4/b0/5efefacd9d12b411ebe57c3db6d05a38883cd52e0ff46ca7b217df3151a1/wandb-0.16.3-py3-none-any.whl")
    version("0.16.2", sha256="6b119cf3c01f35e7276b62d052128e5320621d182c9eb5796a12cf62a9b3134f", url="https://pypi.org/packages/28/3b/f1485df03e33a390b833081693e56be9e62fef097a82c26ef615605f768d/wandb-0.16.2-py3-none-any.whl")
    version("0.16.1", sha256="1d7423f92520984585bae9693bb637ae08d3e0c1d75ad4b34215bc44431f114c", url="https://pypi.org/packages/35/d3/6bfe29e4ba1eb2400d478caf8e3af9a1c366390390069cda59a7c6bf6063/wandb-0.16.1-py3-none-any.whl")
    version("0.16.0", sha256="e103142a5ecdb158d29441c2bf9f935ae149ed562377f7cebffd2a6f7c9de949", url="https://pypi.org/packages/5c/81/1780aa129564b11709a6d7f0739257174f0a3a1b432ba804b3c6f00e0f88/wandb-0.16.0-py3-none-any.whl")
    version("0.15.12", sha256="75c57b5bb8ddae21d45a02f644628585bdd112fea686de3177099a0996f1c41c", url="https://pypi.org/packages/1c/5e/0362fa88679852c7fd3ac85ee5bd949426c4a51a61379010d4089be6d7ac/wandb-0.15.12-py3-none-any.whl")
    version("0.15.11", sha256="d0ea8b683c1416b626de0a57800687fb6c36307b3e1a455b7ed4dee6e342f391", url="https://pypi.org/packages/8a/ab/3b6cce52474f273522b4381f4ed93120f1a196d09a8ba65e1f4615fbaa39/wandb-0.15.11-py3-none-any.whl")
    version("0.15.10", sha256="bc810879fecd1b62ccd498658e55ade3702939090a94b99418630e77e1f43d50", url="https://pypi.org/packages/fe/10/18b03623c460fd433525d9b4739af58c5e69f5974328dcdd037cfbc855d7/wandb-0.15.10-py3-none-any.whl")
    version("0.15.9", sha256="879365e5fcd00444874785b02f56f25973e7064420d9de3cc08a9948ecdf565b", url="https://pypi.org/packages/3d/2d/4b115c075a4a5eda4c905efb012a585813d6d40ee3199393bc48f1fdba1f/wandb-0.15.9-py3-none-any.whl")
    version("0.13.9", sha256="b8752e5287aca9f8192eca7be352882975973cd3cd0c88815930498fd357569d", url="https://pypi.org/packages/a3/b4/279ec12c6c481d0f672e9cf89fbdf7e57f5aacaf23493c699e1c00671ce0/wandb-0.13.9-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-appdirs@1.4.3:", when="@0.13.8:")
        depends_on("py-click@7.1:8.0.0-rc1,8.0.1:", when="@0.15.5:")
        depends_on("py-click@7:8.0.0-rc1,8.0.1:", when="@0.10.32:0.15.4")
        depends_on("py-docker-pycreds@0.4:", when="@0.7:")
        depends_on("py-gitpython@1:3.1.28,3.1.30:", when="@0.13.11:")
        depends_on("py-gitpython@1:", when="@0.6:0.13.10")
        depends_on("py-numpy", when="@0.10:0.10.0-rc1")
        depends_on("py-pathtools", when="@0.10.16:0.16.0-beta1")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=windows")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=linux ^python@3.9.1:")
        depends_on("py-protobuf@3.12.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=linux ^python@:3.8")
        depends_on("py-protobuf@3.15.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=linux ^python@3.9:3.9.0")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=freebsd")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=darwin")
        depends_on("py-protobuf@3.19.0:4.21.0-rc2,4.21.1:4", when="@0.13.6: platform=cray")
        depends_on("py-psutil@5:", when="@0.6.29:")
        depends_on("py-pyyaml", when="@0.10:")
        depends_on("py-requests@2:", when="@0.10.0-rc7:")
        depends_on("py-sentry-sdk@1:", when="@0.11.1:")
        depends_on("py-setproctitle", when="@0.12.11:")
        depends_on("py-setuptools", when="@0.12.16:")
        depends_on("py-typing-extensions", when="@0.13.8: ^python@:3.9")

