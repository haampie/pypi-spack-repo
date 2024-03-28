# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH5io(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.2", sha256="eec440800119765151b1aa35af96c18e05be8275be0dea1bdbc20a48f0aa54bb", url="https://pypi.org/packages/c6/f7/649c516119cd385036e884176d3ae263d176ac66636e11f4f31f16a79ca2/h5io-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="5432cca882f4cd25892205ccc9beb737902d3fe09b6feadbd8bb1ca33853e257", url="https://pypi.org/packages/5c/8d/39ca5a07487b2a08b50c5006f52ef920b3f974e3791391b6b59a9c9ad765/h5io-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="4845b4d5455c8f79987b5783baede71b3a956f4884caf760065fcd9491eb86d0", url="https://pypi.org/packages/96/7b/cbd98caca25bb9d5c2510cc5df8f8fa3d69d2e8ccc040c4a868a6d0d0127/h5io-0.2.0-py3-none-any.whl")
    version("0.1.10", sha256="fe70c1025750b444df9f3fca1f4aa34dd1730f284f73da66a487659ab21909c0", url="https://pypi.org/packages/5f/0c/d3ddaa214ef1405129deb37cce072b1255aa2da886fd1d7eb367904b4f45/h5io-0.1.10-py3-none-any.whl")
    version("0.1.9", sha256="75a8b16731849888ba0c754da71ed4f1e05e73ebf76b1bd1eefe3f6c5b1f051b", url="https://pypi.org/packages/ba/e5/3677123515a5e3f91c2e64c86e54ba6fb64de973cae171cb5acde554b648/h5io-0.1.9-py3-none-any.whl")
    version("0.1.8", sha256="16e70df19bae4d7407d152a6b03488964ba177ebe8abae9d54ec619d974807ee", url="https://pypi.org/packages/d6/49/344b3c5af35cde551ca4c8ba95d3844a7ec5a8b267bb1f8e7c5848f0883e/h5io-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="a6af826cea2da19901ca39a8a6212522c151cdf1fc171c4a381e3f7f25bb737e", url="https://pypi.org/packages/07/da/9a458c143ee79d7b340e2ac1301de14a9558336bdb07bfbd97f8e9252637/h5io-0.1.7-py3-none-any.whl")
    version("0.1.6", sha256="099b0aa16fb61d860ebd447acc77e33020f6f2850390f1ac5a22c5a41b447fdf", url="https://pypi.org/packages/29/65/c47a854941f421ab80fc4cf459c944bfba5e434c0035069f93f00e253c87/h5io-0.1.6-py3-none-any.whl")
    version("0.1.5", sha256="2e4d2eb83f69900d2562026ee0cae01121173b80f37b15169499a502cfed8674", url="https://pypi.org/packages/88/b3/c70bf743ee3d175623bd96a424e895290b68f66c99a5cb1757053f02471e/h5io-0.1.5.tar.gz")
    version("0.1.4", sha256="623690ce134522c0b5184d4793c1fe7bd1230308f0a35f77631aa69af81c36ed", url="https://pypi.org/packages/11/81/f1e24d13abc4f3d92b3c1457ea47e3c0dbb2b3726bf5ac9f199f4cc8c152/h5io-0.1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-h5py", when="@0.1.7:")
        depends_on("py-numpy", when="@0.1.6:")
    # END DEPENDENCIES

