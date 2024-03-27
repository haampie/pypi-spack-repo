##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatalad(PythonPackage):
    version("0.19.6", sha256="030c7d8a7c941a9bda92c35bc14f3f73f4e5519961ffe6b0f5e294f40ed97eed", url="https://pypi.org/packages/3f/a2/d1093eda6efd0ab353e69ca225a07886ea3dd173a3ac26f31f6e760ae03a/datalad-0.19.6-py3-none-any.whl")
    version("0.19.5", sha256="16b5b948e76b9ec4ef78da78deb57d0f2ff6f510561c73d61fd3c573bbaff5ea", url="https://pypi.org/packages/5c/29/597828ab89ae808d73e4b948c272276751f336375f5953a02c55e2a11c46/datalad-0.19.5-py3-none-any.whl")
    version("0.19.4", sha256="40a8fb7ed9f666d1b6caa9536152e92c02ae9db3d7101e4f578bd7ab701bb493", url="https://pypi.org/packages/71/49/0f796d8f88958f6cfd63a986861bfa5f3f62847aab25e5895b17c8badd90/datalad-0.19.4-py3-none-any.whl")
    version("0.19.3", sha256="75ee17d571f17cef8a75dad996e558188f583f3c3e017e6a6467d471a64d9ab0", url="https://pypi.org/packages/b6/23/4d8fc9b9efe9a15c09e9361954171bc8630d159f14bbf280de278552905d/datalad-0.19.3-py3-none-any.whl")
    version("0.19.2", sha256="b32e92240af6f6b381d0b3eef600ac85c62d421317cb500e56fd3a9bf6e66b49", url="https://pypi.org/packages/fe/34/4232aec3df17bd9339fc422ee1643c19432b97811b4f14999d7c44141c7a/datalad-0.19.2-py3-none-any.whl")
    version("0.19.1", sha256="d592c977da4de94d47913729993c8d53106b3cb087ed2499b0baf66d44bc11f3", url="https://pypi.org/packages/02/da/97f010e93cdb9f53ece18b649bc1f232e8eb6e69e364b5a2eeba6eeeff43/datalad-0.19.1-py3-none-any.whl")
    version("0.19.0", sha256="91f3478d4234952f3d1333c380fe52f278301c340d063d675d7b3f0e90664b4e", url="https://pypi.org/packages/e9/a0/62f8ede9c313a0f9522f43f7645babdeb31d056779191ad061d13cf0cd46/datalad-0.19.0-py3-none-any.whl")
    version("0.18.5", sha256="4473a4a89000c0bd214f003935d6212fa791a223cf9b83f611e7eb260477bf17", url="https://pypi.org/packages/37/a1/e4a0aa55ef9f39ddaea73ff5cd7440f86b7a7e9f8b771bc5ee8b84a0bbb4/datalad-0.18.5-py3-none-any.whl")
    version("0.18.4", sha256="75bf85db017bb5cff0e62b6e75ba282bf04d061e1410017e132320dd6a4e79e4", url="https://pypi.org/packages/34/3a/639e37dc2c516342d4582ab9364aac948e235b661532ba56f3bd5f9a1d1b/datalad-0.18.4-py3-none-any.whl")
    version("0.18.3", sha256="a2607b592be02b7dbb5633484fd7055f3d7d6c1bd8c8490e80b85d49010ab69e", url="https://pypi.org/packages/b3/5d/0f639182dd8bf8c5c98e9010b366fe252a8f0f1a53983e37d9e04c379fa6/datalad-0.18.3-py3-none-any.whl")
    version("0.15.5", sha256="ab2d929887a5a1e04ab361740fe44dd60d2155c9a6938ae60490b67197e4711e", url="https://pypi.org/packages/54/cd/7336e65f5e8dab85406deb3955b268fe543114c7c61d7d99c617d0f072cc/datalad-0.15.5-py3-none-any.whl")
    version("0.15.3", sha256="ccd34eb26594c5f2aa3a7f5b562cde397a4e0f075bfff3d6685f8c6766051a5c", url="https://pypi.org/packages/e5/5f/84354ada51ca68c08af4b00ea88a2785417efa10cc94dace81df5df98c00/datalad-0.15.3-py3-none-any.whl")
    version("0.15.2", sha256="e8dbe5f940b704ef4c70043c499f30716b6e6d7d7287c12ea0c2c4ae5050108f", url="https://pypi.org/packages/fd/20/f4dc92cb59b047709256d6b8f3e6a473c0ac86aeb9f1dde6b02ba2bf4a68/datalad-0.15.2-py3-none-any.whl")
    version("0.15.1", sha256="afa91c75f7fd1e686e752e5272bc653e59037ee6644b8d48325e44dd17a225a3", url="https://pypi.org/packages/17/3f/2446b7699463bcafbc8a28b0b35f6fadc0dee4ca26b3a4b4884750e556b5/datalad-0.15.1-py3-none-any.whl")
    version("0.14.6", sha256="09b479a1411ce6464feef326059ab2bd70192851940808e168d16409181a56d8", url="https://pypi.org/packages/20/c6/8304d2a184e1f24aff1a4db9728f08c15a1bc02b3c698610ac3cdf9bc309/datalad-0.14.6-py3-none-any.whl")

    variant("full", default=False)

    with default_args(type="run"):
        depends_on("py-annexremote", when="@0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-annexremote", when="@0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-appdirs", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15+full")
        depends_on("py-appdirs", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15")
        depends_on("py-argcomplete@1.12.3:", when="@0.17.10:+full")
        depends_on("py-argcomplete", when="@0.14.7,0.15.1:0.15+full")
        depends_on("py-beautifulsoup4", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-boto", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-boto", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-chardet@3.0.4:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.18.2:+full")
        depends_on("py-chardet@3.0.4:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.18.2:")
        depends_on("py-colorama", when="@0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full platform=windows")
        depends_on("py-colorama", when="@0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10: platform=windows")
        depends_on("py-distro", when="@0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-distro", when="@0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-duecredit", when="@0.10:0.10.0-rc4,0.12.0-rc3:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-duecredit", when="@0.10:0.10.0-rc4")
        depends_on("py-exifread", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-fasteners@0.14:", when="@0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-fasteners@0.14:", when="@0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-httpretty@0.9.4:", when="@0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-humanize", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-humanize", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-importlib-metadata@3.6:", when="@0.17.10:+full ^python@:3.9")
        depends_on("py-importlib-metadata@3.6:", when="@0.17.10: ^python@:3.9")
        depends_on("py-importlib-resources@3:", when="@0.19.3:+full ^python@:3.8")
        depends_on("py-importlib-resources@3:", when="@0.19.3: ^python@:3.8")
        depends_on("py-iso8601", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-iso8601", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-jsmin", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7+full")
        depends_on("py-jsmin", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7")
        depends_on("py-keyring@20:23.8,23.9.1:", when="@0.17.10:+full")
        depends_on("py-keyring@20:23.8,23.9.1:", when="@0.17.10:")
        depends_on("py-keyring@8:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15+full")
        depends_on("py-keyring@8:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15")
        depends_on("py-keyrings-alt", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-keyrings-alt", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-looseversion", when="@0.18:+full")
        depends_on("py-looseversion", when="@0.18:")
        depends_on("py-msgpack", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-msgpack", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-mutagen@1.36:", when="@0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-mypy", when="@0.18.3:+full")
        depends_on("py-nose@1.3.4:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15+full")
        depends_on("py-packaging", when="@0.15.4:0.15,0.17.10:+full")
        depends_on("py-packaging", when="@0.15.4:0.15,0.17.10:")
        depends_on("py-patool", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-patool", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-pillow", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-platformdirs", when="@0.17.10:+full")
        depends_on("py-platformdirs", when="@0.17.10:")
        depends_on("py-pygithub", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15+full")
        depends_on("py-pygithub", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15")
        depends_on("py-pyperclip", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-pytest", when="@0.17.10:+full")
        depends_on("py-pytest-cov", when="@0.17.10:+full")
        depends_on("py-pytest-fail-slow@0.2:", when="@0.17.10:+full")
        depends_on("py-python-dateutil", when="@0.10.0-rc3:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-python-gitlab", when="@0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-python-gitlab", when="@0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-python-xmp-toolkit", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-pyyaml", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-requests@1.2:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-requests@1.2:", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:")
        depends_on("py-requests-ftp", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-simplejson", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-simplejson", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17")
        depends_on("py-tqdm@4.32:", when="@0.19:+full")
        depends_on("py-tqdm@4.32:", when="@0.19:")
        depends_on("py-tqdm", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.18+full")
        depends_on("py-tqdm", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.18")
        depends_on("py-types-python-dateutil", when="@0.17.10:+full")
        depends_on("py-types-requests", when="@0.17.10:+full")
        depends_on("py-typing-extensions@4:", when="@0.18.4:+full ^python@:3.10")
        depends_on("py-typing-extensions@4:", when="@0.18.4: ^python@:3.10")
        depends_on("py-typing-extensions", when="@0.18.3+full ^python@:3.9")
        depends_on("py-typing-extensions", when="@0.18.3 ^python@:3.9")
        depends_on("py-vcrpy", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:+full")
        depends_on("py-whoosh", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17+full")
        depends_on("py-whoosh", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15,0.17.10:0.17")
        depends_on("py-wrapt", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15+full")
        depends_on("py-wrapt", when="@0.10:0.10.0-rc4,0.10.1,0.12:0.12.0-rc5,0.12.0:0.12.3,0.14.6:0.14.7,0.15.1:0.15")

