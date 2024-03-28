# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutograd(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.2", sha256="208dde2a938e63b4f8f5049b1985505139e529068b0d26f8cd7771fd3eb145d5", url="https://pypi.org/packages/81/70/d5c7c2a458b8be96495c8b1634c2155beab58cbe864b7a9a5c06c2e52520/autograd-1.6.2-py3-none-any.whl")
    version("1.6.1", sha256="0d6ca0b2c6c156e10679f2d4a0f8c029a78fde2443ea184b4b683e992e0a0577", url="https://pypi.org/packages/a8/5a/35ae16c02940fba457fa3c929f9c4406aebde41c850f2abafd3feb228a3f/autograd-1.6.1-py3-none-any.whl")
    version("1.6", sha256="86f5d5262e6f366965a1281e6285c6a528e4af4208a5e3e89a6d6cb587e4542d", url="https://pypi.org/packages/3c/1e/96cae89e9984077196823884cc02d9ec2427f013698bb24d44b349793ada/autograd-1.6-py3-none-any.whl")
    version("1.5", sha256="a22a17e71c4a601359d544827762dd66d5ba50b287a8444d4f85ada1ee762ef6", url="https://pypi.org/packages/69/f1/6243ceee10af0b0252bd7a94a9a715793c9097eed6d83f877b244e362372/autograd-1.5-py3-none-any.whl")
    version("1.4", sha256="5cd6051bf1440643bf8f1104c933b2dedefb7610b951091768c1c680b1e0ceda", url="https://pypi.org/packages/d9/6e/5aec16d68bf07e17e1a6cac5011e1c8f5f8dadb0ac5e875d432ee8aaa733/autograd-1.4-py3-none-any.whl")
    version("1.3", sha256="a15d147577e10de037de3740ca93bfa3b5a7cdfbc34cfb9105429c3580a33ec4", url="https://pypi.org/packages/23/12/b58522dc2cbbd7ab939c7b8e5542c441c9a06a8eccb00b3ecac04a739896/autograd-1.3.tar.gz")
    version("1.2", sha256="a08bfa6d539b7a56e7c9f4d0881044afbef5e75f324a394c2494de963ea4a47d", url="https://pypi.org/packages/08/7a/1ccee2a929d806ba3dbe632a196ad6a3f1423d6e261ae887e5fef2011420/autograd-1.2.tar.gz")
    version("1.1.13", sha256="37ab7eb4bc996ae8cf0099cc429b5c437e4097e1c56c224aede28a7d8c8439d5", url="https://pypi.org/packages/7c/86/cd14f81f9983d50842991e0aad103c57ed8d6b31ee2b1c7f5071cac9be47/autograd-1.1.13.tar.gz")
    version("1.1.12", sha256="55054b7f1247980f0a8c015b9c8530b5afc51a470911472a76d5fd0c447426e2", url="https://pypi.org/packages/c6/46/6740c8e622a36f86ca8d78cc7c7e0d7f7e4db51c5cea65b42ad35d4e8ef7/autograd-1.1.12.tar.gz")
    version("1.1.11", sha256="6a50cc28a17a1411b8e817b9c1e171e6d7a9b3fef1568622f87fe184c471b14c", url="https://pypi.org/packages/6b/3d/e2730b076e77a2c9351673acaefd756466a28dc5b7ce88e2c66059b205b6/autograd-1.1.11.tar.gz")
    version("1.1.10", sha256="bdf5fdfb3074494791e10b06b6959e41b82765c9c8cd3b12ca3734ddd0c5743a", url="https://pypi.org/packages/c1/ba/9c09c920643131904af74671e4e4070d46749d0c028a83e245279cd5e656/autograd-1.1.10.tar.gz")
    version("1.1.9", sha256="746aed6d825655fdb1e96d187362fe3ce096814fd2b561ebb792ae359c6d5535", url="https://pypi.org/packages/54/9c/d5d6abd14c4c5dee1489b530da238004fed4ea76cf48a196ba8fe40baa17/autograd-1.1.9.tar.gz")
    version("1.1.8", sha256="c4026aae9fb1f691044a89024e66f02c1711fbf6acb9cdfded68e8e2df4abe87", url="https://pypi.org/packages/9b/30/eb49e35e5fd7c963186a4db460ada70cb43f6c8b6f99bfb70979ffd73544/autograd-1.1.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future@0.15.2:", when="@1.4:")
        depends_on("py-numpy@1.12.0:", when="@1.4:")
    # END DEPENDENCIES

