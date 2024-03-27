##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRedis(PythonPackage):
    version("5.1.0-beta4", sha256="8a74fae7cbd25493142c8cc2f79c21b2e3c03bf85dd3525a1db9f33ff47a3f2d", url="https://pypi.org/packages/43/47/5b0c2ccdb0d6b727550f51a79eb1e6d13ab2ec5019ddb3ae364e6e1bde3e/redis-5.1.0b4-py3-none-any.whl")
    version("5.1.0-beta3", sha256="8e83465ce69eb7b86b96d4e793ad1a8888d368815e47f1f6081d2d65d655a89c", url="https://pypi.org/packages/6b/13/72a07ba11d68b7d0c036b8bc7f9c39edc7651a739f5145477a7b694a8841/redis-5.1.0b3-py3-none-any.whl")
    version("5.0.3", sha256="5da9b8fe9e1254293756c16c008e8620b3d15fcc6dde6babde9541850e72a32d", url="https://pypi.org/packages/bb/f1/a384c5582d9a28e4a02eb1a2c279668053dd09aafeb08d2bd4dd323fc466/redis-5.0.3-py3-none-any.whl")
    version("5.0.2", sha256="4caa8e1fcb6f3c0ef28dba99535101d80934b7d4cd541bbb47f4a3826ee472d1", url="https://pypi.org/packages/63/c9/7e8397d1eedaadcd2fbcbbd34b1373c08743ebb475a0afda7089df6bb646/redis-5.0.2-py3-none-any.whl")
    version("5.0.1", sha256="ed4802971884ae19d640775ba3b03aa2e7bd5e8fb8dfaed2decce4d0fc48391f", url="https://pypi.org/packages/0b/34/a01250ac1fc9bf9161e07956d2d580413106ce02d5591470130a25c599e3/redis-5.0.1-py3-none-any.whl")
    version("5.0.0", sha256="06570d0b2d84d46c21defc550afbaada381af82f5b83e5b3777600e05d8e2ed0", url="https://pypi.org/packages/df/b2/dfdc17f701f7b587f6c89c2b9b6b5978c87a8a785555efc810b064c875de/redis-5.0.0-py3-none-any.whl")
    version("4.6.0", sha256="e2b03db868160ee4591de3cb90d40ebb50a90dd302138775937f6a42b7ed183c", url="https://pypi.org/packages/20/2e/409703d645363352a20c944f5d119bdae3eb3034051a53724a7c5fee12b8/redis-4.6.0-py3-none-any.whl")
    version("4.5.5", sha256="77929bc7f5dab9adf3acba2d3bb7d7658f1e0c2f1cafe7eb36434e751c471119", url="https://pypi.org/packages/e0/7f/21a09f8c9f5db6f5e24432f7a0f916ca386025d74e4da6d0f5164aa9a78a/redis-4.5.5-py3-none-any.whl")
    version("4.5.4", sha256="2c19e6767c474f2e85167909061d525ed65bea9301c0770bb151e041b7ac89a2", url="https://pypi.org/packages/b5/d4/ef474a49ec5821f3155c5de2d37ddcc4a497e2500cd16d4a9e51ce02030d/redis-4.5.4-py3-none-any.whl")
    version("4.5.3", sha256="7df17a0a2b72a4c8895b462dd07616c51b1dcb48fdd7ecb7b6f4bf39ecb2e94e", url="https://pypi.org/packages/2e/77/fd2dafad569c22459c172267aeb2b2002c3bfad2c8cda09fdf878bbbad09/redis-4.5.3-py3-none-any.whl")
    version("4.5.2", sha256="4b12b3a1e9bfb43dc533330ec6d142329d0c27ea6bb6716a9d0389e8f2038a4e", url="https://pypi.org/packages/1f/ec/a64e0e8d74c68eef15aac1cb88737f7c023cd8342340ef52e1d2fe3b30ff/redis-4.5.2-py3-none-any.whl")
    version("4.5.1", sha256="5deb072d26e67d2be1712603bfb7947ec3431fb0eec9c578994052e33035af6d", url="https://pypi.org/packages/06/b5/328851ee54bbf00cc609671a658e0420d88aa2b4f5ace7aa669932d59a0e/redis-4.5.1-py3-none-any.whl")
    version("3.5.3", sha256="432b788c4530cfe16d8d943a09d40ca6c16149727e4afe8c2c9d5580c59d9f24", url="https://pypi.org/packages/a7/7c/24fb0511df653cf1a5d938d8f5d19802a88cef255706fdda242ff97e91b7/redis-3.5.3-py2.py3-none-any.whl")
    version("3.5.0", sha256="174101a3ce04560d716616290bb40e0a2af45d5844c8bd474c23fc5c52e7a46a", url="https://pypi.org/packages/d2/07/20cb8df2ded4b5db176a65da48b7c8d4295d868776296580b11071218a2b/redis-3.5.0-py2.py3-none-any.whl")
    version("3.3.8", sha256="c504251769031b0dd7dd5cf786050a6050197c6de0d37778c80c08cb04ae8275", url="https://pypi.org/packages/bd/64/b1e90af9bf0c7f6ef55e46b81ab527b33b785824d65300bb65636534b530/redis-3.3.8-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-async-timeout@4.0.3:", when="@5.0.3:5.0 ^python@:3.11.2")
        depends_on("py-async-timeout@4.0.3:", when="@5.0.2,5.1.0-beta3:")
        depends_on("py-async-timeout@4.0.2:", when="@4.5.4:4,5.0.0-rc2:5.0.1,5.1:5.1.0-beta2 ^python@:3.11.2")
        depends_on("py-async-timeout@4.0.2:", when="@4.5.2:4.5.3,5:5.0.0-rc1 ^python@:3.10")
        depends_on("py-async-timeout@4.0.2:", when="@4.2:4.5.1")

