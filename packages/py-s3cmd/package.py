##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyS3cmd(PythonPackage):
    version("2.3.0", sha256="2204306742c33c24fbca02b78e059bacfc1bfc04af09c7e9866f267a11a9ddb2", url="https://pypi.org/packages/6a/ba/828b5b88aeca434938b8d7a6aece672fa738f6909f19b9611aae54ff08eb/s3cmd-2.3.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="50ef46a83c6292439aaa2b15d6d134eddb3f28757732e3c65e30cbed2a8a9565", url="https://pypi.org/packages/1e/88/9630c6e894575f03c1685104a6562a31ecf9e82b5b687d8516445a051fbe/s3cmd-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="49cd23d516b17974b22b611a95ce4d93fe326feaa07320bd1d234fed68cbccfa", url="https://pypi.org/packages/26/44/19e08f69b2169003f7307565f19449d997895251c6a6566ce21d5d636435/s3cmd-2.1.0-py2.py3-none-any.whl")
    version("2.0.2", sha256="231fe00daedb13095ce38ccf264bbe81d133f6e82f1484ef2f5efdc3f21b9ee8", url="https://pypi.org/packages/5e/1c/c3697bc3afadc7f6a80a8afb5968fa6f5dc2876090f06fd49a4bf1eb8c44/s3cmd-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="caf09f1473301c442fba6431c983c361c9af8bde503dac0953f0d2f8f2c53c8f", url="https://pypi.org/packages/c0/55/ff0ba1d725d3b43c1b116907b4891da0a3b3193e7fa23f75d9fff7a6431e/s3cmd-2.0.1.tar.gz")
    version("2.0.0", sha256="bf2a50802f1031cba83e99be488965803899d8ab0228c800c833b55c7269cd48", url="https://pypi.org/packages/f1/ca/dcec06e5ffeb6add7cc919cd952a5881b03ad6e43a9ecf158c0fce5c48ab/s3cmd-2.0.0.tar.gz")
    version("1.6.1", sha256="9772aa810189bf20e9ae292e489521376741c53f7db01dc1acbdbf4a5f26edaf", url="https://pypi.org/packages/fb/01/058591e96c8369bf68fda7d699fe77f98e1399b878003d2609173890cc10/s3cmd-1.6.1.zip")
    version("1.6.0", sha256="abd99e42b69775129e20f28935ccc80aa32f51f9cff1b064eecdafc7e22bed25", url="https://pypi.org/packages/a7/40/91218e3986488d607b54e1f7456a8d052c00468f1b58d177ae860aafb429/s3cmd-1.6.0.zip")
    version("1.5.2", sha256="84996210190c82be69c262069293efca8fd50abfe3dbcc5022fde1ad0c00d850", url="https://pypi.org/packages/1a/29/5184124615ac56997b667bfa0f426b06c8b4c864ed7bee3767502b30ffa0/s3cmd-1.5.2.zip")

    with default_args(type="run"):
        depends_on("py-python-dateutil", when="@2.1:")
        depends_on("py-python-magic", when="@2.1:")

