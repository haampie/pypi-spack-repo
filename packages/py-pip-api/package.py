# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPipApi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.33", sha256="b8d6eb5a87d3a9e112a20a8e9d24a6fc12d4e1c94d7595eeaf74be11ad47276c", url="https://pypi.org/packages/d5/a5/ecff8712be393a0d9c221e036082163b69d491f99b7772d37b935cb078d6/pip_api-0.0.33-py3-none-any.whl")
    version("0.0.30", sha256="2a0314bd31522eb9ffe8a99668b0d07fee34ebc537931e7b6483001dbedcbdc9", url="https://pypi.org/packages/05/c8/d319552f0ef7af0cb57c80be8c8181184ab66a205d18b4574214b0940ba1/pip_api-0.0.30-py3-none-any.whl")
    version("0.0.29", sha256="36c3211975e69c46c1d3b13b702dcc96d054d54e02147b1485300cf5fc45c1a0", url="https://pypi.org/packages/f6/70/48d87f6f5f05940cc56fa6a8a3ec7a10308bda14f7476cfe31b9ab993d4c/pip_api-0.0.29-py3-none-any.whl")
    version("0.0.28", sha256="68631896064751baad4b6fc675bc1281a4aa930453f9c6a71b6c0de7aaf095c4", url="https://pypi.org/packages/43/d8/6509a48e4c4301838ed52644085401b118ad1bb17de532fed2d151c63133/pip_api-0.0.28-py3-none-any.whl")
    version("0.0.27", sha256="da0a10870b9105bc7ff7f347793db885c5c30102032de9112a6118b7af645478", url="https://pypi.org/packages/67/43/92f9d2cb310336ac32296c3b0a3788efd6df941d376f11d380d37b567e46/pip_api-0.0.27-py3-none-any.whl")
    version("0.0.26", sha256="b24e94e5d5d3f161a2db49653798e6a4c1f0ed6b379e511b45a8fa57c185d711", url="https://pypi.org/packages/00/f8/cf02ee8bcc8a39ad2e2992468fd6a6998795f4af9173090f6aaff8175318/pip_api-0.0.26-py3-none-any.whl")
    version("0.0.25", sha256="cd188cbcf20c387b73236e64b0ade5545e6e211ab003be35283aeacf36091f3f", url="https://pypi.org/packages/b8/3e/c79ab5a3f609fd326a270fead01dc6519f21cb2e5e9ef85e621afeaeb46c/pip_api-0.0.25-py3-none-any.whl")
    version("0.0.24", sha256="00acc1e6e6da4399029298ae44e7387e1be17cecb3d3bc03ac0a691096530bfb", url="https://pypi.org/packages/7c/9e/91d9e21a1e6d8a805e239e07c198f8e0e51470e9ccb285ddafdcbfc5dec9/pip_api-0.0.24-py3-none-any.whl")
    version("0.0.23", sha256="e313fa77454148ac8b3c7d7480141039c3a5d1f9680cd79a5a1ecae12c2d03ac", url="https://pypi.org/packages/e8/28/b6b91e2dd3dbc964db396650703b922d5f0047a32c7f1af5c3c6c662b5cb/pip_api-0.0.23-py3-none-any.whl")
    version("0.0.22", sha256="07dd637640cf5a1056f9dc24de50c67dee833d6bba797c4b4b3db9a89706a2d5", url="https://pypi.org/packages/8d/be/2dbb5102d2e450a78a219dcc76b0cb9123b16fdc4922e11f49eca3288669/pip_api-0.0.22-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pip", when="@0.0.3:")
    # END DEPENDENCIES

