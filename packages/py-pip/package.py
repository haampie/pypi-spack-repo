# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPip(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("24.0", sha256="ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc", url="https://pypi.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl")
    version("23.3.2", sha256="5052d7889c1f9d05224cd41741acb7c5d6fa735ab34e339624a614eaaa7e7d76", url="https://pypi.org/packages/15/aa/3f4c7bcee2057a76562a5b33ecbd199be08cdb4443a02e26bd2c3cf6fc39/pip-23.3.2-py3-none-any.whl")
    version("23.3.1", sha256="55eb67bb6171d37447e82213be585b75fe2b12b359e993773aca4de9247a052b", url="https://pypi.org/packages/47/6a/453160888fab7c6a432a6e25f8afe6256d0d9f2cbd25971021da6491d899/pip-23.3.1-py3-none-any.whl")
    version("23.3", sha256="bc38bb52bc286514f8f7cb3a1ba5ed100b76aaef29b521d48574329331c5ae7b", url="https://pypi.org/packages/e0/63/b428aaca15fcd98c39b07ca7149e24bc14205ad0f1c80ba2b01835aedde1/pip-23.3-py3-none-any.whl")
    version("23.2.1", sha256="7ccf472345f20d35bdc9d1841ff5f313260c2c33fe417f48c30ac46cccabf5be", url="https://pypi.org/packages/50/c2/e06851e8cc28dcad7c155f4753da8833ac06a5c704c109313b8d5a62968a/pip-23.2.1-py3-none-any.whl")
    version("23.2", sha256="78e5353a9dda374b462f2054f83a7b63f3f065c98236a68361845c1b0ee7e35f", url="https://pypi.org/packages/02/65/f15431ddee78562355ccb39097bf9160a1689f2db40dc418754be98806a1/pip-23.2-py3-none-any.whl")
    version("23.1.2", sha256="3ef6ac33239e4027d9a5598a381b9d30880a1477e50039db2eac6e8a8f6d1b18", url="https://pypi.org/packages/08/e3/57d4c24a050aa0bcca46b2920bff40847db79535dc78141eb83581a52eb8/pip-23.1.2-py3-none-any.whl")
    version("23.1.1", sha256="3d8d72fa0714e93c9d3c2a0ede91e898c64596e0fa7d4523f72dd95728efc418", url="https://pypi.org/packages/f8/f8/17bd3f7c13515523d811ce4104410c16c03e3c6830f9276612e2f4b28382/pip-23.1.1-py3-none-any.whl")
    version("23.1", sha256="64b1d4528e491aa835ec6ece0c1ac40ce6ab6d886e60740f6519db44b2e9634d", url="https://pypi.org/packages/ae/db/a8821cdac455a1740580c92de3ed7b7f257cfdbad8b1ba8864e6abe58a08/pip-23.1-py3-none-any.whl")
    version("23.0.1", sha256="236bcb61156d76c4b8a05821b988c7b8c35bf0da28a4b614e8d6ab5212c25c6f", url="https://pypi.org/packages/07/51/2c0959c5adf988c44d9e1e0d940f5b074516ecc87e96b1af25f59de9ba38/pip-23.0.1-py3-none-any.whl")
    version("23.0", sha256="b5f88adff801f5ef052bcdef3daa31b55eb67b0fccd6d0106c206fa248e0463c", url="https://pypi.org/packages/ab/43/508c403c38eeaa5fc86516eb13bb470ce77601b6d2bbcdb16e26328d0a15/pip-23.0-py3-none-any.whl")
    version("22.3.1", sha256="908c78e6bc29b676ede1c4d57981d490cb892eb45cd8c214ab6298125119e077", url="https://pypi.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl")
    version("22.3", sha256="1daab4b8d3b97d1d763caeb01a4640a2250a0ea899e257b1e44b9eded91e15ab", url="https://pypi.org/packages/47/ef/8b5470b5b94b36231ed9c0bde90caa71c0d4322d4a15f009b2b7f4287fe0/pip-22.3-py3-none-any.whl")
    version("22.2.2", sha256="b61a374b5bc40a6e982426aede40c9b5a08ff20e640f5b56977f4f91fed1e39a", url="https://pypi.org/packages/1f/2c/d9626f045e7b49a6225c6b09257861f24da78f4e5f23af2ddbdf852c99b8/pip-22.2.2-py3-none-any.whl")
    version("22.2.1", sha256="0bbbc87dfbe6eed217beff0021f8b7dea04c8f4a0baa9d31dc4cff281ffc5b2b", url="https://pypi.org/packages/84/25/5734a44897751d8bac6822efb819acda2d969bcc1b915bbd7d48102952cb/pip-22.2.1-py3-none-any.whl")
    version("22.2", sha256="9abf423d5d64f3289ab9d5bf31da9e6234f2e9c5d8dcf1423bcb46b809a02c2c", url="https://pypi.org/packages/9b/9e/9e0610f25e65e2cdf90b1ee9c47ca710865401904038558ac0129ea23cbc/pip-22.2-py3-none-any.whl")
    version("22.1.2", sha256="a3edacb89022ef5258bf61852728bf866632a394da837ca49eb4303635835f17", url="https://pypi.org/packages/96/2f/caec18213f6a67852f6997fb0673ae08d2e93d1b81573edb93ba4ef06970/pip-22.1.2-py3-none-any.whl")
    version("22.1.1", sha256="e7bcf0b2cbdec2af84cc1b7b79b25fdbd7228fbdb61a4dca0b82810d0ba9d18b", url="https://pypi.org/packages/9b/e6/aa8149e048eda381f2a433599be9b1f5e5e3a189636cd6cf9614aa2ff5be/pip-22.1.1-py3-none-any.whl")
    version("22.1", sha256="802e797fb741be1c2d475533d4ea951957e4940091422bd4a24848a7ac95609d", url="https://pypi.org/packages/f3/77/23152f90de45957b59591c34dcb39b78194eb67d088d4f8799e9aa9726c4/pip-22.1-py3-none-any.whl")
    version("22.0.4", sha256="c6aca0f2f081363f689f041d90dab2a07a9a07fb840284db2218117a52da800b", url="https://pypi.org/packages/4d/16/0a14ca596f30316efd412a60bdfac02a7259bf8673d4d917dc60b9a21812/pip-22.0.4-py3-none-any.whl")
    version("22.0.3", sha256="c146f331f0805c77017c6bb9740cec4a49a0d4582d0c3cc8244b057f83eca359", url="https://pypi.org/packages/6a/df/a6ef77a6574781a668791419ffe366c8acd1c3cf4709d210cb53cd5ce1c2/pip-22.0.3-py3-none-any.whl")
    version("22.0.2", sha256="682eabc4716bfce606aca8dab488e9c7b58b0737e9001004eb858cdafcd8dbdd", url="https://pypi.org/packages/83/b5/df8640236faa5a3cb80bfafd68e9fb4b22578208b8398c032ccff803f9e0/pip-22.0.2-py3-none-any.whl")
    version("22.0.1", sha256="30739ac5fb973cfa4399b0afff0523d4fe6bed2f7a5229333f64d9c2ce0d1933", url="https://pypi.org/packages/89/a1/2f4e58eda11e591fbfa518233378835679fc5ab766b690b3df85215014d5/pip-22.0.1-py3-none-any.whl")
    version("22.0", sha256="6cb1ea2bd7fda0668e26ae8c3e45188f301a7ef17ff22efe1f70f3643e56a822", url="https://pypi.org/packages/9f/8b/a094f5da22d7abf5098205367b3296dd15b914f4232af5ca39ba6214d08c/pip-22.0-py3-none-any.whl")
    version("21.3.1", sha256="deaf32dcd9ab821e359cd8330786bcd077604b5c5730c0b096eda46f95c24a2d", url="https://pypi.org/packages/a4/6d/6463d49a933f547439d6b5b98b46af8742cc03ae83543e4d7688c2420f8b/pip-21.3.1-py3-none-any.whl")
    version("21.3", sha256="4a1de8f97884ecfc10b48fe61c234f7e7dcf4490a37217011ad9369d899ad5a6", url="https://pypi.org/packages/90/a9/1ea3a69a51dcc679724e3512fc2aa1668999eed59976f749134eb02229c8/pip-21.3-py3-none-any.whl")
    version("21.2.4", sha256="fa9ebb85d3fd607617c0c44aca302b1b45d87f9c2a1649b46c26167ca4296323", url="https://pypi.org/packages/ca/31/b88ef447d595963c01060998cb329251648acf4a067721b0452c45527eb8/pip-21.2.4-py3-none-any.whl")
    version("21.2.3", sha256="895df6014c2f02f9d278a8ad6e31cdfd312952b4a93c3068d0556964f4490057", url="https://pypi.org/packages/ca/bf/4133a0e05eac641ec270bbcef30512b5ad307d7838adb994acd652cc30e3/pip-21.2.3-py3-none-any.whl")
    version("21.2.2", sha256="b02a9d345f913e03fde2ed41896687cc1a2053c6adbe142ec03cff6b0827233d", url="https://pypi.org/packages/8a/d7/f505e91e2cdea53cfcf51f4ac478a8cd64fb0bc1042629cedde20d9a6a9b/pip-21.2.2-py3-none-any.whl")
    version("21.2.1", sha256="da0ac9d9032d1d7bac69e9e301778f77b8b6626b85203f99edd2b545434d90a7", url="https://pypi.org/packages/7c/02/9ab8b431aca1b46fcc1ac830a5870a28a12ba1abfa681904b1d2da876a86/pip-21.2.1-py3-none-any.whl")
    version("21.2", sha256="71f447dff669d8e2f72b880e3d7ddea2c85cfeba0d14f3307f66fc40ff755176", url="https://pypi.org/packages/03/0f/b125bfdd145c1d018d75ce87603e7e9ff2416e742c71b5ac7deba13ca699/pip-21.2-py3-none-any.whl")
    version("21.1.3", sha256="78cb760711fedc073246543801c84dc5377affead832e103ad0211f99303a204", url="https://pypi.org/packages/47/ca/f0d790b6e18b3a6f3bd5e80c2ee4edbb5807286c21cdd0862ca933f751dd/pip-21.1.3-py3-none-any.whl")
    version("21.1.2", sha256="f8ea1baa693b61c8ad1c1d8715e59ab2b93cd3c4769bacab84afcc4279e7a70e", url="https://pypi.org/packages/cd/82/04e9aaf603fdbaecb4323b9e723f13c92c245f6ab2902195c53987848c78/pip-21.1.2-py3-none-any.whl")
    version("21.1.1", sha256="11d095ed5c15265fc5c15cc40a45188675c239fb0f9913b673a33e54ff7d45f0", url="https://pypi.org/packages/cd/6f/43037c7bcc8bd8ba7c9074256b1a11596daa15555808ec748048c1507f08/pip-21.1.1-py3-none-any.whl")
    version("20.2.4", sha256="51f1c7514530bd5c145d8f13ed936ad6b8bfcb8cf74e10403d0890bc986f0033", url="https://pypi.org/packages/cb/28/91f26bd088ce8e22169032100d4260614fc3da435025ff389ef1d396a433/pip-20.2.4-py2.py3-none-any.whl")
    version("20.2.3", sha256="0f35d63b7245205f4060efe1982f5ea2196aa6e5b26c07669adcf800e2542026", url="https://pypi.org/packages/4e/5f/528232275f6509b1fff703c9280e58951a81abe24640905de621c9f81839/pip-20.2.3-py2.py3-none-any.whl")
    version("20.2.2", sha256="5244e51494f5d1dfbb89da492d4250cb07f9246644736d10ed6c45deb1a48500", url="https://pypi.org/packages/5a/4a/39400ff9b36e719bdf8f31c99fe1fa7842a42fa77432e584f707a5080063/pip-20.2.2-py2.py3-none-any.whl")
    version("20.2.1", sha256="7792c1a4f60fca3a9d674e7dee62c24e21a32df1f47d308524d3507455784f29", url="https://pypi.org/packages/bd/b1/56a834acdbe23b486dea16aaf4c27ed28eb292695b90d01dff96c96597de/pip-20.2.1-py2.py3-none-any.whl")
    version("20.2", sha256="d75f1fc98262dabf74656245c509213a5d0f52137e40e8f8ed5cc256ddd02923", url="https://pypi.org/packages/36/74/38c2410d688ac7b48afa07d413674afc1f903c1c1f854de51dc8eb2367a5/pip-20.2-py2.py3-none-any.whl")
    version("20.1.1", sha256="b27c4dedae8c41aa59108f2fa38bf78e0890e590545bc8ece7cdceb4ba60f6e4", url="https://pypi.org/packages/43/84/23ed6a1796480a6f1a2d38f2802901d078266bda38388954d01d3f2e821d/pip-20.1.1-py2.py3-none-any.whl")
    version("20.1", sha256="4fdc7fd2db7636777d28d2e1432e2876e30c2b790d461f135716577f73104369", url="https://pypi.org/packages/54/2e/df11ea7e23e7e761d484ed3740285a34e38548cf2bad2bed3dd5768ec8b9/pip-20.1-py2.py3-none-any.whl")
    version("20.0.2", sha256="4ae14a42d8adba3205ebeb38aa68cfc0b6c346e1ae2e699a0b3bad4da19cef5c", url="https://pypi.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl")
    version("20.0.1", sha256="b7110a319790ae17e8105ecd6fe07dbcc098a280c6d27b6dd7a20174927c24d7", url="https://pypi.org/packages/57/36/67f809c135c17ec9b8276466cc57f35b98c240f55c780689ea29fa32f512/pip-20.0.1-py2.py3-none-any.whl")
    version("20.0", sha256="eea07b449d969dbc8c062c157852cf8ed2ad1b8b5ac965a6b819e62929e41703", url="https://pypi.org/packages/60/65/16487a7c4e0f95bb3fc89c2e377be331fd496b7a9b08fd3077de7f3ae2cf/pip-20.0-py2.py3-none-any.whl")
    version("19.3.1", sha256="6917c65fc3769ecdc61405d3dfd97afdedd75808d200b2838d7d961cebc0c2c7", url="https://pypi.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl")
    version("19.3", sha256="e100a7eccf085f0720b4478d3bb838e1c179b1e128ec01c0403f84e86e0e2dfb", url="https://pypi.org/packages/4a/08/6ca123073af4ebc4c5488a5bc8a010ac57aa39ce4d3c8a931ad504de4185/pip-19.3-py2.py3-none-any.whl")
    version("19.2.3", sha256="340a0ba40fdeb16413914c0fcd8e0b4ebb0bf39a900ec80e11c05d836c05103f", url="https://pypi.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl")
    version("19.2.2", sha256="4b956bd8b7b481fc5fa222637ff6d0823a327e5118178f1ec47618a480e61997", url="https://pypi.org/packages/8d/07/f7d7ced2f97ca3098c16565efbe6b15fafcba53e8d9bdb431e09140514b0/pip-19.2.2-py2.py3-none-any.whl")
    version("19.2.1", sha256="80d7452630a67c1e7763b5f0a515690f2c1e9ad06dda48e0ae85b7fdf2f59d97", url="https://pypi.org/packages/62/ca/94d32a6516ed197a491d17d46595ce58a83cbb2fca280414e57cd86b84dc/pip-19.2.1-py2.py3-none-any.whl")
    version("19.2", sha256="468c67b0b1120cd0329dc72972cf0651310783a922e7609f3102bd5fb4acbf17", url="https://pypi.org/packages/3a/6f/35de4f49ae5c7fdb2b64097ab195020fb48faa8ad3a85386ece6953c11b1/pip-19.2-py2.py3-none-any.whl")
    version("19.1.1", sha256="993134f0475471b91452ca029d4390dc8f298ac63a712814f101cd1b6db46676", url="https://pypi.org/packages/5c/e0/be401c003291b56efc55aeba6a80ab790d3d4cece2778288d65323009420/pip-19.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

