##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyaml(PythonPackage):
    version("23.12.0", sha256="90407d74c95a55d9b41d3860fcc1759640444d2795df748a328d077bc4f58393", url="https://pypi.org/packages/25/ec/8aaf0d127751f84d8b10395fe47def9ac3552990b70abffdd92714836d39/pyaml-23.12.0-py3-none-any.whl")
    version("23.9.7", sha256="fdb4c111b676d2381d1aa88c378fcde46c167575dfd688e656977a77075b692c", url="https://pypi.org/packages/7e/ed/b5f644b7a1de2e966345e60dacc040d98371213df6ae4070ba19280ae6d4/pyaml-23.9.7-py3-none-any.whl")
    version("23.9.6", sha256="9dcc67922b7278f3680e573324b2e8a8d2f86c5d09bf640cba83735fb1663e97", url="https://pypi.org/packages/56/db/01bc52d991716ccac7366b6e763fdaaf7b57910dbc2f85466c997f915284/pyaml-23.9.6-py3-none-any.whl")
    version("23.9.5", sha256="e426cd4d1dfa3a6d4c3f177d421662b1249665151bc01f80d3e6bbb110b0427a", url="https://pypi.org/packages/3a/a4/9f3e2afe7340232fb6762d4108e8b22ae2dfe868e060997bf8a9aa02d883/pyaml-23.9.5-py3-none-any.whl")
    version("23.9.4", sha256="0b6f13bfaf50c8a3e19d2a6974c56170d08d8d90dd7b8bf7dced24d2091cb9d7", url="https://pypi.org/packages/16/94/0d281a2138dbbbb11b3802ea36c2c45606333cf03b1050dfa6c8e94af544/pyaml-23.9.4-py3-none-any.whl")
    version("23.9.3", sha256="4b364804fe50d7b031904f37ab58cd744d48a406e9d7617bcf339b970eb00dc5", url="https://pypi.org/packages/43/57/868c5a656ff1e2d24948840d610f7cb92c31bf04208ea610349a9f69f963/pyaml-23.9.3-py3-none-any.whl")
    version("23.9.2", sha256="66dbd8652103866c7f004e2575d97e2d9805ddbfb33588b0d7e30f18bd7c808c", url="https://pypi.org/packages/fb/88/4b7ea32cca1419277260db8a058117e9cdc9ae1fc52b50466940b1ccf544/pyaml-23.9.2-py3-none-any.whl")
    version("23.9.1", sha256="bb7daf311c59891671a5c816973cd15734e545b1a01514a39bce7d68a61d8c86", url="https://pypi.org/packages/fd/12/7caf83557690bd0ef5597e454dea9d977fb21e8019603b7624ffb3c0e2ba/pyaml-23.9.1-py3-none-any.whl")
    version("23.9.0", sha256="e1d88be0b8198fcd1cfc528f0324b18d8a98a99fbc3288a103a7c3b5bfc6a925", url="https://pypi.org/packages/dd/06/3d0a6de9de92b2f024214b7c74452c9d436e6fe764845d7239c8544135dd/pyaml-23.9.0-py3-none-any.whl")
    version("23.7.0", sha256="0a37018282545ccc31faecbe138fda4d89e236af04d691cfb5af00cd60089345", url="https://pypi.org/packages/9e/50/bd36e3abbab7db2a9d33a71540266189d036177cf7932d5465328ec851e8/pyaml-23.7.0-py3-none-any.whl")
    version("21.8.3", sha256="aa61d6ebef7cd8ec691620616258d904bfbc152e9cf44557202b8bacc9ce5cce", url="https://pypi.org/packages/7b/33/12e2e89527df0e1f5bc07f94a039b981cc4a15f040f29a6cc978f8f99dd4/pyaml-21.8.3-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyyaml", when="@21:")

