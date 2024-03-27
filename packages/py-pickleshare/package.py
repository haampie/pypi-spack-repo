##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPickleshare(PythonPackage):
    version("0.7.5", sha256="9649af414d74d4df115d5d718f82acb59c9d418196b7b4290ed47a12ce62df56", url="https://pypi.org/packages/9a/41/220f49aaea88bc6fa6cba8d05ecf24676326156c23b991e80b3f2fc24c77/pickleshare-0.7.5-py2.py3-none-any.whl")
    version("0.7.4", sha256="c9a2541f25aeabc070f12f452e1f2a8eae2abd51e1cd19e8430402bdf4c1d8b5", url="https://pypi.org/packages/9f/17/daa142fc9be6b76f26f24eeeb9a138940671490b91cb5587393f297c8317/pickleshare-0.7.4-py2.py3-none-any.whl")
    version("0.7.3", sha256="6c11e6a57c0cd25f941ec1451a7d73f01913ba4f0e19aeb38ae4e750e885c7c2", url="https://pypi.org/packages/a0/d0/d2daee922f1c5128128e4737b1c7fdd4f93670a303ceafe80e5414b959a3/pickleshare-0.7.3-py2.py3-none-any.whl")
    version("0.7.2", sha256="92ee3b0e21632542ecc9a0a245e69a126f62e5114081bdb0d32e0edd10410033", url="https://pypi.org/packages/ad/69/bcf0c55ded3779e6e1c9460c69854678d4b78f08482449caaf8e82d5f8eb/pickleshare-0.7.2.tar.gz")
    version("0.7.1", sha256="f160791e1bf513c1957904d5cf6cf503195010d3aa88cd91bee8357e75e4b4ff", url="https://pypi.org/packages/4b/c4/6fb142a1579e9de6f5cd9213e85ee6cc119f43b2dabc8861d62af25fab40/pickleshare-0.7.1.tar.gz")
    version("0.7", sha256="2e6bb018179fdffda5c46b360198ab83acd0f99ad7865ab5163bc1d153bca64f", url="https://pypi.org/packages/c5/a9/fcb641df59b757739917bf8e9078dc02d4502fd28ced65b8b683608dd178/pickleshare-0.7.tar.gz")
    version("0.6", sha256="4c24a277a2220bc9a5b52e45d47433d9db4b9235637cbc86c366f74131da8109", url="https://pypi.org/packages/ba/d3/f8e5c37786288e502b3cd5017b701c3e2f17cbdf8e35673b6c7983ef5099/pickleshare-0.6-py2.py3-none-any.whl")
    version("0.5", sha256="c0be5745035d437dbf55a96f60b7712345b12423f7d0951bd7d8dc2141ca9286", url="https://pypi.org/packages/58/47/8b219a446eb351e1cb966cc10662bf8fa90a7710a9c61c2e81a585661ebb/pickleshare-0.5.tar.gz")
    version("0.4", sha256="13a7fb10b97ae5d0dca09b696a50b079b08cb3109105b2bafad6b50a6b6db53b", url="https://pypi.org/packages/7b/5f/36348c02caad79310a97c2a03899a4572a870dc0d925d7f3f647c1ff7891/pickleshare-0.4.tar.gz")
    version("0.3", sha256="4889087b65edeaad8af83b53f8f4fd5edfa5042b34683e5dd76e8b11a188e173", url="https://pypi.org/packages/6c/19/621ba06fb9f9d8606e4b096aeea9f09954cecdcc83f0e64b22197dca09ef/pickleshare-0.3.zip")

    with default_args(type="run"):
        depends_on("py-path-py@6.2:", when="@0.6")

        # marker: python_version in "2.6 2.7 3.2 3.3"
        # depends_on("py-pathlib2", when="@0.7.3:")

