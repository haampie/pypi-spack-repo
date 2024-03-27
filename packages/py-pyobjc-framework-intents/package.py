##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIntents(PythonPackage):
    version("10.2", sha256="ec27d5d19212fcec180ff04e2bc617fee0a018e2eaf29b2590c5512da167aa6a", url="https://pypi.org/packages/bf/26/f36e7e0f0078b5b2667e76afb7f9df36778a3db80252c0c4440be309d374/pyobjc-framework-Intents-10.2.tar.gz")
    version("10.1", sha256="85a84a5912b8d8a876767ca8fa220dc24bf1c075ed81b58c386d25c835cec804", url="https://pypi.org/packages/cf/6e/998c8905f795ac51c7fd9b75e0fe1df5ae2b8e0eba3fcd87a33973d3bd78/pyobjc-framework-Intents-10.1.tar.gz")
    version("10.0", sha256="228177cd32e63b2b2c76befdb80e520c4db81be7186549753c3dc7b9f74d4a4b", url="https://pypi.org/packages/23/b8/79fbeacf793a699fbeb59c788884cf193614d000ea04330ee698e4f874ce/pyobjc-framework-Intents-10.0.tar.gz")
    version("9.2", sha256="59b34014e7bc0b72be6d64ae53c12c4f8232d7697e7eec1cd870fabacbe187d4", url="https://pypi.org/packages/50/7e/bed616e6234a3294d5281c00f043069e904e091847d0b077a67ac64e568c/pyobjc-framework-Intents-9.2.tar.gz")
    version("9.1.1", sha256="d667ad8e52d9c2b7f2b0b3a7ecf03140886856df87d27af4e9b7cec62e29f4f9", url="https://pypi.org/packages/18/89/fabcbb12483b24d7984fe643a3f96a6facd1285e95e802c64247db580dbe/pyobjc-framework-Intents-9.1.1.tar.gz")
    version("9.1", sha256="471bdde21dac70faa1550a7071b89b941b3463239fc0842b64bbe4024e105d41", url="https://pypi.org/packages/84/18/1f502e0c9fab78845a60fed0637992a95c6b2fcec21b4c469a2e054fa495/pyobjc-framework-Intents-9.1.tar.gz")
    version("9.0.1", sha256="556494335d12cefd7344ac1f6a371d6d0a6a573d876cc82fdbdfd351535fc42e", url="https://pypi.org/packages/ec/0a/cb499a3797be067a4f216dc95cd7db2afe743ccd77280bbf414bb97cffdb/pyobjc-framework-Intents-9.0.1.tar.gz")
    version("9.0", sha256="e59a2137b1191aa4ac300f26606b741c2ae3c822a61e7eab5760e50c05468bcb", url="https://pypi.org/packages/4a/5a/8a1cefa972abef415b24a5e8f17398289605dac480da7273fecac31900e9/pyobjc-framework-Intents-9.0.tar.gz")
    version("8.5.1", sha256="582cb38e85a4f042d31f81a27938fd5ebc17bd606c0e213c348f16ecc2467c32", url="https://pypi.org/packages/0f/b6/8f75b55839314e47c940ffe7529d0d028024225f68ee3fcf6eed85db16d7/pyobjc-framework-Intents-8.5.1.tar.gz")
    version("8.5", sha256="da7eb47977de518a129ce6457e826b0884efe809bb15ff6a9c4f5e77fe6d2313", url="https://pypi.org/packages/53/56/a911bd9c9e7f83d6d1e1378ee8a6878f16e2bbf45d2290eed65e94f03da8/pyobjc-framework-Intents-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

