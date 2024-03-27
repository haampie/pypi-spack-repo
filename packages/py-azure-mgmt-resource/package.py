##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtResource(PythonPackage):
    version("23.0.1", sha256="f185eec72bbc39f42bcb83ae6f1bad744f0e3f20a12d9b2b3e70d16c74ad9cc0", url="https://pypi.org/packages/40/14/9e0ffa0b24958081416005b49a7d903c1c12712accdd2cf9ebad7b3b41ee/azure_mgmt_resource-23.0.1-py3-none-any.whl")
    version("23.0.0", sha256="b556803a3b8699dbcd1f4c33c8229830225c8c61ba058323d5bae7dc7785d65e", url="https://pypi.org/packages/c6/53/6a8118e1063d2b60ea33e8dd16ea2dafd1e89c91ee83a6581f108fdea940/azure_mgmt_resource-23.0.0-py3-none-any.whl")
    version("22.0.0", sha256="5c9712aacb230c7dde59cd7b43a734ed88a326140042ae02746d095fe779ae20", url="https://pypi.org/packages/b7/0a/8826c211f8904dbbe88cddaf39c7d38a419427f8f7454ea6cf8ab0962e10/azure_mgmt_resource-22.0.0-py3-none-any.whl")
    version("21.2.1", sha256="c6f6987e6f61f0cb23abc3fb3658770bae8d299a46834d43d4b20251495d3806", url="https://pypi.org/packages/41/78/6c514040e16c8c3fa2f7afa43c16dd92233d4ebe3cd5750dd74f69e6cfd1/azure_mgmt_resource-21.2.1-py3-none-any.whl")
    version("21.2.0", sha256="3a75e326bf0f6c5689bb153df041f70bed715790c5c5a179c216f4acf9adf149", url="https://pypi.org/packages/d9/27/81c3683761e4ea7e612db2d1685dd757c4ac0c71067074992421b50bc8d1/azure_mgmt_resource-21.2.0-py3-none-any.whl")
    version("21.1.0", sha256="5c8203f72bfb483adb345f73df1be65351072f25714fc6bb77eb0d5b970aba3b", url="https://pypi.org/packages/9e/24/9a2e9dbc24ebd3a9cf652a856ef931864b0ac5d7776dcec911e3f76e93a1/azure_mgmt_resource-21.1.0-py3-none-any.whl")
    version("21.0.0", sha256="1f1c07ebe9099c1301d03297d5743427efe04b41785df1f5d0326945aece5dba", url="https://pypi.org/packages/8b/cb/1e20e7bdf81d35e815c25f00a1abcad077f41e689a5d156ff051f5263a3f/azure_mgmt_resource-21.0.0-py3-none-any.whl")
    version("20.1.0", sha256="b009dcd66bee43691b71048b97c3da9c269ea24f338f1f9788bbd4c4726336c3", url="https://pypi.org/packages/1f/5e/e0c0b7458c20d622acdb9120f052ce8b4aa851e1b5ba839828433bb8c519/azure_mgmt_resource-20.1.0-py3-none-any.whl")
    version("20.0.0", sha256="0ebad05a946e27c17d5a86ea5a68b2d9a0142257656ae8211dee9fc191c849b7", url="https://pypi.org/packages/27/75/f4256022eae712acacfbb80b3a18d0a4a8c52fb81271db1151bb60d92060/azure_mgmt_resource-20.0.0-py2.py3-none-any.whl")
    version("19.0.0", sha256="6902e62510f9500fd907a6f9187f61ee7d5fff18217d808bd650cd1092ad6233", url="https://pypi.org/packages/e8/6a/fc92a0a1740111dd00827ab9435a5c33c9294ba2a82ee62bbb3d21886652/azure_mgmt_resource-19.0.0-py2.py3-none-any.whl")
    version("13.0.0", sha256="1a2c96a026e8ba434d430c7f179ce1e96bf3ce389b53ac96b74c13162426461c", url="https://pypi.org/packages/a3/54/19dce89424cc93776c583d5f95b61782dc95dc9572a96611ce40999aec99/azure_mgmt_resource-13.0.0-py2.py3-none-any.whl")
    version("12.1.0", sha256="6aff35fcd23aaf508418c5d4885d5fb37ccf7aa601a580d97ca671d61738a78a", url="https://pypi.org/packages/55/f6/7db7f9f144cac5924dbd6a8bcba2bac872dfbf3137b83c41a0ea136b3449/azure_mgmt_resource-12.1.0-py2.py3-none-any.whl")
    version("12.0.0", sha256="719842002bd4f9558e501a088977f6d784059ca53a0f70404aa528614e9aa823", url="https://pypi.org/packages/77/0f/cb596ca094c6ffdd86f7b8a0190042d1ab2d732b87398c7e76def9b5d815/azure_mgmt_resource-12.0.0-py2.py3-none-any.whl")
    version("11.0.0", sha256="c5717350a23517c1f67c288abcc05c59dc8f13c891aebd7f8d1d68b51fae24a2", url="https://pypi.org/packages/a7/85/d58eef1c0cc591398d42967b4b166efa84e7e68be47b00bb3043c2e1cc72/azure_mgmt_resource-11.0.0-py2.py3-none-any.whl")
    version("10.3.0", sha256="b838920ed5a036b4b86ae2749e14b9817b963315913e5954c320434d30458d0d", url="https://pypi.org/packages/0d/25/01bea28662a6e1a37862eb9ab26648c12f6068fd2ea1e9c9ada6c478482c/azure_mgmt_resource-10.3.0-py2.py3-none-any.whl")
    version("10.2.0", sha256="e7e72209e7b7f0e1fc5ff43caab1e95d8893f286300338bbfe9a884cb9342c17", url="https://pypi.org/packages/af/b3/8009c149d7d162b7a2a22a5007f984aa090f089bf8dc09e7e84bd354b868/azure_mgmt_resource-10.2.0-py2.py3-none-any.whl")
    version("10.1.0", sha256="33ae072d0f60b804eda68c4396a73a7154005c88abf85d42c40a8991d0aa4eb9", url="https://pypi.org/packages/36/81/1d108d908c526c70c79a1b8ec833d09e6d5e0619282516f510840eb97c5d/azure_mgmt_resource-10.1.0-py2.py3-none-any.whl")
    version("10.0.0", sha256="c1e2d834dee84953a4e25bef119008854a861d6d3fbe79b436589dc042e5a7c5", url="https://pypi.org/packages/be/20/b639d8e4b0c1c49e3f1373c6a7948fd4ced55e57f204b63fb15a7cd77e73/azure_mgmt_resource-10.0.0-py2.py3-none-any.whl")
    version("9.0.0", sha256="055e85a4053a987bf427653e75f537c750ecc27c0e7c74623a67cb859689b5a6", url="https://pypi.org/packages/6e/cb/a3dabcff89c3cce5836d030435d8aba136dfe8f84dda4c89630cf7234268/azure_mgmt_resource-9.0.0-py2.py3-none-any.whl")
    version("8.0.1", sha256="d90b7d8f237b71b54cfd06480dc1ecd7dac81b22301bf2f4ead98a53cf269b6a", url="https://pypi.org/packages/35/b3/87b49dfb82f8868b47ec6da76812cd2549db65c87474f6bcfc458b2a7999/azure_mgmt_resource-8.0.1-py2.py3-none-any.whl")
    version("8.0.0", sha256="455a10bbae15673c7879d7515b38e1548cb1a8982dd35029ab3192565262c573", url="https://pypi.org/packages/ee/f0/3a3fe6f66a33a4a84e21984b7450475ee031c7d82c09a6d27170f2ccd34e/azure_mgmt_resource-8.0.0-py2.py3-none-any.whl")
    version("7.0.0", sha256="20b3394e4dc76fbd9459723cb8c0300fb18a8c32100076f023b5470426b9f104", url="https://pypi.org/packages/10/2a/26db9b79f00699e6033f0667dd950085daeb6abf84ae765adfa092f59e37/azure_mgmt_resource-7.0.0-py2.py3-none-any.whl")
    version("6.0.0", sha256="a557a87fad2a2a5190d03e12cd7cf6307a194604e808773972c34847503b482b", url="https://pypi.org/packages/76/2e/5ba951dda43e5bddc65730e5b39bc45f04074612db69477fdb2ef9dd0702/azure_mgmt_resource-6.0.0-py2.py3-none-any.whl")
    version("5.1.0", sha256="50ffb1986056a67b5381d366f0a6ada0cdd5ad275c0e85b07baa91cb1de08997", url="https://pypi.org/packages/7c/0d/80815326fa04f2a73ea94b0f57c29669c89df5aa5f5e285952f6445a91c4/azure_mgmt_resource-5.1.0-py2.py3-none-any.whl")
    version("5.0.0", sha256="ce901f97d04257b13c7424d27dc1c8585c0527fca19942ac0419e99a5591da54", url="https://pypi.org/packages/74/ae/ea83233d6d3315151b0f08266cd8c33bad32bd109f68b520c6320006b034/azure_mgmt_resource-5.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1.2:2.0.0-rc1,2.1:")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@21.2:")
        depends_on("py-azure-mgmt-core@1.3.0:", when="@20.1:21.1")
        depends_on("py-azure-mgmt-core@1.2:", when="@15.0.0:20.0")
        depends_on("py-isodate@0.6.1:", when="@23.0.0:")
        depends_on("py-msrest@0.7.1:", when="@21.2:23.0.0-beta1")
        depends_on("py-msrest@0.6.21:", when="@16.1:21.1")
        depends_on("py-msrest@0.5:", when="@2.1:16.0")
        depends_on("py-msrestazure@0.4.32:", when="@2.1:13")

