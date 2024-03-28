# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRq(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.16.1", sha256="273de33f10bb9f18cd1e8ccc0a4e8dba2b8eb86a6ab2a91ae674f99bd68025f1", url="https://pypi.org/packages/7d/77/622e350bc73bbc9d50c725742b35968d4be6629f0e058ef450ae5e0d817a/rq-1.16.1-py3-none-any.whl")
    version("1.16.0", sha256="d71859da6f3af597bd79675b240e138587878ce9b693d1bcf681443e2a8193ce", url="https://pypi.org/packages/84/62/9a6b14d4a724607f740cc4b3d132c52af24e753fe2a958d0b8c9d6d24e0a/rq-1.16.0-py3-none-any.whl")
    version("1.15.1", sha256="6e243d8d9c4af4686ded4b01b25ea1ff4bac4fc260b02638fbe9c8c17b004bd1", url="https://pypi.org/packages/e1/24/5ae8bfcea4f24b32e079da421015ad380eadfc8250892a2470b6f19df0d8/rq-1.15.1-py2.py3-none-any.whl")
    version("1.15.0", sha256="6bdc8885bf839a246c4b4e02f2ee31d8f840061fced200f13df9a58a582ec04a", url="https://pypi.org/packages/7c/cd/00d034628960820b5604fb402f060a3905011a3a50605a7f738301ef4108/rq-1.15.0-py2.py3-none-any.whl")
    version("1.14.1", sha256="37e003db1da205e08db6cc4653b7c6ccfd9292000954240308abfce2ebde43ba", url="https://pypi.org/packages/74/7f/2e44ef5bb1607f55d2aac60d19fe1f02c1638aa4dbd0d498f84c04603a14/rq-1.14.1-py2.py3-none-any.whl")
    version("1.14.0", sha256="dc2c54f4f56e637b056f0ff5859c0e4b4baec657a08c57cee86ebe84bbf984ce", url="https://pypi.org/packages/e5/ca/cdd6889c8ccfc1787fdbd036a82a0759d166083ea9fb38bfd458d8818d87/rq-1.14.0-py2.py3-none-any.whl")
    version("1.13.0", sha256="621966d7cbf96d5609557a4bd3fd77f749d6d10997d2e353a3e89a14e08eea16", url="https://pypi.org/packages/7d/70/8a9a07e450b42765023fb77b322dca8cd64ae30005f3deeb6d5e75bfa445/rq-1.13.0-py2.py3-none-any.whl")
    version("1.12.0", sha256="b268947a94a1da7de3c5f3925a59db60bffdede782ca1f23da654bf985a83c7a", url="https://pypi.org/packages/17/67/632a700649da413902a5a7ddfe92459812c7d598dea34e695b1c5bf43bb4/rq-1.12.0-py2.py3-none-any.whl")
    version("1.11.1", sha256="433882bde50ac462eb489dc1ffa476209c42b284d0031270631da26363923702", url="https://pypi.org/packages/30/5f/b771ee633258bc73c21e4836efe68bb8343c5a147432f687ed774c8a9554/rq-1.11.1-py2.py3-none-any.whl")
    version("1.11.0", sha256="c0bbf898b56817da053cdc992ab46da2729a7ccd70dd50316ad9209b7d7b71c1", url="https://pypi.org/packages/45/20/db8ed899a5646cab11ce56ae86707db8d89b244d0fdeceae85bb883ae870/rq-1.11.0-py2.py3-none-any.whl")
    version("1.5.2", sha256="6e32a39d467ffc56fc18f0f0f10abd6aa258895dbac03af31e38fe0c2337aab8", url="https://pypi.org/packages/31/9b/e24f0814474f315d9bc78f60fc65253d1682d74363df61a49c18e6f862c8/rq-1.5.2-py2.py3-none-any.whl")
    version("1.5.1", sha256="4d8268e0d541d8016cbb915befd30fc68f1c3a9e77a8cfc02de3e6f22a5314d9", url="https://pypi.org/packages/76/1f/8f60388a11fc939b005d7bf18fcda34fac7eb3dc64db4b66b2fe9e3a9bc2/rq-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="3da8554f3ea2ee9e48d54063ebe1437c6aa743483c1f46d2ad65294ab4e38873", url="https://pypi.org/packages/e0/66/eeb4a9528107af5664abb4a971a47a53b74bf90b8e55803258f5ba4ddb29/rq-1.5.0-py2.py3-none-any.whl")
    version("1.4.3", sha256="ee7fb24bc84dba87446264ca7162b2ed7d6d6af3cbd68f0b6b220ce7c23c8ae8", url="https://pypi.org/packages/21/0d/f70cc2d0c2f21a01bb5d6bb1705025c781927aa1be3bcb650a3795d70b4f/rq-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="ef61f4517a1dc499b57bc0fa9e8a8f1c561e1f72abab936dbe9081a4508f8874", url="https://pypi.org/packages/e8/a3/caa4ceeb0bab04cd554868cb67ae892daa14cc1c97d6f58863f975304f53/rq-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="e6d82156eb43a8fffe451099a716114f5f163ec7603b6e8c8dab16a1b31f4547", url="https://pypi.org/packages/7b/7e/4b066e02e0916b3b12f5c77810301724180c612457413eb862d7692d4243/rq-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="c88623cd7528fad8620ee7a2d793493b85b63855f74a2da28c14671bab34a161", url="https://pypi.org/packages/41/bf/f67d9235c5d69f65932b40450416847ab3963f339dc790503254a440db50/rq-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="c3e65a8ba5e59287308f23679f7fe729b9380531e4f6cdabb2dee99b82834811", url="https://pypi.org/packages/50/d5/5956980ef7151855892003e9fd8e525b4982b261867a53caa597158aa29d/rq-1.3.0-py2.py3-none-any.whl")
    version("1.2.2", sha256="cc1505c9b122435d40ba36afd5d9b462be2438fa8742c02645359f909068f03c", url="https://pypi.org/packages/8d/a7/cd204520bffb1841af7438a45c9cb7127c6e71b4c34c6ab0387531cbd3ab/rq-1.2.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="a0fb79f6dc2592968583af8ab9f558f92aedea60ec6013bf3b3901d4e5827c24", url="https://pypi.org/packages/0d/33/77e67eb90dd6ac785269623b9f20af32da55318578a68d28f27e00422fdf/rq-1.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@5:", when="@0.13:")
        depends_on("py-redis@4.0.0:", when="@1.15")
        depends_on("py-redis@3.5:", when="@1.5:1.14,1.16:")
        depends_on("py-redis@3:", when="@0.13:1.4")
    # END DEPENDENCIES

