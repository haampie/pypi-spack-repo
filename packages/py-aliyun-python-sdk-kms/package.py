# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAliyunPythonSdkKms(PythonPackage):
    # BEGIN VERSIONS
    version("2.16.2", sha256="83166468817a4fbc4c958af43ec22856e1bd80f1363f56acf822206febe6b059", url="https://pypi.org/packages/3d/ea/d88e08bfc4a0aee0111f1f24c98b19107bc6783441e7e944907c77b2243d/aliyun_python_sdk_kms-2.16.2-py2.py3-none-any.whl")
    version("2.16.1", sha256="9bc39c693ba83944f5dfb871b118a2925eb8a5ee214dfcce61ee2ea3b6317ef1", url="https://pypi.org/packages/13/90/02d05478df643ceac0021bd3db4f19b42dd06c2b73e082569d0d340de70c/aliyun_python_sdk_kms-2.16.1-py2.py3-none-any.whl")
    version("2.16.0", sha256="c800a1f64d5bac2b1f3589767355f4da606ddf86164f9613d0fb2a84e65b3bea", url="https://pypi.org/packages/70/25/a361278473fb39a1f1aded563518706abad6a0e2d4104cae60b2de056028/aliyun_python_sdk_kms-2.16.0-py2.py3-none-any.whl")
    version("2.15.0", sha256="046ddcde1bc05297a640ca6b6497f7b088e6a437c0b38a9272f7b3bfb9ea1299", url="https://pypi.org/packages/c9/12/e3d05db24485759380582dbd8ad86eef0be762ae54a6ff8bf3ec1bf2c9bf/aliyun_python_sdk_kms-2.15.0-py2.py3-none-any.whl")
    version("2.14.0", sha256="5043fdd78efdb42887eed1d3408c6b12fdf6d7324fd474f72846d97339e1e977", url="https://pypi.org/packages/e5/2c/2056559e7ece7bcb59aabfab54cb67252743993c223e00a42e2a745c3080/aliyun_python_sdk_kms-2.14.0-py2.py3-none-any.whl")
    version("2.13.0", sha256="759d3bb461278830f24462bc0566f8544b6c143b96d0b6d1966ee3e5b84cfa40", url="https://pypi.org/packages/95/83/a840e6c2a921964635663ed6eb02d8abeccc66adcb5b524088344e0a2ba6/aliyun-python-sdk-kms-2.13.0.tar.gz")
    version("2.12.0", sha256="543ce0ef35178a991f65830b1748a422628231e802c88eb334bd266d53c2a509", url="https://pypi.org/packages/9d/39/20f8d6cd49189dac0d79546edeb4188e94d0c746b4ee097814a40db461b9/aliyun-python-sdk-kms-2.12.0.tar.gz")
    version("2.11.0", sha256="6fad3918ae4a45c93e47bea897e9933dc154dc6224a708dcb686a6a9e82f93d2", url="https://pypi.org/packages/e0/90/53403e07470ae560b0a69bf3c0ada9cc4c7a86c8bc0ac593b95839f5602a/aliyun-python-sdk-kms-2.11.0.tar.gz")
    version("2.10.1", sha256="82cf3a94041dda614568a63c69158c8d3b04007344825a250595bf4d17b393b2", url="https://pypi.org/packages/c4/24/8df245371834ae68c748b74c8824cce9b15ff52bd50d71931c6f77310adb/aliyun-python-sdk-kms-2.10.1.tar.gz")
    version("2.10.0", sha256="9c1fc509bfc6ebb73b39a70392343b4144b13be29fc1cb1e880b6a37e6d60af2", url="https://pypi.org/packages/d2/32/834f13c95a7adc5e87652abf1aff938b056cf7bfff406a1a59022398b053/aliyun-python-sdk-kms-2.10.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aliyun-python-sdk-core@2.11.5:", when="@2.14:")
    # END DEPENDENCIES

