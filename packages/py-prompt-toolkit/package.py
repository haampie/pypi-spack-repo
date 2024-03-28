# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPromptToolkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.43", sha256="a11a29cb3bf0a28a387fe5122cdb649816a957cd9261dcedf8c9f1fef33eacf6", url="https://pypi.org/packages/ee/fd/ca7bf3869e7caa7a037e23078539467b433a4e01eebd93f77180ab927766/prompt_toolkit-3.0.43-py3-none-any.whl")
    version("3.0.42", sha256="3b50b5fc50660dc8e39dfe464b170959ad82ff185ffa53bfd3be02222e7156a1", url="https://pypi.org/packages/82/d3/9a794648e76d04e68ddd13889da4aae01a0368814728cb968e1147600d79/prompt_toolkit-3.0.42-py3-none-any.whl")
    version("3.0.41", sha256="f36fe301fafb7470e86aaf90f036eef600a3210be4decf461a5b1ca8403d3cb2", url="https://pypi.org/packages/1f/9d/be9b01085bbd67a71c4b6aa02518fade8104e7a2224e5de5e947811d7176/prompt_toolkit-3.0.41-py3-none-any.whl")
    version("3.0.40", sha256="99ba3dfb23d5b5af89712f89e60a5f3d9b8b67a9482ca377c5771d0e9047a34b", url="https://pypi.org/packages/ed/29/cd63ff872dfc213e1cd8131f8060262db184b975868cef33302f44616c3e/prompt_toolkit-3.0.40-py3-none-any.whl")
    version("3.0.39", sha256="9dffbe1d8acf91e3de75f3b544e4842382fc06c6babe903ac9acb74dc6e08d88", url="https://pypi.org/packages/a9/b4/ba77c84edf499877317225d7b7bc047a81f7c2eed9628eeb6bab0ac2e6c9/prompt_toolkit-3.0.39-py3-none-any.whl")
    version("3.0.38", sha256="45ea77a2f7c60418850331366c81cf6b5b9cf4c7fd34616f733c5427e6abbb1f", url="https://pypi.org/packages/87/3f/1f5a0ff475ae6481f4b0d45d4d911824d3218b94ee2a97a8cb84e5569836/prompt_toolkit-3.0.38-py3-none-any.whl")
    version("3.0.37", sha256="6a2948ec427dfcc7c983027b1044b355db6aaa8be374f54ad2015471f7d81c5b", url="https://pypi.org/packages/6b/f8/1bb04f1ed50ceffa077ad762911c10aa27defdea6094e1f78ed5cbae1d81/prompt_toolkit-3.0.37-py3-none-any.whl")
    version("3.0.36", sha256="aa64ad242a462c5ff0363a7b9cfe696c20d55d9fc60c11fd8e632d064804d305", url="https://pypi.org/packages/eb/37/791f1a6edd13c61cac85282368aa68cb0f3f164440fdf60032f2cc6ca34e/prompt_toolkit-3.0.36-py3-none-any.whl")
    version("3.0.35", sha256="bfbd4a45aaa695b45903acb02032f63c216865a4faa35e2269767d6c77dc5d6d", url="https://pypi.org/packages/e4/5a/d55415fe79a0524726849993f4135d2fb8f5e0448d28a5492a69c8ab681a/prompt_toolkit-3.0.35-py3-none-any.whl")
    version("3.0.34", sha256="c419ef139a56b61ac257a1227279bd5ea6dc49cfcd855bb9af7b1c4979b1d5b2", url="https://pypi.org/packages/4f/61/51a29f3291939242fb8ff8ec7ada1cd37e22360d9e9d218308de3a1355a9/prompt_toolkit-3.0.34-py3-none-any.whl")
    version("3.0.33", sha256="ced598b222f6f4029c0800cefaa6a17373fb580cd093223003475ce32805c35b", url="https://pypi.org/packages/58/87/cac418cef18781a9081cb2075cc2cf08c77e0679c1f9b474587d71bbf777/prompt_toolkit-3.0.33-py3-none-any.whl")
    version("3.0.31", sha256="9696f386133df0fc8ca5af4895afe5d78f5fcfe5258111c2a79a1c3e41ffa96d", url="https://pypi.org/packages/26/ec/2ebddd1f0584fec4a6d4b5dc57627254070c3db310f00981bc5de03dd5ab/prompt_toolkit-3.0.31-py3-none-any.whl")
    version("3.0.29", sha256="62291dad495e665fca0bda814e342c69952086afb0f4094d0893d357e5c78752", url="https://pypi.org/packages/3f/2d/dcb44d69f388ca2ee1a4a4d3c204ab66b36975c0d5166781eaeeff76b882/prompt_toolkit-3.0.29-py3-none-any.whl")
    version("3.0.24", sha256="e56f2ff799bacecd3e88165b1e2f5ebf9bcd59e80e06d395fa0cc4b8bd7bb506", url="https://pypi.org/packages/fb/37/4f9ae5a6cd0ebdfc1fbafcfd03e812df1ed92a92bf0bee09441c52164f58/prompt_toolkit-3.0.24-py3-none-any.whl")
    version("3.0.17", sha256="4cea7d09e46723885cb8bc54678175453e5071e9449821dce6f017b1d1fbfc1a", url="https://pypi.org/packages/ce/ee/08ceeb759c570bf96b4c636582ebf18c14c3c844a601b2e77b17f462aa6b/prompt_toolkit-3.0.17-py3-none-any.whl")
    version("3.0.16", sha256="62c811e46bd09130fb11ab759012a4ae385ce4fb2073442d1898867a824183bd", url="https://pypi.org/packages/a6/0b/c6de29441b29f8b54d5bbe29a8b223de6e400714ff50e85541bd4c783421/prompt_toolkit-3.0.16-py3-none-any.whl")
    version("3.0.7", sha256="83074ee28ad4ba6af190593d4d4c607ff525272a504eb159199b6dd9f950c950", url="https://pypi.org/packages/2b/c1/53ac685833200eb77ef485c2220dac5bfc255418e660790a9eb5cf3abf25/prompt_toolkit-3.0.7-py3-none-any.whl")
    version("2.0.10", sha256="e7f8af9e3d70f514373bf41aa51bc33af12a6db3f71461ea47fea985defb2c31", url="https://pypi.org/packages/66/6a/2c0693ec21528c10dfea279662788b28b2a01cce961160791084d975521a/prompt_toolkit-2.0.10-py2-none-any.whl")
    version("2.0.9", sha256="977c6583ae813a37dc1c2e1b715892461fcbdaa57f6fc62f33a528c4886c8f55", url="https://pypi.org/packages/c8/ab/10d2c114828bd20ca0d757acee37ab5a7bae588139739b24d6cd3f45f8de/prompt_toolkit-2.0.9-py2-none-any.whl")
    version("2.0.8", sha256="df5835fb8f417aa55e5cafadbaeb0cf630a1e824aad16989f9f0493e679ec010", url="https://pypi.org/packages/f0/fe/564f7f7d2735265460225232441cb8aadee8e58e6a3cefae38220d38481e/prompt_toolkit-2.0.8-py2-none-any.whl")
    version("2.0.7", sha256="d4c47f79b635a0e70b84fdb97ebd9a274203706b1ee5ed44c10da62755cf3ec9", url="https://pypi.org/packages/c7/f8/04aec108fe1d76b59d93c98438bce32bc633e99e7e1453e22b8d82722b14/prompt_toolkit-2.0.7-py2-none-any.whl")
    version("2.0.6", sha256="646b3401b3b0bb7752100bc9b7aeecb36cb09cdfc63652b5856708b5ba8db7da", url="https://pypi.org/packages/bb/5d/0952036a5bd109cd911885cdba543eda9d93ce34728eafcedc6091d03111/prompt_toolkit-2.0.6-py2-none-any.whl")
    version("2.0.5", sha256="81da9ecf6ca6806a549697529af8ec3ac5b739c13ac14607218e650db1b53131", url="https://pypi.org/packages/40/fa/3e88dae1d06d3d718cdf9fe974ecab223f6a423309bcd178a826e13059bd/prompt_toolkit-2.0.5-py2-none-any.whl")
    version("2.0.4", sha256="12e076b21178064b5627f74c4819559c125e31046b55a28d5e024b85fef5617e", url="https://pypi.org/packages/fe/6e/29d42360930704dbf461a9802737930d96c44297bde8e0ad709af1f9cea7/prompt_toolkit-2.0.4-py2-none-any.whl")
    version("2.0.3", sha256="2e684ce7278eefb2eb6715e026169031376b60711eb62b3faf1f0d21f158280f", url="https://pypi.org/packages/bc/03/b779acfe9171a684e8ce0ab508f9950590beed1c784a582f8534389b89b3/prompt_toolkit-2.0.3-py2-none-any.whl")
    version("2.0.2", sha256="3e87a08d1acd179d2ddf0e0670437da03b88df8c8033d0843ad03cf7e69f1322", url="https://pypi.org/packages/a3/e6/a535cdfc133bb9fb6411b782c61f9195ff99b4220be19634009bbeb29c1a/prompt_toolkit-2.0.2-py2-none-any.whl")
    version("2.0.1", sha256="bbecacf5310a0b0b590446e8e1d3d83d8dc9cae68adb361214e561fa4775e6e1", url="https://pypi.org/packages/9b/8c/30b7b8891eb95c791f71256ca5ab134651a92136a2b72c1fd3eb7474249e/prompt_toolkit-2.0.1-py2-none-any.whl")
    version("1.0.18", sha256="37925b37a4af1f6448c76b7606e0285f79f434ad246dda007a27411cca730c6d", url="https://pypi.org/packages/64/27/5fd61a451d086ad4aa806dc72fe1383d2bc0e74323668672287f616d5d51/prompt_toolkit-1.0.18-py3-none-any.whl")
    version("1.0.17", sha256="be243da571de5a96590e02f2180497e11600c422a76519040444b41699eff27f", url="https://pypi.org/packages/10/97/fdc9cb23f6522e2e1d37b795dd6b4a628e6d6416523fddcf5f00323577cb/prompt_toolkit-1.0.17-py2-none-any.whl")
    version("1.0.16", sha256="1e71341526efa4b11bb44d323e687a5d9cef204aabe2907e3f0dc1534cda0ecc", url="https://pypi.org/packages/57/a8/a151b6c61718eabe6b4672b6aa760b734989316d62ec1ba4996765e602d4/prompt_toolkit-1.0.16-py3-none-any.whl")
    version("1.0.15", sha256="3f473ae040ddaa52b52f97f6b4a493cfa9f5920c255a12dc56a7d34397a398a4", url="https://pypi.org/packages/d1/b0/1a6c262da35c779dd79550137aa7c298a424987240a28792ec5ccf48f848/prompt_toolkit-1.0.15-py2-none-any.whl")
    version("1.0.14", sha256="82c7f8e07d7a0411ff5367a5a8ff520f0112b9179f3e599ee8ad2ad9b943d911", url="https://pypi.org/packages/4b/85/58829b76140b81b30d2d455040808665b2041b923134a287643b684de4e3/prompt_toolkit-1.0.14-py2-none-any.whl")
    version("1.0.13", sha256="92e946fc7b87417924605b0d688347cba85048f958fb6a929db032f1380719a3", url="https://pypi.org/packages/dc/da/d464207343a08ff5e97ed991556ec1c69dafca55007f2c0baff17dbad978/prompt_toolkit-1.0.13-py2-none-any.whl")
    version("1.0.10", sha256="32a8929dbfa17c49f81d7838b167c1a965f5263e3727eed3060d50c9b11f3244", url="https://pypi.org/packages/49/23/83991804adb65d16b414a4666f5416c8ff710b7c5f6c2327f6558cf31ff0/prompt_toolkit-1.0.10-py2-none-any.whl")
    version("1.0.9", sha256="b7bbbc221159be8daab91269d48575f6c740000c03d537fc076ee176476c8b4c", url="https://pypi.org/packages/fc/80/6a3cb891118635fd79be261c1f5a5d1fe479f15841526808c5aaa246f1ef/prompt_toolkit-1.0.9-py2-none-any.whl")
    version("1.0.8", sha256="608bd2c7070a5feb00bc02fe63cdd2e404901dac12ed47519e7c0d85eaf48717", url="https://pypi.org/packages/47/87/65c959e0aef5d9fbd2aa2b92507891253b80d8ffa0b635cd9c8e43d9bba2/prompt_toolkit-1.0.8-py2-none-any.whl")
    version("1.0.7", sha256="2611504e98b09c8e726073596f218b05632e24c8c20dc66a27b35621507dcbd8", url="https://pypi.org/packages/03/66/aad0711f484f1388ce6f368bbed29b68a247bfd7d701b0d01a9822e3eefd/prompt_toolkit-1.0.7-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wcwidth", when="@3:")
    # END DEPENDENCIES

