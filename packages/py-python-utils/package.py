# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.8.2", sha256="ad0ccdbd6f856d015cace07f74828b9840b5c4072d9e868a7f6a14fd195555a8", url="https://pypi.org/packages/26/45/98431ba6d17b99468bd3f4c53fdeefff402167f006a06773905296f6d489/python_utils-3.8.2-py2.py3-none-any.whl")
    version("3.8.1", sha256="efdf31c8154667d7dc0317547c8e6d3b506c5d4b6e360e0c89662306262fc0ab", url="https://pypi.org/packages/f0/7b/e83e7b184e53530abe064b237a3731c738d3cb59f4201f3ce1a4ec0efe6f/python_utils-3.8.1-py2.py3-none-any.whl")
    version("3.8.0", sha256="957295c68ee0ebc4b13e8b0f57fdf768b3e3c1fb8503cb0417a24f4aa88cd1b8", url="https://pypi.org/packages/ef/fc/692d11fe9bc8625f46064c1dd26445d0e0d87a4e0514d78b26163ab81f47/python_utils-3.8.0-py2.py3-none-any.whl")
    version("3.7.0", sha256="e31c1187168c314c984932e99c2d3f973465443493869ae041dd9e2e18e998aa", url="https://pypi.org/packages/dc/68/95b72e9f9bf5c00f9e6db5e0876e748daa9a9bc82395479ae0c495c3cadf/python_utils-3.7.0-py2.py3-none-any.whl")
    version("3.6.1", sha256="d7dbc0dc3ca4450fc2c119b6076bab0a3dbddf3ad1709c5babb2e3a90c9f6456", url="https://pypi.org/packages/a7/b5/41adc2c85895505adde8d05cd7e3c641aa7081050870751e1cc5cba416fc/python_utils-3.6.1-py2.py3-none-any.whl")
    version("3.6.0", sha256="c6980fda703aa4c1b5d774b9c11da211f6a69af77f445c0e805f05909c9078b3", url="https://pypi.org/packages/2a/b7/b4c74eda021126e7167622c6af48bd5770d8e6d9867d3b8bc67640ef1edd/python_utils-3.6.0-py2.py3-none-any.whl")
    version("3.5.2", sha256="8bfefc3430f1c48408fa0e5958eee51d39840a5a987c2181a579e99ab6fe5ca6", url="https://pypi.org/packages/79/80/4276fba30da6ed26165b67093ce4a2ca78b701a55920d39e59cc82ee9639/python_utils-3.5.2-py2.py3-none-any.whl")
    version("3.5.1", sha256="fbe7ca2ee8f51613c76768fc7c24df683fa5ac28eed5a2769a942d513fc0ab65", url="https://pypi.org/packages/f1/cc/18c3bbafd5f4349c1d50405d5ccd9ba60d9e2b42f4a795e550ca67c36ac7/python_utils-3.5.1-py2.py3-none-any.whl")
    version("3.5.0", sha256="c6ef380fc3f9d8d425f6bf97323d17b060ff0722823264261a6d9055cdd7d879", url="https://pypi.org/packages/7e/64/049b9560156cc955bf436f7ed8c15d8279b4cb745328120f6a980d346e40/python_utils-3.5.0-py2.py3-none-any.whl")
    version("3.4.5", sha256="22990259324eae88faa3389d302861a825dbdd217ab40e3ec701851b3337d592", url="https://pypi.org/packages/45/8a/d5656afa0aac6cc7d34bbd0a9eb7730302e435e48441030009a240ab12a0/python_utils-3.4.5-py2.py3-none-any.whl")
    version("2.7.1", sha256="9d535eda3fd4c0cd51f459bb9cfddd983a50f5adfacb0995504d12bf0c2981cb", url="https://pypi.org/packages/0a/c2/962e0ec22173309d8914733dc78cf8a689fe2ae612938ec64c26d0f29ac6/python_utils-2.7.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="ebaadab29d0cb9dca0a82eab9c405f5be5125dbbff35b8f32cc433fa498dbaa7", url="https://pypi.org/packages/d9/ff/623dfa533f3277199957229f053fdb2c73a9c18048680e1899c9a5c95e6b/python_utils-2.4.0-py2.py3-none-any.whl")
    version("2.3.0", sha256="e25f840564554eaded56eaa395bca507b0b9e9f0ae5ecb13a8cb785305c56d25", url="https://pypi.org/packages/eb/a0/19119d8b7c05be49baf6c593f11c432d571b70d805f2fe94c0585e55e4c8/python_utils-2.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@3.6:")
        depends_on("py-six", when="@2.6:2")
        depends_on("py-typing-extensions@4:", when="@3.6.1:")
        depends_on("py-typing-extensions", when="@3.6:3.6.0")
    # END DEPENDENCIES

