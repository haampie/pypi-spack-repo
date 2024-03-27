##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyasn1(PythonPackage):
    version("0.5.1", sha256="4439847c58d40b1d0a573d07e3856e95333f1976294494c325775aeca506eb58", url="https://pypi.org/packages/d1/75/4686d2872bf2fc0b37917cbc8bbf0dd3a5cdb0990799be1b9cbf1e1eb733/pyasn1-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="87a2121042a1ac9358cabcaf1d07680ff97ee6404333bacca15f76aa8ad01a57", url="https://pypi.org/packages/14/e5/b56a725cbde139aa960c26a1a3ca4d4af437282e20b5314ee6a3501e7dfc/pyasn1-0.5.0-py2.py3-none-any.whl")
    version("0.5.0-rc2", sha256="760db2dafe04091b000af018c45dff6e3d7a204cd9341b760d72689217a611cc", url="https://pypi.org/packages/8b/92/fdf998c5bc9d0f4a9e8aec6f52d30331bc93473f239669e790accf4f1a92/pyasn1-0.5.0rc2-py2.py3-none-any.whl")
    version("0.5.0-rc1", sha256="8106f14b6a54088ac4f94faca2996fa3dfc5a0e602b3b3a17001f57446fe6a6c", url="https://pypi.org/packages/b7/2a/3bc29f4de889beac9adcc166da5ba35c4c9bbe3e0e5ba645d868d398444d/pyasn1-0.5.0rc1-py2.py3-none-any.whl")
    version("0.4.8", sha256="39c7e2ec30515947ff4e87fb6f456dfc6e84857d34be479c9d4a4ba4bf46aa5d", url="https://pypi.org/packages/62/1e/a94a8d635fa3ce4cfc7f506003548d0a2447ae76fd5ca53932970fe3053f/pyasn1-0.4.8-py2.py3-none-any.whl")
    version("0.4.7", sha256="62cdade8b5530f0b185e09855dd422bc05c0bbff6b72ff61381c09dac7befd8c", url="https://pypi.org/packages/a1/71/8f0d444e3a74e5640a3d5d967c1c6b015da9c655f35b2d308a55d907a517/pyasn1-0.4.7-py2.py3-none-any.whl")
    version("0.4.6", sha256="3bb81821d47b17146049e7574ab4bf1e315eb7aead30efe5d6a9ca422c9710be", url="https://pypi.org/packages/6a/6e/209351ec34b7d7807342e2bb6ff8a96eef1fd5dcac13bdbadf065c2bb55c/pyasn1-0.4.6-py2.py3-none-any.whl")
    version("0.4.5", sha256="da6b43a8c9ae93bc80e2739efb38cc776ba74a886e3e9318d65fe81a8b8a2c6e", url="https://pypi.org/packages/7b/7c/c9386b82a25115cccf1903441bba3cbadcfae7b678a20167347fa8ded34c/pyasn1-0.4.5-py2.py3-none-any.whl")
    version("0.4.4", sha256="b9d3abc5031e61927c82d4d96c1cec1e55676c1a991623cfed28faea73cdd7ca", url="https://pypi.org/packages/d1/a1/7790cc85db38daa874f6a2e6308131b9953feb1367f2ae2d1123bb93a9f5/pyasn1-0.4.4-py2.py3-none-any.whl")
    version("0.4.3", sha256="a66dcda18dbf6e4663bde70eb30af3fc4fe1acb2d14c4867a861681887a5f9a2", url="https://pypi.org/packages/a0/70/2c27740f08e477499ce19eefe05dbcae6f19fdc49e9e82ce4768be0643b9/pyasn1-0.4.3-py2.py3-none-any.whl")
    version("0.4.2", sha256="d5cd6ed995dba16fad0c521cfe31cd2d68400b53fcc2bce93326829be73ab6d1", url="https://pypi.org/packages/ba/fe/02e3e2ee243966b143657fb8bd6bc97595841163b6d8c26820944acaec4d/pyasn1-0.4.2-py2.py3-none-any.whl")
    version("0.4.1", sha256="49cabfbf30df3ccd1a3c4b162b2b4a041d5bf809543c460e525eb31c25510092", url="https://pypi.org/packages/ab/ce/fadac5d6cace1b5c5c14c2f1e2aa3956a40cb9d5a1acbb049b4d3235a68c/pyasn1-0.4.1-py2.py3-none-any.whl")
    version("0.3.7", sha256="16e896433f84575f0636cd9aa8b24659689268a62e00f17235e1fc23c6b00b25", url="https://pypi.org/packages/31/fd/08e985cb75c39157cd066b709298c8d027c54a790bf9b265097c5444c336/pyasn1-0.3.7-py2.py3-none-any.whl")
    version("0.3.6", sha256="06afc633971ab80943f06b96d3d6314f461001c92418fc0cd682a8357a1db47f", url="https://pypi.org/packages/bf/56/47712763865a8639e6634e80405f6c758d4415620725896f412c464705f0/pyasn1-0.3.6-py2.py3-none-any.whl")
    version("0.3.5", sha256="90a6dfe991beb1f6240bc19e9fda02f513517523e3b96474a0887a94022dbad0", url="https://pypi.org/packages/f7/f4/2c140464fc9e715535a8e0696518492ec8ca58e76cc7947a67f808e52ec6/pyasn1-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="2eed483375bb3b90b7cf8556ba5dae861ce3d4a9d81a6ed784ce30041b505588", url="https://pypi.org/packages/b8/26/9e3e2b4792a7f362e97d49d08739abdfbdc692c69c0dcbf5504c9933c6cb/pyasn1-0.3.4-py2.py3-none-any.whl")
    version("0.2.3", sha256="738c4ebd88a718e700ee35c8d129acce2286542daa80a82823a7073644f706ad", url="https://pypi.org/packages/69/17/eec927b7604d2663fef82204578a0056e11e0fc08d485fdb3b6199d9b590/pyasn1-0.2.3.tar.gz")


