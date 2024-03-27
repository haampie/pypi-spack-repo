##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleApiPythonClient(PythonPackage):
    version("2.122.0", sha256="a5953e60394b77b98bcc7ff7c4971ed784b3b693e9a569c176eaccb1549330f2", url="https://pypi.org/packages/90/82/eeffa2e210482ac66ecfca2f08e89184111a29ea5865970b22ff7e0f0113/google_api_python_client-2.122.0-py2.py3-none-any.whl")
    version("2.121.0", sha256="bb4da677150dd16c45818620baca8a63208c6f4180a0691ad1c1708b384c10be", url="https://pypi.org/packages/c6/5a/8285f25d8bfe1586cf543e816e4c371e8c01826af49ef8a0d098b2cfa32c/google_api_python_client-2.121.0-py2.py3-none-any.whl")
    version("2.120.0", sha256="e2cdf4497bfc758fb44a4b487920cc1ca0571c2428187697a8e43e3b9feba1c9", url="https://pypi.org/packages/9a/3d/1709ca24b093d37aa3233b78161a6d96d190922408041a6fea9df9c78646/google_api_python_client-2.120.0-py2.py3-none-any.whl")
    version("2.119.0", sha256="84e43bdb58dd8d2301669513863996378ffe9a3bf6d23b5ccd4f1e021323dbeb", url="https://pypi.org/packages/f5/f0/7ee7c16b34e6e22e50010ba3c350c8a7ac9a02550de2933bea11c71e2658/google_api_python_client-2.119.0-py2.py3-none-any.whl")
    version("2.118.0", sha256="9d83b178496b180e058fd206ebfb70ea1afab49f235dd326f557513f56f496d5", url="https://pypi.org/packages/be/c6/edbba414d1c87a47fb24813de7baa1e92615905d15d62affba1dbfb5df40/google_api_python_client-2.118.0-py2.py3-none-any.whl")
    version("2.117.0", sha256="bd6d393d0eaa7ea1fa13aefb44be787d1ebdc068ab8255f1c3f1d8b486f46afd", url="https://pypi.org/packages/15/ef/e5515c6eab9eb5dda9b33ec17b8d43c1e71eb063642f5684bbfc4ddc038d/google_api_python_client-2.117.0-py2.py3-none-any.whl")
    version("2.116.0", sha256="846e44417c6b7385fa5f5a46cb6b9d23327754c560830245ee53a577c5e44cec", url="https://pypi.org/packages/73/e4/d8d38ca79045a72880c98e6d2ebc737c92d596d5dc0bf2e4233b00be5daa/google_api_python_client-2.116.0-py2.py3-none-any.whl")
    version("2.115.0", sha256="26178e33684763099142e2cad201057bd27d4efefd859a495aac21ab3e6129c2", url="https://pypi.org/packages/d8/25/c1bd7163c4e063ad2339bb66bfc95928db0642187f98b2eaea7a60208c50/google_api_python_client-2.115.0-py2.py3-none-any.whl")
    version("2.114.0", sha256="690e0bb67d70ff6dea4e8a5d3738639c105a478ac35da153d3b2a384064e9e1a", url="https://pypi.org/packages/f1/76/8129340d82e782570c901e12cd870ce7a001782bf190407c0821d4aec275/google_api_python_client-2.114.0-py2.py3-none-any.whl")
    version("2.113.0", sha256="25659d488df6c8a69615b2a510af0e63b4c47ab2cb87d71c1e13b28715906e27", url="https://pypi.org/packages/39/fe/24b02d442dfef2456f46e0dd9e5b833f2dbfb6a8393602a600153ac3781a/google_api_python_client-2.113.0-py2.py3-none-any.whl")
    version("2.80.0", sha256="b9cd2550c2cdfeb78c3150d8c52208841082dabe597063a116476937170907ab", url="https://pypi.org/packages/f8/63/fea1330ab4966d37a64bfd23378f8c32722ed7b91178cab4ab3601f4fd5e/google_api_python_client-2.80.0-py2.py3-none-any.whl")
    version("1.7.10", sha256="60f2ac2f27997d9af10ae126d9937b7d8c1fd061d12668ccaf94b4347ee85021", url="https://pypi.org/packages/ab/4b/66b7591b83864caef0d960aefd05a110bcf9cb18cc6dd957414e34861530/google_api_python_client-1.7.10-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-api-core@1.31.5:1,2.3.1:", when="@2.40:")
        depends_on("py-google-auth@1.19:", when="@2.52:")
        depends_on("py-google-auth@1.4.1:", when="@1.7:1.8")
        depends_on("py-google-auth-httplib2@0.1:", when="@2.1:")
        depends_on("py-google-auth-httplib2@0.0.3:", when="@1.7:2.0")
        depends_on("py-httplib2@0.15:", when="@1.12.3:")
        depends_on("py-httplib2@0.9.2:", when="@1.5.5:1.7.11,1.8:1.12.2")
        depends_on("py-six@1.6.1:", when="@1.5.4:1.12.0")
        depends_on("py-uritemplate@3.0.1:", when="@2.34:")
        depends_on("py-uritemplate@3", when="@1.5.4:2.25")

