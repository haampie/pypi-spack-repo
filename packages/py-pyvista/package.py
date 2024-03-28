# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvista(PythonPackage):
    # BEGIN VERSIONS
    version("0.43.4", sha256="f1fc56ac9ea1447660dec91e06b37f48736fd6983a2ed9fb2780252724b1caeb", url="https://pypi.org/packages/e2/82/97681e292c06651c51cee8cf32b0605a7008d2f8f3e80335503a086226fd/pyvista-0.43.4-py3-none-any.whl")
    version("0.43.3", sha256="5eb589bbea294761cd44aed0330481019e8eca2ddb950a1f332a5a132000e93d", url="https://pypi.org/packages/8e/6b/7546903fb8674c7e08a5c48b9d3a888378f7297545ae8c74703441319ac4/pyvista-0.43.3-py3-none-any.whl")
    version("0.43.2", sha256="798a62eddb307e09d18e86ee75141fd8bc90d497bb5da9695fdc52f69ebac204", url="https://pypi.org/packages/b5/09/59e6d72fd2212ab4edd2e2e1d7351fe971141060a896c5cba86ac0cb4124/pyvista-0.43.2-py3-none-any.whl")
    version("0.43.1", sha256="e7e7597c3938ad7e695a1de724ba4d5fcb05cdfa4ac81bb9bee7e75659c25f8a", url="https://pypi.org/packages/13/1b/5ac31cf55d8a2538341de15eae0f003d7692e4f4cdf1089b917a8ed65e88/pyvista-0.43.1-py3-none-any.whl")
    version("0.43.0", sha256="b062ba699956b0fff2d34398db15b276ca836de67d262c51e361d816c00e8004", url="https://pypi.org/packages/f0/49/e2f3b9a4af3dff4c70781b3b6bd769e745187037f17c9198a82518fff6bc/pyvista-0.43.0-py3-none-any.whl")
    version("0.42.3", sha256="b6170689209eec58246b32abb3c5f99246b45948e51228504cda2d4d301e7463", url="https://pypi.org/packages/6d/ee/24d100341e673347f80347ec8f20b4e48b1326fd968d7fb1139829f8bb66/pyvista-0.42.3-py3-none-any.whl")
    version("0.42.2", sha256="1301eee63f884966bd9ce80069a92745f1b8ac9b927d98d28d9af4275a043efc", url="https://pypi.org/packages/67/44/23211baa449bb9dd4f75d1a619a0b7e60900369da3993b5251cbfb657c1f/pyvista-0.42.2-py3-none-any.whl")
    version("0.42.1", sha256="83f88a41549a0fd1dc989a6d4ebddd1c7d52d0234f19aacc8f26366daf677f27", url="https://pypi.org/packages/58/c9/8445f59fe46419d4384916ec6ef711e47db8eb392ce6951c6c659140c319/pyvista-0.42.1-py3-none-any.whl")
    version("0.42.0", sha256="b205e09b9ad8de9f79a78063bd814c1f13efa71b21f0ee9e6bca147bc86ed693", url="https://pypi.org/packages/0d/ff/8fa9ee0e764215d468b4711be1be180f9121afbd3ef37001254589ef0d5d/pyvista-0.42.0-py3-none-any.whl")
    version("0.41.1", sha256="320785b45432089a37d3a09828853af1edf629eca8ded0fe0002c2a661e26c77", url="https://pypi.org/packages/70/3f/88bae63eee660f28d5f648d3026fb8a9b125c067cdd956c57bebfa67de91/pyvista-0.41.1-py3-none-any.whl")
    version("0.41.0", sha256="92e80a52b615fa3a89950bc73586a5e5a2c65c1770e9cd37f131721a3c62ccb0", url="https://pypi.org/packages/78/cc/3afb276275b5e72b44b2955822ccdcd36f350c709ba2d2c88f8c1f127bde/pyvista-0.41.0-py3-none-any.whl")
    version("0.38.6", sha256="661c0c550fa63a748a2361bc4bbff52ba5e8f22a32991be64ec8ec6b14754a1d", url="https://pypi.org/packages/f7/67/21198db0c97bdff0cd5b6c3913765cca1faf1168068c66370e2fe13c01aa/pyvista-0.38.6-py3-none-any.whl")
    version("0.38.5", sha256="b9d5da2280550119c3eb3cb516f1642de0f4f0c94e2edd12c14cf6101634f64d", url="https://pypi.org/packages/bd/54/c1937968f3aa83f7064b2d11765c1aa274f147e4f43ce997d50f50943617/pyvista-0.38.5-py3-none-any.whl")
    version("0.38.4", sha256="06a2de529ddb08015a1a71fa50ab8a1d06291c4b48ecb7484367057b0017621d", url="https://pypi.org/packages/11/e6/30229900c9d6b299a5b87e6b08262b50d8cb9975ebe680e7f3019c475257/pyvista-0.38.4-py3-none-any.whl")
    version("0.38.3", sha256="67f9611c357b8d1ad3e7dfecba57ae549e1c22a966df0a9e1f387570b88a5a60", url="https://pypi.org/packages/46/da/c90ab56727475cbd5a69e03c65200f88aab54d61e57368bb416e0335eb3b/pyvista-0.38.3-py3-none-any.whl")
    version("0.38.2", sha256="870a39449979f96a81432f02e1e4c5aa63274114e9d98808d1c059569a7c522e", url="https://pypi.org/packages/b1/38/56f9c5ab64fed0c07b9ab30d3a72acef40e02169c8f88efbfa5b3d4d2d39/pyvista-0.38.2-py3-none-any.whl")
    version("0.38.1", sha256="c3fd590e19cb9d1c2a46d9c7f5838d6d84507599d891afcb3fd454c5baa80cc2", url="https://pypi.org/packages/fa/a7/e3009f77897adb0c35e6602554bcd6b515cec10115e50d9fe96d22f6d5cf/pyvista-0.38.1-py3-none-any.whl")
    version("0.38.0", sha256="d24ba29210f200dd747f7035415d656aa484d77643f25634711343f22da80166", url="https://pypi.org/packages/90/40/d2bd4e2df0b2ae631675bc7ce0b815968b06871c29afefc086c81bb5b814/pyvista-0.38.0-py3-none-any.whl")
    version("0.22.4", sha256="1647b08530c48d58b39dfcca86c3af913946a3859ffff4c4a1b1a657679ffea4", url="https://pypi.org/packages/3d/00/d4904a3b587beb4d42980a40323726926b82ba5beeadfb0c367f879f804b/pyvista-0.22.4.tar.gz")
    version("0.22.2", sha256="2da25785155cc97a3f513a5fc053b91f3dbe4650476d18152db4058943c7dd68", url="https://pypi.org/packages/f5/c1/215af1d438728fe4eed237f4bc7f7354f79df848aade8bfc6f3c0d0e4074/pyvista-0.22.2.tar.gz")
    version("0.22.1", sha256="4ba14a4202e77f3ec116ec4f7d00f3b860d93f61c3a9a4ef14c707a1da71d9bd", url="https://pypi.org/packages/93/3d/26ba69da500f84dd350b0cfc39cc4bce4fdf4af0f96d480267c8344209ca/pyvista-0.22.1.tar.gz")
    version("0.22.0", sha256="182de762045b5f95b4ab4e6ab626195bc0a68fda59bfd7793d24e9e4376e13a0", url="https://pypi.org/packages/07/53/d9080588b2dc20a56b2bc12b07bca12a3f3ca06fa55a0051a1b0d2ed7665/pyvista-0.22.0.tar.gz")
    version("0.21.4", sha256="7e2915a1fa8580a080a59164e724a6212e6010e009ddb02a6c2aa2d70536e882", url="https://pypi.org/packages/d6/34/d384b2da6283a37fce076d836723be1d89d6563d8ac85e73a01405984cc8/pyvista-0.21.4.tar.gz")
    version("0.21.3", sha256="ae33ae617125df767704fb5a59236c4d97bb9105d704dc1c90908350dda29b9a", url="https://pypi.org/packages/f5/3a/1036284943fd52c57059fbf106a4afe276a1120dc2a29457dccd3f531103/pyvista-0.21.3.tar.gz")
    version("0.21.2", sha256="0b2a12c962291720e04b94bbd0118e1f4f7bcb27049ffd150d5c499a4250f0c7", url="https://pypi.org/packages/17/a7/95a2bbc6f89eb735b4191f6c1a7acf5490ffcf970cc804c48401d7fdf025/pyvista-0.21.2.tar.gz")
    version("0.21.1", sha256="d09e43dae3118fe5bb73ba722afa6ebe2c2f430c767bcbb4d04411e35769b20a", url="https://pypi.org/packages/05/ea/b4b2cee63348d7fbd4238c51d018d2f65d35d415995c4a4dc2098cbd9fbb/pyvista-0.21.1.tar.gz")
    version("0.21.0", sha256="877b776a9930926791c72a050df4586837be33516089d780d1b79da09b30d38b", url="https://pypi.org/packages/e0/37/52332d0412e5f5cf231ceee67bcb74d5213b85da7194605019ae1fc6dcc9/pyvista-0.21.0.tar.gz")
    version("0.20.4", sha256="66680cea8b175075457823b7275e1c07ad7d00920a26b3cac51c3f9c3080fc10", url="https://pypi.org/packages/09/ff/f0de1d01ad7cdda5a33d4f99a739fa9ae46c6e192d16434186cbdaee5da6/pyvista-0.20.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-imageio", when="@0.38")
        depends_on("py-matplotlib@3.0.1:", when="@0.39:")
        depends_on("py-numpy@1.21.0:", when="@0.43:")
        depends_on("py-numpy", when="@0.38:0.42")
        depends_on("py-pillow", when="@0.38:")
        depends_on("py-pooch", when="@0.38:")
        depends_on("py-scooby@0.5.1:", when="@0.38:")
        depends_on("py-vtk", when="@0.38:")
    # END DEPENDENCIES

