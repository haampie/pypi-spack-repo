##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTraitlets(PythonPackage):
    version("5.14.2", sha256="fcdf85684a772ddeba87db2f398ce00b40ff550d1528c03c14dbf6a02003cd80", url="https://pypi.org/packages/7c/c4/366a09036c07f46eb8c9b2af39c97f502ef24f11f2a6e4d763655d9f2708/traitlets-5.14.2-py3-none-any.whl")
    version("5.14.1", sha256="2e5a030e6eff91737c643231bfcf04a65b0132078dad75e4936700b213652e74", url="https://pypi.org/packages/45/34/5dc77fdc7bb4bd198317eea5679edf9cc0a186438b5b19dbb9062fb0f4d5/traitlets-5.14.1-py3-none-any.whl")
    version("5.14.0", sha256="f14949d23829023013c47df20b4a76ccd1a85effb786dc060f34de7948361b33", url="https://pypi.org/packages/a7/1d/7d07e1b152b419a8a9c7f812eeefd408a0610d869489ee2e86973486713f/traitlets-5.14.0-py3-none-any.whl")
    version("5.13.0", sha256="baf991e61542da48fe8aef8b779a9ea0aa38d8a54166ee250d5af5ecf4486619", url="https://pypi.org/packages/ed/fd/cfc0d27ca11f3dd12b2a90d06875d8bfb532ef40ce67be4066d10807f4aa/traitlets-5.13.0-py3-none-any.whl")
    version("5.12.0", sha256="81539f07f7aebcde2e4b5ab76727f53eabf18ad155c6ed7979a681411602fa47", url="https://pypi.org/packages/e0/ad/0ec97a5a37481552b43352190e509b8dfb2e379d55b41fac8ba5a635bb9a/traitlets-5.12.0-py3-none-any.whl")
    version("5.11.2", sha256="98277f247f18b2c5cabaf4af369187754f4fb0e85911d473f72329db8a7f4fae", url="https://pypi.org/packages/85/e9/d82415708306eb348fb16988c4697076119dfbfa266f17f74e514a23a723/traitlets-5.11.2-py3-none-any.whl")
    version("5.11.1", sha256="2351372ff87fc912c483d1cb6aa466573d5f44eb4ed9e602c8d0ac012c9daece", url="https://pypi.org/packages/4f/a8/080bb740051da5cf21cd9a71be9eef6b097576f284def626b695a8822d45/traitlets-5.11.1-py3-none-any.whl")
    version("5.11.0", sha256="a71e489c4b70e2f91b799d0c2e77bd1fe208912cba554792e17f0f88c604d779", url="https://pypi.org/packages/be/7b/cc39f676b09b062124faa40fb0d54109d5283ddf26ab227c5da76cf16fca/traitlets-5.11.0-py3-none-any.whl")
    version("5.10.1", sha256="07ab9c5bf8a0499fd7b088ba51be899c90ffc936ffc797d7b6907fc516bcd116", url="https://pypi.org/packages/ba/f0/b6056454b2e3b009fc7c216927791b4db35cc798c4737f81f8f806710924/traitlets-5.10.1-py3-none-any.whl")
    version("5.10.0", sha256="417745a96681fbb358e723d5346a547521f36e9bd0d50ba7ab368fff5d67aa54", url="https://pypi.org/packages/fb/00/78472b256929614443c3fa3be31ee60777e5a9e3c6770d8d934154aa2cab/traitlets-5.10.0-py3-none-any.whl")
    version("5.9.0", sha256="9e6ec080259b9a5940c797d58b613b5e31441c2257b87c2e795c5228ae80d2d8", url="https://pypi.org/packages/77/75/c28e9ef7abec2b7e9ff35aea3e0be6c1aceaf7873c26c95ae1f0d594de71/traitlets-5.9.0-py3-none-any.whl")
    version("5.7.1", sha256="57ba2ba951632eeab9388fa45f342a5402060a5cc9f0bb942f760fafb6641581", url="https://pypi.org/packages/cb/1e/7b8ae7bbc4c0d4b913cabb345c2ac98450bbd9cfe90ee2be275019037932/traitlets-5.7.1-py3-none-any.whl")
    version("5.3.0", sha256="65fa18961659635933100db8ca120ef6220555286949774b9cfc106f941d1c7a", url="https://pypi.org/packages/83/a9/1059771062cb80901c34a4dea020e76269412e69300b4ba12e3356865ad8/traitlets-5.3.0-py3-none-any.whl")
    version("5.1.1", sha256="2d313cc50a42cd6c277e7d7dc8d4d7fedd06a2c215f78766ae7b1a66277e0033", url="https://pypi.org/packages/37/46/be8a3c030bd3673f4800fa7f46eda972dfa2990089a51ec5dd0a26ed33e9/traitlets-5.1.1-py3-none-any.whl")
    version("5.0.4", sha256="9664ec0c526e48e7b47b7d14cd6b252efa03e0129011de0a9c1d70315d4309c3", url="https://pypi.org/packages/e6/20/f73a1130598ffaf561fda74d761bbe66db7a3639f34456761e781509881b/traitlets-5.0.4-py3-none-any.whl")
    version("4.3.3", sha256="70b4c6a1d9019d7b4f6846832288f86998aa3b9207c6821f3578a6a6a467fe44", url="https://pypi.org/packages/ca/ab/872a23e29cec3cf2594af7e857f18b687ad21039c1f9b922fac5b9b142d5/traitlets-4.3.3-py2.py3-none-any.whl")
    version("4.3.2", sha256="c6cb5e6f57c5a9bdaa40fa71ce7b4af30298fbab9ece9815b5d995ab6217c7d9", url="https://pypi.org/packages/93/d6/abcb22de61d78e2fc3959c964628a5771e47e7cc60d53e9342e21ed6cc9a/traitlets-4.3.2-py2.py3-none-any.whl")
    version("4.3.1", sha256="50522e46dd7b66c80686d50ff1b774000f1d2a80c84b2bcfbd657d588e99a368", url="https://pypi.org/packages/b6/72/f62f13fb8cdb85af5239788d4c57c281b3a92efc9d2ad9cc44cb14c8c26d/traitlets-4.3.1-py2.py3-none-any.whl")
    version("4.3.0", sha256="c13c85694e33272612c61f9d0f368eca63350b0300d7e3b9331f809f0fc360b5", url="https://pypi.org/packages/68/fe/a542484eb8d1b7b8949a06936f702dac80d316becc5d8416def728e13cea/traitlets-4.3.0-py2.py3-none-any.whl")
    version("4.2.2", sha256="c6176a597361219f2f4cc1e82c560cc976c479b6f001fd851ac849391d6a648e", url="https://pypi.org/packages/ad/25/a507caa3514e7651fd14ffcffcd279779f604fefa3391b225bfb09d5c407/traitlets-4.2.2-py2.py3-none-any.whl")
    version("4.2.1", sha256="05a66843c96a320eec09df674c16ff330a43cb07f731cf2bd88aa3645a180541", url="https://pypi.org/packages/db/f3/a24062437f01ceae74edf622ac3f8c55b555a2ed1967e5e3d945efe54c3d/traitlets-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="b920f170255dda49415f3ebf3caf666d3dadd08e38d490c84009792bd16d338f", url="https://pypi.org/packages/10/ed/37ca0815e846baea11d2cc65d7eeb127aef9c22f886847f151c372fc0d66/traitlets-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="0fdac5614e5cb3329a39d48bbbc4b95813920af7565c1488b5d787ef2863be26", url="https://pypi.org/packages/c7/ac/7bb361161e9b37d00a0b81f0e360fe0be8e2b9156e4da74aabf7f167b237/traitlets-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="0b140b4a94a4f1951887d9bce4650da211f79600fc9fdb422acc90c5bbe0233b", url="https://pypi.org/packages/29/23/df9b27cc2e327260458f6f5b6a23f59f61f5b3857645fdbf8930e8544a2c/traitlets-4.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-decorator", when="@4.1.0:4")
        depends_on("py-ipython-genutils", when="@4.1.0:5.0")
        depends_on("py-six", when="@4.3:4")

