# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPulp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.0", sha256="4a19814a5b0a4392d788ac2315263435293579b0583c3469943fe0c6a586f263", url="https://pypi.org/packages/09/d7/57e71e11108203039c895643368c0d1a99fe719a6a80184edf240c33d25f/PuLP-2.8.0-py3-none-any.whl")
    version("2.7.0", sha256="b6de42c929e80325bf44cc7a2997f02535440800c376b9eb8cb7b4670ed53769", url="https://pypi.org/packages/a6/60/b91acaa7995bfcd72f1739ea2b0f5cda707329e17f0b7f921fd8acc79889/PuLP-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="37ea19fde27c2a767989a40e945d7a44b8c9cf007bd433e2c0a73acbd5e92f0c", url="https://pypi.org/packages/37/77/fdaf479eac225c0c172a92be397dbdbc0ef35cb71767c3e8fec804b02239/PuLP-2.6.0-py3-none-any.whl")
    version("2.5.1", sha256="7da33c71388de692bd47f54299f64e06dbff005fb7330abc27ce08c05b871097", url="https://pypi.org/packages/4c/8a/4d36747f104ff682173a76784a604f6b99dbb3db491ed7692d6712d606a7/PuLP-2.5.1-py3-none-any.whl")
    version("2.5.0", sha256="dec41176fcb5d935726f98d4ad5e51346ba7165b3ec814e44dbd762006b0a605", url="https://pypi.org/packages/44/56/9454be3d6c3019ab54b32a90e2a9201916da208a28963fe7dadbbfc9761a/PuLP-2.5.0-py3-none-any.whl")
    version("2.4", sha256="10aa02198435ad5792b7922737fb66a19a7cb4579d49317e402c8a1e1fc099ed", url="https://pypi.org/packages/14/c4/0eec14a0123209c261de6ff154ef3be5cad3fd557c084f468356662e0585/PuLP-2.4-py3-none-any.whl")
    version("2.3.1", sha256="399f95edae0ac0abd9baddc75465632ebfb368861086c86bdf94bd850af192da", url="https://pypi.org/packages/89/0c/6d80f5f81a92d1733cc5ca180491b8a3cd5839e335627a0046c81b7d3d3d/PuLP-2.3.1-py3-none-any.whl")
    version("2.3", sha256="1953894015ed3b9dfefea14a2fba1deef4b47138ef847d05c66ef9806f9fc3b4", url="https://pypi.org/packages/c3/22/5743d7b5d69f84fb63a0b4925862522dbf80e82defcd0c447afb694f3fd0/PuLP-2.3-py3-none-any.whl")
    version("2.2", sha256="bdb3bd766e8d1362ae59787c508d8db02163b32633f06224701d815535f36cdf", url="https://pypi.org/packages/16/c8/cdb6e4c47c775e837f6f1a26162963440b7f9d47d01dcb92ce712d5eecb9/PuLP-2.2-py3-none-any.whl")
    version("2.1", sha256="c15f265ae3d0c205900ff91cce2d157f191adc8a6a3967b3e146ec7faaca70e0", url="https://pypi.org/packages/41/34/757c88c320f80ce602199603afe63aed1e0bc11180b9a9fb6018fb2ce7ef/PuLP-2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-amply@0.1.2:", when="@2.2:2.4")
        depends_on("py-pyparsing@2.0.1:", when="@2.1")
    # END DEPENDENCIES

