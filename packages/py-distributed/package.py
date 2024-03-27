##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDistributed(PythonPackage):
    version("2024.3.1", sha256="abab8658122e97c507ce8a5b0d46dc6cb414a2a531f92e1c5933d7c5e0dd65ac", url="https://pypi.org/packages/3c/a1/13c23f0eb985f8150670e47fb71d59c8a3343cc252d60a3818bfe932753a/distributed-2024.3.1-py3-none-any.whl")
    version("2024.3.0", sha256="467f52bb624ff6f4b6c3e9827652147d78ea3264d16ea3b802b878679082e82e", url="https://pypi.org/packages/c6/5c/90275fcf214bab9c3aefeb4b6d86cd39c1941fabedff71d66a273ed274d9/distributed-2024.3.0-py3-none-any.whl")
    version("2024.2.1", sha256="633947b55198a0c7444272342c425d14f127a44d26a8ac46824d0daa3940da34", url="https://pypi.org/packages/3d/74/6d08be57bc06ddefd6fe9cf09f322e1c1105da0ae2264145600312d72099/distributed-2024.2.1-py3-none-any.whl")
    version("2024.2.0", sha256="9545a176a7684b155cdfc56c1bf9b1b588e08e107f9f937166d4912b1ee809f7", url="https://pypi.org/packages/e3/a0/12cc57de8f6015bfbfbfd83a6562251f60ba7cc2de5704ccc06d7761079b/distributed-2024.2.0-py3-none-any.whl")
    version("2024.1.1", sha256="cf05d3b38e1700339b3e36395729ab62110e723efefaecc21a8260fdc7555cf9", url="https://pypi.org/packages/98/21/d40b69bda1bbb3c52a742689fa0c28142f701b7c932355e7af0286ad022a/distributed-2024.1.1-py3-none-any.whl")
    version("2024.1.0", sha256="b552c9331350ba0e7cb8eccb1da8942b44997ccb680338f61c43fe9843c69988", url="https://pypi.org/packages/1c/2c/38d271ab0cb88ba64d9cd30699de77419061dab3077f987c6bf2f6582f55/distributed-2024.1.0-py3-none-any.whl")
    version("2023.12.1", sha256="f0c5e50c26b6cf5106b2d4116bf168dfccebe42e9670ddf58cfe3618b8b94ed8", url="https://pypi.org/packages/96/b0/547d4ef38afea651d10c79961c275df4a55ffbaf846d79ea165aeffb669f/distributed-2023.12.1-py3-none-any.whl")
    version("2023.12.0", sha256="f573310a39aa0b9c922be01409c4d4e69154b555bef36b65202ad15ac1bf3918", url="https://pypi.org/packages/68/91/90af696c0192cd1a7b7dfddba2da54395c28133c8ba689e6997d2da3595e/distributed-2023.12.0-py3-none-any.whl")
    version("2023.11.0", sha256="44ad1fff31ece202cc64bdb72dd33d6964d78bdbe1ec1ec06e01f9544187cd2e", url="https://pypi.org/packages/77/a6/34c16487b659de5b42942f13949af8a03c3ea0208f0cd6bcf2cd576e2c28/distributed-2023.11.0-py3-none-any.whl")
    version("2023.10.1", sha256="0e0fe280d3b7b8be45840df3697dcb07d954c9c21c2a31d0c8e2dbe60bdaef21", url="https://pypi.org/packages/5e/6b/4a5dc8bf17a2714f53f648b6f44f1cd2ad7ab41aaaffe1c25489947c24f6/distributed-2023.10.1-py3-none-any.whl")
    version("2023.4.1", sha256="14f9b106f069e528711190eb5fd871de48de2d023a97d63c146c2c4b80790ec8", url="https://pypi.org/packages/dd/26/7c3c4b2c7fc73028b989bf4c8d364e383a92403576aa417b523d7da91a18/distributed-2023.4.1-py3-none-any.whl")
    version("2023.3.2.1", sha256="a7756a4b952ec5a7fd3163e93aef99aaf8b0000568fa9ee7c000113a470d7f8e", url="https://pypi.org/packages/0f/62/14c82cb48f6ae656813cb64c31bf77a5c58f51fd5baa65a0ef91987bd352/distributed-2023.3.2.1-py3-none-any.whl")
    version("2023.3.2", sha256="43b74f08ea4ea0696ae8d2f1ea53adcda998a2a159bd34dffd42e4e678ff5f8a", url="https://pypi.org/packages/b4/a8/e9f19d80467b731c7ba592736846fc114342166d75d449985e1128de1ef2/distributed-2023.3.2-py3-none-any.whl")
    version("2023.3.1", sha256="542f691b6871eb9d3909e1f8eb4c274f09c69b89f07ff5a598de38a60237f162", url="https://pypi.org/packages/53/05/ec09a38d8e83efe850670cef22c9a9421bf5e08cb3f716db8043f1fa96c2/distributed-2023.3.1-py3-none-any.whl")
    version("2023.3.0", sha256="dd1f5854d1117a40c397f08f24e0d832d7e0ef15fba3266c85af4420c6a379ec", url="https://pypi.org/packages/a2/1e/96d430d905fa3a43bd27fe16fa3832e5f7df11cdaf965fb86849dcb34454/distributed-2023.3.0-py3-none-any.whl")
    version("2023.2.1", sha256="34e9266af2bd24f14e4449934d900300ad994bb2c6929a56fbe7d0e398a3ed07", url="https://pypi.org/packages/c2/bc/4dace47fe2191390a60528fba725577916a545765e534452fde65498e173/distributed-2023.2.1-py3-none-any.whl")
    version("2023.2.0", sha256="26a359ec4cb16f50e421ddba18a26262e51f1c30bd12a9173207a02d14c992da", url="https://pypi.org/packages/75/f2/db610aa16edf42c95dfcbf513458a1bb1d17da97c28e167a623da19dd1d1/distributed-2023.2.0-py3-none-any.whl")
    version("2023.1.1", sha256="9b18dc9acbbbe885612dc5ba08571f38ccfb89d648048d3e48be2e4e1122877f", url="https://pypi.org/packages/fb/61/ddd22d74ebe226b8a1b2dc6af8339e91512c5f410e68ce71cf70ded4f4c8/distributed-2023.1.1-py3-none-any.whl")
    version("2023.1.0", sha256="bc922eae66afd1b23784f3fcc3cacd7a8d60907163e0d7c41e565a77815a10c1", url="https://pypi.org/packages/1e/8f/61a3db6d70f603e8ba026bf1a60e5451221bbd95e56600f72ab12530a0e2/distributed-2023.1.0-py3-none-any.whl")
    version("2022.12.1", sha256="d7abd29277c6b7af8df7fef68c1552100478d3da7bf6a4a3562142be8948c1e8", url="https://pypi.org/packages/4c/15/859d2dcb27911384571b6cef7fe320b48ab1b42a27984cf811937a00f80f/distributed-2022.12.1-py3-none-any.whl")
    version("2022.12.0", sha256="3544ac4b6857bbf65657895e52f0068b69ae88529223c9ba5e79c1024e6f9a66", url="https://pypi.org/packages/3a/64/e9c008896c39a3d2d4f530c28545c30a4066ce0dd03edf2b74fdf3839965/distributed-2022.12.0-py3-none-any.whl")
    version("2022.10.2", sha256="ae4fffdb55c6cb510ba1cbdf2856563af80ebf93e5ceacb91c1ce79e7da108d8", url="https://pypi.org/packages/28/54/62702b9c98df725de6c7e88dd67c240f078cd657b1a3938a81bd1d977489/distributed-2022.10.2-py3-none-any.whl")
    version("2022.2.1", sha256="51ee30d5f55c968c7dfdb3054a31cb03fea7b9b012d9c4d498e3d813c7935099", url="https://pypi.org/packages/38/7a/8c2576048e36ec93d115af8d01bc10d936e5354c80f6b85bf25e11f85119/distributed-2022.2.1-py3-none-any.whl")
    version("2021.6.2", sha256="68251734ec68254280d855db5a77cead2712df2580ec9d44fde14321e7f3806c", url="https://pypi.org/packages/14/03/104c2cb8f498165da0037fbe76581678027ea2722bac2775f04aaeafef65/distributed-2021.6.2-py3-none-any.whl")
    version("2021.4.1", sha256="fe0e005e9aa79d68e185008bd2ce6562388311efd1c59a04ab6127ee631b8808", url="https://pypi.org/packages/63/f8/ac2c18adde6477bca3881c4d3cfa74c7f4da7ee82f3c83c201aa3b9ca5ee/distributed-2021.4.1-py3-none-any.whl")
    version("2020.12.0", sha256="532294b005009ce7c480073e467f9043c5292a735ed535f3fd00517a83a51bfc", url="https://pypi.org/packages/b5/12/3c25bb53c9b508e6332b62c33a8806ec7a33c926d8e32e7e53df0b512b84/distributed-2020.12.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.5.1:")
        depends_on("py-click@8.0.0:", when="@2023.3.1:")
        depends_on("py-click@7:", when="@2022.11:2023.3.0")
        depends_on("py-click@6.6:", when="@1.13.3:2022.10")
        depends_on("py-cloudpickle@1.5:", when="@2.21:")
        depends_on("py-dask@2024.3.1:", when="@2024.3.1:")
        depends_on("py-dask@2024.3:2024.3.0", when="@2024.3:2024.3.0")
        depends_on("py-dask@2024.2.1:2024.2", when="@2024.2.1:2024.2")
        depends_on("py-dask@2024.2:2024.2.0", when="@2024.2:2024.2.0")
        depends_on("py-dask@2024.1.1:2024.1", when="@2024.1.1:2024.1")
        depends_on("py-dask@2024:2024.1.0", when="@2024:2024.1.0")
        depends_on("py-dask@2023.12.1:2023", when="@2023.12.1:2023")
        depends_on("py-dask@2023.12:2023.12.0", when="@2023.12:2023.12.0")
        depends_on("py-dask@2023.11", when="@2023.11")
        depends_on("py-dask@2023.10.1:2023.10", when="@2023.10.1:2023.10")
        depends_on("py-dask@2023.4.1:2023.4", when="@2023.4.1:2023.4")
        depends_on("py-dask@2023.3.2:2023.3", when="@2023.3.2:2023.3")
        depends_on("py-dask@2023.3.1", when="@2023.3.1")
        depends_on("py-dask@2023.3:2023.3.0", when="@2023.3:2023.3.0")
        depends_on("py-dask@2023.2.1:2023.2", when="@2023.2.1:2023.2")
        depends_on("py-dask@2023.2:2023.2.0", when="@2023.2:2023.2.0")
        depends_on("py-dask@2023.1.1:2023.1", when="@2023.1.1:2023.1")
        depends_on("py-dask@2023:2023.1.0", when="@2023:2023.1.0")
        depends_on("py-dask@2022.12.1:2022", when="@2022.12.1:2022")
        depends_on("py-dask@2022.12:2022.12.0", when="@2022.12:2022.12.0")
        depends_on("py-dask@2022.10.2:2022.10", when="@2022.10.2:2022.10")
        depends_on("py-dask@2022.2.1:2022.2", when="@2022.2.1:2022.2")
        depends_on("py-dask@2021.6.2:2021.6", when="@2021.6.2:2021.6")
        depends_on("py-dask@2021.3:", when="@2021.3:2021.4")
        depends_on("py-dask@2020:", when="@2020:2021.1")
        depends_on("py-jinja2@2.10.3:", when="@2023:")
        depends_on("py-jinja2", when="@2021.8:2022")
        depends_on("py-locket@1:", when="@2022.4.2:")
        depends_on("py-msgpack@1.0.0:", when="@2023:")
        depends_on("py-msgpack@0.6:", when="@2.11:2022")
        depends_on("py-packaging@20:", when="@2022:")
        depends_on("py-psutil@5.7.2:", when="@2023.5.1:")
        depends_on("py-psutil@5.7:", when="@2023:2023.5.0")
        depends_on("py-psutil@5:", when="@1.24.1:2022")
        depends_on("py-pyyaml@5.3.1:", when="@2023:")
        depends_on("py-pyyaml", when="@1.22:2022")
        depends_on("py-setuptools", when="@2.9.1:2022.2")
        depends_on("py-sortedcontainers@2.0.5:", when="@2023:")
        depends_on("py-sortedcontainers@:1,2.0.2:", when="@1.22:2022")
        depends_on("py-tblib@1.6:", when="@2.11:")
        depends_on("py-toolz@0.10:", when="@2022.11.1:")
        depends_on("py-toolz@0.8.2:", when="@2.13:2022.11.0")
        depends_on("py-tornado@6.0.4:", when="@2023.5.1:")
        depends_on("py-tornado@6.0.3:6.1", when="@2022.7:2022.11")
        depends_on("py-tornado@6.0.3:", when="@2.11:2022.6,2022.12:2023.5.0")
        depends_on("py-urllib3@1.24.3:", when="@2023:")
        depends_on("py-urllib3", when="@2022.4:2022")
        depends_on("py-zict@3:", when="@2023.9:")
        depends_on("py-zict@2.2:", when="@2023.4:2023.8")
        depends_on("py-zict@2.1:", when="@2023:2023.3")
        depends_on("py-zict@0.1.3:", when="@1.19:2022")
