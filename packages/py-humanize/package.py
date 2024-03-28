# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHumanize(PythonPackage):
    # BEGIN VERSIONS
    version("4.9.0", sha256="ce284a76d5b1377fd8836733b983bfb0b76f1aa1c090de2566fcf008d7f6ab16", url="https://pypi.org/packages/aa/2b/2ae0c789fd08d5b44e745726d08a17e6d3d7d09071d05473105edc7615f2/humanize-4.9.0-py3-none-any.whl")
    version("4.8.0", sha256="8bc9e2bb9315e61ec06bf690151ae35aeb65651ab091266941edf97c90836404", url="https://pypi.org/packages/4a/52/cccfc7a0d3bcf52cca6f6e1792786075df979346d638bf4cf5bc8bf2be3c/humanize-4.8.0-py3-none-any.whl")
    version("4.7.0", sha256="df7c429c2d27372b249d3f26eb53b07b166b661326e0325793e0a988082e3889", url="https://pypi.org/packages/5e/81/60bbbb745b397fa56b82ec71ecbada00f574319b8f36c5f53c6c0c0c0601/humanize-4.7.0-py3-none-any.whl")
    version("4.6.0", sha256="401201aca462749773f02920139f302450cb548b70489b9b4b92be39fe3c3c50", url="https://pypi.org/packages/22/2b/30e8725481b071ca53984742a443f944f9c74fb72f509a40b746912645e1/humanize-4.6.0-py3-none-any.whl")
    version("4.5.0", sha256="127e333677183070b82e90e0faef9440f9a16dab92143e52f4523afb08ca9290", url="https://pypi.org/packages/ab/bf/4e526ef224ca00f0a2f14513895c8a728aa94682ebbe756447de41230baa/humanize-4.5.0-py3-none-any.whl")
    version("4.4.0", sha256="8830ebf2d65d0395c1bd4c79189ad71e023f277c2c7ae00f263124432e6f2ffa", url="https://pypi.org/packages/9d/fc/28d2b631c5220b2a594d5d13b6ad79ee60d50688f1cd43f6707c06fb0db4/humanize-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="5dd159c9910cd57b94072e4d7decae097f0eb84c4645153706929a7f127cb2ef", url="https://pypi.org/packages/b6/92/7caf90478ead425a31e6c765a13c5525c527ff2dad57997b2863220996ce/humanize-4.3.0-py3-none-any.whl")
    version("4.2.3", sha256="bed628920d45cd5018abb095710f0c03a8336d6ac0790e7647c6a328f3880b81", url="https://pypi.org/packages/12/b0/da61e315115d563f8ef098836c237f1de723aa434b0ffbfd2290b165985a/humanize-4.2.3-py3-none-any.whl")
    version("4.2.2", sha256="fd36c627eee0d2cea22a1dee6d4ff8d4ad5a0b03d3184a4c42967945fa350215", url="https://pypi.org/packages/7f/51/92d69a10dd61f8ad1ae01e13feca0b7faee25fa17ee8bd181cc1dd459d4f/humanize-4.2.2-py3-none-any.whl")
    version("4.2.1", sha256="895af56cfc63e1d453df6899d3f13861ecdef23e02407d2a84741561210416da", url="https://pypi.org/packages/4f/fd/dd6a8f629227945f3f2f70e8c87148edd47a31764f4e7323597a2923564f/humanize-4.2.1-py3-none-any.whl")
    version("4.0.0", sha256="8d86333b8557dacffd4dce1dbe09c81c189e2caf7bb17a970b2212f0f58f10f2", url="https://pypi.org/packages/89/8a/eea987b881522536af2a8fc008214a2bf1ac14b61ae483643165cedbbf35/humanize-4.0.0-py3-none-any.whl")
    version("3.12.0", sha256="4c71c4381f0209715cd993058e717c1b74d58ae2f8c6da7bdb59ab66473b9ab0", url="https://pypi.org/packages/fd/5e/9840102591431f86c2e99c5a8e4f18bb399f9f2e982b0dbba87c98ae800f/humanize-3.12.0-py3-none-any.whl")
    version("0.5.1", sha256="a43f57115831ac7c70de098e6ac46ac13be00d69abbf60bdcac251344785bb19", url="https://pypi.org/packages/8c/e0/e512e4ac6d091fc990bbe13f9e0378f34cf6eecd1c6c268c9e598dcf5bb9/humanize-0.5.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@3:3.12")
    # END DEPENDENCIES

