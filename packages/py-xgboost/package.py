# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXgboost(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.3", sha256="505955b5d770f8217a049beecce79e04a93787371c06dfb4b2414fec9d496bf3", url="https://pypi.org/packages/53/4a/316018e4d5d47f2a671d89e2ee5a8b6686689e7576258929b222b07aa097/xgboost-2.0.3.tar.gz")
    version("2.0.2", sha256="55b5188e6da1d61f02f30a5dd8daffc3a6b5bb975a7249bf381dc1754dc89688", url="https://pypi.org/packages/94/2c/d6246b29c78975f6afc52287cff4e083b5cc86f922e6e18ac4f5bf6b5f2f/xgboost-2.0.2.tar.gz")
    version("2.0.1", sha256="2cdc75f5896766c0498a37a1f30be7bd12cf16549b1b9cfb9ad3caa2a83548c2", url="https://pypi.org/packages/69/c4/e58319c1b2b879e3c06cdb864368912a7bdb0f2393406b501e2b2326985d/xgboost-2.0.1.tar.gz")
    version("2.0.0", sha256="a89a4504c486043dbfdad41e5f426e2a0b4e5494a5f3ca99cf7ad85a665c79e7", url="https://pypi.org/packages/bc/f5/31bf11e175c18cde6cc71c5d3447c140f2c08861ce7b5b8b76ea1dbc7322/xgboost-2.0.0.tar.gz")
    version("1.7.6", sha256="1c527554a400445e0c38186039ba1a00425dcdb4e40b37eed0e74cb39a159c47", url="https://pypi.org/packages/19/fe/327b4a56ef3e3843b97537ff60381cc4d57a8be7ee99375a8710ee690cb2/xgboost-1.7.6.tar.gz")
    version("1.7.5", sha256="63474265a0194f27889c6fb54e5939ad21bcd5fcfaca7b6a89e143be42ed7ad1", url="https://pypi.org/packages/08/44/65ef54bf0ed613c955cbcada4f22959cae94b3c5c9e223e75734d0e7caf2/xgboost-1.7.5.tar.gz")
    version("1.7.4", sha256="7a2406562277d0f7f6ed08f1cda8fef0ed64956bc13a1ff1da1b4201b431e721", url="https://pypi.org/packages/5f/1f/ec8651b2c235c319e925918f355466294de8f3846d1a749898a70bfce01c/xgboost-1.7.4.tar.gz")
    version("1.7.3", sha256="d1ee270b67e8fc5b90002e17493d1c910ae6abe856e6d0d86c619c0002e7c7d1", url="https://pypi.org/packages/e0/90/59ae0c5969c3ad9aefaa92e5d0806b677763fc45342372de6472c235708f/xgboost-1.7.3.tar.gz")
    version("1.7.2", sha256="f1a749aedb9330afc48007cc78b8bbbbea35ce372f48a2735f9c71bbc7b8dcfb", url="https://pypi.org/packages/05/ab/835b3594f04550e58cc6f51bf130be3dcf0cc65457733365b446a624d61a/xgboost-1.7.2.tar.gz")
    version("1.7.1", sha256="bb302c5c33e14bab94603940987940f29203ecb8767a7a719daf579fbfaace64", url="https://pypi.org/packages/fd/29/0248be9be4d6e740fee86d304060a4e5580b097129fa934e2d6cc9ef49f5/xgboost-1.7.1.tar.gz")
    version("1.6.2", sha256="e1f5c91ba88cf8edb409d7fd2ca150dcd80b6f2115587d87365f0c10b2d4f009", url="https://pypi.org/packages/25/e0/f00261d3357eafbe7c657de718abd3c0f6613633a38d05350f63ee099cde/xgboost-1.6.2.tar.gz")
    version("1.6.1", sha256="24072028656f3428e7b8aabf77340ece057f273e41f7f85d67ccaefb7454bb18", url="https://pypi.org/packages/0e/8c/19309bcaf9a88b0bab34b88935925153f3f3f646163acaae9aa148cf72bb/xgboost-1.6.1.tar.gz")
    version("1.5.2", sha256="404dc09dca887ef5a9bc0268f882c54b33bfc16ac365a859a11e7b24d49da387", url="https://pypi.org/packages/c4/04/32989ec64004dca894f1d3ea4c41b1397272857edf14c1a9d1492b692d2d/xgboost-1.5.2.tar.gz")
    version("1.3.3", sha256="397051647bb837915f3ff24afc7d49f7fca57630ffd00fb5ef66ae2a0881fb43", url="https://pypi.org/packages/f8/e0/d7c3e7c97d72e48425fda3d7eaa49db40e7122b6c8f7ab210b7167b3302b/xgboost-1.3.3.tar.gz")
    version("0.90", sha256="d69f90d61a63e8889fd39a31ad00c629bac1ca627f8406b9b6d4594c9e29ab84", url="https://pypi.org/packages/96/84/4e2cae6247f397f83d8adc5c2a2a0c5d7d790a14a4c7400ff6574586f589/xgboost-0.90.tar.gz")
    version("0.82", sha256="ff5aaa039fb43aae331a916b392994c32696279d9b6b5840cc7c74e06f183a95", url="https://pypi.org/packages/2e/bd/ad3a963b630fa3ee72d1a672fd207263fa0a18113688273afe8298293535/xgboost-0.82.tar.gz")
    version("0.81", sha256="f7c8057610350b0b2f91e1ac7c034f2f03d233919d111759346559e628061e0c", url="https://pypi.org/packages/4f/4c/4969b10939c4557ae46e5569d07c0c7ce772b3d6b9c1401a6ed07059fdee/xgboost-0.81.tar.gz")
    version("0.80", sha256="ec990238943988e73734ad483cf6c53b81aec9745811c7b6c5cbb189ef5e328b", url="https://pypi.org/packages/c6/1e/6d13dacd1d5ea3273210162292e818f82629328ce51cdb7eb633f03e0b52/xgboost-0.80.tar.gz")
    version("0.72.1", sha256="a4be2482694351b6610f1d8faf79eb049ca572aec80c8ba00c7020b8d44d8c1d", url="https://pypi.org/packages/49/40/dfc5d356d2bf002298f0d1b8f7fd08671a455828f5804818a36d964bb29d/xgboost-0.72.1.tar.gz")
    version("0.71", sha256="a76fb937fe28c7ce2a7348173efba90eb3524454b0ce4e196d8124e6edab9ec4", url="https://pypi.org/packages/4b/c4/57e246bc99e45c048f9805f2773e7369f0d30896d19fa089fa1794c7b246/xgboost-0.71.tar.gz")
    version("0.7.post4", sha256="62be4ffcb9175f992f803380bc137b9a3a29b6ced6d4120bfd5f16be81d9fe73", url="https://pypi.org/packages/67/d0/5b9b883fe4b6ca671cdcc80e37459ccb9ab5654bb466c696f414d282c21c/xgboost-0.7.post4.tar.gz")
    version("0.7.post3", sha256="4224193159763ab50352b3c53087510a9ebef4c9dcbafb5c5f8c7e2a1d6d7b70", url="https://pypi.org/packages/cb/1c/a2ec1798d444e2b86b27fdbf18d9ab08c25c3d374de77429b55a76f42404/xgboost-0.7.post3.tar.gz")
    version("0.6-alpha2", sha256="ebc4e2bf8c8266212e342ff8ec4f6ae469e8c41a05d099b6778de8424ce32563", url="https://pypi.org/packages/34/85/456a1a8c762f646671043e446a59efbce02b5f408f522c4ef8793e860c5e/xgboost-0.6a2.tar.gz")
    version("0.6-alpha1", sha256="919050c614d24917016de1fb4cd54eea513e17b9ba714dc5f55e0f7eb376348d", url="https://pypi.org/packages/7f/36/e55ba853acc85d7ebaddec498c72c768bb2700415c5a2ea967a0b8dc8957/xgboost-0.6a1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dask", default=False)
    variant("pandas", default=False)
    variant("plotting", default=False)
    variant("scikit-learn", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dask", when="@1:1.0.0-rc2,1.0.1:1.1,2:+dask")
        depends_on("py-distributed", when="@1:1.0.0-rc2,1.0.1:1.1,2:+dask")
        depends_on("py-graphviz", when="@1:1.0.0-rc2,1.0.1:1.1,2:+plotting")
        depends_on("py-matplotlib", when="@1:1.0.0-rc2,1.0.1:1.1,2:+plotting")
        depends_on("py-numpy", when="@0.80:1.0.0-rc2,1.0.1:1.1,2:")
        depends_on("py-pandas", when="@1:1.0.0-rc2,1.0.1:1.1,2:+pandas")
        depends_on("py-pandas", when="@1:1.0.0-rc2,1.0.1:1.1,2:+dask")
        depends_on("py-scikit-learn", when="@1.1,2:+scikit-learn")
        depends_on("py-scipy", when="@0.80:1.0.0-rc2,1.0.1:1.1,2:")
    # END DEPENDENCIES

