# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBoto3(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.34.72", sha256="a33585ef0d811ee0dffd92a96108344997a3059262c57349be0761d7885f6ae7", url="https://pypi.org/packages/12/88/86ae378d3db210eb91a6d02c31f52690bf11510665dd9519d960024c0359/boto3-1.34.72-py3-none-any.whl")
    version("1.34.71", sha256="7ce8c9a50af2f8a159a0dd86b40011d8dfdaba35005a118e51cd3ac72dc630f1", url="https://pypi.org/packages/b1/f1/657850c7ac20e3b6566ede060a2db967b1f29f245e2cbb3cf16de889852e/boto3-1.34.71-py3-none-any.whl")
    version("1.34.70", sha256="8d7902e2c0c62837457ba18146e3feaf1dec62018617edc5c0336b65b305b682", url="https://pypi.org/packages/2a/2c/4b87fe046ad059c7ede17fa402a0658d131e31413d12942c6d3c72d60805/boto3-1.34.70-py3-none-any.whl")
    version("1.34.69", sha256="2e25ef6bd325217c2da329829478be063155897d8d3b29f31f7f23ab548519b1", url="https://pypi.org/packages/a1/f3/a6626ed248468ab33b2f68cc98f9cb0f40beab0803af382e6c52c5545a45/boto3-1.34.69-py3-none-any.whl")
    version("1.34.68", sha256="14f1e23b3f83ec365628a6ef849f1038b4c7338c4fabff159007c711b8147efc", url="https://pypi.org/packages/f0/4c/3e89092c83de6ccf94b6f74088f8ba54acaa701ff78b31855daab9d9ffbc/boto3-1.34.68-py3-none-any.whl")
    version("1.34.67", sha256="473febdf2606cf36f14c470dc3ff1b986efac15f69e37eb0fd728d42749065dd", url="https://pypi.org/packages/07/7f/94b3dde3263222874ce7b132aea2f4fb5c4ae75c3d6bef8bef5a24a378de/boto3-1.34.67-py3-none-any.whl")
    version("1.34.66", sha256="036989117c0bc4029daaa4cf713c4ff8c227b3eac6ef0e2118eb4098c114080e", url="https://pypi.org/packages/b5/65/7b4a2f86342261d1208c3c3cdff3acf0206ccb8a0e25ad8756141ad1bff7/boto3-1.34.66-py3-none-any.whl")
    version("1.34.65", sha256="b611de58ab28940a36c77d7ef9823427ebf25d5ee8277b802f9979b14e780534", url="https://pypi.org/packages/c8/a6/04b1cd7f38cbe781ef0d55f7459ee3ebb44771982cde3575ba4963bb24bf/boto3-1.34.65-py3-none-any.whl")
    version("1.34.64", sha256="8c6fbd3d45399a4e4685010117fb2dc52fc6afdab5a9460957d463ae0c2cc55d", url="https://pypi.org/packages/26/fb/b89de0e5e585e6fdecbf93fe1e05df8582d558cd92f8e3162fa88277fd78/boto3-1.34.64-py3-none-any.whl")
    version("1.34.63", sha256="617174f9051b564a57fb1079186ad15db6519ab3bb0d1fb22cb54767b0c4f46e", url="https://pypi.org/packages/a3/09/225d978bbe08b3c7b916732dbd7c65c03d4d89d47ea04df7fc0d149738fd/boto3-1.34.63-py3-none-any.whl")
    version("1.34.44", sha256="40f89fb2acee0a0879effe81badffcd801a348e715483227223241ae311c48fc", url="https://pypi.org/packages/15/1e/cbec55e05c0577429945d785cce8e16eebf2a8bd9c5ccda2b9c6e2a51ab4/boto3-1.34.44-py3-none-any.whl")
    version("1.26.26", sha256="b1d2521bd2239c4d2d8ee2a79d932bc64bf4779521ecc60c1074ae8a5d88adaa", url="https://pypi.org/packages/dc/cb/11560a590526f6049389bdfb5a993c4abc11eb20c12448d922909ac641fb/boto3-1.26.26-py3-none-any.whl")
    version("1.25.5", sha256="17ce7b6b702f9e844a33ce3ce9612f09d9d73eb7d34aaeffc77353ec036a9615", url="https://pypi.org/packages/29/17/8dd2d2c231cdfed1b24e31e49c628b8490c2846fe3116ced9d2fa73de0aa/boto3-1.25.5-py3-none-any.whl")
    version("1.24.96", sha256="748c055214c629744c34c7f94bfa888733dfac0b92e1daef9c243e1391ea4f53", url="https://pypi.org/packages/e2/53/e9c9f18f97f1565d9194c0ebbfb8bd9bd4bbb93a54569d2e7af256980511/boto3-1.24.96-py3-none-any.whl")
    version("1.23.10", sha256="40d08614f17a69075e175c02c5d5aab69a6153fd50e40fa7057b913ac7bf40e7", url="https://pypi.org/packages/75/ca/d917b244919f1ebf96f7bbd5a00e4641f7e9191b0d070258f5dc10f5eaad/boto3-1.23.10-py3-none-any.whl")
    version("1.22.13", sha256="240931d41341f30d3cc0bba72ede4dbfe9704721bf13ca19bcd31a435c235f8d", url="https://pypi.org/packages/e6/9a/0ea77f98a6018ae5a4fcb7fe74dd9369060dbedf2984612249007f08a834/boto3-1.22.13-py3-none-any.whl")
    version("1.21.46", sha256="3b13d727854aba9dea900b6c7fa134c52396869d842460d14fab8b85b69645f7", url="https://pypi.org/packages/f0/58/911753da74405a538cd81f2f51521a9c8ec0d927d0cfecdf9f58b7363e02/boto3-1.21.46-py3-none-any.whl")
    version("1.20.54", sha256="1a272a1dd36414b1626a47bb580425203be0b5a34caa117f38a5e18adf21f918", url="https://pypi.org/packages/f7/d7/7ccb6daf350f9b81550e3f2e25ba24672ea45975ee08f0cbca0a573417c0/boto3-1.20.54-py3-none-any.whl")
    version("1.19.12", sha256="b9105554477978e80fda1103ff21ecf07502080667730e45383e1d3951c87954", url="https://pypi.org/packages/5e/e1/156846b09fca21b9b164c54200011e3bd17f29187cbfc6903a8e0281a304/boto3-1.19.12-py3-none-any.whl")
    version("1.18.65", sha256="bbbc3a71949af31c33101ee0daf4db9b11148d67a4e574b6c66cbe35d985b5af", url="https://pypi.org/packages/73/42/9f0173f83f8c2717ce102cf98e5668a1858a21eadd28a235e9b3b0824fa4/boto3-1.18.65-py3-none-any.whl")
    version("1.18.12", sha256="e5abbb2b5ebe5ad1157a3af8f28c5c944e9c6eff0dd3e778008894e018bc7e09", url="https://pypi.org/packages/9d/28/cdb684f0afb4ab3880b5da31ee18aac3990c57ae81bf1345aab8f1afacec/boto3-1.18.12-py3-none-any.whl")
    version("1.17.112", sha256="8716465313c50ad9e5c2ac1767642ca0ddf7d1729c3d5c884d82880c1a15a310", url="https://pypi.org/packages/5a/fd/d814f9cbefebbea88977628d11b860b5d564ba6f16f64c378e2da2a36405/boto3-1.17.112-py2.py3-none-any.whl")
    version("1.17.27", sha256="6758751f1181b9363e4e7559dcbd5ac0fc7147b73f429c976ec5ecd1688c9ec7", url="https://pypi.org/packages/7b/3c/92634ca0da72db047a4957bdd3984d72fbcc82fb9dcda04ea628c9a87dba/boto3-1.17.27-py2.py3-none-any.whl")
    version("1.10.50", sha256="aa58c8de6aed36211e0897598de2a3d89122ad8cd1450165679720180ab880ef", url="https://pypi.org/packages/43/a6/433564e7b241ecb012c67e6580e302ecdc79c8b5189e3f7efb6e7b0fde45/boto3-1.10.50-py2.py3-none-any.whl")
    version("1.10.44", sha256="3728506de1be9a3fe0ddc7849abf5d47f768eca68a958303739ad040b5d5f92d", url="https://pypi.org/packages/b5/27/d2fce3e49c992b180e7340dd41ed1f098f2b0370f4a0e17d36a76b32a23a/boto3-1.10.44-py2.py3-none-any.whl")
    version("1.10.38", sha256="d64ec82b5125d8f8cae00f92d33a338c6c55cb5984967cfc7f4c52cf138126c4", url="https://pypi.org/packages/2e/b4/e8fb59efd68d4889528cb0d4227484b5aa511b765d81e05d2cd7d9bb3ca5/boto3-1.10.38-py2.py3-none-any.whl")
    version("1.9.253", sha256="839285fbd6f3ab16170af449ae9e33d0eccf97ca22de17d9ff68b8da2310ea06", url="https://pypi.org/packages/f6/fa/6397049020b312f71c397fff8d10247c2e49da760e2807af7d21e3c23695/boto3-1.9.253-py2.py3-none-any.whl")
    version("1.9.169", sha256="58ae308e4539264754e4e2a21bfec71b2fbffe02e86a77e680077e10b7c0ed54", url="https://pypi.org/packages/a6/1f/b272ead5ccc5370717f3c65ebd5092feab90e748db041bd96c565e7d1a72/boto3-1.9.169-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-botocore@1.34.72:", when="@1.34.72:")
        depends_on("py-botocore@1.34.71:", when="@1.34.71")
        depends_on("py-botocore@1.34.70:", when="@1.34.70")
        depends_on("py-botocore@1.34.69:", when="@1.34.69")
        depends_on("py-botocore@1.34.68:", when="@1.34.68")
        depends_on("py-botocore@1.34.67:", when="@1.34.67")
        depends_on("py-botocore@1.34.66:", when="@1.34.66")
        depends_on("py-botocore@1.34.65:", when="@1.34.65")
        depends_on("py-botocore@1.34.64:", when="@1.34.64")
        depends_on("py-botocore@1.34.63:", when="@1.34.63")
        depends_on("py-botocore@1.34.44:", when="@1.34.44")
        depends_on("py-botocore@1.29.26:1.29", when="@1.26.26")
        depends_on("py-botocore@1.28.5:1.28", when="@1.25.5:1.25")
        depends_on("py-botocore@1.27.96:1.27", when="@1.24.96:1.24")
        depends_on("py-botocore@1.26.10:1.26", when="@1.23.10:1.23")
        depends_on("py-botocore@1.25.13:1.25", when="@1.22.13:1.22")
        depends_on("py-botocore@1.24.46:1.24", when="@1.21.46:1.21")
        depends_on("py-botocore@1.23.54:1.23", when="@1.20.54:1.20")
        depends_on("py-botocore@1.22.12:1.22", when="@1.19.12:1.19")
        depends_on("py-botocore@1.21.65:1.21", when="@1.18.65:1.18")
        depends_on("py-botocore@1.21.12:1.21", when="@1.18.12")
        depends_on("py-botocore@1.20.112:1.20", when="@1.17.112:1.17")
        depends_on("py-botocore@1.20.27:1.20", when="@1.17.27")
        depends_on("py-jmespath@0.7.1:", when="@1.21.21:")
        depends_on("py-jmespath@0.7.1:0", when="@1.14.25:1.21.20")
        depends_on("py-s3transfer@0.10:", when="@1.34.6:")
        depends_on("py-s3transfer@0.6", when="@1.24:1.28.54")
        depends_on("py-s3transfer@0.5", when="@1.18:1.23")
        depends_on("py-s3transfer@0.4", when="@1.17.54:1.17")
        depends_on("py-s3transfer@0.3", when="@1.14.25:1.17.53")
    # END DEPENDENCIES

