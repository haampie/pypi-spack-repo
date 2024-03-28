# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCwlUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.32", sha256="5239ce4781e61c0b5c467593c10ffcb342dedd0a79e4c86c37b89b467129c333", url="https://pypi.org/packages/e3/cc/c0761ae4dab49d8fd263efaba8f79f66782357693e42500ea5d88213a72d/cwl_utils-0.32-py3-none-any.whl")
    version("0.31", sha256="f553631af66efb9336e34813a3720e20b3813c1fa6df7b8e5b6b2b147bba7018", url="https://pypi.org/packages/0d/80/adf19321a0216709b46d6d51299a0b1ed60473abdccdab3ee9bb690ec488/cwl_utils-0.31-py3-none-any.whl")
    version("0.30", sha256="4234dfd8025a3384ab9fefc8f336cb689952db89732d793820732d8599fa0f17", url="https://pypi.org/packages/59/fb/e722a3e5db90d6866991d59aa04e285446101c0cbb89015d7e3b3029f19e/cwl_utils-0.30-py3-none-any.whl")
    version("0.29", sha256="cb98cdccf3f4bf6779342a38d3ba050f45f8e5159f6a366e9a4699fd15bdafa2", url="https://pypi.org/packages/b6/40/59298d9ed5001b7277a237bbaadfc36637a91baa82caf62929667c8a439c/cwl_utils-0.29-py3-none-any.whl")
    version("0.28", sha256="eba865d46967fc9aecdcd694dd89b201892bfb6e1a25871540155d8a22aa1bfd", url="https://pypi.org/packages/3d/0c/1f8eb82826d7d4d75b70f7ecbecd1491611387aad4c2788a1835721b9871/cwl_utils-0.28-py3-none-any.whl")
    version("0.27", sha256="59c9d1da842257ebbeb22622e5c5e0c3f63287460dfd99a33d8478f500b46014", url="https://pypi.org/packages/96/bf/c392e704e82d598a5e402af3aab5455671a62bb654f19d559d28e5d88d41/cwl_utils-0.27-py3-none-any.whl")
    version("0.26", sha256="407ff08f1a988121ca15c35b75d840b8a92a006612bd0087133ec096f0515bb4", url="https://pypi.org/packages/71/37/c02b2c2543e4b64b3bc4eeb816d3b386b7f3aa0cf7fdd0a34fc766c73e71/cwl_utils-0.26-py3-none-any.whl")
    version("0.25", sha256="23b481e7e86e1db47b1ee6a19cf1d84125746416eb046f819d4f9934a43b447c", url="https://pypi.org/packages/d5/57/2808e0ba8d58d402e8ed05f59f7b7db4c4d7025ad061fa59ca3ad32ec178/cwl_utils-0.25-py3-none-any.whl")
    version("0.24", sha256="9a2cbff910d7eab69672858e005a677443dd66c2f2c7328a0f20a6b5dfd89467", url="https://pypi.org/packages/4e/14/e0e943f4fa20e9b165550dc24fe89f4e6397bc1ab8842c6049798f7bb000/cwl_utils-0.24-py3-none-any.whl")
    version("0.23", sha256="9cefce488e962403e7fe5b868ff8b809d58e919532acacfda349044570dc605d", url="https://pypi.org/packages/30/1d/19cb0563509131cff2885b4612bfa68d26fb430d66fa0e082db6bc679096/cwl_utils-0.23-py3-none-any.whl")
    version("0.21", sha256="fba9348bfef42e7d359f1a93e1188f1da40cce714532a3e49901343bae6b01a0", url="https://pypi.org/packages/03/15/a4156b82adf2a6f7575c3229adf1e523237786c25385151460dd8d2eb560/cwl_utils-0.21-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cachecontrol@:0.12", when="@0.26:0.27")
        depends_on("py-cachecontrol", when="@0.15:0.25")
        depends_on("py-cwl-upgrader@1.2.3:", when="@0.15:")
        depends_on("py-cwlformat", when="@0.8:0.12")
        depends_on("py-importlib-resources", when="@0.32: ^python@:3.8")
        depends_on("py-packaging", when="@0.14:")
        depends_on("py-rdflib", when="@0.15:")
        depends_on("py-requests", when="@0.2:0.3,0.8:")
        depends_on("py-ruamel-yaml@0.17.6:", when="@0.30:")
        depends_on("py-ruamel-yaml@0.17.6:0.17", when="@0.28:0.29")
        depends_on("py-ruamel-yaml@0.16.12:0.17", when="@0.28:0.29")
        depends_on("py-ruamel-yaml@0.17.6:0.17.26", when="@0.26:0.27")
        depends_on("py-ruamel-yaml@0.16.12:0.17.26", when="@0.26:0.27")
        depends_on("py-ruamel-yaml@0.17.6:0.17.22", when="@0.25")
        depends_on("py-ruamel-yaml@0.16.12:0.17.22", when="@0.25")
        depends_on("py-ruamel-yaml@0.17.6:0.17.21", when="@0.23:0.24")
        depends_on("py-ruamel-yaml@0.16.12:0.17.21", when="@0.23:0.24")
        depends_on("py-schema-salad@8.5:", when="@0.32:")
        depends_on("py-schema-salad@8.3.20220825114525:", when="@0.16:0.31")
        depends_on("py-urllib3@:1", when="@0.26:0.27")
    # END DEPENDENCIES

