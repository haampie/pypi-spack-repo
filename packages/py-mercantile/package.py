# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMercantile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="30f457a73ee88261aab787b7069d85961a5703bb09dc57a170190bc042cd023f", url="https://pypi.org/packages/b2/d6/de0cc74f8d36976aeca0dd2e9cbf711882ff8e177495115fd82459afdc4d/mercantile-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="9b0ca248a459efdc1263e9baee8040b3559a636d97050a86c9f59077af718241", url="https://pypi.org/packages/cc/76/8f67751784ccf54d1bf4fc04639e7c7667ee0764fb1eff003767aae502ad/mercantile-1.2.0-py3-none-any.whl")
    version("1.1.6", sha256="20895bcee8cb346f384d8a1161fde4773f5b2aa937d90a23aebde766a0d1a536", url="https://pypi.org/packages/b9/cd/ee6dbee0abca93edda53703fe408d2a6abdc8c1b248a3c9a4539089eafa2/mercantile-1.1.6-py3-none-any.whl")
    version("1.1.5", sha256="3dac4e6c4105a73caeb1d170bc3256a9cb6b0f78e0a5d5a2e76d162b980579ae", url="https://pypi.org/packages/8c/f0/fb498613ac49ffbe3f3d3691a5592b6de3eb6c270fa8a03d296fa67eada4/mercantile-1.1.5-py3-none-any.whl")
    version("1.1.4", sha256="f6713dd64511fda3ee3aed001122fdeb6dc1e36fc19df4772759764cfb674c35", url="https://pypi.org/packages/85/68/bc926fe7ff3bbf7b21c00f18e9b803cb828600f35cc5b5b6db1a4fc28d23/mercantile-1.1.4-py3-none-any.whl")
    version("1.1.3", sha256="3e327771ac661a2f52fc38005efe93afd558bbdb1108c6fc274d7570309a17a9", url="https://pypi.org/packages/9d/21/54fe0d6f5f75ecf8f9d907a85944266af6be3689376b1fd0d0aea3aa300c/mercantile-1.1.3-py3-none-any.whl")
    version("1.1.2", sha256="6ef7301b8f5b29f622b97f5ab2c43edfa2e1c3857b96adbfc6eac9ec376abe0e", url="https://pypi.org/packages/9d/1d/80d28ba17e4647bf820e8d5f485d58f9da9c5ca424450489eb49e325ba66/mercantile-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="98132989070b576a794d54db7f9037c8b7741ceccd93e6e3bc78b3b378ede4e2", url="https://pypi.org/packages/f8/d4/f79431df2ea725206e845d06980a2eb7f4264aa6a7cc749647dd6233d6fa/mercantile-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="a68973d956b55f67add404e1dcb3ae72e81666c2f9f6b123f53393ecd8feb977", url="https://pypi.org/packages/8a/41/36f786e23ca6db86f51e07725f52641576526e84055899cee75cbedf5d38/mercantile-1.1.0-py3-none-any.whl")
    version("1.0.4", sha256="db13b7d674a38ea69673898e96f6c6b33e3fd41ccbbfe8ba54860d427fa7d492", url="https://pypi.org/packages/1d/9d/1bec2ab2df26fee5db91bacbc021a8933ad0a7d0281fa867d181ae09ea3c/mercantile-1.0.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@3:", when="@0.8.3:")
    # END DEPENDENCIES

