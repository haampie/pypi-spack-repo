##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyConfection(PythonPackage):
    version("0.1.5-alpha0", sha256="e4f81fdcc0b5c513245e47ece99606c54d60e95bfad3148e34c100406126cea0", url="https://pypi.org/packages/a6/b4/00f611b95f1404212a75b59930b93bf696431408438fb44f5bf9d1d37f09/confection-0.1.5a0-py3-none-any.whl")
    version("0.1.4", sha256="a658818d004939069c3e2b3db74a2cb9d956a5e61a1c9ad61788e0ee09a7090f", url="https://pypi.org/packages/39/78/f9d18da7b979a2e6007bfcea2f3c8cc02ed210538ae1ce7e69092aed7b18/confection-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="58b125c9bc6786f32e37fe4d98bc3a03e5f509a4b9de02541b99c559f2026092", url="https://pypi.org/packages/93/f8/e89268a1f885048fb2ee6b5c9f93c4e90de768534acfef3652f87d97d4cb/confection-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="8bde19143fe36c38ea6e7241dec7be14b8a16e51c9d7ade93d19f72d9f8f1115", url="https://pypi.org/packages/ce/a3/21634c476fd55f06f5c31876985da59024fab75a537b0398aa4039e4e730/confection-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="d2d9e53a5a61395caae1ab09281bab17b08a23fa94aabd1cc24c134880d41c30", url="https://pypi.org/packages/05/5e/1a56e81e3335ce18f6742539edd2f6ea98bbf477fefc9a4dc5c0694bace4/confection-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="1d6de16297efe937efaad13f83f45467dedc05acafdb0fb16074299a9c683d85", url="https://pypi.org/packages/63/05/2d7acb83610e0c5171dfcb4a2968d676800da8082fc456e284fa8e0924f4/confection-0.1.0-py3-none-any.whl")
    version("0.0.4", sha256="aeac5919ba770c7b281aa5863bb6b0efed42568a7ad8ea26b6cb632154503fb2", url="https://pypi.org/packages/b1/c4/07291f4947d20f545eee76ef20d1eacfb1f80d1d6ab4792bfa6797e0578c/confection-0.0.4-py3-none-any.whl")
    version("0.0.3", sha256="51af839c1240430421da2b248541ebc95f9d0ee385bcafa768b8acdbd2b0111d", url="https://pypi.org/packages/36/9f/03c9137e34b3064f0eba298340d00a8dd4719c0b7021704187a7ddf1e382/confection-0.0.3-py3-none-any.whl")
    version("0.0.2", sha256="20663e54b472d77f2add23c2bc2ecad33b9fcb3c3679d303b74003ad45ff5927", url="https://pypi.org/packages/c9/41/a05cccafe74d2acc64dfdd5908a15dc2f502a5741d984ac3ce1abcfc217f/confection-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="e4b43ee84af1c2088726d7b91d4b6b958a6d6d5cc374108742a6db585b93ee44", url="https://pypi.org/packages/ed/e6/32f079bbfc92a60db21b269bee49d442eb94acb54bd8ce30bdb3a8daeaa0/confection-0.0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:", when="@0.1.1:")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:1", when="@0.0.3:0.1.0")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:1.9", when="@0.0.1:0.0.2")
        depends_on("py-srsly@2.4:2.4.0.0,2.4.1:", when="@0.0.1:")

