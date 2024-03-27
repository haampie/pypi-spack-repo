##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIntelOpenmp(PythonPackage):
    version("2024.0.3", sha256="8005ce24ffd0d45a00d58437a36e7ff9b4e65efe13884010ff098f9a86bec892", url="https://pypi.org/packages/ee/44/670a5a9583ce34a9177165c4aece998d8884f165103d98b3adf5ab4eaee3/intel_openmp-2024.0.3-py2.py3-none-win_amd64.whl")
    version("2024.0.2", sha256="1e08b76f1f6aafb9db51335e242594cdca39bbc0e5803aad1bd968a4e41f0b77", url="https://pypi.org/packages/80/59/80d3d0505468f13fd0a487eecb0cb41146a3b8a0d119e89857fa38190401/intel_openmp-2024.0.2-py2.py3-none-manylinux1_x86_64.whl")
    version("2024.0.1", sha256="3c5f0062dec663930b268c42450f7d8bb6080813d15ac695da4ab5477a7ae0ea", url="https://pypi.org/packages/1d/ee/ddb61366f32dc36f71ae2a39bf3a8e02b6cdc8444dcd4789eeb011f73850/intel_openmp-2024.0.1-py2.py3-none-manylinux1_x86_64.whl")
    version("2024.0.0", sha256="3a0ad4e3803a79be14a22652c70d8c349ca84e5396517bfc4ee1080072fbd9c2", url="https://pypi.org/packages/77/cc/d58fac9b741e69badf6cd14fd2718d9719ac33a3423748365675c317b38b/intel_openmp-2024.0.0-py2.py3-none-win_amd64.whl")
    version("2023.2.4", sha256="2d1e9696b3692fdf47e1a90067cdb72afc2e128f2d8e6934b1b0db638d03dc33", url="https://pypi.org/packages/86/01/e816ebd5632e93c29ee56ef397f947d937329d99971225bf7f2c97bf52d8/intel_openmp-2023.2.4-py2.py3-none-win_amd64.whl")
    version("2023.2.3", sha256="724d585722f93d6104f61b85cce549cbacf34266107bbd22c7bff8aa621dc5ea", url="https://pypi.org/packages/2b/2a/e87aaf10b7e03872adde3b009b91fcce8504dab354a6b2907f91ce051fda/intel_openmp-2023.2.3-py2.py3-none-manylinux1_x86_64.whl")
    version("2023.2.2", sha256="bafc32250c7cb6bb2c04cc91e0ae9c3d48d91873f7bb01567a74f36005aa45be", url="https://pypi.org/packages/94/a1/550f60452635a474d8d732a58f16a854bc10e8d162b1e761d02800a45825/intel_openmp-2023.2.2-py2.py3-none-win_amd64.whl")
    version("2023.2.0", sha256="b937d37b3ce736be29c9740ff7396a88ce09438b484a81b4542ea066eb3021dd", url="https://pypi.org/packages/fe/06/f05ece5295b96cd4fa617cbd0751c12886d41d8cf9e38ddcb3c59779256f/intel_openmp-2023.2.0-py2.py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.whl")
    version("2023.1.0", sha256="39308882e7bcdbd17e2d2b3be96e34ed475f60205bc90cb86694d0bcfc955bbc", url="https://pypi.org/packages/3f/71/72f38f9340420e3a1456834ddd88442be97476174e4a24a1cc30d834659b/intel_openmp-2023.1.0-py2.py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.whl")
    version("2023.0.0", sha256="adfb32b0dde6b3a95ced62608b05a45a7cfad928054136ddbfe0563e16cbf33c", url="https://pypi.org/packages/26/49/ee0d58c2e73e6faee43c2e45b271e68e1079bdc49a44f847e83d2afae134/intel_openmp-2023.0.0-py2.py3-none-manylinux1_i686.whl")
    version("2022.2.1", sha256="77414289c14cb48d7f99926da69c9ced9e70c27feb825b0608f304f9d49844ae", url="https://pypi.org/packages/a0/39/9be1803f45c779ef2df43920fe24140915b992a1e42bf9a37e3beec1ee48/intel_openmp-2022.2.1-py2.py3-none-win_amd64.whl")
    version("2022.2.0", sha256="9c4aea2e340b836255dfe4bb40005e6b6fbecdf975dfadae82d5e3c64746a923", url="https://pypi.org/packages/ff/8e/889c69e6830c06522aa462c05479ec140d1c1a3bdc762153dc6bd7764838/intel_openmp-2022.2.0-py2.py3-none-win32.whl")
    version("2022.1.0", sha256="1b0b92d0ca5599686b5024dd6824e47a6756cbe0253ac7782c0ba84ec18f150c", url="https://pypi.org/packages/d8/e1/da6daa7676e779edc8de06cdbde20b7a9d6dfabd91ad35d9df1e3e28e44c/intel_openmp-2022.1.0-py2.py3-none-win_amd64.whl")
    version("2022.0.3", sha256="6585f004740f2271a353cf58732060c161c8f82826b58832a27501b36c106f0d", url="https://pypi.org/packages/18/07/8d1b8887404199516ee532b035c7ec8c5e4491a81ce06b78bbf5e4a1a390/intel_openmp-2022.0.3-py2.py3-none-win_amd64.whl")
    version("2022.0.2", sha256="346ad5dca716a077ab3c600e71939a80569ab7b1985ae1f43c40ff81917d9e99", url="https://pypi.org/packages/97/12/3c93403a6d6a5f7ca895b45003cae5126c6e7a12f194b08bb74020be30ff/intel_openmp-2022.0.2-py2.py3-none-win_amd64.whl")
    version("2022.0.1", sha256="e7e6c860559a75f03b931e4b59c59072b1edba594f9b79f7f11d8e23cfa10889", url="https://pypi.org/packages/ff/5c/d22b05b96c796ab3787b529b3b8ad74b641373dfb7bfb9326b37171f427a/intel_openmp-2022.0.1-py2.py3-none-manylinux1_x86_64.whl")
    version("2022.0.0", sha256="ee571ad749ce12f3bb294277d258b6d44d98feb192d9496a57167b1ba6e161d3", url="https://pypi.org/packages/cf/4f/a3a6c152b9a225595eb516e3cbc79c6da4e8adbbda7167149e24cd345e01/intel_openmp-2022.0.0-py2.py3-none-win_amd64.whl")
    version("2021.1.2", sha256="8796797ecae99f39b27065e4a7f1f435e2ca08afba654ca57a77a2717f864dca", url="https://pypi.org/packages/27/92/68c00e053c0e38fc5e7b0eb1a47a048ce499e12829aede84b400a4c38a96/intel_openmp-2021.1.2-py2.py3-none-manylinux1_x86_64.whl")


