##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCachetools(PythonPackage):
    version("5.3.3", sha256="0abad1021d3f8325b2fc1d2e9c8b9c9d57b04c3932657a72465447332c24d945", url="https://pypi.org/packages/fb/2b/a64c2d25a37aeb921fddb929111413049fc5f8b9a4c1aefaffaafe768d54/cachetools-5.3.3-py3-none-any.whl")
    version("5.3.2", sha256="861f35a13a451f94e301ce2bec7cac63e881232ccce7ed67fab9b5df4d3beaa1", url="https://pypi.org/packages/a2/91/2d843adb9fbd911e0da45fbf6f18ca89d07a087c3daa23e955584f90ebf4/cachetools-5.3.2-py3-none-any.whl")
    version("5.3.1", sha256="95ef631eeaea14ba2e36f06437f36463aac3a096799e876ee55e5cdccb102590", url="https://pypi.org/packages/a9/c9/c8a7710f2cedcb1db9224fdd4d8307c9e48cbddc46c18b515fefc0f1abbe/cachetools-5.3.1-py3-none-any.whl")
    version("5.3.0", sha256="429e1a1e845c008ea6c85aa35d4b98b65d6a9763eeef3e37e92728a12d1de9d4", url="https://pypi.org/packages/db/14/2b48a834d349eee94677e8702ea2ef98b7c674b090153ea8d3f6a788584e/cachetools-5.3.0-py3-none-any.whl")
    version("5.2.1", sha256="8462eebf3a6c15d25430a8c27c56ac61340b2ecf60c9ce57afc2b97e450e47da", url="https://pypi.org/packages/a4/7e/9a87d3b3ca48e253b5c0e114a6601160b9b29f175f4268cb30e21d9e8b63/cachetools-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="f9f17d2aec496a9aa6b76f53e3b614c965223c061982d434d160f930c698a9db", url="https://pypi.org/packages/68/aa/5fc646cae6e997c3adf3b0a7e257cda75cff21fcba15354dffd67789b7bb/cachetools-5.2.0-py3-none-any.whl")
    version("5.1.0", sha256="4ebbd38701cdfd3603d1f751d851ed248ab4570929f2d8a7ce69e30c420b141c", url="https://pypi.org/packages/99/33/c605db9880c7bf6d58db6bb2953860b1927d28dd033d3bea82323d4e7b25/cachetools-5.1.0-py3-none-any.whl")
    version("5.0.0", sha256="8fecd4203a38af17928be7b90689d8083603073622229ca7077b72d8e5a976e4", url="https://pypi.org/packages/19/99/ace1769546388976b45e93445bb04c6df95e96363f03fbb56f916da5ebde/cachetools-5.0.0-py3-none-any.whl")
    version("4.2.4", sha256="92971d3cb7d2a97efff7c7bb1657f21a8f5fb309a37530537c71b1774189f2d1", url="https://pypi.org/packages/ea/c1/4740af52db75e6dbdd57fc7e9478439815bbac549c1c05881be27d19a17d/cachetools-4.2.4-py3-none-any.whl")
    version("4.2.3", sha256="6a6fa6802188ab7e77bab2db001d676e854499552b0037d999d5b9f211db5250", url="https://pypi.org/packages/12/09/64bfb4ae6624248f1ceac7474bb9088ff6fe912f1ee050393cb17bb910f0/cachetools-4.2.3-py3-none-any.whl")
    version("4.2.2", sha256="2cc0b89715337ab6dbba85b5b50effe2b0c74e035d83ee8ed637cf52f12ae001", url="https://pypi.org/packages/bf/28/c4f5796c67ad06bb91d98d543a5e01805c1ff065e08871f78e52d2a331ad/cachetools-4.2.2-py3-none-any.whl")
    version("4.2.1", sha256="1d9d5f567be80f7c07d765e21b814326d78c61eb0c3a637dffc0e5d1796cb2e2", url="https://pypi.org/packages/bb/72/8df2e0dc991f1a1d2c6869404e7622e8ee50d80bff357dbb57c3df70305b/cachetools-4.2.1-py3-none-any.whl")
    version("4.2.0", sha256="c6b07a6ded8c78bf36730b3dc452dfff7d95f2a12a2fed856b1a0cb13ca78c61", url="https://pypi.org/packages/92/da/d3c94fc7c72ad9298072681ec3e8cea86949acc5c4cce4290ba21f7050a8/cachetools-4.2.0-py3-none-any.whl")
    version("4.1.1", sha256="513d4ff98dd27f85743a8dc0e92f55ddb1b49e060c2d5961512855cda2c01a98", url="https://pypi.org/packages/cd/5c/f3aa86b6d5482f3051b433c7616668a9b96fbe49a622210e2c9781938a5c/cachetools-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="de5d88f87781602201cde465d3afe837546663b168e8b39df67411b0bf10cefc", url="https://pypi.org/packages/b3/59/524ffb454d05001e2be74c14745b485681c6ed5f2e625f71d135704c0909/cachetools-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="b304586d357c43221856be51d73387f93e2a961598a9b6b6670664746f3b6c6c", url="https://pypi.org/packages/08/6a/abf83cb951617793fd49c98cb9456860f5df66ff89883c8660aa0672d425/cachetools-4.0.0-py3-none-any.whl")
    version("3.1.1", sha256="428266a1c0d36dc5aca63a2d7c5942e88c2c898d72139fca0e97fdd2380517ae", url="https://pypi.org/packages/2f/a6/30b0a0bef12283e83e58c1d6e7b5aabc7acfc4110df81a4471655d33e704/cachetools-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="219b7dc6024195b6f2bc3d3f884d1fef458745cd323b04165378622dcc823852", url="https://pypi.org/packages/39/2b/d87fc2369242bd743883232c463f28205902b8579cb68dcf5b11eee1652f/cachetools-3.1.0-py2.py3-none-any.whl")


