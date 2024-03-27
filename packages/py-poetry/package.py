##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPoetry(PythonPackage):
    version("1.8.2", sha256="b42b400d9a803af6e788a30a6f3e9998020b77860e28df20647eb10b6f414910", url="https://pypi.org/packages/bd/9c/aff8a1fac5c8ae6180a56f6ff6f515057b188789923b1afb897196116735/poetry-1.8.2-py3-none-any.whl")
    version("1.8.1", sha256="cf133946661025822672422769567980f8e489ed5b6fc170d1025a4d6c9aac29", url="https://pypi.org/packages/df/61/21a99a01784516fe55a2a6431208ce14932bba789259b4cc74b39fef0996/poetry-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="5c418265099b681e399a1521e72d98f407a015cade8ff37260b1359c1afd773c", url="https://pypi.org/packages/71/61/0b37e623445b765376d5541b607ee1ef9af98eb85ad11aeb5b19f8bbebe7/poetry-1.8.0-py3-none-any.whl")
    version("1.7.1", sha256="03d3807a0fb3bc1028cc3707dfd646aae629d58e476f7e7f062437680741c561", url="https://pypi.org/packages/79/94/95c62fb8463d3f7dd86f1fc27369f63b4e028cbdbc7f62716183d4f51d16/poetry-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="cd34af106676bf4224e6aa7aaa31e89d191f7af562d2a0ee08628dea5dc8779b", url="https://pypi.org/packages/5f/7c/fb9e4addaabec3ce54370ebaf6d6ed2a77cb4b69f79b966ead6c8e148b77/poetry-1.7.0-py3-none-any.whl")
    version("1.6.1", sha256="9b4cb6079c08cc0d91e8cba18a6bd4d4f7d7830263a7fb18ecb3faa77937c988", url="https://pypi.org/packages/7d/25/f3bfda3c458d114005af99441d009936b85a34a730aeb9cf57fb2630d9f7/poetry-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="3b0b0a5f1e556115a48950f1ae20bd62431c9390188a3372c8d7da5f1a8a3a38", url="https://pypi.org/packages/50/45/8f1050c7d9a9cf53017bde6148bb96d931a9d5b9001fe0350d4cfab254de/poetry-1.6.0-py3-none-any.whl")
    version("1.5.1", sha256="dfc7ce3a38ae216c0465694e2e674bef6eb1a2ba81aa47a26f9dc03362fe2f5f", url="https://pypi.org/packages/ac/da/506b45c82484efb896cadb27348cca8a4ba960968428804417e7b6e866cd/poetry-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="e66c728b3c645a12c24f553a3e60f3b1ee425aa4a09c331dd372ff14e0976d26", url="https://pypi.org/packages/8b/3f/9e87a74505639a63c64b94e64aee8a1d24e10cfc7df5e3eec67708477d9b/poetry-1.5.0-py3-none-any.whl")
    version("1.4.2", sha256="c39c483cde7930915c992f932c163994ce3d870765efb8235ad0139cd65f0c5b", url="https://pypi.org/packages/19/17/ae08e68ea73bfa0d2ba5f560f75edf0d3b595088a260cffeaea8652a657b/poetry-1.4.2-py3-none-any.whl")
    version("1.2.1", sha256="43be0a7b0fdc3efa661324e288e9630ad00c54dcf17e2a054740a160d7f25d63", url="https://pypi.org/packages/d2/e5/13164394035758f572c86427159aca03fa24e956b7642337a7f6fd7cb973/poetry-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="af99cad115cb0fbad8c41eb31c5a5dee25a9f6c74fc1d4d6dad8e51a69ebe348", url="https://pypi.org/packages/ea/43/5dfea5153589e7663e5606484e6af65a83b2f3f04cee1013753feb32d159/poetry-1.2.0-py3-none-any.whl")
    version("1.1.13", sha256="52deb0792a2e801967ba9c4cdb39b56fe68b0b5cd3f195b004bef603db9d51a7", url="https://pypi.org/packages/c5/b2/a7259ac429bd628c4a6ab962d1022cf7e596d0d5ecf31bab8101b362d2e5/poetry-1.1.13-py2.py3-none-any.whl")
    version("1.1.12", sha256="3d4dc5d4c7171fb251b32e49a98cecbe2795d5e681ecee2297e2b2d2ccd671fc", url="https://pypi.org/packages/81/66/0eb0022ca0e2cf05513527ba4a1be11db154b23b858d40bc5f9280ac239d/poetry-1.1.12-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-build@1.0.3:", when="@1.7:")
        depends_on("py-build@0.10:0", when="@1.4:1.6")
        depends_on("py-cachecontrol@0.14:+filecache", when="@1.8:")
        depends_on("py-cachecontrol@0.13+filecache", when="@1.6:1.7")
        depends_on("py-cachecontrol@0.12.9:0.12+filecache", when="@1.1.12:1.1,1.2.0-beta1:1.5")
        depends_on("py-cachy@0.3:", when="@1.0.0-beta1:1.2,1.3.0.dev:1.3.0")
        depends_on("py-cleo@2.1:", when="@1.7:")
        depends_on("py-cleo@2:", when="@1.3:1.3.0.0,1.3.1:1.6")
        depends_on("py-cleo@1.0.0-alpha5:1", when="@1.2.0-beta2:1.2,1.3.0.dev:1.3.0")
        depends_on("py-cleo@0.8.1:0", when="@1.1.0-alpha2:1.1")
        depends_on("py-clikit@0.6.2:", when="@1.1.0-alpha2:1.1")
        depends_on("py-crashtest@0.4.1:", when="@1.3:1.3.0.0,1.3.1:")
        depends_on("py-crashtest@:0.3", when="@1.1.0-alpha2:1.2,1.3.0.dev:1.3.0")
        depends_on("py-dulwich@0.21.2:", when="@1.4:")
        depends_on("py-dulwich@0.20.46:0.20", when="@1.2.1:1.3.0.0,1.3.1:1.3")
        depends_on("py-dulwich@0.20.44:0.20", when="@1.2.0-beta3:1.2.0,1.3.0.dev:1.3.0")
        depends_on("py-fastjsonschema@2.18:", when="@1.7:")
        depends_on("py-filelock@3.8:", when="@1.3:1.3.0.0,1.3.1:1.5")
        depends_on("py-html5lib@1.0:", when="@0.10.0-alpha2:1.5")
        depends_on("py-importlib-metadata@4.4:", when="@1.4: ^python@:3.9")
        depends_on("py-importlib-metadata@4.4:4", when="@1.2.0-beta2:1.3 ^python@:3.9")
        depends_on("py-installer@0.7:", when="@1.4.1:")
        depends_on("py-jsonschema@4.10:4.17", when="@1.6")
        depends_on("py-jsonschema@4.10:", when="@1.2.0-rc1:1.5")
        depends_on("py-keyring@24", when="@1.6:")
        depends_on("py-keyring@23.9:23", when="@1.3:1.3.0.0,1.3.1:1.5")
        depends_on("py-keyring@21.2:", when="@1.1.13:1.2,1.3.0.dev:1.3.0")
        depends_on("py-keyring@21.2:21", when="@1.1.0-alpha2:1.1.12")
        depends_on("py-lockfile@0.12:", when="@1.3.1:1.5")
        depends_on("py-packaging@23.1:", when="@1.8.1:")
        depends_on("py-packaging@20.5:", when="@1.7:1.8.0")
        depends_on("py-packaging@20.4:", when="@1.2.0-beta2:1.6")
        depends_on("py-packaging@20.4:20", when="@1.1.0-alpha3:1.2.0-beta1")
        depends_on("py-pexpect@4.7:", when="@1.0.0-beta2:")
        depends_on("py-pkginfo@1.9.4:", when="@1.4:")
        depends_on("py-pkginfo@1.5:", when="@1.2:1.3")
        depends_on("py-pkginfo@1.4:", when="@0.8.0-alpha4:1.1")
        depends_on("py-platformdirs@3:", when="@1.8:")
        depends_on("py-platformdirs@3", when="@1.5:1.7")
        depends_on("py-platformdirs@2.5.2:2", when="@1.2.0-beta2:1.4")
        depends_on("py-poetry-core@1.9:", when="@1.8:")
        depends_on("py-poetry-core@1.8.1:1.8", when="@1.7")
        depends_on("py-poetry-core@1.7", when="@1.6")
        depends_on("py-poetry-core@1.6.1:1.6", when="@1.5.1:1.5")
        depends_on("py-poetry-core@1.6:1.6.0", when="@1.5:1.5.0")
        depends_on("py-poetry-core@1.5.2:1.5", when="@1.4.1:1.4")
        depends_on("py-poetry-core@1.2", when="@1.2.1")
        depends_on("py-poetry-core@1.1.0:1.1", when="@1.2.0")
        depends_on("py-poetry-core@1.0.7:1.0", when="@1.1.11:1.1")
        depends_on("py-poetry-plugin-export@1.6:", when="@1.7:")
        depends_on("py-poetry-plugin-export@1.5:", when="@1.6")
        depends_on("py-poetry-plugin-export@1.4:", when="@1.5.1:1.5")
        depends_on("py-poetry-plugin-export@1.3.1:", when="@1.5:1.5.0")
        depends_on("py-poetry-plugin-export@1.3:", when="@1.4")
        depends_on("py-poetry-plugin-export@1.0.7:", when="@1.2.1")
        depends_on("py-poetry-plugin-export@1.0.6:", when="@1.2.0-rc1:1.2.0,1.3.0.dev:1.3.0")
        depends_on("py-pyproject-hooks@1:", when="@1.4:")
        depends_on("py-requests@2.26:", when="@1.6.1:")
        depends_on("py-requests@2.18:", when="@:1.6.0")
        depends_on("py-requests-toolbelt@1:", when="@1.8:")
        depends_on("py-requests-toolbelt@0.9.1:", when="@1.5:1.7")
        depends_on("py-requests-toolbelt@0.9.1:0", when="@1.3:1.3.0.0,1.3.1:1.4")
        depends_on("py-requests-toolbelt@0.9.1:0.9", when="@1.1.0-rc1:1.2,1.3.0.dev:1.3.0")
        depends_on("py-shellingham@1.5:", when="@1.2.0-rc1:")
        depends_on("py-shellingham@1.1:", when="@0.11.0-alpha4:1.2.0-beta3")
        depends_on("py-tomli@2.0.1:", when="@1.3:1.3.0.0,1.3.1: ^python@:3.10")
        depends_on("py-tomlkit@0.11.4:", when="@1.5:")
        depends_on("py-tomlkit@0.11.1,0.11.4:", when="@1.2.0-rc1:1.4")
        depends_on("py-tomlkit@0.7:", when="@1.1.0-beta3:1.2.0-beta3")
        depends_on("py-trove-classifiers@2022.5.19:", when="@1.3:1.3.0.0,1.3.1:")
        depends_on("py-urllib3@1.26:1", when="@1.2.0-beta1:1.5")
        depends_on("py-virtualenv@20.23:", when="@1.7:")
        depends_on("py-virtualenv@20.22:", when="@1.5:1.6")
        depends_on("py-virtualenv@:20.16.5", when="@1.4 platform=windows ^python@3.9:3.9.0")
        depends_on("py-virtualenv@20.4.3:20.4.4,20.4.7:", when="@1.3:1.3.0.0,1.3.1:1.3 platform=linux")
        depends_on("py-virtualenv@20.4.3:20.4.4,20.4.7:", when="@1.3:1.3.0.0,1.3.1:1.3 platform=freebsd")
        depends_on("py-virtualenv@20.4.3:20.4.4,20.4.7:", when="@1.3:1.3.0.0,1.3.1:1.3 platform=darwin")
        depends_on("py-virtualenv@20.4.3:20.4.4,20.4.7:", when="@1.3:1.3.0.0,1.3.1:1.3 platform=cray")
        depends_on("py-virtualenv@20.4.3:20.4.4,20.4.7:", when="@1.2.1:1.2,1.4")
        depends_on("py-virtualenv", when="@1.2.0-beta1:1.2.0,1.3.0.dev:1.3.0")
        depends_on("py-virtualenv@20.0.26:", when="@1.1.0-beta1:1.1")
        depends_on("py-xattr@1:", when="@1.8: platform=darwin")
        depends_on("py-xattr@0.10:0", when="@1.3:1.3.0.0,1.3.1:1.7 platform=darwin")
        depends_on("py-xattr@0.9.7:0.9", when="@1.2.0-beta2:1.2,1.3.0.dev:1.3.0 platform=darwin")

