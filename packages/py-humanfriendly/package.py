# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHumanfriendly(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.0", sha256="1697e1a8a8f550fd43c2865cd84542fc175a61dcb779b6fee18cf6b6ccba1477", url="https://pypi.org/packages/f0/0f/310fb31e39e2d734ccaa2c0fb981ee41f7bd5056ce9bc29b2248bd569169/humanfriendly-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="332da98c24cc150efcc91b5508b19115209272bfdf4b0764a56795932f854271", url="https://pypi.org/packages/92/7e/a06472f484fa589933f39bfb41a7b849ca49f6d8e4fdfe978e27f0e3075c/humanfriendly-9.2-py2.py3-none-any.whl")
    version("9.1", sha256="d5c731705114b9ad673754f3317d9fa4c23212f36b29bdc4272a892eafc9bc72", url="https://pypi.org/packages/93/66/363d01a81da2108a5cf446daf619779f06d49a0c4426dd02b40734f10e2f/humanfriendly-9.1-py2.py3-none-any.whl")
    version("9.0", sha256="3c9ab8d28e88e6cc998e41963357736dafd555ee5bb666b50e42f6ce28dd3e3d", url="https://pypi.org/packages/79/59/239f467c4bafad82ad1fdb0d2a16384d8a5e18d5a3197b4840473531e50e/humanfriendly-9.0-py2.py3-none-any.whl")
    version("8.2", sha256="e78960b31198511f45fd455534ae7645a6207d33e512d2e842c766d15d9c8080", url="https://pypi.org/packages/8e/2d/2f1b0a780b8c948c06c74c8c80e68ac354da52397ba432a1c5ac1923c3af/humanfriendly-8.2-py2.py3-none-any.whl")
    version("8.1", sha256="3a831920e40e55ad49adb64c9179ed50c604cabca72cd300e7bd5b51310e4ebb", url="https://pypi.org/packages/9d/25/417cfcd511782bc678c1285a365271bdbe9ec895fa69a4c7a294ae9586f5/humanfriendly-8.1-py2.py3-none-any.whl")
    version("8.0", sha256="6990c0af4b72f50ddf302900eb982edf199247e621e06d80d71b00b1a1574214", url="https://pypi.org/packages/19/a4/6deadfb0ed130b14628eff1cd39dc0e58c8dce9eddf46e2754060fe7f38b/humanfriendly-8.0-py2.py3-none-any.whl")
    version("7.3", sha256="f412b025e1b4ce5ce19ba4e0fb8312a622ac62d06ce4e6b9b25c858cf16271f0", url="https://pypi.org/packages/af/b7/798372f9ddf5429c69a36cb940ee1da7e6f37192c058db7ccb5d85af72d4/humanfriendly-7.3-py2.py3-none-any.whl")
    version("7.2", sha256="e8e2e4524409e55d5c5cbbb4c555a0c0a9599d5e8f74d0ce1ac504ba51ad1cd2", url="https://pypi.org/packages/f8/d4/f28089b2146f5dd175fb0f7a65f4c3db459f9cbecd0e38b3682021459aad/humanfriendly-7.2-py2.py3-none-any.whl")
    version("7.1.1", sha256="a9a41074c24dc5d6486e8784dc8f057fec8b963217e941c25fb7c7c383a4a1c1", url="https://pypi.org/packages/ba/b3/80b90fa705f8809c0a25d15c8cb7864e6e57ebad30048926fd9c3414f21d/humanfriendly-7.1.1-py2.py3-none-any.whl")
    version("7.1", sha256="1a2df7c533161580a9c0fcec9c02674ee29b5f8fcbca7bf6bc6ac2bcf4caeb33", url="https://pypi.org/packages/f7/71/5cf23906339bd1574e84b1c0f1a17f761694fdeef93b8fa0c3cb436e527e/humanfriendly-7.1-py2.py3-none-any.whl")
    version("7.0", sha256="ebe8cfdf1bfa1af98a1477eb0dc5e64a256d18e782bd4541a95bb286422ebca8", url="https://pypi.org/packages/2f/26/c6f5fca266afcb7586f460ae83f585def604a762608d12de86b78b59cb73/humanfriendly-7.0-py2.py3-none-any.whl")
    version("6.1", sha256="5a57c973dd28a24f45ab723521c84b111fbe79e9d9fcdca6f9aeb668c18a0f40", url="https://pypi.org/packages/1e/dc/8aac3921fd2a03978542a22eb7485b63c8e85ca75a4d3bb904fab82cf032/humanfriendly-6.1-py2.py3-none-any.whl")
    version("6.0", sha256="d112bb6d6f7859c5cda7233fdebadb82636730b25738c15ba44ce4c4dc023f77", url="https://pypi.org/packages/b0/dd/37a08313472fee1d92b158f771f41bdb5e962160f9bce07d446da15ee833/humanfriendly-6.0-py2.py3-none-any.whl")
    version("4.18", sha256="23057b10ad6f782e7bc3a20e3cb6768ab919f619bbdc0dd75691121bbde5591d", url="https://pypi.org/packages/90/df/88bff450f333114680698dc4aac7506ff7cab164b794461906de31998665/humanfriendly-4.18-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyreadline", when="@4.4.2:9 platform=windows")
        depends_on("py-pyreadline3", when="@10: platform=windows")
    # END DEPENDENCIES

