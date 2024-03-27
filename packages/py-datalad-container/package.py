##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladContainer(PythonPackage):
    version("1.2.5", sha256="b4b0f34d87bdbf783b996b09244615de1cbf55166aa978574f544d83bcb81ca2", url="https://pypi.org/packages/4b/a5/e6999cb129d9581674eefd4579e7d318a1aee32c1032586c7314f71cf799/datalad_container-1.2.5-py3-none-any.whl")
    version("1.2.4", sha256="c7a76f79fa7a00ab31c39712d2f7a900d11217d501f0857f28c82f26bcc61d48", url="https://pypi.org/packages/08/fa/7bbd0e32595b05904d24dd0c040105dff86db510a50c27276d2d2cf159df/datalad_container-1.2.4-py3-none-any.whl")
    version("1.2.3", sha256="f3f74f2c50d6cf160004fd06e23bcb381d928bebd21886811d1f64929f4ec7ad", url="https://pypi.org/packages/d3/b8/c92d8dda7643f06f8761753c76cf779d92b855d0a721dbd8ad435f154d2c/datalad_container-1.2.3-py3-none-any.whl")
    version("1.2.2", sha256="c5b98be947b8c536c4f82b2f18db98ad375fdd6463a5731f844fc6e9cb8b66dd", url="https://pypi.org/packages/f1/63/afe0c6aea47e1aed4acbb37ef0738cc9d144fe2667a8254412f000e5d48a/datalad_container-1.2.2-py3-none-any.whl")
    version("1.2.1", sha256="b2ae218a5df27c3ee76f2a3d4e831f20f884cb84beb997a18a82c991968ccaa1", url="https://pypi.org/packages/96/3e/d54b1afbc40195002f7a2f0e72264630a56d8bfd7c17fc81009addecb1c5/datalad_container-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="c42e1f0b475dae866f82545e6f39ef2e45572d05a1341aa7e6ff8135935e3863", url="https://pypi.org/packages/d6/f3/3f9f50fba9d9c4f37ef2effb7f22d44014aedc7f480582934a3c6d78d8c3/datalad_container-1.2.0-py3-none-any.whl")
    version("1.1.9", sha256="8f06b38c528008711241e5f9bfd7c705bf471418ca1612be369a729b3dac7398", url="https://pypi.org/packages/a4/5c/f5410fe70bb093f71bde6eb5a53b338e4bd10d15f0ea93641694379f975b/datalad_container-1.1.9-py3-none-any.whl")
    version("1.1.8", sha256="130cce1f2545421ab10beae25555d45c6e165d7dea7a2431b6198893acc0f468", url="https://pypi.org/packages/30/40/62057ae1fa447e423f5468e60b2b964cdd80e81c52234cddcbdb1b8e5392/datalad_container-1.1.8-py3-none-any.whl")
    version("1.1.7", sha256="0a628b21ad1145ba3512eee2d8cf49196a1dce344a6f35782a44b1eb7f9fa588", url="https://pypi.org/packages/1c/24/bf1e49b6bde41e09d6c5cb951c4540c21b2cef3075431f00f32a05b43845/datalad_container-1.1.7-py3-none-any.whl")
    version("1.1.6", sha256="a70b6525d8a82d295e8836018d01f2113e551f8fb0b5455ef301126b91821b8b", url="https://pypi.org/packages/d4/ef/cb1549f6adc7103c2da502b02a82c60aa2c93e8ad6566410b17dbd6dbbc9/datalad_container-1.1.6-py3-none-any.whl")
    version("1.1.5", sha256="5b4f40edb781c95f7bf91091894bb73b920531dabb7e5a3b9b79ee118b6097cb", url="https://pypi.org/packages/a2/7f/e615773bd6a1a54ab3ec868d3eefe2f3ce841b04278fe7e44333875b698c/datalad_container-1.1.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-datalad@0.18:", when="@1.1.9:")
        depends_on("py-datalad@0.13.0:", when="@1.1:1.1.8")
        depends_on("py-requests@1.2:", when="@0.1.1:0.3,0.5.1:0,1.0.1:")

