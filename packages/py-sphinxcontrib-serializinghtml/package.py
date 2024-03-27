##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribSerializinghtml(PythonPackage):
    version("1.1.10", sha256="326369b8df80a7d2d8d7f99aa5ac577f51ea51556ed974e7716cfd4fca3f6cb7", url="https://pypi.org/packages/38/24/228bb903ea87b9e08ab33470e6102402a644127108c7117ac9c00d849f82/sphinxcontrib_serializinghtml-1.1.10-py3-none-any.whl")
    version("1.1.9", sha256="9b36e503703ff04f20e9675771df105e58aa029cfcbc23b8ed716019b7416ae1", url="https://pypi.org/packages/95/d6/2e0bda62b2a808070ac922d21a950aa2cb5e4fcfb87e5ff5f86bc43a2201/sphinxcontrib_serializinghtml-1.1.9-py3-none-any.whl")
    version("1.1.8", sha256="27849e7227277333d3d32f17c138ee148a51fa01f888a41cd6d4e73bcabe2d06", url="https://pypi.org/packages/dc/85/ea34b6be0494eff8ae281107bb4a83f6c83066b358f2525a251dc852817c/sphinxcontrib_serializinghtml-1.1.8-py3-none-any.whl")
    version("1.1.7", sha256="424164fc3a8b4355a29d5ea8b7f18199022d160c8f7b96e68bb6c50217729b87", url="https://pypi.org/packages/36/c6/0d5b3f258fdb107558163e88607eb6c245d8785fbd707e027f2da7fbc795/sphinxcontrib_serializinghtml-1.1.7-py3-none-any.whl")
    version("1.1.6", sha256="f7e8e508f5c973601fa29a9114aa60bc11164db3d6c55aa7fd51710185477237", url="https://pypi.org/packages/82/a2/962548d13ceddff95eac7843c9ff37b451c02b69429007b93d6a10a353d3/sphinxcontrib_serializinghtml-1.1.6-py3-none-any.whl")
    version("1.1.5", sha256="352a9a00ae864471d3a7ead8d7d79f5fc0b57e8b3f95e9867eb9eb28999b92fd", url="https://pypi.org/packages/c6/77/5464ec50dd0f1c1037e3c93249b040c8fc8078fdda97530eeb02424b6eea/sphinxcontrib_serializinghtml-1.1.5-py2.py3-none-any.whl")
    version("1.1.4", sha256="f242a81d423f59617a8e5cf16f5d4d74e28ee9a66f9e5b637a18082991db5a9a", url="https://pypi.org/packages/9a/ca/bfad79b79b3821d0c6361c431f0ef4aec16ee248338b2c2013008b34d345/sphinxcontrib_serializinghtml-1.1.4-py2.py3-none-any.whl")
    version("1.1.3", sha256="db6615af393650bf1151a6cd39120c29abaf93cc60db8c48eb2dddbfdc3a9768", url="https://pypi.org/packages/57/b3/3648e48fa5682e61e9839d62de4e23af1795ceb738d68d73bd974257a95c/sphinxcontrib_serializinghtml-1.1.3-py2.py3-none-any.whl")
    version("1.1.1", sha256="01d9b2617d7e8ddf7a00cae091f08f9fa4db587cc160b493141ee56710810932", url="https://pypi.org/packages/9e/1e/57beb109ebfd765ac1adf35eb982ac35692d7a25f7002281afffcbd2f817/sphinxcontrib_serializinghtml-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="4989174ec3f49b5440344bb5397ac2c81ca266413c370186e8f9c3eadc66450a", url="https://pypi.org/packages/fb/47/5fa80011869d85500a179ec1ede43487b5ddc0f57e77cefe858613581102/sphinxcontrib_serializinghtml-1.1.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.1.6:")
        depends_on("py-sphinx@5.0.0:", when="@1.1.6:1.1.9")

