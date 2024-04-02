# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTraits(PythonPackage):
    # BEGIN VERSIONS
    version("6.4.2", sha256="5be7cc5fb7a99cba7e9014786373e3ad2f75efb445eeced094654bbaf3b0fa82", url="https://pypi.org/packages/73/29/3c105ce8464a9993c1437a4922f3f9b48572cd49a49ff5180c4daf447426/traits-6.4.2.tar.gz")
    version("6.4.1", sha256="78bb2ccafd60aff606515aac46de64668a0a81cb5c54c650b9877a841aa9e812", url="https://pypi.org/packages/ca/72/8d08717884ac41811c4cdbd5bce3101a3df64e0a1890aab7b1a1311c1f50/traits-6.4.1.tar.gz")
    version("6.3.1", sha256="ebdd9b067a262045840a85e3ff34e1567ce4e9b6548c716cdcc82b5884ed9100", url="https://pypi.org/packages/89/86/dd4bd05d0e6526b119c9fb9cc688ddd31140642982882e4b7ebd20a6f12c/traits-6.3.1.tar.gz")
    version("6.2.0", sha256="16fa1518b0778fd53bf0547e6a562b1787bf68c8f6b7995a13bd1902529fdb0c", url="https://pypi.org/packages/44/f3/2fd5d25717536009cbc967449b5598fab7fe9466b84a758fc2f83ebd2c7e/traits-6.2.0.tar.gz")
    version("6.0.0", sha256="dbcd70166feca434130a1193284d5819ca72ffbc8dbce8deeecc0cebb41a3bfb", url="https://pypi.org/packages/b9/af/c6dc88130106d69e4f9a192043c85ed4cb522f83b9041b8691f0b0678405/traits-6.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@6.4.2:")
    # END DEPENDENCIES

