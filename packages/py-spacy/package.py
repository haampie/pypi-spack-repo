##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpacy(PythonPackage):
    version("3.7.4", sha256="525f2ced2e40761562c8cace93ef6a1e6e8c483f27bd564bc1b15f608efbe85b", url="https://pypi.org/packages/b8/42/2b2062b1ad8d13915ed9365b342cdd8c9dd32926d31ed4524def0584e225/spacy-3.7.4.tar.gz")
    version("3.7.3", sha256="99265028fbdc6e12249c53305e461f79a103637b0e6866c28af0e46365f751e1", url="https://pypi.org/packages/ef/b9/8b098779dd888076220498da27890f9017691b6ff1e1edf76fc0fc2e2929/spacy-3.7.3.tar.gz")
    version("3.7.2", sha256="cedf4927bf0d3fec773a6ce48d5d2c91bdb02fed3c7d5ec07bdb873f1126f1a0", url="https://pypi.org/packages/ef/9f/0afee264faa799e7300e2261680c518b2ec32bc2c1e5646684b51ec8b677/spacy-3.7.2.tar.gz")
    version("3.7.1", sha256="5c6b727194d676f642534353d129d4f110c9cbf533268c230a333a4f92a5a185", url="https://pypi.org/packages/ca/16/843e55cfae62c0608c5caf939e1a080d6291487fcced65eab62da5a557d1/spacy-3.7.1.tar.gz")
    version("3.7.0", sha256="ba07890a607d5a0421a3a1f63e1aa76694085eaf5f94e12a98edbff321fc9323", url="https://pypi.org/packages/a7/84/4210080c47e24d1ebff42466551f837d34ae137a6387258698ebd822e291/spacy-3.7.0.tar.gz")
    version("3.6.1", sha256="6323a98706ae2d5561694b03a8b0b5751887a002903a4894e68aeb29cc672166", url="https://pypi.org/packages/94/f5/c1cb70915af0a1976c40512e450ec86dba02ef547e3af49bd9061af4bbd0/spacy-3.6.1.tar.gz")
    version("3.6.0", sha256="3185c28cd005ba2e0c2dfa9755e262abbad20e885c08df0040543c3092236221", url="https://pypi.org/packages/9a/92/314ea496b9e91695be405765ce45f207f352e5ce3ac564598ead9de2e422/spacy-3.6.0.tar.gz")
    version("3.5.4", sha256="9a9c167e9dcebfefacc75dac34a8e72becbe348eb45bbf06a6c0523ae05ac425", url="https://pypi.org/packages/8a/5c/e05f2e37d23d7a99a27edb6ebf41112e1bc39c4f22649423d38f8e223af3/spacy-3.5.4.tar.gz")
    version("3.5.3", sha256="35971d6721576538d6c423c66a09ce00bf66e10e40726a57b7a81993180c248c", url="https://pypi.org/packages/4c/a6/ea3bb98bb7fcb6177c3b44e778d17e3aaebfa283feb6763578abaa8664de/spacy-3.5.3.tar.gz")
    version("3.5.2", sha256="22c1ffaab285b7477003d4b5b038414cc32468a690d479015b9a698c531c813b", url="https://pypi.org/packages/7f/17/46f037b3d49844e4cd529f8d24e3873d52befeab1533899f183290b8b6d1/spacy-3.5.2.tar.gz")
    version("2.3.7", sha256="c0f2315fea23497662e28212f89af3a03667f97c867c597b599c37ab84092e22", url="https://pypi.org/packages/79/1c/7c5f7541eb883181b564a8c8ba15d21b2d7b8a38ae32f31763575cf8857d/spacy-2.3.7.tar.gz")
    version("2.3.2", sha256="818de26e0e383f64ccbe3db185574920de05923d8deac8bbb12113b9e33cee1f", url="https://pypi.org/packages/18/db/499f374339b522b6618234b93f25d2990692795ccce3152519ccc508586c/spacy-2.3.2.tar.gz")
    version("2.2.4", sha256="f0f3a67c5841e6e35d62c98f40ebb3d132587d3aba4f4dccac5056c4e90ff5b9", url="https://pypi.org/packages/92/1b/a982be17aa65d61121718f0309a2d8a56a04d6babee4c1a6882965f0d56d/spacy-2.2.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-blis@0.4:0.4.0.0,0.4.1:0.4", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-catalogue@2.0.6:2.0", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-catalogue@0.0.7:1", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-cymem@2:", when="@2.1.3,2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-jinja2", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-langcodes@3.2:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-murmurhash@0.28:1.0", when="@2.1.3,2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-numpy@1.15.0:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2: ^python@:3.8")
        depends_on("py-numpy@1.19.0:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2: ^python@3.9:")
        depends_on("py-numpy@1.15.0:", when="@2.1.3,2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-packaging@20:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-pathy@0.10:", when="@3.7:3.7.0.0,3.7.1")
        depends_on("py-plac@0.9.6:1.1", when="@2.2.4:2.3.2,3.0.0.dev:3.0.0.dev8")
        depends_on("py-preshed@3.0.2:3", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-requests@2.13:", when="@2.1.3,2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-setuptools", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-smart-open@5.2.1:6", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-spacy-legacy@3.0.11:3", when="@3.7:3.7.0.0,3.7.1:3")
        depends_on("py-spacy-loggers", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-srsly@2.4.3:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-srsly@1.0.2:1", when="@2.2.4:2.3.2")
        depends_on("py-thinc@8.2.2:8", when="@3.7.3:3")
        depends_on("py-thinc@8.1.8:8", when="@3.7:3.7.0.0,3.7.1:3.7.2")
        depends_on("py-thinc@7.4.1", when="@2.3:2.3.2")
        depends_on("py-thinc@7.4:7.4.0.0", when="@2.2.4:2.2")
        depends_on("py-tqdm@4.38:", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-typer@0.3:0.9", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-wasabi@0.9.1:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-wasabi@0.4:0", when="@2.2.4:2.3.2,3.0.0.dev:3.0.0.dev8")
        depends_on("py-weasel@0.1.0:", when="@3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")

