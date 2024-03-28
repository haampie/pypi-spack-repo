# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonargparse(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.27.7", sha256="9042339d1fc9f39b2ef61c0f9c4accd144db14a3aab9359e9b2e883d3af3740a", url="https://pypi.org/packages/c0/89/8ebd5bff5067063356c9b5b6253807cd768b57d97a3ed9c5a18f11e8cfe4/jsonargparse-4.27.7-py3-none-any.whl")
    version("4.27.6", sha256="f429b4a1b1fe92ef2e3e531615f53e81720a424f3f3181eca7a28c994515fc15", url="https://pypi.org/packages/c0/fe/ec7905ac3f1d93cf464039dab62196380852a03b4f860b279709ad98dcba/jsonargparse-4.27.6-py3-none-any.whl")
    version("4.27.5", sha256="95d1ff000efa759c171fca816685c1d1a66daab056fe30a73062a0fc4a734a05", url="https://pypi.org/packages/1a/dc/eb2ffcfbd529c3e6e9fe28d55b8663d2450370e6553f4f51cc89628efa2f/jsonargparse-4.27.5-py3-none-any.whl")
    version("4.27.4", sha256="15d1d1a19f29e3457147082289e229719698933cfeb3c513568810e1c5fbe87e", url="https://pypi.org/packages/fb/ee/a1fbe1eb2502379f731d7255a20fa0b830a3dc4089fe5d07aff028a4c428/jsonargparse-4.27.4-py3-none-any.whl")
    version("4.27.3", sha256="74c0f4ff60af074cc20b8693003cd16ccc249030980a131e7eca001d9f79ad1a", url="https://pypi.org/packages/cf/3b/d6c5108fa2451d7e9ade53670ca212b931153c06ed26652de1027ccc4ded/jsonargparse-4.27.3-py3-none-any.whl")
    version("4.27.2", sha256="b344ee8a50eb0911e405803658a80f49762723d244d00dbfb5b9273ed2ea3c05", url="https://pypi.org/packages/10/d9/f3856637f28ec31adb67ea18ddbb2d98d83175d84b2a94206cf947728836/jsonargparse-4.27.2-py3-none-any.whl")
    version("4.27.1", sha256="de11caf52174357589ee4570b45e37bd3c3c12b4f4823e4897b266ebfa31f625", url="https://pypi.org/packages/4c/e2/0fb56cd61f6d09c30ea93d3c51519b1fbfe0f4a258e756283fcf6f2bf059/jsonargparse-4.27.1-py3-none-any.whl")
    version("4.27.0", sha256="a6378bc8b7bbe38b708f090b10ea8431216e71f8b2eea1f9a4f095ae4abd0f2e", url="https://pypi.org/packages/c1/a6/e5d57cbcc05b08351f531231657affc43f36eebe668692168849d9bd6478/jsonargparse-4.27.0-py3-none-any.whl")
    version("4.26.2", sha256="5c7195e36cd9991aa4c1a9cf8a1cfd8bf5b7adc144eee8c4587eb8eb4e00d81c", url="https://pypi.org/packages/27/51/a836a62504ce5b118d719e59651876a54350cb5517015604a72dc6067c34/jsonargparse-4.26.2-py3-none-any.whl")
    version("4.26.1", sha256="7f5c3e5b8935b002be46d720192884780652b4fa058301a4d64d61976d94782f", url="https://pypi.org/packages/ef/8f/3a31ef7b8605ec995ab07e5f2a9b0acd5075573cb53e29a71b3f226fe352/jsonargparse-4.26.1-py3-none-any.whl")
    version("4.25.0", sha256="90719b4070de26a2677d23f374c1cf52f6b9dbfd479e7ee5b96f47da893ee5b5", url="https://pypi.org/packages/46/1a/1687c20b1c7aa9df40120b8faff067fce77bfdac215f9efbe3f39b7a6227/jsonargparse-4.25.0-py3-none-any.whl")
    version("4.19.0", sha256="f4377718317c6f7b42d437ea08a1833e6afda4ecf8a2d0704d21dff1f21017af", url="https://pypi.org/packages/88/32/a68ac6cc18194fa88a56b1e7920e1a96deee14e759a906d902275a86c301/jsonargparse-4.19.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("signatures", default=False)
    variant("typing-extensions", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docstring-parser@0.15:", when="@4.14:+signatures")
        depends_on("py-jsonschema@3.2:", when="@3:3.8+signatures")
        depends_on("py-pyyaml@3.13:")
        depends_on("py-typeshed-client@2.1:", when="@4.19:+signatures")
        depends_on("py-typing-extensions@3.10:", when="@4.21:+typing-extensions ^python@:3.9")

        # marker: os_name != "posix" and extra == "all"
        # depends_on("py-jsonnet-binary", when="@4.12:4.20")

        # marker: os_name != "posix" and extra == "jsonnet"
        # depends_on("py-jsonnet-binary", when="@4.12:")

        # marker: os_name == "posix" and extra == "all"
        # depends_on("py-jsonnet@0.13.0:", when="@4.12:4.20")

        # marker: os_name == "posix" and extra == "jsonnet"
        # depends_on("py-jsonnet@0.13.0:", when="@4.12:")

        # self-dependency
        # depends_on("py-jsonargparse+typing-extensions", when="@4.21:+signatures")
    # END DEPENDENCIES

