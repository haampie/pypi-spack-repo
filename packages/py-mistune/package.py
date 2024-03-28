# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMistune(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.2", sha256="71481854c30fdbc938963d3605b72501f5c10a9320ecd412c121c163a1c7d205", url="https://pypi.org/packages/f0/74/c95adcdf032956d9ef6c89a9b8a5152bf73915f8c633f3e3d88d06bd699c/mistune-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="b9b3e438efbb57c62b5beb5e134dab664800bdf1284a7ee09e8b12b13eb1aac6", url="https://pypi.org/packages/cc/c0/ac9587149e37cde62ae338e9db8241ae2fdc79a84bde8c8ba7caea2c22d8/mistune-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="32eaf3c092715730f754903698c99cba8474606f66c72c393ebb7f1dfa5c8c48", url="https://pypi.org/packages/55/97/adcde5767133f2f49023caa8312bf8202e9f1f410b6ef73c185ea3abb6d8/mistune-3.0.0-py3-none-any.whl")
    version("3.0.0-rc5", sha256="4f6a4e6624a99bf1e48a2d2868715a5939d3932f988d54e18d36c8585cd9b479", url="https://pypi.org/packages/8a/2a/518e65a5fd0e360144e139fd3ca0597544df4557f0a043f9a8972c7935f4/mistune-3.0.0rc5-py3-none-any.whl")
    version("3.0.0-rc4", sha256="c5d2002dcfb14d963c9f70dc9cd95b907eb1330fbf99a481139b2c21c05bffd4", url="https://pypi.org/packages/f3/c3/fa81ef3b64c58be3ad3e993fdef938f7e5ddddd9a427ab154b9f1d67f0d6/mistune-3.0.0rc4-py2.py3-none-any.whl")
    version("3.0.0-rc3", sha256="c703f92f20ae64ded98e00adb395afc3aae037a1ad041c4454aed1f9c365321b", url="https://pypi.org/packages/39/fe/246bb864afe5c9dc29e6d91832af8d47253a7d50dbcf8902a417243ad9e9/mistune-3.0.0rc3-py2.py3-none-any.whl")
    version("3.0.0-rc2", sha256="9d81d190dc655b9c7adf5ccd583be1185fb6bcafa4b5f15bb88126b37806bc77", url="https://pypi.org/packages/17/37/0a4c3d17b08e8fd5952db6445edebee7e68810c63e9bbafa9bf7f24ab23b/mistune-3.0.0rc2-py2.py3-none-any.whl")
    version("2.0.5", sha256="bad7f5d431886fcbaf5f758118ecff70d31f75231b34024a1341120340a65ce8", url="https://pypi.org/packages/9f/e5/780d22d19543f339aad583304f58002975b586757aa590cbe7bea5cc6f13/mistune-2.0.5-py2.py3-none-any.whl")
    version("2.0.4", sha256="182cc5ee6f8ed1b807de6b7bb50155df7b66495412836b9a74c8fbdfc75fe36d", url="https://pypi.org/packages/3a/c7/b0a4413a4d9b7a4fda0d710fd90dba62375f0d0c4544e848dc7656757c0c/mistune-2.0.4-py2.py3-none-any.whl")
    version("2.0.3", sha256="e3964140c0775535fba50bd616fe180920044a64bc21850253267b07bff89924", url="https://pypi.org/packages/37/7f/3cfa697f14943e7ffd9a1d864ac857ebe269813228dc00ebbf28ed6cea43/mistune-2.0.3-py2.py3-none-any.whl")
    version("2.0.2", sha256="6bab6c6abd711c4604206c7d8cad5cd48b28f072b4bb75797d74146ba393a049", url="https://pypi.org/packages/a7/39/c1c7f390413f378b5291a7943e05bd2a4df772b5526f17cb8fa5e6fcf497/mistune-2.0.2-py2.py3-none-any.whl")
    version("2.0.1", sha256="6361adbdd2763cd7a31ce53b5f127b762ac543b72f3891f8465f418a1456be59", url="https://pypi.org/packages/55/12/b6cf3319d5bc5bf0526b93c7e25e8a9a5b0f925345f9aff9160191f32c39/mistune-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="7fce5b2df20061d177dcc55fba2d9d06e8af65c39a84eba537db3cf685ed282f", url="https://pypi.org/packages/b0/bb/babd4df1d6809a58c19ee1b42100c3921b209b60c7f30a8874575f57e171/mistune-2.0.0-py2.py3-none-any.whl")
    version("0.8.4", sha256="88a1051873018da288eee8538d476dffe1262495144b33ecb586c4ab266bb8d4", url="https://pypi.org/packages/09/ec/4b43dae793655b7d8a25f76119624350b4d65eb663459eb9603d7f1f0345/mistune-0.8.4-py2.py3-none-any.whl")
    version("0.8.3", sha256="b4c512ce2fc99e5a62eb95a4aba4b73e5f90264115c40b70a21e1f7d4e0eac91", url="https://pypi.org/packages/c8/8c/87f4d359438ba0321a2ae91936030110bfcc62fef752656321a72b8c1af9/mistune-0.8.3-py2.py3-none-any.whl")
    version("0.8.2", sha256="74c8bee5aba17f37d394c58df6a8d4ccc306ea7990fbea0aa338572fd8f7aa1c", url="https://pypi.org/packages/d5/f8/177f311bc9366a22c815f4b9179c63520f0f2cb373333998252be25ba777/mistune-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="511f11b307b061136b2aaa99854fa078d688c79426ee9c5857ba784f7a2fad40", url="https://pypi.org/packages/95/bd/a16b8dd4b8a2921e006fd81ca764f748ea5a7e31974095392de970b17228/mistune-0.8.1-py2.py3-none-any.whl")
    version("0.8", sha256="78f5d7f4850c0df94aeec64f994bb8390ca0bc717034bff8d63452815695f02f", url="https://pypi.org/packages/55/7d/06fa3e6d908360866e5f2d731ef5e11a5c001167229fa6e43b9adf7791dd/mistune-0.8-py2.py3-none-any.whl")
    version("0.7.4", sha256="8517af9f5cd1857bb83f9a23da75aa516d7538c32a2c5d5c56f3789a9e4cd22f", url="https://pypi.org/packages/25/a4/12a584c0c59c9fed529f8b3c47ca8217c0cf8bcc5e1089d3256410cfbdbc/mistune-0.7.4.tar.gz")
    version("0.7.3", sha256="ee7447aadcf1962b5af767ff0443dcb0499c16bf73ad36dc99d230e7574571e5", url="https://pypi.org/packages/78/56/cda1a8b9cc613d79ac812c7f51ae6d3f0574a4d6642fbcf964ebe79bbe7c/mistune-0.7.3-py2.py3-none-any.whl")
    version("0.7.2", sha256="84ca34642f46a06a5abcc3981f1d89281abc6aa589f145f93f3f8a0b2388fc98", url="https://pypi.org/packages/ee/18/bf9abc9ad14abe4e0eadd6f007ee838dd4c47473ec46540843ca6c43e7d3/mistune-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="6076dedf768348927d991f4371e5a799c6a0158b16091df08ee85ee231d929a7", url="https://pypi.org/packages/47/c6/77dbbbfec1288a6cd1eeeeff3861019443b323a38a759fa26625309f6cf7/mistune-0.7.1.tar.gz")
    version("0.7", sha256="1daa2e55f5de63ecde7c446c4677c0447006752f78ad2c9c1c3c3452d395f89f", url="https://pypi.org/packages/42/b7/2847eccf4e93d8962de4763d6d08dd6b6d41b8f85416f6194a7f50f3b45a/mistune-0.7.tar.gz")
    version("0.6", sha256="d54a69365d01bc97412a39c11674a8aae3f333586e91f38895cc1ad818e13dc5", url="https://pypi.org/packages/c7/52/67cc5e5657e8e7eaf54a583d9c47f078517d702d3bbe3d6f3a04cace8dfb/mistune-0.6.tar.gz")
    version("0.5.1", sha256="cc66489a28845c0e1848ae290af5b555074eb76185136ca058e8eed1faa89692", url="https://pypi.org/packages/dc/65/7c54f73e18b85364dd956d47bed3f331bd2bcf67861fdc2d4890d10a7a6c/mistune-0.5.1.tar.gz")
    version("0.5", sha256="d53d868cfd10cf757160e88adb5760fce95f7026a243f15a02b7c604238e5869", url="https://pypi.org/packages/7f/54/056588bc6885df533dabb3bb7e65d082a4de6dda2bee408278112809c0ec/mistune-0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

