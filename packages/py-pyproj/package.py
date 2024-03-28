# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyproj(PythonPackage):
    # BEGIN VERSIONS
    version("3.6.1", sha256="44aa7c704c2b7d8fb3d483bbf75af6cb2350d30a63b144279a09b75fead501bf", url="https://pypi.org/packages/7d/84/2b39bbf888c753ea48b40d47511548c77aa03445465c35cc4c4e9649b643/pyproj-3.6.1.tar.gz")
    version("3.6.1-rc0", sha256="1789ed7df0726d94dc61b32b29c4233c81f2967d21982980e836500bbc26dc7d", url="https://pypi.org/packages/4b/5e/83cbcac997b585d704bdd085e399b7e842c0d343ddddf64b355fb0b60801/pyproj-3.6.1rc0.tar.gz")
    version("3.6.0", sha256="a5b111865b3f0f8b77b3983f2fbe4dd6248fc09d3730295949977c8dcd988062", url="https://pypi.org/packages/38/77/46fe6a107b934fd23b903cb7402b69c8b2480a6cab9481d9f98c6dc7726e/pyproj-3.6.0.tar.gz")
    version("3.6.0-rc0", sha256="122fc92dda0e875c985a6a14841c474cd77355e2ccaab9f69abbaf6c54c25aba", url="https://pypi.org/packages/00/4f/f672812136b07bb624a2c23dde631cbbcf0aab33c7231f00017286c14bc9/pyproj-3.6.0rc0.tar.gz")
    version("3.5.0", sha256="9859d1591c1863414d875ae0759e72c2cffc01ab989dc64137fbac572cc81bf6", url="https://pypi.org/packages/9c/f5/cd9371194d3c939dffddff9e118a018bb7c2f560549bea4c6bc21b24eadd/pyproj-3.5.0.tar.gz")
    version("3.5.0-rc0", sha256="8d0b0f7751b5625fd96354335b3427db1817cad99148017a9afce3742b7f5f28", url="https://pypi.org/packages/10/ce/9235b503514543a2953d58aa6ebdbe4e03d97f5c25b07f8a8fe10f466332/pyproj-3.5.0rc0.tar.gz")
    version("3.4.1", sha256="261eb29b1d55b1eb7f336127344d9b31284d950a9446d1e0d1c2411f7dd8e3ac", url="https://pypi.org/packages/c0/fc/fd53e45d2ad5862d32ab8614e70c3c1f52a8e0d8bd243ee6a23b6a481b4a/pyproj-3.4.1.tar.gz")
    version("3.4.0", sha256="a708445927ace9857f52c3ba67d2915da7b41a8fdcd9b8f99a4c9ed60a75eb33", url="https://pypi.org/packages/aa/d5/492f4284cb88f912d329e8430917ac2f5427833c31843a712cf9dc703471/pyproj-3.4.0.tar.gz")
    version("3.3.1", sha256="b3d8e14d91cc95fb3dbc03a9d0588ac58326803eefa5bbb0978d109de3304fbe", url="https://pypi.org/packages/e3/4d/348402c2fb0d8a8e85a88b8babc6f4efaae9692b7524aedce5fddbef3baf/pyproj-3.3.1.tar.gz")
    version("3.3.0", sha256="ce8bfbc212729e9a643f5f5d77f7a93394e032eda1e2d8799ae902d08add747e", url="https://pypi.org/packages/e4/36/c151d658ca1a1ccfd5ed82ac3b41d13c36cbd0687da97ac1beaeb3381fa8/pyproj-3.3.0.tar.gz")
    version("3.2.1", sha256="4a936093825ff55b24c1fc6cc093541fcf6d0f6d406589ed699e62048ebf3877", url="https://pypi.org/packages/02/48/9d64166dfbb98d515655c3d28bce68f4b984a96c3bfe5ce81b160f16c763/pyproj-3.2.1.tar.gz")
    version("3.2.0", sha256="48df0d5ab085bd2dc6db3bca79e20bf15b08ffca4f4e42df6d87b566633b800c", url="https://pypi.org/packages/2e/9f/217f0cfb328b57a5e471e3d8e1eb58376086ffb50ce74f9977b5bb86f56a/pyproj-3.2.0.tar.gz")
    version("3.1.0", sha256="67b94f4e694ae33fc90dfb7da0e6b5ed5f671dd0acc2f6cf46e9c39d56e16e1a", url="https://pypi.org/packages/7c/1d/20ea3b603db61ccc60f45064a9e00ba2e6263f1de560e33306f6f3d42fcb/pyproj-3.1.0.tar.gz")
    version("3.0.1", sha256="bfbac35490dd17f706700673506eeb8170f8a2a63fb5878171d4e6eef242d141", url="https://pypi.org/packages/2c/12/7a8cca32506747c05ffd5c6ba556cf8435754af0939906cbcc7fa5802ea3/pyproj-3.0.1.tar.gz")
    version("3.0.0", sha256="539e320d06e5441edadad2e2ab276e1877445eca384fc1c056b5501453d433c2", url="https://pypi.org/packages/44/b8/a645507e4188333e15da29a445102ce2621d69788c586b0625ccd16f8a63/pyproj-3.0.0.tar.gz")
    version("2.6.1", sha256="52556f245f1112f121091937b47738d1fbcbd0f13be6fb32689de31ab0975d24", url="https://pypi.org/packages/33/2a/44d5631fe4ad9396a3eecdb4de36bc0cbc4b9893c63e4552413bd97d3465/pyproj-2.6.1.tar.gz")
    version("2.6.0", sha256="977542d2f8cf2981cf3ad72cedfebcd6ac56977c7aa830d9b49fa7888b56e83d", url="https://pypi.org/packages/c0/c2/8c7f27e57835782563715970ec73da41dffc5bb93622f86cc7c3626a9317/pyproj-2.6.0.tar.gz")
    version("2.2.0", sha256="0a4f793cc93539c2292638c498e24422a2ec4b25cb47545addea07724b2a56e5", url="https://pypi.org/packages/73/ef/53a7e9e98595baf4d7212aa731fcec256b432a3db60a55b58a027a4d9d47/pyproj-2.2.0.tar.gz")
    version("2.1.3", sha256="99c52788b01a7bb9a88024bf4d40965c0a66a93d654600b5deacf644775f424d", url="https://pypi.org/packages/a5/05/edfcfd0752e1e3fe5e06245863412bb9aa77888143f6c8900dea62aecdc2/pyproj-2.1.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.6:")
        depends_on("py-certifi", when="@3.6.1-rc0:")
    # END DEPENDENCIES

