##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPystacClient(PythonPackage):
    version("0.7.6", sha256="221800ea54f408557fc947be08928638fb83b3e7506d3629f9a7ad594c577975", url="https://pypi.org/packages/17/8d/1d44e6bab19884f56e2565d997797f240b722f04d505b06e232bab57b9c6/pystac_client-0.7.6-py3-none-any.whl")
    version("0.7.5", sha256="b07c21f0bfbe7ea19cd23e535406ee08ee604b8ff8d9afcee666c0b1fe017dc4", url="https://pypi.org/packages/95/57/a9c987b9c9d6c41bbe7050ea5f1ac50c9e50af5c317e6e9122066aeef822/pystac_client-0.7.5-py3-none-any.whl")
    version("0.7.4", sha256="2173b346a56f5008b6acbe2f69dfdf424ff3c039df3a8937a734458b7d4fbb8a", url="https://pypi.org/packages/1b/34/1fd3ce4c250e93a8241a494f3b0c04a049ce57081ce26c47985a664cb9b2/pystac_client-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="44f97310ff0a3b57050dcfa51d0fc4db0e4e9cc7997a1957fe57c96bb1476786", url="https://pypi.org/packages/a7/9e/c8dd1ac35f85911dc6196316033e158d485efbd751c730d8556abfa26708/pystac_client-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="5101ab8400536d5a08713dff093817f3f51ea617785070745c45ed34060b9154", url="https://pypi.org/packages/44/20/3a594b416f0b8ea2942d08bbbdc6a491441fcd720a6dc87668865ea33f32/pystac_client-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="0c6fe6e873ef697bd69da2ac3c52b32dfdddd7101d38265d4382cf9d47dd7cd1", url="https://pypi.org/packages/ca/9e/7fb66f245a576766baacf8d1e73440b87375a19d40aaf1484f553da4ff8b/pystac_client-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="5a0ae988c75602975a0d53abe616c48d44928a8663790c5c501fcda25fd9468f", url="https://pypi.org/packages/b6/53/6ba858cad5001b05100a3ade49d11058179b0325e185d4ed4262ecc28df8/pystac_client-0.7.0-py3-none-any.whl")
    version("0.6.1", sha256="124d81bd9653b3e12c7ff244bf0dad420cadeaf86ab394dfdc804958ff723fcd", url="https://pypi.org/packages/4c/99/c7b19b8198f714fb00d57908a447216ecad5c815f357f848ed066c9a170b/pystac_client-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="2896a61dadc6cfda882eee91dafc30797382ff4e34543eae78ac60e11dd51e6b", url="https://pypi.org/packages/86/bb/adca5d48c48ea4e886e0ea5236cfb529f9779d5601175179d8151c5864e9/pystac_client-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="f181c5d078e3c0b0769d492c79b213afb673666c6d0dc89c5f194dde0a8bcbb4", url="https://pypi.org/packages/df/c6/9ffa4d823a628a1addc1718cb0bd37352c17c6365637a62c7bcf46d741f2/pystac_client-0.5.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pystac@1.8.2:+validation", when="@0.7.3:")
        depends_on("py-pystac@1.7.2:+validation", when="@0.7:0.7.2")
        depends_on("py-pystac@1.7:", when="@0.6.1:0.6")
        depends_on("py-pystac@1.4:", when="@0.3.3:0.6.0")
        depends_on("py-python-dateutil@2.8.2:", when="@0.7:")
        depends_on("py-python-dateutil@2.7:", when="@:0.3.0,0.3.4:0.6")
        depends_on("py-requests@2.28.2:", when="@0.7:")
        depends_on("py-requests@2.27.1:", when="@0.5:0.6")

