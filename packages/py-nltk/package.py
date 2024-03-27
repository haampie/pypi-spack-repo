##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNltk(PythonPackage):
    version("3.8.1", sha256="fd5c9109f976fa86bcadba8f91e47f5e9293bd034474752e92a520f81c93dda5", url="https://pypi.org/packages/a6/0a/0d20d2c0f16be91b9fa32a77b76c60f9baf6eba419e5ef5deca17af9c582/nltk-3.8.1-py3-none-any.whl")
    version("3.8", sha256="3306502f487aa9fb0566e23443fa287a85a8d8d0821e2ef1655b4e3f0ea4aeee", url="https://pypi.org/packages/35/45/64f4abaa5b36b698aaeb556ae6dc533e57a6b9e72ac6fc7f0d7f9cb15bb4/nltk-3.8-py3-none-any.whl")
    version("3.7", sha256="ba3de02490308b248f9b94c8bc1ac0683e9aa2ec49ee78536d8667afb5e3eec8", url="https://pypi.org/packages/43/0b/8298798bc5a9a007b7cae3f846a3d9a325953e0f9c238affa478b4d59324/nltk-3.7-py3-none-any.whl")
    version("3.6.7", sha256="22e97be5d6c784d93a52d17860515cc50c5cfcc620b1f5c3747765041255a01e", url="https://pypi.org/packages/c5/ea/84c7247f5c96c5a1b619fe822fb44052081ccfbe487a49d4c888306adec7/nltk-3.6.7-py3-none-any.whl")
    version("3.6.6", sha256="69470ba480ff4408e8ea82c530c8dc9571bab899f49d4571e8c8833e0916abd0", url="https://pypi.org/packages/90/35/8848a41a983a923aa2496fbe4ee4df796c6b32b2a59f04c2b2047aafd3c3/nltk-3.6.6-py3-none-any.whl")
    version("3.6.5", sha256="95fb4f577efe93af21765e9b2852235c2c6a405885da2a70f397478d94e906e0", url="https://pypi.org/packages/aa/b8/09ac15436591cefc0adc882798d5cf629f13addae0495b20b682219e3afe/nltk-3.6.5-py3-none-any.whl")
    version("3.6.4", sha256="2b9a54bbd2142282cb41aa4b25b8a356bb96f032f509302b4cca9992eda6e793", url="https://pypi.org/packages/e7/b0/6a693aa7ddef9d5e921827fdafc264aca130f40d38adcaf71332b222d29f/nltk-3.6.4-py3-none-any.whl")
    version("3.6.3", sha256="665225d585367f64a73ff1cb436964b425304dc772406653412e19dfe0157688", url="https://pypi.org/packages/5e/a0/04763ddc4bf3bac6f3bd38934c36a0f3ac30e48c39a51b3ec5649ed17374/nltk-3.6.3-py3-none-any.whl")
    version("3.5", sha256="845365449cd8c5f9731f7cb9f8bd6fd0767553b9d53af9eb1b3abf7700936b35", url="https://pypi.org/packages/92/75/ce35194d8e3022203cca0d2f896dbb88689f9b3fce8e9f9cff942913519d/nltk-3.5.zip")
    version("3.4.5", sha256="bed45551259aa2101381bbdd5df37d44ca2669c5c3dad72439fa459b29137d94", url="https://pypi.org/packages/f6/1d/d925cfb4f324ede997f6d47bea4d9babba51b49e87a767c170b77005889d/nltk-3.4.5.zip")

    with default_args(type="run"):
        depends_on("py-click", when="@3.6:")
        depends_on("py-joblib", when="@3.6:")
        depends_on("py-regex@2021.8:", when="@3.6.5:")
        depends_on("py-regex", when="@3.6:3.6.4")
        depends_on("py-tqdm", when="@3.6:")

