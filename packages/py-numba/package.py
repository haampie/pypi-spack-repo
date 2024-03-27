##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumba(PythonPackage):
    version("0.59.1", sha256="76f69132b96028d2774ed20415e8c528a34e3299a40581bae178f0994a2f370b", url="https://pypi.org/packages/bb/84/468592513867604800592b58d106f5e7e6ef61de226b59c1e9313917fbbb/numba-0.59.1.tar.gz")
    version("0.59.0", sha256="12b9b064a3e4ad00e2371fc5212ef0396c80f41caec9b5ec391c8b04b6eaf2a8", url="https://pypi.org/packages/a3/5e/ad8f7a2ca55b5903cea0aa6ec0bb0eee7faeec3ca1c4f871d99ff46aad36/numba-0.59.0.tar.gz")
    version("0.58.1", sha256="487ded0633efccd9ca3a46364b40006dbdaca0f95e99b8b83e778d1195ebcbaa", url="https://pypi.org/packages/13/2b/0f750d451fd961fd91d6bc86c512781fa46f9ef64813007e501482522ff9/numba-0.58.1.tar.gz")
    version("0.58.0", sha256="e5d5a318dc65a101ef846d7fd93f3cf2f7942494019e8342e51238b360739125", url="https://pypi.org/packages/c6/95/985695c7355606dc631f0ba75609e004aa5d36dc5d3d56fbb5a747a214df/numba-0.58.0.tar.gz")
    version("0.57.1", sha256="33c0500170d213e66d90558ad6aca57d3e03e97bb11da82e6d87ab793648cb17", url="https://pypi.org/packages/f0/51/cc9d67b9357ac04e7c838dfa880acbfee0c15e02ca5a35b3e064a36131f7/numba-0.57.1.tar.gz")
    version("0.57.0", sha256="2af6d81067a5bdc13960c6d2519dbabbf4d5d597cf75d640c5aeaefd48c6420a", url="https://pypi.org/packages/7e/cf/aa289fc5d668c368b2c7655e6ac916dbee34df96dc6eae9ad70993b169cb/numba-0.57.0.tar.gz")
    version("0.56.4", sha256="32d9fef412c81483d7efe0ceb6cf4d3310fde8b624a9cecca00f790573ac96ee", url="https://pypi.org/packages/e2/1e/de917b683bb5f0b6078fb1397293eab84c4eaa825fbf94d73d6488eb354f/numba-0.56.4.tar.gz")
    version("0.56.3", sha256="07a2d8a149ecc6eca4ef5c7216e58511d48184854e07b7f59d0c32fab0742e8f", url="https://pypi.org/packages/a3/95/7df08647e773a2417e24de8fea9087606b37074f63830a3f2dbabd97f01b/numba-0.56.3.tar.gz")
    version("0.56.2", sha256="3492f0a5d09e257fc521f5377a6c6b907eec1920d14739f0b2458b9d29946a5a", url="https://pypi.org/packages/d9/fa/4905b6ca79084ecf47c543121e317a9dc4b69183343f9c07c3e78bd7e2a1/numba-0.56.2.tar.gz")
    version("0.56.0", sha256="87a647dd4b8fce389869ff71f117732de9a519fe07663d9a02d75724eb8e244d", url="https://pypi.org/packages/b3/23/fd8e7aa70f6c0b41c99de6aae7afc6850ebac2477687e68c6529bfaa41ba/numba-0.56.0.tar.gz")
    version("0.55.2", sha256="e428d9e11d9ba592849ccc9f7a009003eb7d30612007e365afe743ce7118c6f4", url="https://pypi.org/packages/39/dd/7109030bb584e8f0c4c8796bfd39fc5811cb77368a8c5db335f99c1fec9e/numba-0.55.2.tar.gz")
    version("0.55.1", sha256="03e9069a2666d1c84f93b00dbd716fb8fedde8bb2c6efafa2f04842a46442ea3", url="https://pypi.org/packages/69/df/bd36068b2c1d0d34794f8ac0c222f9c4ad88dc710b400e65dbb3b59ea57e/numba-0.55.1.tar.gz")
    version("0.54.0", sha256="bad6bd98ab2e41c34aa9c80b8d9737e07d92a53df4f74d3ada1458b0b516ccff", url="https://pypi.org/packages/24/66/4720b6f70b42c74f10296a9803f8ba28c284f55cee6839f457bc67588277/numba-0.54.0.tar.gz")
    version("0.53.1", sha256="9cd4e5216acdc66c4e9dab2dfd22ddb5bef151185c070d4a3cd8e78638aff5b0", url="https://pypi.org/packages/e3/7d/3d61160836e49f40913741c464f119551c15ed371c1d91ea50308495b93b/numba-0.53.1.tar.gz")
    version("0.53.0", sha256="55c11d7edbba2ba715f2b56f5294cad55cfd87bff98e2627c3047c2d5cc52d16", url="https://pypi.org/packages/b0/6d/bb1204879726d6db6dc92de995bdbd64792369f0be3f8a36710cc2d93f78/numba-0.53.0.tar.gz")
    version("0.53.0-rc3", sha256="0913c85342260b2ed40d21e047b6925eaac381225e67c406069cd60828428858", url="https://pypi.org/packages/5e/ef/d761365ea63f28b85574069e953664e9fe218d50b85b3f84849ebecf953c/numba-0.53.0rc3.tar.gz")
    version("0.52.0", sha256="44661c5bd85e3d3619be0a40eedee34e397e9ccb3d4c458b70e10bf95d1ce933", url="https://pypi.org/packages/46/e1/cbbc7c7967d9b10e54c852bf5bece0222a63bfb809d3354014c957ef1bda/numba-0.52.0.tar.gz")
    version("0.51.2", sha256="16bd59572114adbf5f600ea383880d7b2071ae45477e84a24994e089ea390768", url="https://pypi.org/packages/5e/81/6fd1dd064bcf71a79da109e8966a39e2da61d68bf0bd1e0839fa997f8c41/numba-0.51.2.tar.gz")
    version("0.51.1", sha256="1e765b1a41535684bf3b0465c1d0a24dcbbff6af325270c8f4dad924c0940160", url="https://pypi.org/packages/a0/25/118cfd7d323abf3e353710e2ff7fe12b1470c302103ad9675cd794f2988e/numba-0.51.1.tar.gz")
    version("0.51.0", sha256="da57ef00bc814bf54446fb3f8c0374557a7476e40279ceabefd9f12b05cc3c0c", url="https://pypi.org/packages/cb/fd/8f75a154d45aa5ab9f2b55dba1f118f9f6ae14553912de4d4fc606fcb6e2/numba-0.51.0.tar.gz")
    version("0.50.1", sha256="89e81b51b880f9b18c82b7095beaccc6856fcf84ba29c4f0ced42e4e5748a3a7", url="https://pypi.org/packages/62/17/d42c2bb47cab6668cb2e47ee44b86556f4fb95fd6e8105ed55211c89c8dd/numba-0.50.1.tar.gz")
    version("0.50.0", sha256="c9e5752821530694294db41ee19a4b00e5826c689821907f6c2ece9a02756b29", url="https://pypi.org/packages/34/c1/6cad072da9dba912aa67bcf16f952ddbf6e4598e48180c402057d062df19/numba-0.50.0.tar.gz")
    version("0.49.1", sha256="89e1ad8215918036b0ffc53501888d44ed44c1f2cb09a9e047d06af5cd7e7a5a", url="https://pypi.org/packages/a8/23/d56b70e79c18c34c1787bf2cda957f821790ec7ccd35a1962d5be102d572/numba-0.49.1.tar.gz")
    version("0.48.0", sha256="9d21bc77e67006b5723052840c88cc59248e079a907cc68f1a1a264e1eaba017", url="https://pypi.org/packages/c3/81/453926761dc00b02b22d1cd6935aaa8a736fca011d33615315bc7c132788/numba-0.48.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.59:")
        depends_on("python@:3.10", when="@0.55")
        depends_on("python@:3.9", when="@0.53:0.54")
        depends_on("python@:3.8", when="@0.52.0-rc3:0.52")
        depends_on("py-llvmlite@0.42:", when="@0.59:")
        depends_on("py-llvmlite@0.33", when="@0.50")
        depends_on("py-llvmlite@0.31:0.32", when="@0.49")
        depends_on("py-llvmlite@0.31", when="@0.48")
        depends_on("py-numpy@1.22.0:1", when="@0.59:")
        depends_on("py-numpy@1.15.0:", when="@0.48:0.50")
        depends_on("py-setuptools", when="@0.47:0.50")

