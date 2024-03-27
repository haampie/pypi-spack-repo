##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGradioClient(PythonPackage):
    version("0.13.0", sha256="f47225bb274834a33a297b5bba95250b63a76ae9f90217631e1e29e90cd857f1", url="https://pypi.org/packages/93/4e/a9b8251a0d6eeb10e16a069eeb44ff9de87e1b8ebe5cea2b25e86d3ef076/gradio_client-0.13.0-py3-none-any.whl")
    version("0.12.0", sha256="ead1d3016cd42e9275cf62dd3227ab4472d4093da1a1c6c3c0fe6ca516e9d31f", url="https://pypi.org/packages/cd/4d/5b430cc0fbb19b20368e9cd791700270c9551dab7234e6501b1587c414de/gradio_client-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="638a43ccc73937790a3c68adb732da03ee7077732a0b6540a9196bacbb1f6539", url="https://pypi.org/packages/56/12/961688d564c46d43bc08d8851b2cd23150a1e4c7a1d0bf6fc1f3edadcf7d/gradio_client-0.11.0-py3-none-any.whl")
    version("0.10.1", sha256="a0413fffdde3360e0f6aaec8b8c23d8a320049a571de2d111d85ebd295002165", url="https://pypi.org/packages/68/ae/ef4a28fac1aca895a2abbf99a14b11d46bdccc735943e50b12e95fa3eb9d/gradio_client-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="2bcfe61710f9f1c8f336fa9ff0f5c5f0ea52079233196cd753ad30cccdfd585c", url="https://pypi.org/packages/85/7c/956b96c8bd76ae19bf40ef477f7631336cc5728edbb3b4304f81e7a84e2a/gradio_client-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="b6696135d03471257cfd26eeb963c1360ccc68a76c2009563966629aadf19f58", url="https://pypi.org/packages/e5/3d/4e491cdd9b9b7e74361dc53a4a0f4ba3e421091bb95bc75701b2d34091bc/gradio_client-0.9.0-py3-none-any.whl")
    version("0.8.1", sha256="5a987492905314baf64b50bc12319d8208bbe23bd0c6fb4c2dcd4d9a8825fb56", url="https://pypi.org/packages/55/25/caf754ea7959ad12bdb08aabcda88c4092ce0210004f4f81f58c9965c871/gradio_client-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="0d817e9ff72fc1ba0866c11612a2b1c995d370ab7ea0fbf2bd0649e6da49ad76", url="https://pypi.org/packages/c4/e7/5da3a4b6108f5e2e43d034d7923c3562f93beba8f3d13a0ec7c201a6f33c/gradio_client-0.8.0-py3-none-any.whl")
    version("0.7.3", sha256="b91073770470ceb9f284977064c35bc0cffaf868eb887bf352db77aa01fe342a", url="https://pypi.org/packages/78/52/a96eada27a2f711464c4a8c85a6110d46e35034cd2108640980c1fa4e8bb/gradio_client-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="29014b281db3d2dacecbc4cd9979dd335b3b6511d40af04edfeb4ce409ef15b1", url="https://pypi.org/packages/28/f9/e9a1a40327bde4091a1a73f2a20c88bb95f108687cb32dc8949249c0e2c9/gradio_client-0.7.2-py3-none-any.whl")
    version("0.2.9", sha256="9174476e8965b6f622a4426d631c1c29f2209329f110242278fcb6ad26f813d5", url="https://pypi.org/packages/fc/be/50b4ba7b5ab067e31b67526f9cdbdd2241854af2f6b205f678c9da316ac9/gradio_client-0.2.9-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-fsspec")
        depends_on("py-httpx@0.24.1:", when="@0.10.1:")
        depends_on("py-httpx", when="@0.0.9:0.10.0")
        depends_on("py-huggingface-hub@0.19.3:", when="@0.7.2:")
        depends_on("py-huggingface-hub@0.13.0:", when="@0.0.5:0.7.1")
        depends_on("py-packaging")
        depends_on("py-requests", when="@:0.2.9")
        depends_on("py-typing-extensions@4:", when="@0.2.10:")
        depends_on("py-typing-extensions", when="@0.0.6-beta10,0.0.7:0.2.9")
        depends_on("py-websockets@10:11", when="@0.2.10:")
        depends_on("py-websockets", when="@:0.2.9")

