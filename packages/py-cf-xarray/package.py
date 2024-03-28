# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCfXarray(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.0", sha256="338ae3e55138b6374f64a70844a1f0dac63811781c456b4c30878874b8b4c2c0", url="https://pypi.org/packages/fd/68/c563ac1b9646579e3b8d47c37442ddaeb46ea983025e348d21b358b20c20/cf_xarray-0.9.0-py3-none-any.whl")
    version("0.8.9", sha256="e6267926f388898a4298152cf173c095bb88774acb0b56b7c411e47f5510365b", url="https://pypi.org/packages/c5/54/051ddf40dc5734aea14d4f321e26701271aea7147fc5febca98be16cc9c1/cf_xarray-0.8.9-py3-none-any.whl")
    version("0.8.8", sha256="38f348cfa88658c43a8b02d850d20355b8b7f1cdd8b00bd07757621059f26adb", url="https://pypi.org/packages/6d/0f/3895d2d637f6e8d675935488b25c5eb1b83a2d6744642a6e3feddc8c86de/cf_xarray-0.8.8-py3-none-any.whl")
    version("0.8.7", sha256="c5e1a070c2d1735052ff35a18adfe52c933f3f2a2dc3a1c7d44cf7f89322502e", url="https://pypi.org/packages/a0/88/d0cefe2b9c9e1a393d50d03977a3babdf524b043c484da3e4cb28f052a4f/cf_xarray-0.8.7-py3-none-any.whl")
    version("0.8.6", sha256="17c311d0b52531e0067bb2dae1853b240b28b5abb1045214255a62dcbc7e1a02", url="https://pypi.org/packages/4f/e7/e50a1e1f2ee8a9a15ead579f786e2d172f3a6f57fc6050081ee39ce16497/cf_xarray-0.8.6-py3-none-any.whl")
    version("0.8.4", sha256="b441623146b316f99e7c43286163ba01d6cee0dfa0b44ee6d839a68dfd944ca5", url="https://pypi.org/packages/c7/3e/5f675f0387db29efc591ce8b54ac4b6fb38c4ac5dcfda7fd553ef028b5f7/cf_xarray-0.8.4-py3-none-any.whl")
    version("0.8.3", sha256="89e2a970751cdf5496d321b9c7ab3b634292e6540a691211a26b90736736c22e", url="https://pypi.org/packages/4d/00/454be73c8433fc8d27609fda2e7e95f0afa39e3d0c7a07d3be580dd91af2/cf_xarray-0.8.3-py3-none-any.whl")
    version("0.8.2", sha256="7218077605ed106fd9b27073bf0dd5c957ac8a193d388812af478cdc6de57524", url="https://pypi.org/packages/1c/2c/44676f81099b12933f9cb5a13e7e54c95b6af6b4b98e59c22b0280215ddc/cf_xarray-0.8.2-py3-none-any.whl")
    version("0.8.1", sha256="3e88c16a1021ee24a0f8fd076eacac53b37d6747a4b595c704db9ee7dafa7511", url="https://pypi.org/packages/48/c8/06ba167e6401fe7bb81235eccbbb3f721a3ec434a0ab501f1b616f756675/cf_xarray-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="a537d41b33bf96b67301ad86dfdc50a5a5f870af2bb465830d057a35ea32ba24", url="https://pypi.org/packages/5f/19/9567ce41758ad4f71855463bde367990adc665bbf25f2808ac4f32f4f832/cf_xarray-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.8.7:")
        depends_on("py-xarray", when="@0.6.3:")
    # END DEPENDENCIES

