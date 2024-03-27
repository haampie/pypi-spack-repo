##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDill(PythonPackage):
    version("0.3.8", sha256="c36ca9ffb54365bdd2f8eb3eff7d2a21237f8452b57ace88b1ac615b7e815bd7", url="https://pypi.org/packages/c9/7a/cef76fd8438a42f96db64ddaa85280485a9c395e7df3db8158cfec1eee34/dill-0.3.8-py3-none-any.whl")
    version("0.3.7", sha256="76b122c08ef4ce2eedcd4d1abd8e641114bfc6c2867f49f3c41facf65bf19f5e", url="https://pypi.org/packages/f5/3a/74a29b11cf2cdfcd6ba89c0cecd70b37cd1ba7b77978ce611eb7a146a832/dill-0.3.7-py3-none-any.whl")
    version("0.3.6", sha256="a07ffd2351b8c678dfc4a856a3005f8067aea51d6ba6c700796a4d9e280f39f0", url="https://pypi.org/packages/be/e3/a84bf2e561beed15813080d693b4b27573262433fced9c1d1fea59e60553/dill-0.3.6-py3-none-any.whl")
    version("0.3.5.1", sha256="33501d03270bbe410c72639b350e941882a8b0fd55357580fbc873fba0c59302", url="https://pypi.org/packages/12/ff/3b1a8f5d59600393506c64fa14d13afdfe6fe79ed65a18d64026fe9f8356/dill-0.3.5.1-py2.py3-none-any.whl")
    version("0.3.5", sha256="6eb4bb70a98509e69204e621942c4306580d5bf2229f450f04fcf2efca3908e5", url="https://pypi.org/packages/f1/54/a2df4c5f6181cc4a03387dfac03357a88625515aeecbaa7ec928b9736794/dill-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="7e40e4a70304fd9ceab3535d36e58791d9c4a776b38ec7f7ec9afc8d3dca4d4f", url="https://pypi.org/packages/b6/c3/973676ceb86b60835bb3978c6db67a5dc06be6cfdbd14ef0f5a13e3fc9fd/dill-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="78370261be6ea49037ace8c17e0b7dd06d0393af6513cc23f9b222d9367ce389", url="https://pypi.org/packages/52/d6/79f40d230895fa1ce3b6af0d22e0ac79c65175dc069c194b79cc8e05a033/dill-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="6e12da0d8e49c220e8d6e97ee8882002e624f1160289ce85ec2cc0a5246b3a2e", url="https://pypi.org/packages/e2/96/518a8ea959a734b70d2e95fef98bcbfdc7adad1c1e5f5dd9148c835205a5/dill-0.3.2.zip")
    version("0.3.1.1", sha256="42d8ef819367516592a825746a18073ced42ca169ab1f5f4044134703e7a049c", url="https://pypi.org/packages/c7/11/345f3173809cea7f1a193bfbf02403fff250a3360e0e118a1630985e547d/dill-0.3.1.1.tar.gz")
    version("0.3.1.dev0", sha256="d3ddddf2806a7bc9858b20c02dc174396795545e9d62f243b34481fd26eb3e2c", url="https://pypi.org/packages/3e/ad/31932a4e2804897e6fd2f946d53df51dd9b4aa55e152b5404395d00354d1/dill-0.3.1.tar.gz")
    version("0.3.0", sha256="993409439ebf7f7902d9de93eaa2a395e0446ff773d29f13dc46646482f76906", url="https://pypi.org/packages/39/7a/70803635c850e351257029089d38748516a280864c97cbc73087afef6d51/dill-0.3.0.tar.gz")
    version("0.2.9", sha256="f6d6046f9f9195206063dd0415dff185ad593d6ee8b0e67f12597c0f4df4986f", url="https://pypi.org/packages/fe/42/bfe2e0857bc284cbe6a011d93f2a9ad58a22cb894461b199ae72cfef0f29/dill-0.2.9.tar.gz")
    version("0.2.8.2", sha256="624dc244b94371bb2d6e7f40084228a2edfff02373fe20e018bef1ee92fdd5b3", url="https://pypi.org/packages/6f/78/8b96476f4ae426db71c6e86a8e6a81407f015b34547e442291cd397b18f3/dill-0.2.8.2.tar.gz")
    version("0.2.7", sha256="ddda0107e68e4eb1772a9f434f62a513c080c7171bd0dd6fb65d992788509812", url="https://pypi.org/packages/8f/41/c995c721bd57340b7d84fc644eeb5605791e5ee73a899d58131731eba7e0/dill-0.2.7.tar.gz")
    version("0.2.6", sha256="6c1ccca68be483fa8c66e85a89ffc850206c26373aa77a97b83d8d0994e7f1fd", url="https://pypi.org/packages/ef/69/0d03d5f9af0e16d41bb47262100b0c4c08f90538c9a5c2de0d44284172ba/dill-0.2.6.zip")
    version("0.2.5", sha256="e82b3db7b9d962911c9c2d5cf2bb4a04f43933f505a624fb7dc5f68b949f0a5c", url="https://pypi.org/packages/e9/c9/4ceb72351dd929f5b50d7586b34721efb177fad67114f312ac4d768af4a1/dill-0.2.5.zip")
    version("0.2.4", sha256="db68929eef0e886055d6bcd86f830141c1f653ddbf5d081c086e9d1c45efb334", url="https://pypi.org/packages/ea/c0/3e20aa1bcdd0c73106ca8ca188cdbdeb43f7cabffbf162b540697156c6ca/dill-0.2.4.zip")
    version("0.2.3", sha256="2b98942466b7841c26562a7ebfbf4a15a6026347b5c3edc0a2e57387416f1c86", url="https://pypi.org/packages/85/6a/64e2c6da064f2c30e19c478580db1da3060266f5279886df22f559e793a2/dill-0.2.3.tgz")
    version("0.2.2", sha256="6ad223cc41614dcc8cf217e8d7a32857f13752cd0a5332580c80b9fa054ece69", url="https://pypi.org/packages/f0/a6/6f96502f293e9b126d87dcc18e85283f865664fe89eb0df804f05f1fc1ed/dill-0.2.2.zip")
    version("0.2.1", sha256="a54401bdfae419cfe1c9e0b48e9b290afccaa413d2319d9bb0fdb85c130a7923", url="https://pypi.org/packages/51/76/14048a72ccea086e80621d39b1519fb3219f9c2354ac8481d2a0a027543e/dill-0.2.1.zip")
    version("0.2", sha256="aba8d4c81c4136310e6ce333bd6f4f3ea2d53bd367e2f69c864428f260c0308c", url="https://pypi.org/packages/47/69/9e1312d761d1017363b644864c0e61b741326b220ab7ed8924d8c1937ae8/dill-0.2.zip")


