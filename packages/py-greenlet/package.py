# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGreenlet(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.3", sha256="43374442353259554ce33599da8b692d5aa96f8976d567d4badf263371fbe491", url="https://pypi.org/packages/17/14/3bddb1298b9a6786539ac609ba4b7c9c0842e12aa73aaa4d8d73ec8f8185/greenlet-3.0.3.tar.gz")
    version("3.0.2", sha256="1c1129bc47266d83444c85a8e990ae22688cf05fb20d7951fd2866007c2ba9bc", url="https://pypi.org/packages/d2/62/c657462190d198a45f37e613f910d27cfe8fed6faaeddec004d75dba6811/greenlet-3.0.2.tar.gz")
    version("3.0.1", sha256="816bd9488a94cba78d93e1abb58000e8266fa9cc2aa9ccdd6eb0696acb24005b", url="https://pypi.org/packages/54/df/718c9b3e90edba70fa919bb3aaa5c3c8dabf3a8252ad1e93d33c348e5ca4/greenlet-3.0.1.tar.gz")
    version("3.0.0", sha256="19834e3f91f485442adc1ee440171ec5d9a4840a1f7bd5ed97833544719ce10b", url="https://pypi.org/packages/b6/02/47dbd5e1c9782e6d3f58187fa10789e308403f3fc3a490b3646b2bff6d9f/greenlet-3.0.0.tar.gz")
    version("3.0.0-rc3", sha256="0df5c2ad154f457fd372e39723493b3df519330a4c1bff3ca901be66130f379b", url="https://pypi.org/packages/92/c2/a09095b0c028ab92476207696c899fd6d96f7e06fd1008030df4ca108e07/greenlet-3.0.0rc3.tar.gz")
    version("3.0.0-rc2", sha256="1a250a321e04ea89300c5a493b7f6e41512bac66adbc79b493eba4c2335c1a1d", url="https://pypi.org/packages/b1/2a/0e66a71db5092ba9bf85e8428bc7e103fa6594f4dff6c244a46b048a8164/greenlet-3.0.0rc2.tar.gz")
    version("3.0.0-alpha1", sha256="1bd4ea36f0aeb14ca335e0c9594a5aaefa1ac4e2db7d86ba38f0be96166b3102", url="https://pypi.org/packages/24/5a/29acf7490e5793b65a9b684b036a19a76dad868d8b69c5574c3656b9dcfe/greenlet-3.0.0a1.tar.gz")
    version("2.0.2", sha256="e7c8dc13af7db097bed64a051d2dd49e9f0af495c26995c00a9ee842690d34c0", url="https://pypi.org/packages/1e/1e/632e55a04d732c8184201238d911207682b119c35cecbb9a573a6c566731/greenlet-2.0.2.tar.gz")
    version("2.0.1", sha256="42e602564460da0e8ee67cb6d7236363ee5e131aa15943b6670e44e5c2ed0f67", url="https://pypi.org/packages/fd/6a/f07b0028baff9bca61ecfcd9ee021e7e33369da8094f00eff409f2ff32be/greenlet-2.0.1.tar.gz")
    version("2.0.0.post0", sha256="ad9abc3e4d2370cecb524421cc5c8a664006aa11d5c1cb3c9250e3bf65ab546e", url="https://pypi.org/packages/d4/e7/e41e5150909f58d3161b7ab680d17bb8d47dbbc45385f07a870164d3d02f/greenlet-2.0.0.post0.tar.gz")
    version("2.0.0", sha256="6c66f0da8049ee3c126b762768179820d4c0ae0ca46ae489039e4da2fae39a52", url="https://pypi.org/packages/23/6f/f72865c589d0c79f03b51520a4cdd65647de0513e9ad107a5731df89c235/greenlet-2.0.0.tar.gz")
    version("1.1.3.post0", sha256="f5e09dc5c6e1796969fd4b775ea1417d70e49a5df29aaa8e5d10675d9e11872c", url="https://pypi.org/packages/ea/37/e54ce453b298e890f59dba3db32461579328a07d5b65e3eabf80f971c099/greenlet-1.1.3.post0.tar.gz")
    version("1.1.3", sha256="bcb6c6dd1d6be6d38d6db283747d07fda089ff8c559a835236560a4410340455", url="https://pypi.org/packages/a0/d5/70772b3693f086a362f122516225a43fe4f1182e17158c81ba1ab271ab9b/greenlet-1.1.3.tar.gz")
    version("1.1.2", sha256="e30f5ea4ae2346e62cedde8794a56858a67b878dd79f7df76a0767e356b1744a", url="https://pypi.org/packages/0c/10/754e21b5bea89d0e73f99d60c83754df7cc64db74f47d98ab187669ce341/greenlet-1.1.2.tar.gz")
    version("1.1.0", sha256="c87df8ae3f01ffb4483c796fe1b15232ce2b219f0b18126948616224d3f658ee", url="https://pypi.org/packages/47/6d/be10df2b141fcb1020c9605f7758881b5af706fb09a05b737e8eb7540387/greenlet-1.1.0.tar.gz")
    version("0.4.17", sha256="41d8835c69a78de718e466dd0e6bfd4b46125f21a67c3ff6d76d8d8059868d6b", url="https://pypi.org/packages/72/0c/fd07c7674ad6eded937194b84d8453425c36c6ef118536907b0185624d82/greenlet-0.4.17.tar.gz")
    version("0.4.13", sha256="0fef83d43bf87a5196c91e73cb9772f945a4caaff91242766c5916d1dd1381e4", url="https://pypi.org/packages/13/de/ba92335e9e76040ca7274224942282a80d54f85e342a5e33c5277c7f87eb/greenlet-0.4.13.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

