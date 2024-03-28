# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRaven(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.10.0", sha256="44a13f87670836e153951af9a3c80405d36b43097db869a36e92809673692ce4", url="https://pypi.org/packages/bd/8e/62e26a88c0a1bbae677200baf0767c1022321a6555634f8129e6d55c5ddc/raven-6.10.0-py2.py3-none-any.whl")
    version("6.9.0", sha256="95f44f3ea2c1b176d5450df4becdb96c15bf2632888f9ab193e9dd22300ce46a", url="https://pypi.org/packages/11/3a/b3e46b279b8bdd9eb55857d0e95044cad31732c80f628bb75e1e9e881a32/raven-6.9.0-py2.py3-none-any.whl")
    version("6.8.0", sha256="1c641e5ebc2d4185560608e253970ca0d4b98475f4edf67735015a415f9e1d48", url="https://pypi.org/packages/21/14/a06bcd2aa519bb659f5cf9e0b8c29158155cea7f6ce6e947d06967642df6/raven-6.8.0-py2.py3-none-any.whl")
    version("6.7.0", sha256="e4edf648829a64234800a10ed94ca08e0b38592f7449fa5e70931db62f5cd851", url="https://pypi.org/packages/51/7c/bdfa7eff52208a949bc5ab770c084f4725c42dde41e36d5a9e15f11a9a14/raven-6.7.0-py2.py3-none-any.whl")
    version("6.6.0", sha256="738a52019d01955d5b44b49d67c9f2f4cedb1b4f70d4fb0b493931174d00e044", url="https://pypi.org/packages/09/db/394b12baaf9f14d8efa03e812bfe806ed60f29fe0602a8431bceb54b0ee4/raven-6.6.0-py2.py3-none-any.whl")
    version("6.5.0", sha256="0adae40e004dfe2181d1f2883aa3d4ca1cf16dbe449ae4b445b011c6eb220a90", url="https://pypi.org/packages/33/b3/d626d5136de3a5b7bf99a98cb983261baee30320fa220f7a5726dcafefbd/raven-6.5.0-py2.py3-none-any.whl")
    version("6.4.0", sha256="2c9cd4d8c267f57db625305aaa89e7dd852d6864c13c7b84f4d4500df07bebd9", url="https://pypi.org/packages/0c/0a/76de154a3a8f9fdeeff3463db37cb0e5616740a7d7c5d099ac78127d5fbf/raven-6.4.0-py2.py3-none-any.whl")
    version("6.3.0", sha256="cb644fb12ee886a341041dcd533540dfc82619a50bf0b7c587af070054bd2c7f", url="https://pypi.org/packages/91/53/520a14d0023275a01b2a7c3716700c933133527a5ba77da7bec6d06ce4b8/raven-6.3.0-py2.py3-none-any.whl")
    version("6.2.1", sha256="f58ead6842c02d427617e827f4c0a97cfd3f8b648a52e53ef12182002a8663cb", url="https://pypi.org/packages/92/43/82e9a15874414dcd697ab5fe18eafb076ea84649a572701d00c5e11d6c63/raven-6.2.1-py2.py3-none-any.whl")
    version("6.2.0", sha256="87db5b405543502d8a153fb5a816cc3e69409c269c552984a8869953bb9d3bb7", url="https://pypi.org/packages/b0/6f/edf6a5e6453dd4120ba27f863089b8beefcb42fca85e950e1ff11955f91b/raven-6.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("flask", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-blinker@1.1:", when="@5.2,5.4:5.4.1,5.7.2:5.7,5.33:5,6.1:6.2,6.4,6.6:+flask")
        depends_on("py-flask@0.8:", when="@5.2,5.4:5.4.1,5.7.2:5.7,5.33:5,6.1:6.2,6.4,6.6:+flask")
    # END DEPENDENCIES

