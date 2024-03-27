##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnnexremote(PythonPackage):
    version("1.6.4", sha256="74fdf4d4e20fd3b5a5bc827b4c488dd5de95cb8161cda77ad06a6b5fbd22e82b", url="https://pypi.org/packages/e4/6d/94c47068d57ff648fe1b4cc284fec65c7151ee2b8eb15e61927e1035cab2/annexremote-1.6.4-py3-none-any.whl")
    version("1.6.3", sha256="9ed441bbaad1d3f42a800e4aef156241ddce4358966bf9aaf496738352a1acb2", url="https://pypi.org/packages/d5/84/70e2084a1cef470237766f070c1fa57f298666b6cf18240301b322606525/annexremote-1.6.3-py3-none-any.whl")
    version("1.6.0", sha256="bc5bd2e456d64679e33d71226705673ac213040f8ae495467e9629b550c2ca53", url="https://pypi.org/packages/66/81/32d0563cd017cca305a8b8883abb177880cedde1385213a6b4b33cc07e45/annexremote-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="5aa99e37036c84547cc1f39eb3f99bf4079f1e5de1272b147e8dd32c0e14884f", url="https://pypi.org/packages/cd/9c/ced3458fcd0bb048350b7048412f6fa732ca7c44f6389d68c15e96e8b216/annexremote-1.5.0-py3-none-any.whl")
    version("1.4.5", sha256="6dd5f9a4945c48aa982fcfec4191dd127a5107fd9d617b061ed73b48d6745218", url="https://pypi.org/packages/ca/e9/db208cd34c0082885cc32a02fa985b9ae4b7633d32ad2ba40ce266fa7819/annexremote-1.4.5-py3-none-any.whl")
    version("1.4.4", sha256="1bd482effe9a340796cdec074bdf5422e963859537fad033c5d64e19435e52e9", url="https://pypi.org/packages/3e/7b/ac604e4faff0fede0cc7e9a02b3e47fd58ea207bf0c11b0f7af5ffe3475e/annexremote-1.4.4-py3-none-any.whl")
    version("1.4.3", sha256="8fab823c3a6588fa35b5bc72870ddb260799b36ccf9715911e8dd7abfca7382a", url="https://pypi.org/packages/c0/22/47448eede5882a4b4caa31da3957693fc97faa07438f57df5f72b6487120/annexremote-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="c7382c81d51149717f6c4520524f41ba4c4ac911978ebb9c871ee83f98a871c9", url="https://pypi.org/packages/61/21/99ce15c8976cb7a988c993909a62bf8f243440f8a3014ef1ae8ef4cf53aa/annexremote-1.4.2-py3-none-any.whl")
    version("1.3.1", sha256="3265cebfa07bad3357d1abccab74b68c46d1ec6d025d22e506716397f334d2d8", url="https://pypi.org/packages/e4/67/ae5821eae1d79524e1dcd1b4bf0338398ffb15f2ec4af79d731b0bfddadb/annexremote-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="8228a3d80310ca3aa0a75313402658d06c2169a9c9538a7ed93116b2e4cbce10", url="https://pypi.org/packages/0c/8e/96cc871200bab00ce4f84d631ce323c72cc6538d5fd330695b063f599a7c/annexremote-1.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-future", when="@1.3:1.5")

