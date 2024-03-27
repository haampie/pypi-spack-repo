##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDask(PythonPackage):
    version("2024.3.1", sha256="1ac260b8716b1a9fc144c0d7f958336812cfc3ef542a3742c9ae02387189b32b", url="https://pypi.org/packages/b6/c5/2c1ecdcc4ade43b57795da9cb8e3442eb3012621439c74d34cd570d59d0f/dask-2024.3.1-py3-none-any.whl")
    version("2024.3.0", sha256="553860536696e213b3ba3b55dfa6c12f68da772c022020f5ca344ef102753caa", url="https://pypi.org/packages/36/9a/d5e80d0ed57c527f69a970694b93dfb2e33b0fccd44189b6164ef589481c/dask-2024.3.0-py3-none-any.whl")
    version("2024.2.1", sha256="a13fcdeead3bab3576495023f83097adcffe2f03c371c241b5a1f0b232b35b38", url="https://pypi.org/packages/ff/d3/f1dcba697c7d7e8470ffa34b31ca1e663d4a2654ef806877f1017ecc5102/dask-2024.2.1-py3-none-any.whl")
    version("2024.2.0", sha256="439efe5479a102d4d2712d69a52458e6c1e78b96c7020976399ce249097caf48", url="https://pypi.org/packages/95/a5/2ab515c77b441795d7154c57ba224fa41c827ba1e291bbbbcc12f8ac050b/dask-2024.2.0-py3-none-any.whl")
    version("2024.1.1", sha256="860ce2797905095beff0187c214840b80c77d752dcb9098a8283e3655a762bf5", url="https://pypi.org/packages/8e/17/acc822d32bcdd055be380f9312afe95a5031a9baa06d5cf3ae911a0e4361/dask-2024.1.1-py3-none-any.whl")
    version("2024.1.0", sha256="717102ef7c309297291095a0061d374f3b72e11ce4e1115ab9faff940e274b4b", url="https://pypi.org/packages/9e/38/38920b8d78b19feac758832cef65e72a49c036cd2609509ef8e94865e882/dask-2024.1.0-py3-none-any.whl")
    version("2023.12.1", sha256="55f316f32da9e68fe995e2c0dc460cb8888cd4a1af32096753788e8af45a8d10", url="https://pypi.org/packages/8a/d0/2841c5396ee6718142a29b57166285643b945b762b98945c33560ea8e49a/dask-2023.12.1-py3-none-any.whl")
    version("2023.12.0", sha256="6cef2fa43815adc8fe895dd3ea473a311249ba0e15e1f7eb9b1b68302339d998", url="https://pypi.org/packages/91/03/d3202129672be2931b3dad7407b24e98c0b847f7b158ffdf88d34cdcbbca/dask-2023.12.0-py3-none-any.whl")
    version("2023.11.0", sha256="b950951ee3f8c86f003b577b6928ecf20089eee6677719578deaba8fd9a78203", url="https://pypi.org/packages/9a/83/e11961f175a6aff67a46dcf4f4f4eba709678b5a351bc4d2c913d9eb39b9/dask-2023.11.0-py3-none-any.whl")
    version("2023.10.1", sha256="1fb0ee4d79e3c7c8f2e7c9f2680fd0ef0668801a10eaa290b970982b26a714da", url="https://pypi.org/packages/54/a1/9a846d38298b81d8999b501467653b2feb69ec983dbd6538306c6b8e1884/dask-2023.10.1-py3-none-any.whl")
    version("2023.4.1", sha256="d541c0a228ef3afd0185e932e4f887d1c3f7e852f1b4c7c2c22f6455d17640de", url="https://pypi.org/packages/54/25/480b2ae325f9be4bc99cbc77da0b757e285dabbeba3b82d43baa231e605b/dask-2023.4.1-py3-none-any.whl")
    version("2023.3.2", sha256="5e64763d62feb18afd3ad66f364e0b4f456f7ac92e894fcc87950af75029ecdf", url="https://pypi.org/packages/c9/7b/2994fdf6e5bf66417caf5fe57c5a453fe54ec4f686c633e8216de7c50a20/dask-2023.3.2-py3-none-any.whl")
    version("2023.3.1", sha256="4a83c05760aedb7deeee8c16d24479292635a1ded6c3f803bf6c3d94ec9e7d20", url="https://pypi.org/packages/4c/4d/22fef64830c0313e7185ed1b20eb2ec89c41790509a463cd3d941e8ad99d/dask-2023.3.1-py3-none-any.whl")
    version("2023.3.0", sha256="4b355da5492fd8699017e786e281ad347528d11c868b645d102124df3621e9ee", url="https://pypi.org/packages/16/94/47aa3c13f037824b2b8c351be6f6abc3b93884b338175ea1ef3faaedfc0d/dask-2023.3.0-py3-none-any.whl")
    version("2023.2.1", sha256="283e810ef5772a845fb970c26aefc3694d2ed2fbf56dca381d9bcca44e0212dd", url="https://pypi.org/packages/42/da/ef0659c3501def402604f4f2b3e8af56d67254d5e0b560d896f5c325dea1/dask-2023.2.1-py3-none-any.whl")
    version("2023.2.0", sha256="14dedb3ae0be51116365a52e9f39db6e6c866f5ea2244aaae62bd83a0dbaaa92", url="https://pypi.org/packages/dc/03/0334ab094ceaf8c27e83f183ca661cd1fc76ed401d1dd3a054e268c87601/dask-2023.2.0-py3-none-any.whl")
    version("2023.1.1", sha256="de7c1da6eb669f6fd082ed6deba60b5f99c16c8a01fccda2f0cfe9712753ca6a", url="https://pypi.org/packages/6d/d7/9b341e5889f3d230c54148666fdb561f8dcc44ba402577f458a9dbb8657a/dask-2023.1.1-py3-none-any.whl")
    version("2023.1.0", sha256="ea313767b3d11e0610fbe7c57f7a01b1f8990bb6c699456ba910d9b31da2c9c0", url="https://pypi.org/packages/4b/9e/040acddf25331048c7e16451914519a80d276f2d84a464d5fb197e3a36fd/dask-2023.1.0-py3-none-any.whl")
    version("2022.12.1", sha256="a833ee774bf702c08d22f31412358d12b007df36c6e8c107f32f17a4b20f1f68", url="https://pypi.org/packages/13/77/b1a49279c5bd063a2d73b88d1f4b29e10d7a33f5135f3245d35ba06ab816/dask-2022.12.1-py3-none-any.whl")
    version("2022.12.0", sha256="3995d2b856920f90bc9bba7329cbe839fe0d45b4e674da22320f37a2d0e3e4f8", url="https://pypi.org/packages/fc/08/ee0758d224b51fa72da4af14934f308b770a8fa7b384fee3163f86b0f7b1/dask-2022.12.0-py3-none-any.whl")
    version("2022.10.2", sha256="928003a97b890a14c8a09a01f15320d261053bda530a8bf191d84f33db4a63b8", url="https://pypi.org/packages/98/f1/2d9dcd8dd04544a2f1c02ca321aef84e57a712ec27842370084875c12b2a/dask-2022.10.2-py3-none-any.whl")
    version("2022.2.1", sha256="cb91f3853413e857c2d8b872a3ffe189fbd55a5cc01ab61e204079240c28004d", url="https://pypi.org/packages/00/de/98331d2d9aaf7894f58642134f1a8851ce1df063000975400ad1e0a01417/dask-2022.2.1-py3-none-any.whl")
    version("2021.6.2", sha256="1f18d0815154b938a529ac3081c8952998d709319e57bbc484b42f0094217d43", url="https://pypi.org/packages/02/36/5e18bf30a172efd676fb7d668cc14d2624c15a4417b6c047e1def79ee450/dask-2021.6.2-py3-none-any.whl")
    version("2021.4.1", sha256="344c342d699466c3f742019b7a33caf2472b751f38370b200ede7d2f354aa1e4", url="https://pypi.org/packages/c3/23/42159cdb5c9edac174296c9976e175742513883f0f7bc132cfc2a2480fab/dask-2021.4.1-py3-none-any.whl")
    version("2020.12.0", sha256="5741db6e2426c001cecd374cba3bba8fea16a2da081089376ebcad9f8cf32aca", url="https://pypi.org/packages/73/95/72275bf8edd695ba6db792f4f09088a0c1ebe6506cb9790ff90b90219016/dask-2020.12.0-py3-none-any.whl")

    variant("array", default=False)
    variant("dataframe", default=False)
    variant("delayed", default=False)
    variant("distributed", default=False)

    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.5.1:")
        depends_on("py-click@8.1:", when="@2023.11:")
        depends_on("py-click@8.0.0:", when="@2023.4.1:2023.10")
        depends_on("py-click@7:", when="@2022.10.1:2023.4.0")
        depends_on("py-cloudpickle@1.5:", when="@2023.4.1:")
        depends_on("py-cloudpickle@1.1:", when="@2021.3.1:2023.4.0")
        depends_on("py-cloudpickle@0.2.2:", when="@2.13:2021.3.0+delayed")
        depends_on("py-dask-expr@1:", when="@2024.3:+dataframe")
        depends_on("py-distributed@2024.3.1:", when="@2024.3.1:+distributed")
        depends_on("py-distributed@2024.3:2024.3.0", when="@2024.3:2024.3.0+distributed")
        depends_on("py-distributed@2024.2.1:2024.2", when="@2024.2.1:2024.2+distributed")
        depends_on("py-distributed@2024.2:2024.2.0", when="@2024.2:2024.2.0+distributed")
        depends_on("py-distributed@2024.1.1:2024.1", when="@2024.1.1:2024.1+distributed")
        depends_on("py-distributed@2024:2024.1.0", when="@2024:2024.1.0+distributed")
        depends_on("py-distributed@2023.12.1:2023", when="@2023.12.1:2023+distributed")
        depends_on("py-distributed@2023.12:2023.12.0", when="@2023.12:2023.12.0+distributed")
        depends_on("py-distributed@2023.11", when="@2023.11+distributed")
        depends_on("py-distributed@2023.10.1:2023.10", when="@2023.10.1:2023.10+distributed")
        depends_on("py-distributed@2023.4.1:2023.4", when="@2023.4.1:2023.4+distributed")
        depends_on("py-distributed@2023.3.2:2023.3.2.0", when="@2023.3.2:2023.3+distributed")
        depends_on("py-distributed@2023.3.1", when="@2023.3.1+distributed")
        depends_on("py-distributed@2023.3:2023.3.0", when="@2023.3:2023.3.0+distributed")
        depends_on("py-distributed@2023.2.1:2023.2", when="@2023.2.1:2023.2+distributed")
        depends_on("py-distributed@2023.2:2023.2.0", when="@2023.2:2023.2.0+distributed")
        depends_on("py-distributed@2023.1.1:2023.1", when="@2023.1.1:2023.1+distributed")
        depends_on("py-distributed@2023:2023.1.0", when="@2023:2023.1.0+distributed")
        depends_on("py-distributed@2022.12.1:2022", when="@2022.12.1:2022+distributed")
        depends_on("py-distributed@2022.12:2022.12.0", when="@2022.12:2022.12.0+distributed")
        depends_on("py-distributed@2022.10.2:2022.10", when="@2022.10.2:2022.10+distributed")
        depends_on("py-distributed@2022.2.1:2022.2", when="@2022.2.1:2022.2+distributed")
        depends_on("py-distributed@2021.6.2:2021.6", when="@2021.6.2:2021.6+distributed")
        depends_on("py-distributed@2021.4.1:", when="@2021.4.1:2021.4+distributed")
        depends_on("py-distributed@2:", when="@2:2021.2+distributed")
        depends_on("py-fsspec@2021.9:", when="@2023.4.1:")
        depends_on("py-fsspec@0.6:", when="@2021.3.1:2023.4.0")
        depends_on("py-fsspec@0.6:", when="@2.8:2021.3.0+dataframe")
        depends_on("py-importlib-metadata@4.13:", when="@2024.3: ^python@:3.11")
        depends_on("py-importlib-metadata@4.13:", when="@2023.3.2:2024.2")
        depends_on("py-numpy@1.21.0:", when="@2023.2.1:+array")
        depends_on("py-numpy@1.21.0:", when="@2023.2.1:2023.7+dataframe")
        depends_on("py-numpy@1.18.0:", when="@2021.8:2023.2.0+dataframe")
        depends_on("py-numpy@1.18.0:", when="@2021.8:2023.2.0+array")
        depends_on("py-numpy@1.16.0:", when="@2021.3.1:2021.7+dataframe")
        depends_on("py-numpy@1.16.0:", when="@2021.3.1:2021.7+array")
        depends_on("py-numpy@1.15.1:", when="@2020:2021.3.0+dataframe")
        depends_on("py-numpy@1.15.1:", when="@2020:2021.3.0+array")
        depends_on("py-packaging@20:", when="@2021.7.1:")
        depends_on("py-pandas@1.3.0:", when="@2023.2.1:+dataframe")
        depends_on("py-pandas@1.0.0:", when="@2021.8:2023.2.0+dataframe")
        depends_on("py-pandas@0.25.0:", when="@2020:2021.7+dataframe")
        depends_on("py-partd@1.2:", when="@2023.2.1:")
        depends_on("py-partd@0.3.10:", when="@2021.3.1:2023.2.0")
        depends_on("py-partd@0.3.10:", when="@2:2021.3.0+dataframe")
        depends_on("py-pyyaml@5.3.1:", when="@2022:")
        depends_on("py-pyyaml", when="@2.17.1:2021")
        depends_on("py-toolz@0.10:", when="@2023.4.1:")
        depends_on("py-toolz@0.8.2:", when="@2021.3.1:2023.4.0")
        depends_on("py-toolz@0.8.2:", when="@2.13:2021.3.0+delayed")
        depends_on("py-toolz@0.8.2:", when="@2.13:2021.3.0+dataframe")
        depends_on("py-toolz@0.8.2:", when="@2.13:2021.3.0+array")

        # self-dependency
        # depends_on("py-dask+array", when="@2023.8:+dataframe")
