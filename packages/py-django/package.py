# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDjango(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.0.3", sha256="5c7d748ad113a81b2d44750ccc41edc14e933f56581683db548c9257e078cc83", url="https://pypi.org/packages/9c/5b/eed82065c5d938b17c4b7304ab5ebe762c7a5a7eaa8a10ab35541580d79a/Django-5.0.3-py3-none-any.whl")
    version("5.0.2", sha256="56ab63a105e8bb06ee67381d7b65fe6774f057e41a8bab06c8020c8882d8ecd4", url="https://pypi.org/packages/50/1b/7536019fd20654919dcd81b475fee1e54f21bd71b2b4e094b2ab075478b2/Django-5.0.2-py3-none-any.whl")
    version("5.0.1", sha256="f47a37a90b9bbe2c8ec360235192c7fddfdc832206fcf618bb849b39256affc1", url="https://pypi.org/packages/97/67/6804ff6fc4fa6df188924412601cc418ddc2d0a500963b0801a97b7ec08a/Django-5.0.1-py3-none-any.whl")
    version("5.0", sha256="3a9fd52b8dbeae335ddf4a9dfa6c6a0853a1122f1fb071a8d5eca979f73a05c8", url="https://pypi.org/packages/ba/c7/61b02c0ef9e129080a8c2bffefb3cb2b9ddddece4c44dc473c1c4f0647c1/Django-5.0-py3-none-any.whl")
    version("4.2.11", sha256="ddc24a0a8280a0430baa37aff11f28574720af05888c62b7cfe71d219f4599d3", url="https://pypi.org/packages/a1/b9/5adf3f78e4c7b762eb6f1140057bd128c978c3f85c08e412f951aef65f9e/Django-4.2.11-py3-none-any.whl")
    version("4.2.10", sha256="a2d4c4d4ea0b6f0895acde632071aff6400bfc331228fc978b05452a0ff3e9f1", url="https://pypi.org/packages/20/8c/498ce1ac30228f3bc36d4d427fe10268bd01e6f0361ead6c60b2b255c6b6/Django-4.2.10-py3-none-any.whl")
    version("4.2.9", sha256="2cc2fc7d1708ada170ddd6c99f35cc25db664f165d3794bc7723f46b2f8c8984", url="https://pypi.org/packages/59/7c/e11e300ed554f8626b75eae9bb8f450f830daefb8b40681873ab54d9eaa8/Django-4.2.9-py3-none-any.whl")
    version("4.2.8", sha256="6cb5dcea9e3d12c47834d32156b8841f533a4493c688e2718cafd51aa430ba6d", url="https://pypi.org/packages/8a/79/7f45e9c129c3cd8e4d54806649efeb1db9c223c54a1c54b30511d246bc60/Django-4.2.8-py3-none-any.whl")
    version("4.2.7", sha256="e1d37c51ad26186de355cbcec16613ebdabfa9689bbade9c538835205a8abbe9", url="https://pypi.org/packages/2d/6d/e87236e3c7b2f5911d132034177aebb605f3953910cc429df8061b13bf10/Django-4.2.7-py3-none-any.whl")
    version("4.2.6", sha256="a64d2487cdb00ad7461434320ccc38e60af9c404773a2f95ab0093b4453a3215", url="https://pypi.org/packages/b9/45/707dfc56f381222c1c798503546cb390934ab246fc45b5051ef66e31099c/Django-4.2.6-py3-none-any.whl")
    version("3.0.5", sha256="642d8eceab321ca743ae71e0f985ff8fdca59f07aab3a9fb362c617d23e33a76", url="https://pypi.org/packages/a9/4f/8a247eee2958529a6a805d38fbacd9764fd566462fa0016aa2a2947ab2a6/Django-3.0.5-py3-none-any.whl")
    version("3.0.4", sha256="89e451bfbb815280b137e33e454ddd56481fdaa6334054e6e031041ee1eda360", url="https://pypi.org/packages/12/68/8c125da33aaf0942add5095a7a2a8e064b3812d598e9fb5aca9957872d71/Django-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="c91c91a7ad6ef67a874a4f76f58ba534f9208412692a840e1d125eb5c279cb0a", url="https://pypi.org/packages/c6/b7/63d23df1e311ca0d90f41352a9efe7389ba353df95deea5676652e615420/Django-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="4f2c913303be4f874015993420bf0bd8fd2097a9c88e6b49c6a92f9bdd3fb13a", url="https://pypi.org/packages/55/d1/8ade70e65fa157e1903fe4078305ca53b6819ab212d9fbbe5755afc8ea2e/Django-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="b61295749be7e1c42467c55bcabdaee9fbe9496fdf9ed2e22cef44d9de2ff953", url="https://pypi.org/packages/6a/23/08f7fd7afdd24184a400fcaebf921bd09b5b5235cbd62ffa02308a7d35d6/Django-3.0.1-py3-none-any.whl")
    version("2.2.12", sha256="6ecd229e1815d4fc5240fc98f1cca78c41e7a8cd3e3f2eefadc4735031077916", url="https://pypi.org/packages/af/d1/903cdbda68cd6ee74bf8ac7c86ffa04b2baf0254dfd6edeeafe4426c9c8b/Django-2.2.12-py3-none-any.whl")
    version("2.2.11", sha256="b51c9c548d5c3b3ccbb133d0bebc992e8ec3f14899bce8936e6fdda6b23a1881", url="https://pypi.org/packages/be/76/7ccbcf52366590ca76997ce7860308b257b79962a4e4fada5353f72d7be5/Django-2.2.11-py3-none-any.whl")
    version("2.2.10", sha256="9a4635813e2d498a3c01b10c701fe4a515d76dd290aaa792ccb65ca4ccb6b038", url="https://pypi.org/packages/2b/b2/eb6230a30a5cc3a71b4df733de95c1a888e098e60b5e233703936f9c4dad/Django-2.2.10-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@5:")
        depends_on("py-asgiref@3.7:", when="@5:")
        depends_on("py-asgiref@3.6:", when="@4.2:4")
        depends_on("py-asgiref@3.2:", when="@3.0")
        depends_on("py-backports-zoneinfo", when="@4 ^python@:3.8")
        depends_on("py-pytz", when="@1.11-alpha1:3")
        depends_on("py-sqlparse@0.3.1:", when="@4.2-rc1:")
        depends_on("py-sqlparse@0.2.2:", when="@2.2.14:2,3.0-rc1:4.2-beta1")
        depends_on("py-sqlparse", when="@2.2-alpha1:2.2.13,3:3.0-beta1")
        depends_on("py-tzdata", when="@4: platform=windows")
    # END DEPENDENCIES

