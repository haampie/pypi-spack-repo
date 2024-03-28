# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyutilib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.0.0", sha256="f1f82d05ad8c42baeef915c8d3d97c0a3cbed6c506c857ab0ab7694dea50ebd8", url="https://pypi.org/packages/e1/e7/c3e5994b4e5c90280b5c14ffef409875ec5436d1d0d9f8585794993a7d77/PyUtilib-6.0.0-py2.py3-none-any.whl")
    version("5.8.0", sha256="729606b20f9bbafc3fc8f21612ea0bcdbe7b13085ec3488fc42a9edace432886", url="https://pypi.org/packages/50/f9/1ee24bdd6cb767eff47565b52ced316bd53f889065af84d787d038309c9e/PyUtilib-5.8.0-py2.py3-none-any.whl")
    version("5.7.3", sha256="b253eca421c165ed9586b7e7b05c7a392f923dbe4b945cefef470b6c497f6bf3", url="https://pypi.org/packages/4a/e6/c1768efd31069377169327fb527d81c16db78ac4c5ae61db7465db354d11/PyUtilib-5.7.3-py2.py3-none-any.whl")
    version("5.7.2", sha256="17eea873bbc7969c08b92cdd7df56c71e7facc4749fda97637b5119cdea8fa0a", url="https://pypi.org/packages/77/86/6bcc45e92b7218fa0969c022923fdb8cd1148e2cec7093ea2dd9335ab73c/PyUtilib-5.7.2-py2.py3-none-any.whl")
    version("5.7.1", sha256="22d6aa4dd9225448e23f1bc4e2fd2a2a61215447c6f18a0e44e94fbe5bf66756", url="https://pypi.org/packages/ca/2c/78944c465f1c54c557121e48fdad4b6ba5bd74f1b17292352dc8cf689ad2/PyUtilib-5.7.1-py2.py3-none-any.whl")
    version("5.6.2", sha256="387f543848309c95b0f705986046422f0628ec186eb791398761754594d8dff4", url="https://pypi.org/packages/a1/69/1e8d3ff9c41827e56798a242534afd7657622e0ed74b9ae97c10608951b7/PyUtilib-5.6.2-py2.py3-none-any.whl")
    version("5.6", sha256="a2a7d440b80b97a2143640fd6cef3fd119ccfb087d462d63b7e6ebd5d9b175cc", url="https://pypi.org/packages/39/c7/ae10126705ee353979205a44f86532b8ca02f2774da077b913dd676e76d3/PyUtilib-5.6-py2.py3-none-any.whl")
    version("5.5.1", sha256="3caa1abe21fd6593cf10de582e8710dd34107811b6eddbaa96c62587c14bf682", url="https://pypi.org/packages/95/7c/14f46f157efce7b7a6fc47fcffe0f3ec0437b8432f39385d3dc6a9c91166/PyUtilib-5.5.1-py2.py3-none-any.whl")
    version("5.5", sha256="9219d166ff966546eb87970190ac099718ddcc770f31c6cc650915fc5b040e64", url="https://pypi.org/packages/4a/eb/30038587f3a76c162bdeb5f6320dffd28ba45f45bbac95beceeab0ec503c/PyUtilib-5.5-py2.py3-none-any.whl")
    version("5.4.1", sha256="1ca1ddf6aed05d764ae2b17a69a30ee996cd1d7e18ebf849d3107ceedd519ea7", url="https://pypi.org/packages/ca/4b/9efe65bad50a3024b6b46c23579a4dadb056ccd113a4d810b9315e1f67be/PyUtilib-5.4.1-py2.py3-none-any.whl")
    version("5.4", sha256="f554e6dfd626ba9ff6ef998a5140c467a0d5641b9a3b9e19158514bb7e093fde", url="https://pypi.org/packages/16/45/f378686bf18fd893df03a256471fde9699a0463f8ba1b8bdb3709833a7bf/PyUtilib-5.4-py2.py3-none-any.whl")
    version("5.3.5", sha256="2dcf04c8018367794c4cd74f2433dba6d1605b8f47c147e5dfd33554d619fc29", url="https://pypi.org/packages/d0/0b/fa2c4c5b5a64b80c53381351202cdbd273bbea83899e46e2074e8ca66743/PyUtilib-5.3.5-py2.py3-none-any.whl")
    version("5.3.3", sha256="2bd15dd0494c696026334b018044b261d2c2099893f51ea82d4ff735f8aea838", url="https://pypi.org/packages/7e/f6/eb1038339c6a4ff52085bb4aebec008b747e60202133a9328c315572e305/PyUtilib-5.3.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-nose", when="@5.4:5.4.0,5.5:5.5.0,5.6:5.6.0,5.6.4:")
        depends_on("py-six", when="@5.4:5.4.0,5.5:5.5.0,5.6:5.6.0,5.6.4:")
    # END DEPENDENCIES

