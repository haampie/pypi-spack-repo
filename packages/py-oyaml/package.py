# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOyaml(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0", sha256="3a378747b7fb2425533d1ce41962d6921cda075d46bb480a158d45242d156323", url="https://pypi.org/packages/37/aa/111610d8bf5b1bb7a295a048fc648cec346347a8b0be5881defd2d1b4a52/oyaml-1.0-py2.py3-none-any.whl")
    version("0.9", sha256="968d64dfa3ec1e0698f1b90f409f2993c2ef34f9def1ca5e785c4a2ef3bcfb07", url="https://pypi.org/packages/00/37/ec89398d3163f8f63d892328730e04b3a10927e3780af25baf1ec74f880f/oyaml-0.9-py2.py3-none-any.whl")
    version("0.8", sha256="35cc21a936ee3b4a835cbf1c3289ee80e2483cf7f5b631003328118d603bf4f2", url="https://pypi.org/packages/d3/a4/8e4eb583e536dd990c6ad43a93dcb8192f0c1783fb07a6865bb0c6d9c4fe/oyaml-0.8-py2.py3-none-any.whl")
    version("0.7", sha256="1a81fbb1d5c3158bf6410577f11daf2b741a1b4eea2a47064e7ecd1fb2699425", url="https://pypi.org/packages/7c/31/fb610d5c7a84f7100a31287726f10b6de532b2fc6d72ec89214c0736c5bf/oyaml-0.7-py2.py3-none-any.whl")
    version("0.6", sha256="ec80395be512dbb28c6c7ea6e5d1bd34f9a94abdb8a4bfc3baf42c0c8fd07484", url="https://pypi.org/packages/1e/4e/f7a58da232e2e51b96490cdb8be237e633bf9efc6e6c5139a1d49c528bff/oyaml-0.6-py2.py3-none-any.whl")
    version("0.5", sha256="5f0072546a46ae2c77c03406838d55015646f4025ac99b78f5c05801727ad220", url="https://pypi.org/packages/d7/18/89b8898d1878a8dda9ff9e8219bb9756c959712a1324800fc4df9d641dd1/oyaml-0.5-py2.py3-none-any.whl")
    version("0.4", sha256="5888517bbf3408dd1900a2591b165c24605bc608318f4e4492a12ea2e4cc401c", url="https://pypi.org/packages/bf/94/0fc809082a3bfea7c7e63917ad01c3cc4954413d3ed642e3c24d18852478/oyaml-0.4-py2.py3-none-any.whl")
    version("0.3", sha256="f4c12a7c05f173b864902deb9ed1d076024d7753e59b4ed6cbb10078ed450e52", url="https://pypi.org/packages/7b/ef/43cf84b69bb361b3d00c8df8ec4301ddce54e9be0123fab2af3fd369127d/oyaml-0.3-py2.py3-none-any.whl")
    version("0.2", sha256="37a229934d2b0291bf1d1cd064bc121cdc99350265f4228d1adf0cd755250d2e", url="https://pypi.org/packages/09/88/00207d707fd4bcdf7a11070580b707e8a7f76457eba7fe1656c3f6680720/oyaml-0.2-py2.py3-none-any.whl")
    version("0.1", sha256="bd788d05fcc0c6233b47ed2c0f331918080feb082c68e8b2501fc5c5be3860dd", url="https://pypi.org/packages/99/60/5182b3769eae1140c36910c98972269773109d415735390120bfb5945ba1/oyaml-0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml")
    # END DEPENDENCIES

