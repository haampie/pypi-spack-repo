##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBluepyefe(PythonPackage):
    version("2.3.15", sha256="7a6d902764baea203471317ebb7a3039305c6cc72ee90c6bc278d86b13054c6b", url="https://pypi.org/packages/9b/bf/f7d004bedd1ed5764412bdfbc3539956c8e2401d0b12a68ab283b007f2e6/bluepyefe-2.3.15-py3-none-any.whl")
    version("2.3.14", sha256="1f1b7e0160361b2443e066a209935d3a6d3adcb450e2dfdb3715a8c6849e3aa7", url="https://pypi.org/packages/94/8c/adde1b35dd82142281c684e8d61b452da05535ee9a6d1811ee31981c16d2/bluepyefe-2.3.14-py3-none-any.whl")
    version("2.3.13", sha256="c9fccc3325398d03bfa1dab1eab66c7fa283f771f2c574af05848d71784f6888", url="https://pypi.org/packages/23/1a/e30999878512e3ab776eb945e8b1f98ec828a743245853257b606fb16f8f/bluepyefe-2.3.13-py3-none-any.whl")
    version("2.3.12", sha256="cc03f3970e9cabbf8a2980bbe68d541be5f0bed8da9fd6f1784d0bc61c839319", url="https://pypi.org/packages/8f/c7/7c4cee9ae42e491a409747d90885d99760d00b0bbdd20462ed2c4cb32d83/bluepyefe-2.3.12-py3-none-any.whl")
    version("2.3.11", sha256="d341f61aba139c68e17d5c112dab8af1a9a349d115dbc1000f85d7aa619dc50d", url="https://pypi.org/packages/94/be/3ace228ec8ff45a014d94add0aa18f39dfb74f0b76838a9adb681c7a137b/bluepyefe-2.3.11-py3-none-any.whl")
    version("2.3.10", sha256="d7ab8479928b1b052b6de3d20d54324c9ffe6e9124a569e430d59f4006b62693", url="https://pypi.org/packages/38/75/3dec00d476b80e8111ae09adae200937b565346525ed812cb35c595122b0/bluepyefe-2.3.10-py3-none-any.whl")
    version("2.3.9", sha256="1bf0844f4e8559f07e2c22ff88c4a909c8653a324f1ded10b04d8cba44658f50", url="https://pypi.org/packages/5a/05/c78a52e76f0bdbb6301098414f2898bc4725b298f247e8e89fda485e14c4/bluepyefe-2.3.9-py3-none-any.whl")
    version("2.3.8", sha256="bee2925318548bbfae7ea8d69c6b23761e0db19aa4b2f50628a83bdb4109d469", url="https://pypi.org/packages/18/a8/58422dba595d4b92825e9f2a73a6a578fb80bb4d357736815cca6cabb364/bluepyefe-2.3.8-py3-none-any.whl")
    version("2.3.7", sha256="72a541a4b124b7975b6f589c025edf5c8bdfb923045192d367592948fffbd69f", url="https://pypi.org/packages/81/2f/f3b18d73c814c1d7a0ecb7d1abf4bb240b5f148a0becd93fe516caf1585f/bluepyefe-2.3.7-py3-none-any.whl")
    version("2.3.6", sha256="3b49fe8306910bb0a1f537a6bb0e145e61211f12796427fdd1d02858040a6ff9", url="https://pypi.org/packages/2e/da/39a31517235c7370b098c3635623b0653366daf609a77dcad3dd2765aef8/bluepyefe-2.3.6-py3-none-any.whl")
    version("2.2.18", sha256="9b5ceee89c9b94bfe39bb116afae93a0fb2952d4579c45b15fbbd3cb8c845a06", url="https://pypi.org/packages/be/05/cd88b95bdacababe014740bfb8983bfc554ef6719b4609190fbf7b29a9f7/bluepyefe-2.2.18-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-efel", when="@0.3.123:0,2.1.26:")
        depends_on("py-h5py", when="@2.1.26:")
        depends_on("py-igor", when="@0.3.123:0,2.1.26:2.2.25")
        depends_on("py-igor2", when="@2.2.30:")
        depends_on("py-matplotlib", when="@0.3.123:0,2.1.26:")
        depends_on("py-neo", when="@0.3.123:0,2.1.26:")
        depends_on("py-numpy@:1.23", when="@2.2.11:2.2.25")
        depends_on("py-numpy", when="@0.4.7:0,2.1.26:2.2.2,2.2.30:")
        depends_on("py-scipy", when="@0.3.123:0,2.1.26:")

