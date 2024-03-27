##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCython(PythonPackage):
    version("3.0.9", sha256="a2d354f059d1f055d34cfaa62c5b68bc78ac2ceab6407148d47fb508cf3ba4f3", url="https://pypi.org/packages/0e/17/c5b026cea7a634ee3b8950a7be16aaa49deeb3b9824ba5e81c13ac26f3c4/Cython-3.0.9.tar.gz")
    version("3.0.8", sha256="8333423d8fd5765e7cceea3a9985dd1e0a5dfeb2734629e1a2ed2d6233d39de6", url="https://pypi.org/packages/68/09/ffb61f29b8e3d207c444032b21328327d753e274ea081bc74e009827cc81/Cython-3.0.8.tar.gz")
    version("3.0.7", sha256="fb299acf3a578573c190c858d49e0cf9d75f4bc49c3f24c5a63804997ef09213", url="https://pypi.org/packages/23/e9/ef8607abfbbbaeb93cb1381c8538a22d38d64524df39759dc2787d4909b0/Cython-3.0.7.tar.gz")
    version("3.0.6", sha256="399d185672c667b26eabbdca420c98564583798af3bc47670a8a09e9f19dd660", url="https://pypi.org/packages/d3/20/02f4961b4315b95989abfe4b7cedff263cc89693834222d210a7a62a6214/Cython-3.0.6.tar.gz")
    version("3.0.5", sha256="39318348db488a2f24e7c84e08bdc82f2624853c0fea8b475ea0b70b27176492", url="https://pypi.org/packages/16/fb/82178bc16887eb9b03f2fc73c50aaa96ce528c3fd3c6f89cae631923af15/Cython-3.0.5.tar.gz")
    version("3.0.4", sha256="2e379b491ee985d31e5faaf050f79f4a8f59f482835906efe4477b33b4fbe9ff", url="https://pypi.org/packages/3f/aa/1a5c72615e0ba4dc30cc36de7e8a9a2eca2158922b0677654fced0d3476c/Cython-3.0.4.tar.gz")
    version("3.0.3", sha256="327309301b01f729f173a94511cb2280c87ba03c89ed428e88f913f778245030", url="https://pypi.org/packages/1a/1d/c79482ecb7217fc5840eceb724f7ebb4d3a70c5bf46309add0c0cd299891/Cython-3.0.3.tar.gz")
    version("3.0.2", sha256="9594818dca8bb22ae6580c5222da2bc5cc32334350bd2d294a00d8669bcc61b5", url="https://pypi.org/packages/2f/81/c9fb4b69823f674e1e2acc484eac93a47a1e3a59d4d051c76259dadd6984/Cython-3.0.2.tar.gz")
    version("3.0.1", sha256="f3e49c4eaaa11345486ac0fa2b350636e44a4b45bd7521a6b133924c5ff20bba", url="https://pypi.org/packages/41/eb/416c7f3060a714646a91499822ffac4767ecca6f005d48ef9cef4da10175/Cython-3.0.1.tar.gz")
    version("3.0.0", sha256="350b18f9673e63101dbbfcf774ee2f57c20ac4636d255741d76ca79016b1bd82", url="https://pypi.org/packages/7f/a2/fd5ced5dd33597ef291861bfadd46820de417b41bcb6ca2fa0b5f6fa8152/Cython-3.0.0.tar.gz")
    version("0.29.36", sha256="41c0cfd2d754e383c9eeb95effc9aa4ab847d0c9747077ddd7c0dcb68c3bc01f", url="https://pypi.org/packages/38/db/df0e99d6c5fe19ee5c981d22aad557be4bdeed3ecfae25d47b84b07f0f98/Cython-0.29.36.tar.gz")
    version("0.29.35", sha256="6e381fa0bf08b3c26ec2f616b19ae852c06f5750f4290118bf986b6f85c8c527", url="https://pypi.org/packages/da/a0/298340fb8412574a0b00a0d9856aa27e7038da429b9e31d6825173d1e6bd/Cython-0.29.35.tar.gz")
    version("0.29.34", sha256="1909688f5d7b521a60c396d20bba9e47a1b2d2784bfb085401e1e1e7d29a29a8", url="https://pypi.org/packages/0a/70/1500f05bddb16d795b29fac42954b3c8764c82367b8326c10f038471ae7f/Cython-0.29.34.tar.gz")
    version("0.29.33", sha256="5040764c4a4d2ce964a395da24f0d1ae58144995dab92c6b96f44c3f4d72286a", url="https://pypi.org/packages/dc/f6/e8e302f9942cbebede88b1a0c33d0be3a738c3ac37abae87254d58ffc51c/Cython-0.29.33.tar.gz")
    version("0.29.32", sha256="8733cf4758b79304f2a4e39ebfac5e92341bce47bcceb26c1254398b2f8c1af7", url="https://pypi.org/packages/4c/76/1e41fbb365ad20b6efab2e61b0f4751518444c953b390f9b2d36cf97eea0/Cython-0.29.32.tar.gz")
    version("0.29.30", sha256="2235b62da8fe6fa8b99422c8e583f2fb95e143867d337b5c75e4b9a1a865f9e3", url="https://pypi.org/packages/d4/ad/7ce0cccd68824ac9623daf4e973c587aa7e2d23418cd028f8860c80651f5/Cython-0.29.30.tar.gz")
    version("0.29.24", sha256="cdf04d07c3600860e8c2ebaad4e8f52ac3feb212453c1764a49ac08c827e8443", url="https://pypi.org/packages/59/e3/78c921adf4423fff68da327cc91b73a16c63f29752efe7beb6b88b6dd79d/Cython-0.29.24.tar.gz")
    version("0.29.23", sha256="6a0d31452f0245daacb14c979c77e093eb1a546c760816b5eed0047686baad8e", url="https://pypi.org/packages/d9/cd/0d2d90b27219c07f68f1c25bcc7b02dd27639d2180add9d4b73e70945869/Cython-0.29.23.tar.gz")
    version("0.29.22", sha256="df6b83c7a6d1d967ea89a2903e4a931377634a297459652e4551734c48195406", url="https://pypi.org/packages/d3/38/adc49a5aca4f644e6322237089fdcf194084f5fe41445e6e632f28b32bf7/Cython-0.29.22.tar.gz")
    version("0.29.21", sha256="e57acb89bd55943c8d8bf813763d20b9099cc7165c0f16b707631a7654be9cad", url="https://pypi.org/packages/6c/9f/f501ba9d178aeb1f5bf7da1ad5619b207c90ac235d9859961c11829d0160/Cython-0.29.21.tar.gz")
    version("0.29.20", sha256="22d91af5fc2253f717a1b80b8bb45acb655f643611983fd6f782b9423f8171c7", url="https://pypi.org/packages/3f/61/16a435de52fcda15246597a602aab6132cea50bedeb0919cb8874a068a20/Cython-0.29.20.tar.gz")
    version("0.29.16", sha256="232755284f942cbb3b43a06cd85974ef3c970a021aef19b5243c03ee2b08fa05", url="https://pypi.org/packages/49/8a/6a4135469372da2e3d9f88f71c6d00d8a07ef65f121eeca0c7ae21697219/Cython-0.29.16.tar.gz")
    version("0.29.15", sha256="60d859e1efa5cc80436d58aecd3718ff2e74b987db0518376046adedba97ac30", url="https://pypi.org/packages/d9/82/d01e767abb9c4a5c07a6a1e6f4d5a8dfce7369318d31f48a52374094372e/Cython-0.29.15.tar.gz")
    version("0.29.14", sha256="e4d6bb8703d0319eb04b7319b12ea41580df44fd84d83ccda13ea463c6801414", url="https://pypi.org/packages/9c/9b/706dac7338c2860cd063a28cdbf5e9670995eaea408abbf2e88ba070d90d/Cython-0.29.14.tar.gz")
    version("0.29.13", sha256="c29d069a4a30f472482343c866f7486731ad638ef9af92bfe5fca9c7323d638e", url="https://pypi.org/packages/a5/1f/c7c5450c60a90ce058b47ecf60bb5be2bfe46f952ed1d3b95d1d677588be/Cython-0.29.13.tar.gz")
    version("0.29.10", sha256="26229570d6787ff3caa932fe9d802960f51a89239b990d275ae845405ce43857", url="https://pypi.org/packages/e7/2e/aee8dfff93c7f5d20461ddcefd1da3d43bab18e1666a7777f4d9dbe94065/Cython-0.29.10.tar.gz")
    version("0.29.7", sha256="55d081162191b7c11c7bfcb7c68e913827dfd5de6ecdbab1b99dab190586c1e8", url="https://pypi.org/packages/f8/da/c979464858b257b21a6472a85285548c91f5b4dc773cb049cfdfb3ceeb02/Cython-0.29.7.tar.gz")
    version("0.29.5", sha256="9d5290d749099a8e446422adfb0aa2142c711284800fb1eb70f595101e32cbf1", url="https://pypi.org/packages/e0/31/4a166556f92c469d8291d4b03a187f325c773c330fffc1e798bf83d947f2/Cython-0.29.5.tar.gz")
    version("0.29", sha256="94916d1ede67682638d3cc0feb10648ff14dc51fb7a7f147f4fedce78eaaea97", url="https://pypi.org/packages/f0/66/6309291b19b498b672817bd237caec787d1b18013ee659f17b1ec5844887/Cython-0.29.tar.gz")
    version("0.28.6", sha256="68aa3c00ef1deccf4dd50f0201d47c268462978c12c42943bc33dc9dc816ac1b", url="https://pypi.org/packages/fa/b2/4f4441937b9902fe1dbbde17858de91e5809a938a0110f89df5296e0bc41/Cython-0.28.6.tar.gz")
    version("0.28.3", sha256="1aae6d6e9858888144cea147eb5e677830f45faaff3d305d77378c3cba55f526", url="https://pypi.org/packages/b3/ae/971d3b936a7ad10e65cb7672356cff156000c5132cf406cb0f4d7a980fd3/Cython-0.28.3.tar.gz")
    version("0.28.1", sha256="152ee5f345012ca3bb7cc71da2d3736ee20f52cd8476e4d49e5e25c5a4102b12", url="https://pypi.org/packages/be/08/bb5ffd1c32a951cbc26011ecb8557e59dc7a0a4975f0ad98b2cd7446f7dd/Cython-0.28.1.tar.gz")
    version("0.25.2", sha256="f141d1f9c27a07b5a93f7dc5339472067e2d7140d1c5a9e20112a5665ca60306", url="https://pypi.org/packages/b7/67/7e2a817f9e9c773ee3995c1e15204f5d01c8da71882016cac10342ef031b/Cython-0.25.2.tar.gz")
    version("0.23.5", sha256="1f08f307508c6c128f183d45c562dc11b8b984a00d253989b5644cc623299569", url="https://pypi.org/packages/05/4f/045e2a3ba0c6509378b4390961b6a72b0ebcd5fc812fe25ec3c71a82217a/Cython-0.23.5.zip")
    version("0.23.4", sha256="44444591133c92a30d78a6ec52ea4afd902ee4548ca5e83d94388f6a99f6c9ae", url="https://pypi.org/packages/0a/b6/fd142319fd0fe83dc266cfe83bfd095bc200fae5190fce0a2482560acb55/Cython-0.23.4.zip")


