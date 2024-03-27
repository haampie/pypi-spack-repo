##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkImagecapturecore(PythonPackage):
    version("10.2", sha256="68f1f96982282e786c9c387c177c3b14202d560d68000136562eba1ed3f45a6e", url="https://pypi.org/packages/38/ac/b779c127c35f8f8888cf3636eb853777158d22166e937746040f5d35c252/pyobjc-framework-ImageCaptureCore-10.2.tar.gz")
    version("10.1", sha256="29b85ee9af77bba7e1ea9191bf84edad39d07681b9bd267c8f5057db3b0cdd64", url="https://pypi.org/packages/5e/06/4e9b52e020cceab0f0b0762af8d046d01d9e72a5d9b5b7b62449b7681ccc/pyobjc-framework-ImageCaptureCore-10.1.tar.gz")
    version("10.0", sha256="9660faa140806dd0f2c50c39062863c23188c6b9596e2946234dd3c35882d3c7", url="https://pypi.org/packages/ba/ef/89e90d78c9a9e04cb36c391c5eafab16a9202147327d3c33d68fb16ab1cd/pyobjc-framework-ImageCaptureCore-10.0.tar.gz")
    version("9.2", sha256="f03c6ddffe737239ee57b3f1a0ab10d4dd5f276a24ec17795dbaea7871b5ee8f", url="https://pypi.org/packages/64/15/b0f1d2881d1e921713594b32b8fde9ed7a3c091a55068c308add4e546a7c/pyobjc-framework-ImageCaptureCore-9.2.tar.gz")
    version("9.1.1", sha256="0f7c9e7ace13a034e3bee52170dac8dd359a8e55dc6552ca62567685888b59de", url="https://pypi.org/packages/85/9a/8ff7dcf86b539a0942a851871a3e05496167f20d14c46a99f1cdf48d573e/pyobjc-framework-ImageCaptureCore-9.1.1.tar.gz")
    version("9.1", sha256="c422b623d511e33b17960841d0bf01f64996b83f82801eb30a599c2e1cf12840", url="https://pypi.org/packages/6d/c5/3cc9efb67136be53868ee43f4db87dc25aec0d2f15ccd98ef18e9c4d9d1d/pyobjc-framework-ImageCaptureCore-9.1.tar.gz")
    version("9.0.1", sha256="03a236cb727269ee274e8aeeb970b1eaad10bae7be1b84167253a34cd155fb27", url="https://pypi.org/packages/01/fc/7652044adedafce1b5dbbf0f2ec4b52dd8b43b9c644308da3eac452f39ee/pyobjc-framework-ImageCaptureCore-9.0.1.tar.gz")
    version("9.0", sha256="124e2475f57426efe7c439eb964c01b5f90d6458ab9438a723a3d3ceffa59502", url="https://pypi.org/packages/ac/4b/3f3e68af101b60dd534229e7ffa405b56061069207d930f52b34bbd512c6/pyobjc-framework-ImageCaptureCore-9.0.tar.gz")
    version("8.5.1", sha256="19b53735c73a3f1c32cf288422d318280214e7988d0eb027acdbc56e4953834f", url="https://pypi.org/packages/c4/7e/90fdb455ef30393a50b3709a01a087817ea702898106797339cc2185efee/pyobjc-framework-ImageCaptureCore-8.5.1.tar.gz")
    version("8.5", sha256="b7bd515affee27737d0292bc6aab49c0248077454dbcf01beda8e3f231791d38", url="https://pypi.org/packages/44/eb/da192dfaaff26856291dbcfa7a6295010de5a0e472ae52199bb86e1dedf4/pyobjc-framework-ImageCaptureCore-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

