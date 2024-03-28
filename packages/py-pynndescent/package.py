# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPynndescent(PythonPackage):
    # BEGIN VERSIONS
    version("0.5.11", sha256="a628f4fc8a67757c8fa15613449ac513fd056258a55b4084e47c06640ec90a8d", url="https://pypi.org/packages/4e/82/0b9851a2fd4da9b57d7931446f5ebab92a98f1f35d3dc0dae5f9ed50a462/pynndescent-0.5.11-py3-none-any.whl")
    version("0.5.10", sha256="5d5dc683c03ef55fe3ddf693859720ca18f85c6e6e5bb0b4f14870278d5288ad", url="https://pypi.org/packages/8f/a2/b6a62a42a075abe06839d725f29c2757f3bb8fdd53746c0a685ae90e1294/pynndescent-0.5.10.tar.gz")
    version("0.5.9", sha256="bacf78d914f44724528adcfea9681ddd6c873d14f4b0526c0ff6b9f243338042", url="https://pypi.org/packages/85/4a/2af728e1b7848db1911223e95d4aa4c6f77d4ac46314cb5158159bbf8343/pynndescent-0.5.9.tar.gz")
    version("0.5.8", sha256="a7c552569bf604a101fd54bba1d27c12389e065945dee3a6777a518c63a46f2b", url="https://pypi.org/packages/de/47/3b0b9e3c6201cd05b95697538085a33175974950c491a1c096970ea01962/pynndescent-0.5.8.tar.gz")
    version("0.5.7", sha256="ecb395255fa36a748b5870b4ba0300ea0f7da8b1964864b8edd62577a84dfd7d", url="https://pypi.org/packages/fa/bd/aa2c2f52e2152d99ddce9233b1260903094fec7db17600104058da439f05/pynndescent-0.5.7.tar.gz")
    version("0.5.6", sha256="61fb31885baac469d67933e2c7c935b6edebb06ee498e2f0f9dfc97c59d3725c", url="https://pypi.org/packages/a2/77/c12c52a51eccd460e26b11bd76c6e00793d15eb00e64381ea8b18d0ae9cb/pynndescent-0.5.6.tar.gz")
    version("0.5.5", sha256="7a7df8412b19cfb3596060faf5a8c5d0bf5b3bd504f8efd900fc4e3918c6f882", url="https://pypi.org/packages/65/55/983836c3328f382213b84da42ee405e3dc695b295889a1dbb54007dbea43/pynndescent-0.5.5.tar.gz")
    version("0.5.4", sha256="221124cbad8e3cf3ed421a4089d80ac5a29d3215e76cb49effc1df887533d2a8", url="https://pypi.org/packages/b1/8d/44bf1c9e69dd9bf0697a3b9375b0729942525c0eee7b7859f563439d676a/pynndescent-0.5.4.tar.gz")
    version("0.5.3", sha256="1d5c4dfb560a1c866b2df5608b80773f58ecb6823432ef0e87909fda0e1333e9", url="https://pypi.org/packages/a7/9f/0a2fe8efa70d3fc61acd52d0ebf94d770cf6aa8fb5e5a27ed25e2cc70c9a/pynndescent-0.5.3.tar.gz")
    version("0.5.2", sha256="d9fd22210b8d64368376ff392e876fb72fe3cda282396cfa6a59440ab6600771", url="https://pypi.org/packages/af/65/8189298dd3a05bbad716ee8e249764ff8800e365d8dc652ad2192ca01b4a/pynndescent-0.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.11:", when="@0.5.11:")
        depends_on("py-llvmlite@0.30:", when="@0.5.11:")
        depends_on("py-numba@0.51.2:", when="@0.5.11:")
        depends_on("py-scikit-learn@0.18:", when="@0.5.11:")
        depends_on("py-scipy@1.0.0:", when="@0.5.11:")
    # END DEPENDENCIES

