# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGraphqlCore(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.3", sha256="5766780452bd5ec8ba133f8bf287dc92713e3868ddd83aee4faab9fc3e303dc3", url="https://pypi.org/packages/f8/39/e5143e7ec70939d2076c1165ae9d4a3815597019c4d797b7f959cf778600/graphql_core-3.2.3-py3-none-any.whl")
    version("3.2.2", sha256="4672711cb0f10013df464e450bda006fc449eca90d17a54a7c1103322e246c49", url="https://pypi.org/packages/57/30/17c1be4e38e7a2253c56f5821162f37055b559accae4135c62c3a12a269b/graphql_core-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="f83c658e4968998eed1923a2e3e3eddd347e005ac0315fbb7ca4d70ea9156323", url="https://pypi.org/packages/14/28/c308fc9a5914b9a2333a546f4976d96e0d95230f16593223d727cbc19d52/graphql_core-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="0dda7e63676f119bb3d814621190fedad72fda07a8e9ab780bedd9f1957c6dc6", url="https://pypi.org/packages/46/e1/77af13b8a5498bfd5312fe1a89b31c90eb0144b6e1ca7862ebb63459c66e/graphql_core-3.2.0-py3-none-any.whl")
    version("3.1.7", sha256="9b460f60320be01c7f3b1766cf3e406933003008055079b9d983b8f3988f4400", url="https://pypi.org/packages/05/c3/bbdf432c196aec04d9ac6a12a88d10ac50fe412115bdb917add4b963d113/graphql_core-3.1.7-py3-none-any.whl")
    version("3.1.6", sha256="c78d09596d347e1cffd266c5384abfedf43ed1eae08729773bebb3d527fe5a14", url="https://pypi.org/packages/43/bb/27c6e86c05c780c1a54731a95c7bc6285eca2e0f0d88d190a3fd1f61d75c/graphql_core-3.1.6-py3-none-any.whl")
    version("3.1.5", sha256="91d96ef0e86665777bb7115d3bbb6b0326f43dc7dbcdd60da5486a27a50cfb11", url="https://pypi.org/packages/a1/75/3e97b9980a7f1ebf0c175888c1c2a21207e9d590cbcfa3c2cc10ba7e46a4/graphql_core-3.1.5-py3-none-any.whl")
    version("3.1.4", sha256="2ae62ed27eb5c629fdfd06f89bec36a427bef97d37aef41e8f195c5352f22bea", url="https://pypi.org/packages/c5/3a/9b67ca56632cd468c17e3964e90323bceb512c727a72b97083d2d1c5e2a2/graphql_core-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="95b0d6510bb5532dcac5927f5dfd674a580b33d6ba6417c3dc75086d9a210c83", url="https://pypi.org/packages/40/4b/b38f0d94bfc47e3d1ba19dd8368d5808962891cfa1f7505072da4ff16acf/graphql_core-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="b1826fbd1c6c290f7180d758ecf9c3859a46574cff324bf35a10167533c0e463", url="https://pypi.org/packages/8b/04/5f79f6c48383d40717867bfcbda72adfeff20bb5dcc14abe7d44edf7064d/graphql_core-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="25c2f537b430abc380de8765577938c78b5993584af627b7eb56b061b4ae234d", url="https://pypi.org/packages/4e/4c/8b8646fa9441cabd5a94f0888065cee098db80bb134d3b7f5a93b7b1df6b/graphql_core-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="b654666330c46d6a98405a542e9fde0a499916428cbc11da51eb82be37ef1e05", url="https://pypi.org/packages/4d/df/4a4db43822c1176f30cf8a257818cd7b1b5eec469be045db86f5e01cef19/graphql_core-3.1.0-py3-none-any.whl")
    version("3.0.5", sha256="dfc374d3426677727772d8da9dd010e92d10305ddd9c2f7f0fc388f07cee94c4", url="https://pypi.org/packages/cc/45/c74fe65ade57473105f727ae9c8c36b8cf5b592d88ffae9b8b3198cd52c2/graphql_core-3.0.5-py3-none-any.whl")
    version("2.3.2", sha256="44c9bac4514e5e30c5a595fac8e3c76c1975cae14db215e8174c7fe995825bad", url="https://pypi.org/packages/11/71/d51beba3d8986fa6d8670ec7bcba989ad6e852d5ae99d95633e5dacc53e7/graphql_core-2.3.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="c06e59153246dd48ddbf86ca94a8f045c1b71daf8154b4635e1a0e2e11d9b60b", url="https://pypi.org/packages/a8/e4/838a3747ca511bcd7a6842dfc619c13eb298063ca1681af7bd1b4f8358ef/graphql_core-2.3.1-py2.py3-none-any.whl")
    version("2.3", sha256="c1b1a9f57434ef65bf5379c8a6b53755c2e7a38bd77bf01687f51c3361ac041b", url="https://pypi.org/packages/11/1f/22e70738a072bc8aecef18a62fcecc7e25f80fea9d5929480b9edb149a7b/graphql_core-2.3-py2.py3-none-any.whl")
    version("2.2.1", sha256="1488f2a5c2272dc9ba66e3042a6d1c30cea0db4c80bd1e911c6791ad6187d91b", url="https://pypi.org/packages/6a/11/bc4a7eb440124271289d93e4d208bd07d94196038fabbe2a52435a07d3d3/graphql_core-2.2.1-py2.py3-none-any.whl")
    version("2.2", sha256="6288fe97c32d2f868a2dfe62e766dc85d48c96c1d085294edf44714190f2e4f3", url="https://pypi.org/packages/f1/88/a4a7bf8ab66c35b146e44d77a1f9fd2c36e0ec9fb1a51581608c16deb6e3/graphql_core-2.2-py2.py3-none-any.whl")
    version("2.1", sha256="9462e22e32c7f03b667373ec0a84d95fba10e8ce2ead08f29fbddc63b671b0c1", url="https://pypi.org/packages/35/dd/2dff553c929d059e53a95a8bcff66f6a3930d736dfea17f88d16229eaf84/graphql_core-2.1-py2.py3-none-any.whl")
    version("2.1-rc3", sha256="0e4bfba0c0173a9ddb81c1c9fba7c4195be02658c0f2e3f5b54dffe14f8cc260", url="https://pypi.org/packages/31/6a/cffe87fc2cae9d2c97cf9f1c6757ba67149941148afec5bc923e11a85df6/graphql_core-2.1rc3-py2.py3-none-any.whl")
    version("2.1-rc2", sha256="e5710539d3098aa2ccdb0014901e2e1ac4af0ef09e3de9283192bc7b97211cf8", url="https://pypi.org/packages/c4/3e/dce7e2e24225073a754c45c474dfcf782e630f2d1d634b0a108852cf5c75/graphql_core-2.1rc2-py2.py3-none-any.whl")
    version("2.1-rc1", sha256="f3bbfb9cbc1fb67211527118aecb6dd61335f481bc03e96fe0fea540b362fb02", url="https://pypi.org/packages/c6/df/e8dd4029ab93fae57250d7786050ee20963a3e3b0c14d31126c57fe73fb0/graphql_core-2.1rc1-py2.py3-none-any.whl")
    version("2.0", sha256="539355351343dede3ecb771e0d273a1b72405cb6d64f45bb8f92ecc4d7109af0", url="https://pypi.org/packages/4f/e2/f4fb4ca7cfe13a6d51581c5628b6b44ee78cc832b763f3cc3f1e986850a5/graphql_core-2.0-py2.py3-none-any.whl")
    version("1.2.dev20170724044604", sha256="e4886aeba0cac66e98b0930ff98535f4afd3ce2e6d6ff6170f169be51771fb6c", url="https://pypi.org/packages/31/e4/0d8ee5ec9957a8c8f3c9917e63321d212af7e28b41d2d033b75259e1eda4/graphql-core-1.2.dev20170724044604.tar.gz")
    version("1.1", sha256="63bb8593aeeadb0a53e14207b910027fe51158d017927fad87326dac806185ee", url="https://pypi.org/packages/b0/89/00ad5e07524d8c523b14d70c685e0299a8b0de6d0727e368c41b89b7ed0b/graphql-core-1.1.tar.gz")
    version("1.0.1", sha256="1f5c43afb55c096572854116d7d86cb84a97c7ac30b173018879ea21c591de4a", url="https://pypi.org/packages/69/ce/6c1979ef1eb0c31d130d3b74301e11885221bb976853578c5b1704873844/graphql-core-1.0.1.tar.gz")
    version("1.0", sha256="518d2cde829e4eb538f04dcad115744062d24f82ae5bfa815c75c386b2969146", url="https://pypi.org/packages/34/11/daa388277e97e4ea8853cd51776499c91b69b79f6f31f7c8d8b389d30dfc/graphql-core-1.0.tar.gz")
    version("1.0.dev20160920065529", sha256="3ce0e1128702242859314a53f722f47af62d6d652ee5178cea2d655d9ccd39c6", url="https://pypi.org/packages/bd/d9/e8f830be880532446332cf9584b1e7ea23a39fd9e47e9a073633742b4339/graphql-core-1.0.dev20160920065529.tar.gz")
    version("1.0.dev20160909040033", sha256="b5a5f508c382315e158b4797b5ef50b5609e3be5ba5d84ac2d16ba3767117b13", url="https://pypi.org/packages/83/2e/ceedf726227221a5ff141124cb0b09954da7876971e9b75a7ba80b2abdee/graphql-core-1.0.dev20160909040033.tar.gz")
    version("0.5.3", sha256="4005b88b0ca5718f48c5ae8a4a49bd4ae1a82081301b9312b79d482d7a564a67", url="https://pypi.org/packages/53/74/7f71377be0d0fc9dbf47701853e6608b3da53ecd0e0c57f750d394455345/graphql-core-0.5.3.tar.gz")
    version("0.5.2", sha256="63c6144a8679e192a58a17dce51034840bae0d32cfef83ce2d45f8b807910f2c", url="https://pypi.org/packages/a7/e6/eaa04f65492bfdc5ee73dfed85f09ddaed39392db1db7021d3c4bd17ad23/graphql-core-0.5.2.tar.gz")
    version("0.5.1", sha256="b70561013b9a3dd8a301c95720da71e6cd951258e6393ca4f78c11f99a0a12a4", url="https://pypi.org/packages/1b/91/1517cdcb47d0e658f013d105acfbccd1801d7709e36770a30899c06c914c/graphql-core-0.5.1.tar.gz")
    version("0.5", sha256="d7bcd19f56d26982cb87b95875fb7f46d805a276acef312dc64782e08159cd34", url="https://pypi.org/packages/98/13/c8e9404eab2a601bd11f14f1847a6a79aab5191fef494fa00db99284b80e/graphql-core-0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-promise@2.3:", when="@2.3:2")
        depends_on("py-promise@2.1:2.1.0,2.2-rc1:", when="@2:2.0.0,2.1-rc0:2.2")
        depends_on("py-rx@1.6:1", when="@2.2.1:2")
        depends_on("py-rx@1.6:", when="@2:2.0.0,2.1-rc0:2.2.0")
        depends_on("py-six@1.10:", when="@2:2.0.0,2.1-rc0:2")
    # END DEPENDENCIES

