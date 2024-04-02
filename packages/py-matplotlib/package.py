# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMatplotlib(PythonPackage):
    # BEGIN VERSIONS
    version("3.8.3", sha256="7b416239e9ae38be54b028abbf9048aff5054a9aba5416bef0bd17f9162ce161", url="https://pypi.org/packages/9a/aa/607a121331d5323b164f1c0696016ccc9d956a256771c4d91e311a302f13/matplotlib-3.8.3.tar.gz")
    version("3.8.2", sha256="01a978b871b881ee76017152f1f1a0cbf6bd5f7b8ff8c96df0df1bd57d8755a1", url="https://pypi.org/packages/fb/ab/38a0e94cb01dacb50f06957c2bed1c83b8f9dac6618988a37b2487862944/matplotlib-3.8.2.tar.gz")
    version("3.8.1", sha256="044df81c1f6f3a8e52d70c4cfcb44e77ea9632a10929932870dfaa90de94365d", url="https://pypi.org/packages/b4/1b/1b80fcc6b7f33a4c7fa025e944416f8b63fa8d278fad32470c82a2edf319/matplotlib-3.8.1.tar.gz")
    version("3.8.0", sha256="df8505e1c19d5c2c26aff3497a7cbd3ccfc2e97043d1e4db3e76afa399164b69", url="https://pypi.org/packages/23/e1/77016194621fb1356aafeb2186f07b5dede62ea2043bf03f82325c4fccc5/matplotlib-3.8.0.tar.gz")
    version("3.7.4", sha256="7cd4fef8187d1dd0d9dcfdbaa06ac326d396fb8c71c647129f0bf56835d77026", url="https://pypi.org/packages/eb/24/471a6a15d27ad69f50b2a861d8f96a8b1d055a5ea2464cd5284189b98fa8/matplotlib-3.7.4.tar.gz")
    version("3.7.3", sha256="f09b3dd6bdeb588de91f853bbb2d6f0ff8ab693485b0c49035eaa510cb4f142e", url="https://pypi.org/packages/bc/06/9ec4ae7c6c3a6e00f19b91439c2f226a4bb4adb24c84a7f8058a2224d2d0/matplotlib-3.7.3.tar.gz")
    version("3.7.2", sha256="a8cdb91dddb04436bd2f098b8fdf4b81352e68cf4d2c6756fcc414791076569b", url="https://pypi.org/packages/e5/59/b859fa2539b4121b016ea85758188203522fc12b0711de8b247cfec3cdac/matplotlib-3.7.2.tar.gz")
    version("3.7.1", sha256="7b73305f25eab4541bd7ee0b96d87e53ae9c9f1823be5659b806cd85786fe882", url="https://pypi.org/packages/b7/65/d6e00376dbdb6c227d79a2d6ec32f66cfb163f0cd924090e3133a4f85a11/matplotlib-3.7.1.tar.gz")
    version("3.7.0", sha256="8f6efd313430d7ef70a38a3276281cb2e8646b3a22b3b21eb227da20e15e6813", url="https://pypi.org/packages/65/c2/34158ff731a12802228434e8d17d2ebb5097394ab9d065205cc262cf2a6f/matplotlib-3.7.0.tar.gz")
    version("3.6.3", sha256="1f4d69707b1677560cd952544ee4962f68ff07952fb9069ff8c12b56353cb8c9", url="https://pypi.org/packages/23/6d/2917ed23b17a8c4d1d59974a574cae0a365c392ba8820c8824b03a02f376/matplotlib-3.6.3.tar.gz")
    version("3.6.2", sha256="b03fd10a1709d0101c054883b550f7c4c5e974f751e2680318759af005964990", url="https://pypi.org/packages/91/1c/a48fd779287df3425c289cc2ff728980a5b355f15f4c3c40e1822770ba44/matplotlib-3.6.2.tar.gz")
    version("3.6.1", sha256="e2d1b7225666f7e1bcc94c0bc9c587a82e3e8691da4757e357e5c2515222ee37", url="https://pypi.org/packages/0f/23/2eed6f40e1afca9c272fa7c13b437b7784c94a0c180f796c0da114265bf9/matplotlib-3.6.1.tar.gz")
    version("3.6.0", sha256="c5108ebe67da60a9204497d8d403316228deb52b550388190c53a57394d41531", url="https://pypi.org/packages/69/e6/c36374904b757c8193a44af789ddf5bc27f2fe5fbd0cdd908f09cb21e2e1/matplotlib-3.6.0.tar.gz")
    version("3.5.3", sha256="339cac48b80ddbc8bfd05daae0a3a73414651a8596904c2a881cfd1edb65f26c", url="https://pypi.org/packages/02/81/e8276ec6ca005b3b2bfaaad0ea47dbb3a0e389ec8ab87d08e3ccbe4b2742/matplotlib-3.5.3.tar.gz")
    version("3.5.2", sha256="48cf850ce14fa18067f2d9e0d646763681948487a8080ec0af2686468b4607a2", url="https://pypi.org/packages/2f/be/7d6e073a3eb740ebeba43a69f5de2b141fea50b801e24e0ae024ac94d4ac/matplotlib-3.5.2.tar.gz")
    version("3.5.1", sha256="b2e9810e09c3a47b73ce9cab5a72243a1258f61e7900969097a817232246ce1c", url="https://pypi.org/packages/8a/46/425a44ab9a71afd2f2c8a78b039c1af8ec21e370047f0ad6e43ca819788e/matplotlib-3.5.1.tar.gz")
    version("3.5.0", sha256="38892a254420d95594285077276162a5e9e9c30b6da08bdc2a4d53331ad9a6fa", url="https://pypi.org/packages/78/cf/96af81ef2c15682a020a992cb0f1291bb8ee0b3c296f5cd7978348a72993/matplotlib-3.5.0.tar.gz")
    version("3.4.3", sha256="fc4f526dfdb31c9bd6b8ca06bf9fab663ca12f3ec9cdf4496fb44bc680140318", url="https://pypi.org/packages/21/37/197e68df384ff694f78d687a49ad39f96c67b8d75718bc61503e1676b617/matplotlib-3.4.3.tar.gz")
    version("3.4.2", sha256="d8d994cefdff9aaba45166eb3de4f5211adb4accac85cbf97137e98f26ea0219", url="https://pypi.org/packages/60/d3/286925802edaeb0b8834425ad97c9564ff679eb4208a184533969aa5fc29/matplotlib-3.4.2.tar.gz")
    version("3.4.1", sha256="84d4c4f650f356678a5d658a43ca21a41fca13f9b8b00169c0b76e6a6a948908", url="https://pypi.org/packages/84/61/28711c7773a3a47c7f798cafc219968aab78d260c0d674696a077432bbd4/matplotlib-3.4.1.tar.gz")
    version("3.4.0", sha256="424ddb3422c65b284a38a97eb48f5cb64b66a44a773e0c71281a347f1738f146", url="https://pypi.org/packages/05/3d/45415c62fe3f3e7f0dd0b06b8edb0ed2f3dd5f9ceedb7874642976cb3624/matplotlib-3.4.0.tar.gz")
    version("3.3.4", sha256="3e477db76c22929e4c6876c44f88d790aacdf3c3f8f3a90cb1975c0bf37825b0", url="https://pypi.org/packages/22/d4/e7ca532e68a9357742604e1e4ae35d9c09a4a810de39a9d80402bd12f50f/matplotlib-3.3.4.tar.gz")
    version("3.3.3", sha256="b1b60c6476c4cfe9e5cf8ab0d3127476fd3d5f05de0f343a452badaad0e4bdec", url="https://pypi.org/packages/7b/b3/7c48f648bf83f39d4385e0169d1b68218b838e185047f7f613b1cfc57947/matplotlib-3.3.3.tar.gz")
    version("3.3.2", sha256="3d2edbf59367f03cd9daf42939ca06383a7d7803e3993eb5ff1bee8e8a3fbb6b", url="https://pypi.org/packages/2b/4c/fe4b36325795524f35d39edc390c89584e9a901df9e615df6f5effddaa0e/matplotlib-3.3.2.tar.gz")
    version("3.3.1", sha256="87f53bcce90772f942c2db56736788b39332d552461a5cb13f05ff45c1680f0e", url="https://pypi.org/packages/58/bd/d3b13e93c01226901ceb50a14c110b5722f446e456f7f4fd7fd231b33742/matplotlib-3.3.1.tar.gz")
    version("3.3.0", sha256="24e8db94948019d531ce0bcd637ac24b1c8f6744ac86d2aa0eb6dbaeb1386f82", url="https://pypi.org/packages/7d/d4/e4c40c62cd8608ca09f0684e64139c56512e195f2351ac41a472d4dc8b38/matplotlib-3.3.0.tar.gz")
    version("3.2.2", sha256="3d77a6630d093d74cbbfebaa0571d00790966be1ed204e4a8239f5cbd6835c5d", url="https://pypi.org/packages/9c/4b/06f4aa9bef6b5e4f177881b4dedd94faa6e7cb3d95dfaeaa8a1a8b541095/matplotlib-3.2.2.tar.gz")
    version("3.2.1", sha256="ffe2f9cdcea1086fc414e82f42271ecf1976700b8edd16ca9d376189c6d93aee", url="https://pypi.org/packages/4a/30/eb8e7dd8e3609f05c6920fa82f189302c832e5a0f6667aa96f952056bc0c/matplotlib-3.2.1.tar.gz")
    version("3.2.0", sha256="651d76daf9168250370d4befb09f79875daa2224a9096d97dfc3ed764c842be4", url="https://pypi.org/packages/be/06/81367951cc50695830482eacefdc8289c68770db166a4d4283e7eac22dee/matplotlib-3.2.0.tar.gz")
    version("3.1.3", sha256="db3121f12fb9b99f105d1413aebaeb3d943f269f3d262b45586d12765866f0c6", url="https://pypi.org/packages/be/74/24d058c17b155d131359f1cd01e120b3954686bf8b7853172b279237e1dc/matplotlib-3.1.3.tar.gz")
    version("3.1.2", sha256="8e8e2c2fe3d873108735c6ee9884e6f36f467df4a143136209cff303b183bada", url="https://pypi.org/packages/75/81/53ccadcb8cad0a9837f1487b57f2b46b21caa2b3f35f72bc1acb06b5825c/matplotlib-3.1.2.tar.gz")
    version("3.1.1", sha256="1febd22afe1489b13c6749ea059d392c03261b2950d1d45c17e3aed812080c93", url="https://pypi.org/packages/12/d1/7b12cd79c791348cb0c78ce6e7d16bd72992f13c9f1e8e43d2725a6d8adf/matplotlib-3.1.1.tar.gz")
    version("3.1.0", sha256="1e0213f87cc0076f7b0c4c251d7e23601e2419cd98691df79edb95517ba06f0c", url="https://pypi.org/packages/51/fe/84ab101f8ab543d89b6a128326f62adcdafd2781ab8362a737e6ce78eea7/matplotlib-3.1.0.tar.gz")
    version("3.0.2", sha256="c94b792af431f6adb6859eb218137acd9a35f4f7442cea57e4a59c54751c36af", url="https://pypi.org/packages/89/0c/653aec68e9cfb775c4fbae8f71011206e5e7fe4d60fcf01ea1a9d3bc957f/matplotlib-3.0.2.tar.gz")
    version("3.0.0", sha256="b4e2333c98a7c2c1ff6eb930cd2b57d4b818de5437c5048802096b32f66e65f9", url="https://pypi.org/packages/ec/06/def4fb2620cbe671ba0cb6462cbd8653fbffa4acd87d6d572659e7c71c13/matplotlib-3.0.0.tar.gz")
    version("2.2.5", sha256="a3037a840cd9dfdc2df9fee8af8f76ca82bfab173c0f9468193ca7a89a2b60ea", url="https://pypi.org/packages/10/5f/10c310c943f29e67976dcc26dccf9305a5a9bc7483e631ee74a0f95aa5b2/matplotlib-2.2.5.tar.gz")
    version("2.2.4", sha256="029620799e581802961ac1dcff5cb5d3ee2f602e0db9c0f202a90495b37d2126", url="https://pypi.org/packages/1e/20/2032ad99f0dfe0f60970941af36e8d0942d3713f442bb3df37ac35d67358/matplotlib-2.2.4.tar.gz")
    version("2.2.3", sha256="7355bf757ecacd5f0ac9dd9523c8e1a1103faadf8d33c22664178e17533f8ce5", url="https://pypi.org/packages/eb/a0/31b6ba00bc4dcbc06f0b80d1ad6119a9cc3081ecb04a00117f6c1ca3a084/matplotlib-2.2.3.tar.gz")
    version("2.2.2", sha256="4dc7ef528aad21f22be85e95725234c5178c0f938e2228ca76640e5e84d8cde8", url="https://pypi.org/packages/ec/ed/46b835da53b7ed05bd4c6cae293f13ec26e877d2e490a53a709915a9dcb7/matplotlib-2.2.2.tar.gz")
    version("2.0.2", sha256="0ffbc44faa34a8b1704bc108c451ecf87988f900ef7ce757b8e2e84383121ff1", url="https://pypi.org/packages/f5/f0/9da3ef24ea7eb0ccd12430a261b66eca36b924aeef06e17147f9f9d7d310/matplotlib-2.0.2.tar.gz")
    version("2.0.0", sha256="36cf0985829c1ab2b8b1dae5e2272e53ae681bf33ab8bedceed4f0565af5f813", url="https://pypi.org/packages/79/a9/db688816150a6ef91fd9ce284c828467f7271c7dd5982753a73a8e1aaafa/matplotlib-2.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("animation", default=False, description="animation")
    variant("backend", default=False, description="backend")
    variant("fonts", default=False, description="fonts")
    variant("image", default=False, description="image")
    variant("latex", default=False, description="latex")
    variant("movies", default=False, description="movies")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.8:")
        depends_on("python@3.8:", when="@3.6:3.7")
        depends_on("python@3.7:", when="@3.4:3.5")
        depends_on("py-contourpy@1.0.1:", when="@3.7.3:3.7,3.8.0:")
        depends_on("py-cycler@0.10:", when="@2:2.0.0-beta1,3.7.3:3.7,3.8.0:")
        depends_on("py-fonttools@4.22:", when="@3.7.3:3.7,3.8.0:")
        depends_on("py-importlib-resources@3.2:", when="@3.7.3:3.7,3.8.0: ^python@:3.9")
        depends_on("py-kiwisolver@1.3.1:", when="@3.8.1:")
        depends_on("py-kiwisolver@1.0.1:", when="@3.7.3:3.7,3.8.0")
        depends_on("py-numpy@1.21.0:1", when="@3.8.0:")
        depends_on("py-numpy@1.20.0:1", when="@3.7.3:3.7")
        depends_on("py-packaging@20:", when="@3.7.3:3.7,3.8.0:")
        depends_on("py-pillow@8:", when="@3.8.1:")
        depends_on("py-pillow@6.2:", when="@3.7.3:3.7,3.8.0")
        depends_on("py-pyparsing@2.3.1:", when="@3.7.3:3.7,3.8.0:")
        depends_on("py-python-dateutil@2.7:", when="@3.7.3:3.7,3.8.0:")
        depends_on("py-setuptools-scm@7:", when="@3.7.3:3.7,3.8.0")
    # END DEPENDENCIES

