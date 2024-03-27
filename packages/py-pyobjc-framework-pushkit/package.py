##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPushkit(PythonPackage):
    version("10.2", sha256="e30fc4926a9fcd3427701e48a8908f72e546720e52b1e0f457ba2fa017974917", url="https://pypi.org/packages/77/80/1e592435111b7f3c01d17f62f5d8694c639035bceca09dbbf8fb71075f7f/pyobjc-framework-PushKit-10.2.tar.gz")
    version("10.1", sha256="12798ad9ae87f7e78690d2bce2ea46f0714d30dd938f5b288717660120a00795", url="https://pypi.org/packages/1c/ff/faeef627788392270c4a487d9ba743e46f4d95e5a4108daa461ee806fafb/pyobjc-framework-PushKit-10.1.tar.gz")
    version("10.0", sha256="54e0b9f3374ba26bdd2c08993080862e7dfc5ccd5c74ad2d5c1c4f9c4c0caa32", url="https://pypi.org/packages/e9/3c/fe5032ccae75c7bf19aa7dd2718fcecfd920c127adb4fe777282e32eaae2/pyobjc-framework-PushKit-10.0.tar.gz")
    version("9.2", sha256="25b338c062d1ebb61faf1c61c271ad98ba9b93fb10c0e33d6f292a3c7644a249", url="https://pypi.org/packages/fa/c4/5b837d2aa7be43ac092bd4abf744c603a146f384cf751802ee8744d721ef/pyobjc-framework-PushKit-9.2.tar.gz")
    version("9.1.1", sha256="041eb2f175959df9294bfb324c1657d4c2b459d24c1b9af24bd9607f964e3f9c", url="https://pypi.org/packages/41/c5/435cb3da75478bc222c88e533b92c0ab3aae7ea304cfe7bc951f78b6ddf4/pyobjc-framework-PushKit-9.1.1.tar.gz")
    version("9.1", sha256="f9bb281fd539db29b35ef2472dca8f79fce6a3dac23d2b0d32e4a22eb76c8d1e", url="https://pypi.org/packages/5a/84/4f4f9e024a5b847727465fcfd7219d815a79ea1e90b4725610e539f5bed2/pyobjc-framework-PushKit-9.1.tar.gz")
    version("9.0.1", sha256="444102fce2244cf8fc3853848707643c4bf204e60bf720687da69fc9982efef3", url="https://pypi.org/packages/ca/43/b62a203ee0a87f605916120905d7014c6633c78003722e6c00d1b957e996/pyobjc-framework-PushKit-9.0.1.tar.gz")
    version("9.0", sha256="dc82358040fc6759b0316267b0c8b69ca9a57c555ba190897380e20fe46729b1", url="https://pypi.org/packages/cf/4a/1ba28c54063e42bffc2afab648c820b3cd145b04b04a4b39c7554bbb558e/pyobjc-framework-PushKit-9.0.tar.gz")
    version("8.5.1", sha256="d026c97d4de29cd5f4f91c3a21d2b77a5a744960803ac5072b3cfe74586df329", url="https://pypi.org/packages/7a/9d/59dfb3a042919dfbc6ceb2f4e47d343b30206f6fcbd2bfd4bb6a3210e821/pyobjc-framework-PushKit-8.5.1.tar.gz")
    version("8.5", sha256="a198ced44b4128ed94a7fb5a31f1d1741b445f85647c26fe182f35bfd14360fc", url="https://pypi.org/packages/c2/b7/bbfb412285e4eb29a0fe8d07fa0ee37cf6dbb21cfd264c33079d13d0e8bf/pyobjc-framework-PushKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

