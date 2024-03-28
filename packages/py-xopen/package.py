# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXopen(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.1", sha256="8b90d6f6eedb337dec438aa1622b856749e55de864be75e17e51745689a346f2", url="https://pypi.org/packages/37/6e/dcfef97487c1d2551b3f505356fef2d7d2dd10a301197f0bba6b2e38a695/xopen-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="3334d9b269a946fce5ca111b16e74f58cc51b1686036c3979f692a3045b9b5de", url="https://pypi.org/packages/ed/b5/a96beaf8d4c2676767011586f4db68ae2c34366775be788b07879bc9fb07/xopen-2.0.0-py3-none-any.whl")
    version("1.9.0", sha256="1f48645d109b8cb19c34d3b8fe659286fe531f363b61befc84a2d6854378dd4f", url="https://pypi.org/packages/62/35/ea131bcb97d153f90a779c0eb14de6e2cfa0b7a77269455e3c5aa24c75a6/xopen-1.9.0-py3-none-any.whl")
    version("1.8.0", sha256="e151a23bcaa0913e9683654c197d1da2444d4e59f27aa17e93bbf42eb4a72d7d", url="https://pypi.org/packages/48/dc/de5c8e5d11b252f321045460ceedc3e6d07c7b6de2983a33c2a1e597c7fa/xopen-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="c4c6c978bb5f6f2a4364438da09f4f8fde078b6df4de18e3f72fccc472d1ee33", url="https://pypi.org/packages/ac/7c/9d0f5437e649404e5d2aa202b0ca21a5c4c54583af8693f8ec5395e0833e/xopen-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="a23913c5263c1567562a77a15260e5d933ea5ef27d5ce95df7be8f637636fd7c", url="https://pypi.org/packages/14/a5/b990e46d1c3d309e63357cb730797594b5b7071aaa57b8a4c3d30d007c7f/xopen-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="114b3b7b8a874863cc87af1750b99a8365bd7f6ff100a803b6348de76d4a79c4", url="https://pypi.org/packages/8d/1e/acf07bd3be5c07d36aa4362b4a3176d9961c341cbb2340cbd74b18821336/xopen-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="4b91b75c447c404c630644af63000f53829c119e1c9f8abd1bfe529c83a5dc3b", url="https://pypi.org/packages/1e/4b/0a9253a0223dd2a037df05f848f389b470c40c5016c37481c78615145a68/xopen-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="ddafc025f91ff63df5022b78e622abf769779ca82b5e8a7b68b42ff9c8658035", url="https://pypi.org/packages/49/cd/b901b1ea766fa0692992ca8a91d65e2d0dac8145224a9d8641361631da0a/xopen-1.3.0-py3-none-any.whl")
    version("1.2.1", sha256="5e69aad5cc29d9a1b8d4916b11dcbc729561cb631d9bd1a149be323957048a8c", url="https://pypi.org/packages/24/71/c40b54cc1d0e2beccc13c700fc2a1ea3d05c535d235d42ea8594fb609e12/xopen-1.2.1-py3-none-any.whl")
    version("1.1.0", sha256="6e57d7f0598bc589bb230390ef006ab5c9f1127bbc3e8257c82f0539f8ac9436", url="https://pypi.org/packages/fd/4a/8721495b3681c87251711a8fe0c7b0faa3620dee9096fd3458fc1b50b81f/xopen-1.1.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="3120647d15eceb703e3669210126d0a886a78b293ca64490fa25d2fa83f7e8ab", url="https://pypi.org/packages/7d/1b/99e2ab42d187b6b0e2902044e589a8cd526e388aaddc88a2f7856999254c/xopen-1.0.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="b21c42d5eb686edb80b23eaf31c82b4015fce937da7b871fb89326a58b6d1e8a", url="https://pypi.org/packages/ed/b6/0006cf17f5b2f7b45ea3258602d1e0b13c6012841645b664ff4977054cd5/xopen-0.9.0-py2.py3-none-any.whl")
    version("0.8.4", sha256="2947ddd6eb1e63996a6d446eb7e4af1ed05fb603ebe2052929872b7a7c787f47", url="https://pypi.org/packages/73/e9/bc35fd93cb6af3a011e44463db468914448825aa659f7636e836b8488b03/xopen-0.8.4-py2.py3-none-any.whl")
    version("0.8.3", sha256="af3c723de5123a71ce87dd8c7985edb25d1b19e3dc34aba65a9303ed019305d3", url="https://pypi.org/packages/fd/ab/e30a40285ddd73dcaad2641794e42bc1de416f4209434675d78c1f31a7f9/xopen-0.8.3-py2.py3-none-any.whl")
    version("0.8.2", sha256="5755814617a5b7049c9cd90c2ea5f752f7036c5db18bfcec4a5548708aa48d2c", url="https://pypi.org/packages/23/67/d986a15915ae70bdaa3d65abf1460319fcf89e987e6748fe137e03ca14b4/xopen-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="9087df746c1aee7887715e07d21ab92e9dc9e2991a401281dd9bf497b5e3de38", url="https://pypi.org/packages/14/75/64f9768111d54846c710c1e796ce43516d373b68e9ce5e05143366268d78/xopen-0.8.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="b097cd25e8afec42b6e1780c1f6315016171b5b6936100cdf307d121e2cbab9f", url="https://pypi.org/packages/c4/3b/52f8a5d32c97e6301ea85419f0fc0eaed5cfaedc6a973990a2908116da31/xopen-0.5.0.tar.gz")
    version("0.1.1", sha256="d1320ca46ed464a59db4c27c7a44caf5e268301e68319f0295d06bf6a9afa6f3", url="https://pypi.org/packages/9a/b7/8906d6b2c4f874c0aacc676709a3d533362ac93bebc4a656c9df19421c9b/xopen-0.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-isal@0.3:", when="@1.1 platform=linux")

        # marker: platform_machine == "x86_64" or platform_machine == "AMD64"
        # depends_on("py-isal@0.9:", when="@1.3:1.4")

        # marker: platform_machine == "x86_64" or platform_machine == "AMD64" or platform_machine == "aarch64"
        # depends_on("py-isal@1.6.1:", when="@2:")
        # depends_on("py-isal@1.4.1:", when="@1.8:1")
        # depends_on("py-isal@0.9:", when="@1.2")
        # depends_on("py-zlib-ng@0.4.1:", when="@2:")
        # depends_on("py-zlib-ng@0.4:", when="@1.9:1")

        # marker: platform_python_implementation == "CPython" and (platform_machine == "x86_64" or platform_machine == "AMD64")
        # depends_on("py-isal@1:", when="@1.6:1.7")
        # depends_on("py-isal@0.9:", when="@1.5")
    # END DEPENDENCIES

