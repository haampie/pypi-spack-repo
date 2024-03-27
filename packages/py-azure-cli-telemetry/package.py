##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureCliTelemetry(PythonPackage):
    version("1.1.0", sha256="2fc12608c0cf0ea6e69b392af9cab92f1249340b8caff7e9674cf91b3becb337", url="https://pypi.org/packages/7e/23/5940808a891282e7fdd240d689aedc91bc945b4eb653c15e694f45a4babc/azure_cli_telemetry-1.1.0-py3-none-any.whl")
    version("1.0.8.post20221028041827", sha256="6c5d26af05136048a3d8fe8a056b329169643e4e4cffe120ec1f39e888f7de04", url="https://pypi.org/packages/a1/4b/a69789e61e83bbc4334a7b29be6af58b4d40866d7697937c204e7048ef4e/azure_cli_telemetry-1.0.8.post20221028041827-py3-none-any.whl")
    version("1.0.8", sha256="502cbd90723a16603822909befd096ca0b1707de1e70cf730e7b4700ddd7a456", url="https://pypi.org/packages/8d/3a/5e8c5a923aea492384342254bad0eecf054b62bdee168fa63963066c365e/azure_cli_telemetry-1.0.8-py3-none-any.whl")
    version("1.0.7", sha256="d6b7ef6ec84290b1074314dbdbc3865f736462db21d3ad299f2202c2a929f3ab", url="https://pypi.org/packages/4b/da/197a4607b32708315c7d2a056aae6682462f14132d878ba55a9b98cbcda1/azure_cli_telemetry-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="05c11939b8ed9a98b8bad1d0201909ff7c33671aaa4a98932069594e815aefbe", url="https://pypi.org/packages/c7/2a/5a603f9d9c96a06dd0994ca4c511454a1c7984ef111711b93394edd2bcf9/azure_cli_telemetry-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="4b0b9ceef4bd21b9266f9abf7c5b4e184cbe0c087f73cb23c6b3bdb48d48ffe5", url="https://pypi.org/packages/7d/e5/efcd553907d7f83702bd5ae803e24911bc91348171962b93d1d28bc675bd/azure_cli_telemetry-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="421e80c2fe3fdff8c38d27ee1fdfdfef1326c79212d6e23a6ebe308d19df552a", url="https://pypi.org/packages/f9/eb/4137d6cf4c91c135260dbf566b5fc8fc6d427b3f807523e388dc030dcc65/azure_cli_telemetry-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="39a006a054d9b7c04eae06476a7e078c17b23f3d6eab155276dfadddb01310cc", url="https://pypi.org/packages/e1/74/5d77fada646ba77626fd427f49616dedc9dffa45a192e520e6eeb62e8a22/azure_cli_telemetry-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="946de5b922e3183be13afe348eae6691883d6694ff43806752662e661757de4c", url="https://pypi.org/packages/08/e8/5d56f3527c0db6a9e7ba8f52a0773b5e896ad3d097cafdd153e84c193cae/azure_cli_telemetry-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="45c02276c571b8e87bb8e8f9111b97dd542d18127ca9e8d667c7e963f3b9c106", url="https://pypi.org/packages/e0/6b/bc6faa2f578b53888e383138fd22bb04dc3aea5718292dd5543ac0898d80/azure_cli_telemetry-1.0.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-applicationinsights@0.11.1:0.11.7", when="@1.0.2")
        depends_on("py-applicationinsights@0.11.1:", when="@:1.0.1,1.0.3:")
        depends_on("py-azure-cli-nspkg@2:", when="@:1.0.4")
        depends_on("py-portalocker@1.6:", when="@1.0.7:")
        depends_on("py-portalocker@1.2:1", when="@1.0.3:1.0.6")
        depends_on("py-portalocker@1.2.1:1.2", when="@:1.0.2")

