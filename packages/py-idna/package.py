# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIdna(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.6", sha256="c05567e9c24a6b9faaa835c4821bad0590fbb9d5779e7caa6e1cc4978e7eb24f", url="https://pypi.org/packages/c2/e7/a82b05cf63a603df6e68d59ae6a68bf5064484a0718ea5033660af4b54a9/idna-3.6-py3-none-any.whl")
    version("3.5", sha256="79b8f0ac92d2351be5f6122356c9a592c96d81c9a79e4b488bf2a6a15f88057a", url="https://pypi.org/packages/ea/65/9c7a31be86861d43da3d4f8661f677b38120320540773a04979ad6fa9ecd/idna-3.5-py3-none-any.whl")
    version("3.4", sha256="90b77e79eaa3eba6de819a0c442c0b4ceefc341a7a2ab77d7562bf49f425c5c2", url="https://pypi.org/packages/fc/34/3030de6f1370931b9dbb4dad48f6ab1015ab1d32447850b9fc94e60097be/idna-3.4-py3-none-any.whl")
    version("3.3", sha256="84d9dd047ffa80596e0f246e2eab0b391788b0503584e8945f2368256d2735ff", url="https://pypi.org/packages/04/a2/d918dcd22354d8958fe113e1a3630137e0fc8b44859ade3063982eacd2a4/idna-3.3-py3-none-any.whl")
    version("3.2", sha256="14475042e284991034cb48e06f6851428fb14c4dc953acd9be9a5e95c7b6dd7a", url="https://pypi.org/packages/d7/77/ff688d1504cdc4db2a938e2b7b9adee5dd52e34efbd2431051efc9984de9/idna-3.2-py3-none-any.whl")
    version("3.1", sha256="5205d03e7bcbb919cc9c19885f9920d622ca52448306f2377daede5cf3faac16", url="https://pypi.org/packages/29/88/c52aae187d3b128a0f13f36a6c987fc0d408d03a678ad9996516925d8495/idna-3.1-py3-none-any.whl")
    version("3.0", sha256="320229aadbdfc597bc28876748cc0c9d04d476e0fe6caacaaddea146365d9f63", url="https://pypi.org/packages/0f/6b/3a878f15ef3324754bf4780f8f047d692d9860be894ff8fb3135cef8bed8/idna-3.0-py2.py3-none-any.whl")
    version("2.10", sha256="b97d804b1e9b523befed77c48dacec60e6dcb0b5391d57af6a65a312a90648c0", url="https://pypi.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl")
    version("2.9", sha256="a068a21ceac8a4d63dbfd964670474107f541babbd2250d61922f029858365fa", url="https://pypi.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl")
    version("2.8", sha256="ea8b7f6188e6fa117537c3df7da9fc686d485087abf6ac197f9c46432f7e4a3c", url="https://pypi.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl")
    version("2.7", sha256="156a6814fb5ac1fc6850fb002e0852d56c0c8d2531923a51032d1b70760e186e", url="https://pypi.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl")
    version("2.6", sha256="8c7309c718f94b3a625cb648ace320157ad16ff131ae0af362c9f21b80ef6ec4", url="https://pypi.org/packages/27/cc/6dd9a3869f15c2edfab863b992838277279ce92663d334df9ecf5106f5c6/idna-2.6-py2.py3-none-any.whl")
    version("2.5", sha256="cc19709fd6d0cbfed39ea875d29ba6d4e22c0cebc510a76d6302a28385e8bb70", url="https://pypi.org/packages/11/7d/9bbbd7bb35f34b0169542487d2a8859e44306bb2e6a4455d491800a5621f/idna-2.5-py2.py3-none-any.whl")
    version("2.4", sha256="12468b2e4a71b1cbc342da70fb437dddbfb9d420272c313bd7129a6a22a2dd6a", url="https://pypi.org/packages/08/c6/71319d9ac2055156562992b16cb01dbee74f431c0372d580a8fef6ca0e4c/idna-2.4-py2.py3-none-any.whl")
    version("2.3", sha256="0a33cde64e2d7ba1afdd9586c5ebd000b07b6907c7141562bffe9cbcde4bc367", url="https://pypi.org/packages/e6/d7/930b670f75990f8fa5b2ad598b997d66afbf24b672ce504df224e6a4d760/idna-2.3-py2.py3-none-any.whl")
    version("2.2", sha256="16402893379702342a662d3f7fa7e9369e4b4770876b245dbbab1eb12d0a60cf", url="https://pypi.org/packages/6b/f4/bb42887fb16eb5f5957897fec9e16d18c56dd8cdd2a729c13947ed786b92/idna-2.2-py2.py3-none-any.whl")
    version("2.1", sha256="f28df695e9bede8a19b18a8e4429b4bad4d664e8e98aff27bc39b630f1ae2b42", url="https://pypi.org/packages/71/02/dee75fc3e6f7455bf69221164f94586ee13552c5f33c8002335667a3d122/idna-2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

