# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBidsValidator(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.14.5.dev0", sha256="8657fe39fc885aba852b9316f1ff7e25627fd180083e3af03dd03b3fe3c7f01d", url="https://pypi.org/packages/13/ec/1872ad05c88992f1626e414f3fe8fffad1e9a5e783ecd753222781414055/bids_validator-1.14.5.dev0-py3-none-any.whl")
    version("1.14.4", sha256="162da51e10567ee18c38f56ff46b065ca03b38a4603e98f3aa47310b2e8009dc", url="https://pypi.org/packages/2b/a4/190b9948491bd7cfdc99ea4da07a9ca1f24bc2881321600159f7decdbe84/bids_validator-1.14.4-py3-none-any.whl")
    version("1.14.4.dev0", sha256="a712bf1766ab9d5156602e87637f0d0fbee4324d9f62752ad8aeff8259798d79", url="https://pypi.org/packages/31/3d/acba1e541643f6fb47c20855a8f5893c230fa5bf79498d8a23d6ae09e50f/bids_validator-1.14.4.dev0-py3-none-any.whl")
    version("1.14.3", sha256="67ad3f3e2719ee32c11b7e9700234f81de303969c1109d695c7ccab590a6c134", url="https://pypi.org/packages/42/bd/fcc6ba17eb54b7d2470e6dcd51e4f7bdad0217c37106a9670500300e010e/bids_validator-1.14.3-py3-none-any.whl")
    version("1.14.1", sha256="ed08d7d4ea474cacc3d9957be1afa35d4c3161ec767612ac863859265d2c991c", url="https://pypi.org/packages/ed/db/2c6ee9c83d3dd5163aea4d2a43e9a45fb4dc4a87af6ceb7edd2c72a8d332/bids_validator-1.14.1-py3-none-any.whl")
    version("1.14.0", sha256="bab89f97a8d833235562cf0f3ac981bfca71acf2793a6c12a8af631c29ee0b8f", url="https://pypi.org/packages/85/e6/d9eb19e48328c1ca4cbbbe7ab27207519558e1dbbf6f26f4f643b429b1d0/bids_validator-1.14.0-py3-none-any.whl")
    version("1.13.1", sha256="da6edf5e76ef86c8a63b3fcee1dbfb039a16a9ef63cb0d2d05312c200d4607f7", url="https://pypi.org/packages/f4/a1/248c9394ab59679fd35ac2a4b7d4adec2be55ad5e3b1cf5b12b791918338/bids_validator-1.13.1-py2.py3-none-any.whl")
    version("1.13.0", sha256="bd60dd734e647b5214696f52b3a7eb9cb1876bc2329cf1494202cfc8ae0f54a4", url="https://pypi.org/packages/ad/e9/00e8f6562d25972ecaa15128690692a52abe3533c46ce0d48393c600f08a/bids_validator-1.13.0-py2.py3-none-any.whl")
    version("1.12.0", sha256="7936e9f31960cfbfe9af49b33e8d10999d7497d7fcd313d91ea3eda541ae4500", url="https://pypi.org/packages/4f/6b/7c22873d76d4dbe4b70f42541d3262e93593bd4e508af308662ea5e5f5bc/bids_validator-1.12.0-py2.py3-none-any.whl")
    version("1.11.0", sha256="d2fd8943510453eb2f9fed28fba8e063f280a7bbed8152880783631fd4109f1a", url="https://pypi.org/packages/87/9e/722ca2a2dcacedb8133bec1d226ed62ba775c628c108d20f774002fea767/bids_validator-1.11.0-py2.py3-none-any.whl")
    version("1.10.0", sha256="576fdc401c64a0bc2ec5d8f161112f21fcda40608cfbc9fa4dcd9d849635ab7a", url="https://pypi.org/packages/9f/bd/0a92e9b6043024c1b4007a299dcea5d3791e276062b201a6692b51045630/bids_validator-1.10.0-py2.py3-none-any.whl")
    version("1.9.9", sha256="15188762c6708374f93f2108eb0d7ff115b5edcfea39f0417e52044a292a12e1", url="https://pypi.org/packages/a0/12/173899034bfdebbf004d18d6bf69ad372f549c312a7a2ab122d9d66e069e/bids_validator-1.9.9-py2.py3-none-any.whl")
    version("1.9.8", sha256="8bc1b74bf6dbc277826b60bed6818e70b0fda3ae944c146ff6907a7a1e079b05", url="https://pypi.org/packages/36/55/0f47886b11ee2b7e154d0163814dde6a77b4611bad070deb1a25ca8e0dd2/bids_validator-1.9.8-py2.py3-none-any.whl")
    version("1.9.4", sha256="5bee401d55fb039ac1dd9b97f326c6a538f1d25789abc00d5d2b3350c757756b", url="https://pypi.org/packages/86/39/c50befdf65a28cf8e69efddeb6622fd1f10f436ce28a157d2025d96a270b/bids_validator-1.9.4-py2.py3-none-any.whl")
    version("1.8.9", sha256="b2def483d9d88b9240e44e340687159d7561d6a0eb6ca52afed47becc49582bb", url="https://pypi.org/packages/ab/7e/ac413b12f659c714118b7132ac760fb8e951a55133e42d140def278a9b5f/bids_validator-1.8.9-py2.py3-none-any.whl")
    version("1.8.4", sha256="ce6de214e48051300a738aaf7226b5585c4268646ee890c491ee011e7415fbbf", url="https://pypi.org/packages/89/3b/cdb1ba8648636a897c9108c36ebb4c2d5dab01443693dea27d06a6cefe19/bids_validator-1.8.4-py2.py3-none-any.whl")
    version("1.7.2", sha256="854f56177a4b93cbf2202947b0821646a5af629bbefe796d8114bcad6de9559e", url="https://pypi.org/packages/26/d3/49a2c0ed2af7560baac349befde5f80df61b415cc7c0d577a85ab3142e3f/bids_validator-1.7.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

