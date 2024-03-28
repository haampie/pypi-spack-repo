# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArgcomplete(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.3", sha256="c12355e0494c76a2a7b73e3a59b09024ca0ba1e279fb9ed6c1b82d5b74b6a70c", url="https://pypi.org/packages/88/8c/61021c45428ad2ef6131c6068d14f7f0968767e972e427cd87bd25c9ea7b/argcomplete-3.2.3-py3-none-any.whl")
    version("3.2.2", sha256="e44f4e7985883ab3e73a103ef0acd27299dbfe2dfed00142c35d4ddd3005901d", url="https://pypi.org/packages/f9/75/2cbf82a7ea474786e14b4d5171af88cf2b49e677a927f8b45d091418d889/argcomplete-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="30891d87f3c1abe091f2142613c9d33cac84a5e15404489f033b20399b691fec", url="https://pypi.org/packages/73/44/42ff5ee76b3881bebe226614c658df9423fe8ddd3d7967e6850b008f4899/argcomplete-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="bfe66abee7fcfaf3c6b26ec9b0311c05ee5daf333c8f3f4babc6a87b13f51184", url="https://pypi.org/packages/a1/be/c47944b15cf06712742c8afe8a60e65a30b35c97e0dde8ac759ec0f9a484/argcomplete-3.2.0-py3-none-any.whl")
    version("3.1.6", sha256="71f4683bc9e6b0be85f2b2c1224c47680f210903e23512cfebfe5a41edfd883a", url="https://pypi.org/packages/a6/b1/db437353b42cc3042aae23383b53c7a8f48b68a66f355787429a249d0082/argcomplete-3.1.6-py3-none-any.whl")
    version("3.1.5", sha256="f0105ff52078387ab2e72ad68a83e3b1e36628c6dc2f865ba433d741bc1f6955", url="https://pypi.org/packages/97/3e/fcb28cfa05715b56f263bdab3afc80251397ea54cbfd0770a28ad92128e2/argcomplete-3.1.5-py3-none-any.whl")
    version("3.1.4", sha256="fbe56f8cda08aa9a04b307d8482ea703e96a6a801611acb4be9bf3942017989f", url="https://pypi.org/packages/2f/91/0901d7692aa4615e131f8134769fab468d63990817dbec395fb57702dbdd/argcomplete-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="611c9d068f7a06e71d840d3bea59171aa7c927cb22c9a58557f74dc194f18b4d", url="https://pypi.org/packages/99/33/d7aeab77c36efb7eec4839ac119e35b6ed68a898a5f5d5f6e92e041c80b1/argcomplete-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="d97c036d12a752d1079f190bc1521c545b941fda89ad85d15afa909b4d1b9a99", url="https://pypi.org/packages/1e/05/223116a4a5905d6b26bff334ffc7b74474fafe23fcb10532caf0ef86ca69/argcomplete-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="35fa893a88deea85ea7b20d241100e64516d6af6d7b0ae2bed1d263d26f70948", url="https://pypi.org/packages/4f/ef/8b604222ba5e5190e25851aa3a5b754f2002361dc62a258a8e9f13e866f4/argcomplete-3.1.1-py3-none-any.whl")
    version("3.0.8", sha256="e36fd646839933cbec7941c662ecb65338248667358dd3d968405a4506a60d9b", url="https://pypi.org/packages/ab/ce/2141e1cabe39c90e01fde7feb44c07867fb49bf1c0c091d68fd8924fd6a2/argcomplete-3.0.8-py3-none-any.whl")
    version("2.0.0", sha256="cffa11ea77999bb0dd27bb25ff6dc142a6796142f68d45b1a26b11f58724561e", url="https://pypi.org/packages/d3/e5/c5509683462e51b070df9e83e7f72c1ccfe3f733f328b4a0f06804c27278/argcomplete-2.0.0-py2.py3-none-any.whl")
    version("1.12.3", sha256="291f0beca7fd49ce285d2f10e4c1c77e9460cf823eef2de54df0c0fec88b0d81", url="https://pypi.org/packages/b7/9e/9dc74d330c07866d72f62d553fe8bdbe32786ff247a14e68b5659963e6bd/argcomplete-1.12.3-py2.py3-none-any.whl")
    version("1.12.2", sha256="17f01a9b9b9ece3e6b07058eae737ad6e10de8b4e149105f84614783913aba71", url="https://pypi.org/packages/e3/d0/ee7fc6ceac8957196def9bfa3b955d02163058defd3edd51ef7b1ff2769e/argcomplete-1.12.2-py2.py3-none-any.whl")
    version("1.12.1", sha256="5cd1ac4fc49c29d6016fc2cc4b19a3c08c3624544503495bf25989834c443898", url="https://pypi.org/packages/d2/21/b0cecd5193b4d86818fe5b29b36f6bd5807ed9ab2d4a75681e1d3eaf7ba8/argcomplete-1.12.1-py2.py3-none-any.whl")
    version("1.12.0", sha256="91dc7f9c7f6281d5a0dce5e73d2e33283aaef083495c13974a7dd197a1cdc949", url="https://pypi.org/packages/89/4d/b8e035cca2c9b2484ac12d20e0fb68019e17f0b09918f2765e0a381127fb/argcomplete-1.12.0-py2.py3-none-any.whl")
    version("1.11.1", sha256="890bdd1fcbb973ed73db241763e78b6d958580e588c2910b508c770a59ef37d7", url="https://pypi.org/packages/82/7d/455e149c28c320044cb763c23af375bd77d52baca041f611f5c2b4865cf4/argcomplete-1.11.1-py2.py3-none-any.whl")
    version("1.11.0", sha256="52a08b426bd0b03b6881182dd84149b2493540d1c3109ccf9f09f78e4459e387", url="https://pypi.org/packages/65/a6/4fd54d4f4fe699b8b9b709e7501a2617aa6352de074e0790adb3437ecd98/argcomplete-1.11.0-py2.py3-none-any.whl")
    version("1.10.3", sha256="d8ea63ebaec7f59e56e7b2a386b1d1c7f1a7ae87902c9ee17d377eaa557f06fa", url="https://pypi.org/packages/ae/8e/6b293f883fdbd29b9c8170db44bddff9e7de224d8cf1eb4287f69f1766e5/argcomplete-1.10.3-py2.py3-none-any.whl")
    version("1.10.2", sha256="c6aaa1d534adaa1be0a7e9d51d7f5993dba608f6d2a2b765302c05b0b3e9a719", url="https://pypi.org/packages/b8/3e/370189084cdb7b4a8adb18d179f957d9115f8ee06aa5a1d85b56651a59bf/argcomplete-1.10.2-py2.py3-none-any.whl")
    version("1.10.1", sha256="d1136db4db8ff94d8fc345ea48c89a70c8a985a73d77a052b2f9ba032ec36592", url="https://pypi.org/packages/1e/5d/777a2c0532ffce40dfb7cdee850c8b39955af604330a64824951ca6c353c/argcomplete-1.10.1-py2.py3-none-any.whl")
    version("1.10.0", sha256="2f2052ea5156eb5cc7edce9c0ddc937e30c49c1097d51b24f34350a08632a264", url="https://pypi.org/packages/4d/82/f44c9661e479207348a979b1f6f063625d11dc4ca6256af053719bbb0124/argcomplete-1.10.0-py2.py3-none-any.whl")
    version("1.1.1", sha256="f9bb1e017aa61e52b28023936475963d97d62046a1f87e0f0dfc5a5b439949ff", url="https://pypi.org/packages/b2/64/f622fc5e6a202f802343cf6363fe0ff6a1e7f99cd7e0184a71f038cdbb4e/argcomplete-1.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

