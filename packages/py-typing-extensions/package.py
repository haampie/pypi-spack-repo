# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypingExtensions(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.10.0", sha256="69b1a937c3a517342112fb4c6df7e72fc39a38e7891a5730ed4985b5214b5475", url="https://pypi.org/packages/f9/de/dc04a3ea60b22624b51c703a84bbe0184abcd1d0b9bc8074b5d6b7ab90bb/typing_extensions-4.10.0-py3-none-any.whl")
    version("4.10.0-rc1", sha256="ada05f19b82a2ea6eeac4e7412a2328e70b5237f05f3ffef49cae6db558a914e", url="https://pypi.org/packages/d4/b2/4980568cd3814002f1c04b542e2dd52faa0cec11bd5bda99e43eefe9a808/typing_extensions-4.10.0rc1-py3-none-any.whl")
    version("4.9.0", sha256="af72aea155e91adfc61c3ae9e0e342dbc0cba726d6cba4b6c72c1f34e47291cd", url="https://pypi.org/packages/b7/f4/6a90020cd2d93349b442bfcb657d0dc91eee65491600b2cb1d388bc98e6b/typing_extensions-4.9.0-py3-none-any.whl")
    version("4.9.0-rc1", sha256="cc22327e22d9b583d1565ce1ed9f5ecc22831afa743f8789a403cad849fb702b", url="https://pypi.org/packages/68/1e/4738def2321ec3a3ec2efde1515be665deb88eea3a60187b2ff42cde7447/typing_extensions-4.9.0rc1-py3-none-any.whl")
    version("4.8.0", sha256="8f92fc8806f9a6b641eaa5318da32b44d401efaac0f6678c9bc448ba3605faa0", url="https://pypi.org/packages/24/21/7d397a4b7934ff4028987914ac1044d3b7d52712f30e2ac7a2ae5bc86dd0/typing_extensions-4.8.0-py3-none-any.whl")
    version("4.8.0-rc1", sha256="8ac091074039c3b0ecf99e8e339a9cdbcac65b6e6b9684eb692e1d521a5e6bee", url="https://pypi.org/packages/63/d6/ebc4ad51f7a42b0e46c42693563f38b4299314778a773a802a968d6ae742/typing_extensions-4.8.0rc1-py3-none-any.whl")
    version("4.7.1", sha256="440d5dd3af93b060174bf433bccd69b0babc3b15b1a8dca43789fd7f61514b36", url="https://pypi.org/packages/ec/6b/63cc3df74987c36fe26157ee12e09e8f9db4de771e0f3404263117e75b95/typing_extensions-4.7.1-py3-none-any.whl")
    version("4.7.0", sha256="5d8c9dac95c27d20df12fb1d97b9793ab8b2af8a3a525e68c80e21060c161771", url="https://pypi.org/packages/7e/4d/b0185d077dc1cd070a56859a0ba3bb6e76618393ec693e59faf1368da8f6/typing_extensions-4.7.0-py3-none-any.whl")
    version("4.6.3", sha256="88a4153d8505aabbb4e13aacb7c486c2b4a33ca3b3f807914a9b4c844c471c26", url="https://pypi.org/packages/5f/86/d9b1518d8e75b346a33eb59fa31bdbbee11459a7e2cc5be502fa779e96c5/typing_extensions-4.6.3-py3-none-any.whl")
    version("4.6.2", sha256="3a8b36f13dd5fdc5d1b16fe317f5668545de77fa0b8e02006381fd49d731ab98", url="https://pypi.org/packages/38/60/300ad6f93adca578bf05d5f6cd1d854b7d140bebe2f9829561aa9977d9f3/typing_extensions-4.6.2-py3-none-any.whl")
    version("4.6.1", sha256="6bac751f4789b135c43228e72de18637e9a6c29d12777023a703fd1a6858469f", url="https://pypi.org/packages/82/ed/8ccf53a0ed10bf8fc8877b5833b40f5f99093cadfe6632b8892f74aead0f/typing_extensions-4.6.1-py3-none-any.whl")
    version("4.6.0", sha256="6ad00b63f849b7dcc313b70b6b304ed67b2b2963b3098a33efe18056b1a9a223", url="https://pypi.org/packages/85/d2/949d324c348014f0fd2e8e6d8efd3c0adefdcecd28990d4144f2cfc8105e/typing_extensions-4.6.0-py3-none-any.whl")
    version("4.5.0", sha256="fb33085c39dd998ac16d1431ebc293a8b3eedd00fd4a32de0ff79002c19511b4", url="https://pypi.org/packages/31/25/5abcd82372d3d4a3932e1fa8c3dbf9efac10cc7c0d16e78467460571b404/typing_extensions-4.5.0-py3-none-any.whl")
    version("4.4.0", sha256="16fa4864408f655d35ec496218b85f79b3437c829e93320c7c9215ccfd92489e", url="https://pypi.org/packages/0b/8e/f1a0a5a76cfef77e1eb6004cb49e5f8d72634da638420b9ea492ce8305e8/typing_extensions-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="25642c956049920a5aa49edcdd6ab1e06d7e5d467fc00e0506c44ac86fbfca02", url="https://pypi.org/packages/ed/d6/2afc375a8d55b8be879d6b4986d4f69f01115e795e36827fd3a40166028b/typing_extensions-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="6657594ee297170d19f67d55c05852a874e7eb634f4f753dbd667855e07c1708", url="https://pypi.org/packages/75/e1/932e06004039dd670c9d5e1df0cd606bf46e29a28e65d5bb28e894ea29c9/typing_extensions-4.2.0-py3-none-any.whl")
    version("4.1.1", sha256="21c85e0fe4b9a155d0799430b0ad741cdce7e359660ccbd8b530613e8df88ce2", url="https://pypi.org/packages/45/6b/44f7f8f1e110027cf88956b59f2fad776cca7e1704396d043f89effd3a0e/typing_extensions-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="c13180fbaa7cd97065a4915ceba012bdb31dc34743e63ddee16360161d358414", url="https://pypi.org/packages/6a/1e/df241fd31424de8c834a6c0281652a13a30191bdb10c600c35cef02cd160/typing_extensions-4.1.0-py3-none-any.whl")
    version("4.0.1", sha256="7f001e5ac290a0c0401508864c7ec868be4e701886d5b573a9528ed3973d9d3b", url="https://pypi.org/packages/05/e4/baf0031e39cf545f0c9edd5b1a2ea12609b7fcba2d58e118b11753d68cf0/typing_extensions-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="829704698b22e13ec9eaf959122315eabb370b0884400e9818334d8b677023d9", url="https://pypi.org/packages/17/61/32c3ab8951142e061587d957226b5683d1387fb22d95b4f69186d92616d1/typing_extensions-4.0.0-py3-none-any.whl")
    version("3.10.0.2", sha256="f1d25edafde516b146ecd0613dabcc61409817af4766fbbcfb8d1ad4ec441a34", url="https://pypi.org/packages/74/60/18783336cc7fcdd95dae91d73477830aa53f5d3181ae4fe20491d7fc3199/typing_extensions-3.10.0.2-py3-none-any.whl")
    version("3.10.0.1", sha256="045dd532231acfa03628df5e0c66dba64e2cc8fc8b844538d4ad6d5dd6cb82dc", url="https://pypi.org/packages/e8/ee/237d13b6d3d532778a57df23e6df4b2a82fbbeb833c4016054c6b6730d56/typing_extensions-3.10.0.1-py3-none-any.whl")
    version("3.10.0.0", sha256="779383f6086d90c99ae41cf0ff39aac8a7937a9283ce0a414e5dd782f4c94a84", url="https://pypi.org/packages/2e/35/6c4fff5ab443b57116cb1aad46421fb719bed2825664e8fe77d66d99bcbc/typing_extensions-3.10.0.0-py3-none-any.whl")
    version("3.7.4.3", sha256="7cb407020f00f7bfc3cb3e7881628838e69d8f3fcab2f64742a5e76b2f841918", url="https://pypi.org/packages/60/7a/e881b5abb54db0e6e671ab088d079c57ce54e8a01a3ca443f561ccadb37e/typing_extensions-3.7.4.3-py3-none-any.whl")
    version("3.7.4.2", sha256="6e95524d8a547a91e08f404ae485bbb71962de46967e1b71a0cb89af24e761c5", url="https://pypi.org/packages/0c/0e/3f026d0645d699e7320b59952146d56ad7c374e9cd72cd16e7c74e657a0f/typing_extensions-3.7.4.2-py3-none-any.whl")
    version("3.7.4.1", sha256="cf8b63fedea4d89bab840ecbb93e75578af28f76f66c35889bd7065f5af88575", url="https://pypi.org/packages/03/92/705fe8aca27678e01bbdd7738173b8e7df0088a2202c80352f664630d638/typing_extensions-3.7.4.1-py3-none-any.whl")
    version("3.7.4", sha256="d8179012ec2c620d3791ca6fe2bf7979d979acdbef1fca0bc56b37411db682ed", url="https://pypi.org/packages/27/aa/bd1442cfb0224da1b671ab334d3b0a4302e4161ea916e28904ff9618d471/typing_extensions-3.7.4-py3-none-any.whl")
    version("3.7.2", sha256="f3f0e67e1d42de47b5c67c32c9b26641642e9170fe7e292991793705cd5fef7c", url="https://pypi.org/packages/0f/62/c66e553258c37c33f9939abb2dd8d2481803d860ff68e635466f12aa7efa/typing_extensions-3.7.2-py3-none-any.whl")
    version("3.6.6", sha256="55401f6ed58ade5638eb566615c150ba13624e2f0c1eedd080fc3c1b6cb76f1d", url="https://pypi.org/packages/62/4f/392a1fa2873e646f5990eb6f956e662d8a235ab474450c72487745f67276/typing_extensions-3.6.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing@3.7:", when="@3.7.4:3.7.4.0")
        depends_on("py-typing@3.6.2:", when="@:3.7.2")
    # END DEPENDENCIES

