##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApscheduler(PythonPackage):
    version("3.10.4", sha256="fb91e8a768632a4756a585f79ec834e0e27aad5860bac7eaa523d9ccefd87661", url="https://pypi.org/packages/13/b5/7af0cb920a476dccd612fbc9a21a3745fb29b1fcd74636078db8f7ba294c/APScheduler-3.10.4-py3-none-any.whl")
    version("3.10.3", sha256="1611d207b095ff52d97884e90736c192bdd94dbd44ce27eb92c3f1da24a400d3", url="https://pypi.org/packages/36/2d/8c8c09317e3c95c05d7fc56f878c6c5b4d44e0ed26052798251d95f9cf8d/APScheduler-3.10.3-py3-none-any.whl")
    version("3.10.2", sha256="1b6b4cb3fcb1cfd858d12d77c206f838b1c0cd0489a2643c1303e198ed7c0167", url="https://pypi.org/packages/34/36/ecf1f97c9f8bfd3d5200d37c2aa0763859b5c86f91cd4604b67ba8972c42/APScheduler-3.10.2-py3-none-any.whl")
    version("3.10.1", sha256="e813ad5ada7aff36fb08cdda746b520531eaac7757832abc204868ba78e0c8f6", url="https://pypi.org/packages/d0/08/952d9570f4897dc2b30166fca5afd3a2cd19b3d408abdb470978484e8a09/APScheduler-3.10.1-py3-none-any.whl")
    version("3.10.0", sha256="575299f20073c60a2cc9d4fa5906024cdde33c5c0ce6087c4e3c14be3b50fdd4", url="https://pypi.org/packages/0a/82/e8b6e7e2dfea46bd649ecaf8771fb6552232394fc9adf5c7f10655a87b95/APScheduler-3.10.0-py3-none-any.whl")
    version("3.9.1.post1", sha256="c8c618241dbb2785ed5a687504b14cb1851d6f7b5a4edf3a51e39cc6a069967a", url="https://pypi.org/packages/23/4d/e32c8cd0738942234d7a328ef9272a59c69f3c5db01d46e35003ffef20e4/APScheduler-3.9.1.post1-py2.py3-none-any.whl")
    version("3.9.1", sha256="ddc25a0ddd899de44d7f451f4375fb971887e65af51e41e5dcf681f59b8b2c9a", url="https://pypi.org/packages/e4/9f/c3937d4babe62504b874d4bf2c0d85aa69c7f59fa84cf6050f3b9dc5d83e/APScheduler-3.9.1-py2.py3-none-any.whl")
    version("3.9.0.post2", sha256="f77ea32f0ac09d52010857538f65c407a8f2580185722697d637fd89ad20ec87", url="https://pypi.org/packages/3b/22/efc541cbeb1908d620dd8dc85963f723bc245cefdee8f74f63e3c49e4455/APScheduler-3.9.0.post2-py2.py3-none-any.whl")
    version("3.9.0.post1", sha256="f8a3e6e4d178de40fdbd5a3eefcc217588fc7f42f443e2335bb2dc29daf99357", url="https://pypi.org/packages/8e/b4/fadc940618942703712efc9bb33ea5ca784b16c080df9d0e889c542cbd13/APScheduler-3.9.0.post1-py2.py3-none-any.whl")
    version("3.9.0", sha256="70dd820b9c1bae23a9d7405440d88aff018107fa0618b5d1f29c7f3194b3ab79", url="https://pypi.org/packages/2c/44/7fc2a570282c0797c5fe1ffd67053155a70e640e7e1348555939014777ce/APScheduler-3.9.0-py2.py3-none-any.whl")
    version("3.3.1", sha256="bc9f96e498adb362beb5f1d3715a2570d100183add4ace5227c1a7d5dbaac900", url="https://pypi.org/packages/22/ff/eb9d27536f25253c09573cc7afc6db9708ea0abad02f5ac031b412d5cbda/APScheduler-3.3.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="3b4b44387616902ad6d13122961013630eb25519937e5aa7c450de85656c9753", url="https://pypi.org/packages/09/49/828c768c015ca3ca18b9a2e2029b6acc4c809e37c916659d3b54d69e67b1/APScheduler-2.1.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pytz", when="@3")
        depends_on("py-setuptools@0.7:", when="@3.1:3.10.1")
        depends_on("py-six@1.4:", when="@3.1:3")
        depends_on("py-tzlocal@2.0.0:2,4:", when="@3.8.1:3")
        depends_on("py-tzlocal@1.2:", when="@3.1:3.6")

