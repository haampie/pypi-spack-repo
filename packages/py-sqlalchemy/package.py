# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlalchemy(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.29", sha256="bd9566b8e58cabd700bc367b60e90d9349cd16f0984973f98a9a09f9c64e86f0", url="https://pypi.org/packages/99/04/59971bfc2f192e3b52376ca8d1e134c78d04bc044ef7e04cf10c42d2ce17/SQLAlchemy-2.0.29.tar.gz")
    version("2.0.28", sha256="dd53b6c4e6d960600fd6532b79ee28e2da489322fcf6648738134587faf767b6", url="https://pypi.org/packages/3a/23/cc8844d4873ec0485f961c047ca831040c3ba7ecf9d88ec6f9249e1d1cbe/SQLAlchemy-2.0.28.tar.gz")
    version("2.0.27", sha256="86a6ed69a71fe6b88bf9331594fa390a2adda4a49b5c06f98e47bf0d392534f8", url="https://pypi.org/packages/b9/fc/327f0072d1f5231d61c715ad52cb7819ec60f0ac80dc1e507bc338919caa/SQLAlchemy-2.0.27.tar.gz")
    version("2.0.26", sha256="e1bcd8fcb30305e27355d553608c2c229d3e589fb7ff406da7d7e5d50fa14d0d", url="https://pypi.org/packages/e6/6b/c0a06092d1d33a704653bb824381e8a3117d2e55e4d67b82eaea0646106d/SQLAlchemy-2.0.26.tar.gz")
    version("2.0.25", sha256="a2c69a7664fb2d54b8682dd774c3b54f67f84fa123cf84dda2a5f40dcaa04e08", url="https://pypi.org/packages/7b/bb/85bd8e211f54983e927c7cd9b2ad66773fbef507957156fc72e481a62681/SQLAlchemy-2.0.25.tar.gz")
    version("2.0.24", sha256="6db97656fd3fe3f7e5b077f12fa6adb5feb6e0b567a3e99f47ecf5f7ea0a09e3", url="https://pypi.org/packages/14/72/dd7a1062a9eb723a0c767e151386be92f0cf825317b864e6d5a7c0e60628/SQLAlchemy-2.0.24.tar.gz")
    version("2.0.23", sha256="c1bda93cbbe4aa2aa0aa8655c5aeda505cd219ff3e8da91d1d329e143e4aff69", url="https://pypi.org/packages/ee/46/a3196db7ffd2609c7935798730e21bed8806d9bf4401921587dac4be0747/SQLAlchemy-2.0.23.tar.gz")
    version("2.0.22", sha256="5434cc601aa17570d79e5377f5fd45ff92f9379e2abed0be5e8c2fba8d353d2b", url="https://pypi.org/packages/ae/e2/47f40dc06472df5a906dd8eb9fe4ee2eb1c6b109c43545708f922b406acc/SQLAlchemy-2.0.22.tar.gz")
    version("2.0.21", sha256="05b971ab1ac2994a14c56b35eaaa91f86ba080e9ad481b20d99d77f381bb6258", url="https://pypi.org/packages/fa/fd/f835dcfb49eabf12e8ea7c7779d364f7730a47912ae64ff38cd4a316ab77/SQLAlchemy-2.0.21.tar.gz")
    version("2.0.20", sha256="ca8a5ff2aa7f3ade6c498aaafce25b1eaeabe4e42b73e25519183e4566a16fc6", url="https://pypi.org/packages/88/85/b7fbadd64b30e9d4b882dd323341fc263687bc95b22edec262b12cac8fd7/SQLAlchemy-2.0.20.tar.gz")
    version("2.0.19", sha256="77a14fa20264af73ddcdb1e2b9c5a829b8cc6b8304d0f093271980e36c200a3f", url="https://pypi.org/packages/e5/07/a928d473438adb98ebd2264f584c4bd2dd711dfe6caf4b1906cba14dd375/SQLAlchemy-2.0.19.tar.gz")
    version("1.4.52", sha256="80e63bbdc5217dad3485059bdf6f65a7d43f33c8bde619df5c220edf03d87296", url="https://pypi.org/packages/8a/a4/b5991829c34af0505e0f2b1ccf9588d1ba90f2d984ee208c90c985f1265a/SQLAlchemy-1.4.52.tar.gz")
    version("1.4.51", sha256="e7908c2025eb18394e32d65dd02d2e37e17d733cdbe7d78231c2b6d7eb20cdb9", url="https://pypi.org/packages/c8/56/5a8dcb01ef7b68904f2a3224343d4ab3674b5cc8f48f7cefb0701bc75ab8/SQLAlchemy-1.4.51.tar.gz")
    version("1.4.50", sha256="3b97ddf509fc21e10b09403b5219b06c5b558b27fc2453150274fa4e70707dbf", url="https://pypi.org/packages/5a/0a/dabe332c40afebb0a979d3e66b34570fce2f8611bae19b186f0c69f54643/SQLAlchemy-1.4.50.tar.gz")
    version("1.4.49", sha256="06ff25cbae30c396c4b7737464f2a7fc37a67b7da409993b182b024cec80aed9", url="https://pypi.org/packages/27/7c/ab28273996e8e5b78ddaeddbc1df54033231ff325827b3149d51334ed852/SQLAlchemy-1.4.49.tar.gz")
    version("1.4.48", sha256="b47bc287096d989a0838ce96f7d8e966914a24da877ed41a7531d44b55cdb8df", url="https://pypi.org/packages/b9/7a/6f075e189257f2b70cca85b6f3afeb7ca9cef80f0869e9f43b3e3eadd66d/SQLAlchemy-1.4.48.tar.gz")
    version("1.4.47", sha256="95fc02f7fc1f3199aaa47a8a757437134cf618e9d994c84effd53f530c38586f", url="https://pypi.org/packages/a0/08/3e8923b1094b61736960dc372633b0dfddbf2e12f5a0b8dd1203f7dcc8f7/SQLAlchemy-1.4.47.tar.gz")
    version("1.4.46", sha256="6913b8247d8a292ef8315162a51931e2b40ce91681f1b6f18f697045200c4a30", url="https://pypi.org/packages/af/ae/8d8e67f2691f0fdb845df90013d68c12a9127e009b4dedc34a3228f4e5ad/SQLAlchemy-1.4.46.tar.gz")
    version("1.4.45", sha256="fd69850860093a3f69fefe0ab56d041edfdfe18510b53d9a2eaecba2f15fa795", url="https://pypi.org/packages/76/d5/9ce70fd0d2858c72ecacff0c0518e9ddfbbaf4753b85e49f6d94ad74de36/SQLAlchemy-1.4.45.tar.gz")
    version("1.4.44", sha256="2dda5f96719ae89b3ec0f1b79698d86eb9aecb1d54e990abb3fdd92c04b46a90", url="https://pypi.org/packages/eb/71/f5f512914b86bd007bf842d9b95dba78eedb899d46025ab86b197b22ae62/SQLAlchemy-1.4.44.tar.gz")
    version("1.4.43", sha256="c628697aad7a141da8fc3fd81b4874a711cc84af172e1b1e7bbfadf760446496", url="https://pypi.org/packages/ae/92/815bc4dbd071ec9e215685c31e3ba86269876a2cb36eed38b2da63a22295/SQLAlchemy-1.4.43.tar.gz")
    version("1.4.41", sha256="0292f70d1797e3c54e862e6f30ae474014648bc9c723e14a2fda730adb0a9791", url="https://pypi.org/packages/67/a0/97da2cb07e013fd6c37fd896a86b374aa726e4161cafd57185e8418d59aa/SQLAlchemy-1.4.41.tar.gz")
    version("1.4.40", sha256="44a660506080cc975e1dfa5776fe5f6315ddc626a77b50bf0eee18b0389ea265", url="https://pypi.org/packages/4e/72/e36fa6563c45f8e1f2a5781f43f096500c1bca4963a34e72e8d3d8002d77/SQLAlchemy-1.4.40.tar.gz")
    version("1.4.39", sha256="8194896038753b46b08a0b0ae89a5d80c897fb601dd51e243ed5720f1f155d27", url="https://pypi.org/packages/1f/93/e5211e989324793487efb45405343d81b554886e278234066e20f77d434d/SQLAlchemy-1.4.39.tar.gz")
    version("1.4.38", sha256="93ae1d2ef42fbf0f0b3d44b35225bda123310df4b33c9bf662e7b50a68c48a98", url="https://pypi.org/packages/be/06/8c75ad5b5d2f0935304dbdbd0cdf54761f73f6bc4d18cd092b49ed7520d5/SQLAlchemy-1.4.38.tar.gz")
    version("1.4.37", sha256="3688f92c62db6c5df268e2264891078f17ecb91e3141b400f2e28d0f75796dea", url="https://pypi.org/packages/8c/6b/dd25a730940556f4a0130968f29040e4aa6478285a33ac041d1b0817d398/SQLAlchemy-1.4.37.tar.gz")
    version("1.4.36", sha256="64678ac321d64a45901ef2e24725ec5e783f1f4a588305e196431447e7ace243", url="https://pypi.org/packages/fb/b0/53e540c9fad14ac2da8a15ae95d707b167f64f62d85d4f506b0335dfd66d/SQLAlchemy-1.4.36.tar.gz")
    version("1.4.35", sha256="2ffc813b01dc6473990f5e575f210ca5ac2f5465ace3908b78ffd6d20058aab5", url="https://pypi.org/packages/f6/d6/fcf14b752daba13a02a6669eccb025bf3ba3f814741cd23253c180a12fff/SQLAlchemy-1.4.35.tar.gz")
    version("1.4.34", sha256="623bac2d6bdca3f3e61cf1e1c466c5fb9f5cf08735736ee1111187b7a4108891", url="https://pypi.org/packages/a2/6f/5bda54b52b50801f83bbb5e2ffac503ef57ea8ec889bcef3263470578964/SQLAlchemy-1.4.34.tar.gz")
    version("1.4.33", sha256="84747d1cc4823285b8253a34513162a664d4989217461e111097446b98803bfc", url="https://pypi.org/packages/fe/bf/bf9ab5f5af71c21539ad81225b35df1dcbf00b360d0230a179a519b2228d/SQLAlchemy-1.4.33.tar.gz")
    version("1.4.32", sha256="6fdd2dc5931daab778c2b65b03df6ae68376e028a3098eb624d0909d999885bc", url="https://pypi.org/packages/7a/9f/ace7376a3ab45adf0f7169a5d8d60707c04b171b72a18bb23d505f83f362/SQLAlchemy-1.4.32.tar.gz")
    version("1.4.25", sha256="1adf3d25e2e33afbcd48cfad8076f9378793be43e7fec3e4334306cac6bec138", url="https://pypi.org/packages/69/2b/f0ee898c3270d965300ec30b0bf06e062c4cc92f35d17ae6046f429c5067/SQLAlchemy-1.4.25.tar.gz")
    version("1.4.20", sha256="38ee3a266afef2978e82824650457f70c5d74ec0cadec1b10fe5ed6f038eb5d0", url="https://pypi.org/packages/b6/6b/d802a9223430cc4f55d7993ede4cdafa683fb8a1260516c48bcd59729c74/SQLAlchemy-1.4.20.tar.gz")
    version("1.3.24", sha256="ebbb777cbf9312359b897bf81ba00dae0f5cb69fba2a18265dcc18a6f5ef7519", url="https://pypi.org/packages/c5/ab/81bef2f960abf3cdaf32fbf1994f0c6f5e6a5f1667b5713ed6ebf162b6a2/SQLAlchemy-1.3.24.tar.gz")
    version("1.3.23", sha256="6fca33672578666f657c131552c4ef8979c1606e494f78cd5199742dfb26918b", url="https://pypi.org/packages/ac/cd/f871773f1c1eb043f639b6751d6342539a45da0836bfede6a6889cea5255/SQLAlchemy-1.3.23.tar.gz")
    version("1.3.22", sha256="758fc8c4d6c0336e617f9f6919f9daea3ab6bb9b07005eda9a1a682e24a6cacc", url="https://pypi.org/packages/b7/10/b6d02efa2cb10dca0671fd62c9091c1e49831b266658fd7a056c577621cb/SQLAlchemy-1.3.22.tar.gz")
    version("1.3.21", sha256="0bc49cba55b01b6827d1c303486da1afaaaf65a7a4d0e2be2cbc31c0f56752dc", url="https://pypi.org/packages/6f/e2/a51b021de8340f9fc4b6f6cb3483bb759b6792b1e28e9bd8b0b0bf37904e/SQLAlchemy-1.3.21.tar.gz")
    version("1.3.20", sha256="d2f25c7f410338d31666d7ddedfa67570900e248b940d186b48461bd4e5569a1", url="https://pypi.org/packages/69/ef/6d18860e18db68b8f25e0d268635f2f8cefa7a1cbf6d9d9f90214555a364/SQLAlchemy-1.3.20.tar.gz")
    version("1.3.19", sha256="3bba2e9fbedb0511769780fe1d63007081008c5c2d7d715e91858c94dbaa260e", url="https://pypi.org/packages/e3/aa/63c30deea197969211eb5bdf31f30abc9e3fc91eb01b78b6f328a36c31e5/SQLAlchemy-1.3.19.tar.gz")
    version("1.3.18", sha256="da2fb75f64792c1fc64c82313a00c728a7c301efe6a60b7a9fe35b16b4368ce7", url="https://pypi.org/packages/02/80/c83986fceeed04f7d42e3fd8a67e94e87b56afb223ee653e8a4a8986361e/SQLAlchemy-1.3.18.tar.gz")
    version("1.3.17", sha256="156a27548ba4e1fed944ff9fcdc150633e61d350d673ae7baaf6c25c04ac1f71", url="https://pypi.org/packages/84/f4/5a61726869da51f37f643ea92bfa440e32eb182bdc1a1c7cfc9504930a95/SQLAlchemy-1.3.17.tar.gz")
    version("1.3.16", sha256="7224e126c00b8178dfd227bc337ba5e754b197a3867d33b9f30dc0208f773d70", url="https://pypi.org/packages/7f/4b/adfb1f03da7f50db054a5b728d32dbfae8937754cfa159efa0216a3758d1/SQLAlchemy-1.3.16.tar.gz")
    version("1.3.15", sha256="c4cca4aed606297afbe90d4306b49ad3a4cd36feb3f87e4bfd655c57fd9ef445", url="https://pypi.org/packages/8c/30/4134e726dd5ed13728ff814fa91fc01c447ad8700504653fe99d91fdd34b/SQLAlchemy-1.3.15.tar.gz")
    version("1.3.9", sha256="272a835758908412e75e87f75dd0179a51422715c125ce42109632910526b1fd", url="https://pypi.org/packages/89/4e/f10fc5063d1048b3813c0caf99f06ec2b73851ae1a939feb85315dacb3fc/SQLAlchemy-1.3.9.tar.gz")
    version("1.2.19", sha256="5bb2c4fc2bcc3447ad45716c66581eab982c007dcf925482498d8733f86f17c7", url="https://pypi.org/packages/f9/67/d07cf7ac7e6dd0bc55ba62816753f86d7c558107104ca915e730c9ec2512/SQLAlchemy-1.2.19.tar.gz")
    version("1.2.10", sha256="72325e67fb85f6e9ad304c603d83626d1df684fdf0c7ab1f0352e71feeab69d8", url="https://pypi.org/packages/8a/c2/29491103fd971f3988e90ee3a77bb58bad2ae2acd6e8ea30a6d1432c33a3/SQLAlchemy-1.2.10.tar.gz")
    version("1.1.18", sha256="8b0ec71af9291191ba83a91c03d157b19ab3e7119e27da97932a4773a3f664a9", url="https://pypi.org/packages/cc/4d/96d93ff77cd67aca7618e402191eee3490d8f5f245d6ab7622d35fe504f4/SQLAlchemy-1.1.18.tar.gz")
    version("1.0.12", sha256="6679e20eae780b67ba136a4a76f83bb264debaac2542beefe02069d0206518d1", url="https://pypi.org/packages/5c/52/9b48cd58eac58cae2a27923ff34c783f390b95413ff65669a86e98f80829/SQLAlchemy-1.0.12.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("backend", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@4.6:", when="@2.0.25:")
        depends_on("py-typing-extensions@4.2:", when="@2.0.5:2.0.5.0,2.0.24")

        # marker: platform_machine == "aarch64" or (platform_machine == "ppc64le" or (platform_machine == "x86_64" or (platform_machine == "amd64" or (platform_machine == "AMD64" or (platform_machine == "win32" or platform_machine == "WIN32")))))
        # depends_on("py-greenlet@:0.4.16,1:", when="@2.0.5:2.0.5.0,2.0.24:")

        # marker: python_version >= "3" and (platform_machine == "aarch64" or (platform_machine == "ppc64le" or (platform_machine == "x86_64" or (platform_machine == "amd64" or (platform_machine == "AMD64" or (platform_machine == "win32" or platform_machine == "WIN32"))))))
        # depends_on("py-greenlet@:0.4.16,1:", when="@1.4.51:1")
    # END DEPENDENCIES

