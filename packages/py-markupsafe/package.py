##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarkupsafe(PythonPackage):
    version("2.1.5", sha256="d283d37a890ba4c1ae73ffadf8046435c76e7bc2247bbb63c00bd1a709c6544b", url="https://pypi.org/packages/87/5b/aae44c6655f3801e81aa3eef09dbbf012431987ba564d7231722f68df02d/MarkupSafe-2.1.5.tar.gz")
    version("2.1.4", sha256="3aae9af4cac263007fd6309c64c6ab4506dd2b79382d9d19a1994f9240b8db4f", url="https://pypi.org/packages/fb/5a/fb1326fe32913e663c8e2d6bdf7cde6f472e51f9c21f0768d9b9080fe7c5/MarkupSafe-2.1.4.tar.gz")
    version("2.1.3", sha256="af598ed32d6ae86f1b747b82783958b1a4ab8f617b06fe68795c7f026abbdcad", url="https://pypi.org/packages/6d/7c/59a3248f411813f8ccba92a55feaac4bf360d29e2ff05ee7d8e1ef2d7dbf/MarkupSafe-2.1.3.tar.gz")
    version("2.1.2", sha256="abcabc8c2b26036d62d4c746381a6f7cf60aafcc653198ad678306986b09450d", url="https://pypi.org/packages/95/7e/68018b70268fb4a2a605e2be44ab7b4dd7ce7808adae6c5ef32e34f4b55a/MarkupSafe-2.1.2.tar.gz")
    version("2.1.1", sha256="7f91197cc9e48f989d12e4e6fbc46495c446636dfc81b9ccf50bb0ec74b91d4b", url="https://pypi.org/packages/1d/97/2288fe498044284f39ab8950703e88abbac2abbdf65524d576157af70556/MarkupSafe-2.1.1.tar.gz")
    version("2.1.0", sha256="80beaf63ddfbc64a0452b841d8036ca0611e049650e20afcb882f5d3c266d65f", url="https://pypi.org/packages/62/0f/52c009332fdadd484e898dc8f2acca0663c1031b3517070fd34ad9c1b64e/MarkupSafe-2.1.0.tar.gz")
    version("2.0.1", sha256="594c67807fb16238b30c44bdf74f36c02cdf22d1c8cda91ef8a0ed8dabf5620a", url="https://pypi.org/packages/bf/10/ff66fea6d1788c458663a84d88787bae15d45daa16f6b3ef33322a51fc7e/MarkupSafe-2.0.1.tar.gz")
    version("2.0.0", sha256="4fae0677f712ee090721d8b17f412f1cbceefbf0dc180fe91bab3232f38b4527", url="https://pypi.org/packages/67/6a/5b3ed5c122e20c33d2562df06faf895a6b91b0a6b96a4626440ffe1d5c8e/MarkupSafe-2.0.0.tar.gz")
    version("2.0.0-rc2", sha256="746a22773b02c79ea570cf97f92aad7e58938bcd2670de499e349d8430f989ef", url="https://pypi.org/packages/af/6a/84855224d2c1b5e4b66d8460505383a0719a36d9b65cfc031948ff5e1cef/MarkupSafe-2.0.0rc2.tar.gz")
    version("1.1.1", sha256="29872e92839765e546828bb7754a68c418d927cd064fd4708fab9fe9c8bb116b", url="https://pypi.org/packages/b9/2e/64db92e53b86efccfaea71321f597fa2e1b2bd3853d8ce658568f7a13094/MarkupSafe-1.1.1.tar.gz")
    version("1.1.0", sha256="4e97332c9ce444b0c2c38dd22ddc61c743eb208d916e4265a2a3b575bdccb1d3", url="https://pypi.org/packages/ac/7e/1b4c2e05809a4414ebce0892fe1e32c14ace86ca7d50c70f00979ca9b3a3/MarkupSafe-1.1.0.tar.gz")
    version("1.0", sha256="a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665", url="https://pypi.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz")
    version("0.23", sha256="a4ec1aff59b95a14b45eb2e23761a0179e98319da5a7eb76b56ea8cdc7b871c3", url="https://pypi.org/packages/c0/41/bae1254e0396c0cc8cf1751cb7d9afc90a602353695af5952530482c963f/MarkupSafe-0.23.tar.gz")
    version("0.22", sha256="7642852b6d1e55c9e12e00a552c0b8943880f2172e55141ccb41eb5f8675dfa5", url="https://pypi.org/packages/58/18/646cbd99909a0c86eb7b9c0277b88cb54f3e2619f6115f48199a4accde97/MarkupSafe-0.22.tar.gz")
    version("0.21", sha256="c6465cd6ed2b96509ef0100e7fff8718ed52c2affab1860ed5a9b67f604dd59a", url="https://pypi.org/packages/c6/33/963f57460372f8401e1f9aa32c8ed8f07a5cae0f11024f5ff1d4cb3576c8/MarkupSafe-0.21.tar.gz")
    version("0.20", sha256="f6cf3bd233f9ea6147b21c7c02cac24e5363570ce4fd6be11dab9f499ed6a7d8", url="https://pypi.org/packages/6f/c3/7adab2342dc7f14d32943505c9bd163d93a16fa117b8fee82e48f3529fb5/MarkupSafe-0.20.tar.gz")
    version("0.19", sha256="62fcc5d641df8b5ad271ebbd6b77a19cd92eceba1e1a990de4e96c867789f037", url="https://pypi.org/packages/8e/90/da092a12fb96e0c4cacc279d1f92819ae82bfa291e0a03afe8059518e91a/MarkupSafe-0.19.tar.gz")
    version("0.18", sha256="b7d5d688bdd345bfa897777d297756688cf02e1b3742c56885e2e5c2b996ff82", url="https://pypi.org/packages/98/cf/197c3b0f73224b84eb419a967f87565bcc0b0c1147012397e6bd2d45e253/MarkupSafe-0.18.tar.gz")
    version("0.17", sha256="bdda8df9395253d06af11ce33778aed4d5f297cb1d8cb380ab955c1a04bbb9d4", url="https://pypi.org/packages/04/d0/21c43bb0a9c9b31c8bfeb3676e12ec0aae2b71632497b6bd6505c980a38a/MarkupSafe-0.17.tar.gz")


