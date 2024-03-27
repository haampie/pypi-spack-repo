##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRuamelYamlJinja2(PythonPackage):
    version("0.2.7", sha256="eb36abd4d308794e9a497e48f98cbd2b921d2cd2946bbc9f1bea42c9b142a241", url="https://pypi.org/packages/d0/ef/6281be4ef86a6a0e6f06004c2e4526de3d880f4eaf4210a07a269ad330b3/ruamel.yaml.jinja2-0.2.7-py2.py3-none-any.whl")
    version("0.2.6", sha256="a73594aea5bee73fffc17fe6aaf5a5e48261e6ac3f131f33658fe15e9e2f40f7", url="https://pypi.org/packages/98/96/5138d0a558a8b8bb97e1ff5cdb71e4f6d482f1ee5fa9da570d5729640998/ruamel.yaml.jinja2-0.2.6-py2.py3-none-any.whl")
    version("0.2.5", sha256="22f2ef5f8cca0171fa9e7973e2dda783a727073f6475029e6c42ae3a6ebea211", url="https://pypi.org/packages/16/49/df4f01d6a20eea63b069d8530390f1756a380e2a9a3f49892d8dded809d2/ruamel.yaml.jinja2-0.2.5-py2.py3-none-any.whl")
    version("0.2.4", sha256="cd2fd8278cb00206e605ab5ae146e25b7541e75d914adb88932a811a404fd86e", url="https://pypi.org/packages/7c/9e/578e51d4dbdbbd28d54dbd0f561370d1d955d46228749d531dde6d15a2f2/ruamel.yaml.jinja2-0.2.4-py2.py3-none-any.whl")
    version("0.2.3", sha256="f0a079fdf412982a03138180bf159e799b7c790be12cf918ea06bc27a8aef32e", url="https://pypi.org/packages/e8/9d/a9a2098ba051aac312e5f44d6006c3dbac9ce9bc0f86617371a6200b657d/ruamel.yaml.jinja2-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="b921f6b4df560121803a981e2e763df4a628a2b3617dcb525878fdc40152ea0b", url="https://pypi.org/packages/4f/b4/9676d4fa53d921f98f40dcda2ecfdb9fba2b68fbdccec3d9d4d2c87d96a7/ruamel.yaml.jinja2-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="e5ee41855843506cacc7866b96b1596db4ea5607c442a438ae926ceb79f52c27", url="https://pypi.org/packages/e8/06/6bbbe8113714de069a6be8c66e6c0bffe4014612f5989851178dc51a2947/ruamel.yaml.jinja2-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="43d6016b6a67f235e2ec07327bd9464dc699898591ed950c72e3b83d535772d2", url="https://pypi.org/packages/ef/7e/249ae9c7371dfe03a9f5f4943d6391cdb745ea8145d5ea8e57e0c44277f7/ruamel.yaml.jinja2-0.2.0.tar.gz")
    version("0.1.3", sha256="7d6dacb8e450c66f22313f0001397ff5d1fd0db1c8af0e8520d135ed004018cb", url="https://pypi.org/packages/b4/5d/c2339d0381d1c67c53f301644557546ef2f24c2ec56eb1eb7ac60fda614b/ruamel.yaml.jinja2-0.1.3.tar.gz")
    version("0.1.2", sha256="c67045fa76a98a36b9ef070cce4b43c5fd9459cf03808211008417a765c2717e", url="https://pypi.org/packages/ae/f3/d7811f2395c1f654ebed780de84fe8a29afa30949f9217a3f9947a525db5/ruamel.yaml.jinja2-0.1.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-ruamel-yaml@0.16.1:", when="@0.2.5:")
        depends_on("py-ruamel-yaml@0.15.10:", when="@0.2:0.2.2")

