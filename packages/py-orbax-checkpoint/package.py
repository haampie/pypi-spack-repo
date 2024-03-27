##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOrbaxCheckpoint(PythonPackage):
    version("0.5.6", sha256="b4b15f2724cf2b756d01713e26bd360be40fb6ff259fb42e557f0691198a44ab", url="https://pypi.org/packages/0c/42/c6bc982c0569f683017034ee89591a3e988b311e85f7a7648e6d0b1332c1/orbax_checkpoint-0.5.6-py3-none-any.whl")
    version("0.5.5", sha256="e01d51e60f94e3393a08e8c07292c811b93ac58672dde80fc23844c16f2eddb7", url="https://pypi.org/packages/a4/8f/f5685469962945218d02ab8a63111a85de6afecc351a172df765d223d7fb/orbax_checkpoint-0.5.5-py3-none-any.whl")
    version("0.5.4", sha256="db7fb4bf5f7e5229de855106bbdbb0660b5a2260a118703222ace6e18badc6da", url="https://pypi.org/packages/7b/c2/1603adee54a6ea9376ecbdcceb7686d434a0535ff3a7dafd85e2020ab185/orbax_checkpoint-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="82acdf18acb1e294396dd583634d3b1bd005bbb81f3de650740384c465d735c3", url="https://pypi.org/packages/83/a2/0677f2ee06bdbf7b4e6be4ad931ffe58f2ea82d67bb2a277d9d7b3b1e352/orbax_checkpoint-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="80d27be11732ec30df7214ce6508020d4cc853cc5217232d699539c84d5f9f5f", url="https://pypi.org/packages/27/db/7d1888548b1681acecdb93f5df1f79d455ffa89833390bc38a689b1b3e96/orbax_checkpoint-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="d35bafdf01906fb2a3255f9bebff78fc714a30eeae71228e0064a77bd5a40d90", url="https://pypi.org/packages/67/cf/9c5d23634d43abf0eb31b626ae1eced0eb0f604f1baab1498eea77f74d68/orbax_checkpoint-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="95eaeee41ce8974080d5cfcc17d296234c6dc44cd10f9f10289fc3deaceeeaf4", url="https://pypi.org/packages/16/93/dd53bf35b6f736b65b64418b52649d1ae65e4ddb75d8db25eb1364a581a1/orbax_checkpoint-0.5.0-py3-none-any.whl")
    version("0.4.8", sha256="3440922fa1e92f8298a9543d3ae14cce08b2d006e2f1c9a0486dd317757c4ec8", url="https://pypi.org/packages/d6/df/7a6fb8df0882e4223a6fa1b114348386535ec3687ba55327da639a121b74/orbax_checkpoint-0.4.8-py3-none-any.whl")
    version("0.4.7", sha256="0dc4792ba35cdeafc6bd8730e8f121f70e91910b88879d654cf22890ce3abc37", url="https://pypi.org/packages/fe/2d/6f61d1ccc3d87996ed9c5086daf8b9926d8ad59c1b07b5ef23815e107861/orbax_checkpoint-0.4.7-py3-none-any.whl")
    version("0.4.6", sha256="0127428307cf667fb167af2c107e2452a532addd0befaeba6ac058856dd98dbb", url="https://pypi.org/packages/59/57/d6d15ea1d3362b40f443c397adcaf133818df302c80a40e80f85d97a0f16/orbax_checkpoint-0.4.6-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.2.4:")
        depends_on("py-absl-py", when="@0.1:")
        depends_on("py-etils+epath+epy", when="@0.2.7:")
        depends_on("py-flax", when="@0.1:0.1.1")
        depends_on("py-jax@0.4.9:", when="@0.2.3:")
        depends_on("py-jaxlib", when="@0.1:")
        depends_on("py-msgpack", when="@0.1.4:")
        depends_on("py-nest-asyncio", when="@0.1.6:")
        depends_on("py-numpy", when="@0.1:")
        depends_on("py-protobuf", when="@0.2.7:")
        depends_on("py-pyyaml", when="@0.1:")
        depends_on("py-tensorstore@0.1.51:", when="@0.4.5:")
        depends_on("py-typing-extensions", when="@0.1.4:")

