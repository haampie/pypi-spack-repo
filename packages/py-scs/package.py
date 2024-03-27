##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScs(PythonPackage):
    version("3.2.4.post1", sha256="7015d7a56d1d5b53264fd277289ea169949309e26101677ff88cd0e5030d032f", url="https://pypi.org/packages/5f/15/a9645e3905ffbfad4685df708da0760a98c5ce23bcf794be99a1cddedec8/scs-3.2.4.post1.tar.gz")
    version("3.2.4", sha256="09ffaa670d8608901db94addd8581376498cd9818eb5ef27fed3560f0bf0661b", url="https://pypi.org/packages/d1/c0/fed69fd319a88ea22a242c98ca79afac8b209c4f7d9e001da5575a5fa8a4/scs-3.2.4.tar.gz")
    version("3.2.3", sha256="e3bd779e7e977e3ae5a2f2035aa4c2a309e29082d59a722d5d6592edc4bdb4b3", url="https://pypi.org/packages/b5/21/0391cc2f02ee80bbb44fec4f1f22d00066b690dc10148582f8421ce1f7bc/scs-3.2.3.tar.gz")
    version("3.2.2", sha256="7206a2ad27ca031d693d65cbcbcfc661498f3983838079a66579bcc784b25293", url="https://pypi.org/packages/27/b7/c42972975cfc21d6d28c08442f7738274219aef9ca8a7adef35b00827ad7/scs-3.2.2.tar.gz")
    version("3.2.0", sha256="6a180d86f61999db50b6a305872056b798740c87c4245006924dd654b6a998dd", url="https://pypi.org/packages/f0/a4/e3cbddd60818e7e900fd0a8e0f0555692c353be7aa8ca1a8299a05c20699/scs-3.2.0.tar.gz")
    version("3.1.0", sha256="1693fc9fa4f9dbec7b3e8d357fdcee8e53262997583479f5c4e2dbca39c7065a", url="https://pypi.org/packages/db/e2/48be7ff0b0babfa825948cad65de3014547489c6a69e334bf939f4b3e889/scs-3.1.0.tar.gz")
    version("3.0.1", sha256="22a8f319b989a5c4048e6313ccacf7d0dc4687af87ac1916c5750651b38f0623", url="https://pypi.org/packages/7a/e4/bbcc353f16926f497b92643b0f85cc2fbfb0b09d19a6f6405e8c4bba593d/scs-3.0.1.tar.gz")
    version("3.0.0", sha256="b29b6ae469041fd8e5831905dee5a10335c985e2d0e6a1c78c8a81c3bb974c2b", url="https://pypi.org/packages/0c/93/48069fe996c41c86f530a056ee8d8915fee64a4d35fd22028d51f3025062/scs-3.0.0.tar.gz")
    version("2.1.4", sha256="ddd6614db7f0e63b69672cfd02ba2c8423dade33a58b0a341a5119091c501739", url="https://pypi.org/packages/5f/f3/7e11e9c0dc22c2bf2e8b4be1ade4fb8055dbe9ea29fd9bda455844b9d7ca/scs-2.1.4.tar.gz")
    version("2.1.3", sha256="7c9ca6730638abcbd004909e7f4816b9e2c1486d3e864b1a26261ca84002cbf0", url="https://pypi.org/packages/12/bd/1ab6a3b3f2791741e6e7c142f932ea1808277e92167e322dec43271b2225/scs-2.1.3.tar.gz")
    version("2.1.1.post2", sha256="f816cfe3d4b4cff3ac2b8b96588c5960ddd2a3dc946bda6b09db04e7bc6577f2", url="https://pypi.org/packages/f2/6e/dbdd778c64c1920ae357a2013ea655d65a1f8b60f397d6e5549e4aafe8ec/scs-2.1.1-2.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@3.2.4:")
        depends_on("py-numpy@1.7:", when="@2:2.1.2")
        depends_on("py-scipy", when="@3.2.4:")
        depends_on("py-scipy@0.13.2:", when="@2:2.1.2")

