# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFaker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("24.3.0", sha256="9978025e765ba79f8bf6154c9630a9c2b7f9c9b0f175d4ad5e04b19a82a8d8d6", url="https://pypi.org/packages/0d/7c/572d8c44860a5b4bdbcbdadb4a2c957bc0c1c46e038a1b668662faf021a3/Faker-24.3.0-py3-none-any.whl")
    version("24.2.1", sha256="cf07e69b9293a28cb0390086bf773c8933e122bc15704c836ebbc33ba64b7a09", url="https://pypi.org/packages/9b/35/7ced81e9e945f7f86a007a0c3ea3337d9c33282e9916ca7b93a9575bfb8e/Faker-24.2.1-py3-none-any.whl")
    version("24.2.0", sha256="dce4754921f9fa7e2003c26834093361b8f45072e0f46f172d6ca1234774ecd4", url="https://pypi.org/packages/83/25/45f53826b94f596b5d9f97ec3a6e1ae02969c297e6aea40804991145c910/Faker-24.2.0-py3-none-any.whl")
    version("24.1.1", sha256="85f9bf3f4bcd2b2b71043b8f12077a0ad44acb6e43a22eb4f8ce392c893ffdcb", url="https://pypi.org/packages/6a/16/141add9d4bb59ff193b7c226e96e219ed84b58eb2eeb96c363a29db78ef1/Faker-24.1.1-py3-none-any.whl")
    version("24.1.0", sha256="89ae0932f4f269754790569828859eaa0ae2ce73d1f3eb1f30ae7c20d4daf5ce", url="https://pypi.org/packages/c5/ad/87c165d63be249db767227109d35e22cde75c9c941d69edc1b175f4928f0/Faker-24.1.0-py3-none-any.whl")
    version("24.0.0", sha256="2456d674f40bd51eb3acbf85221277027822e529a90cc826453d9a25dff932b1", url="https://pypi.org/packages/c8/3d/ed83cf090e31f5ef4d191a2e25500fc65281fb46d45f0cc224fd0f48b435/Faker-24.0.0-py3-none-any.whl")
    version("23.3.0", sha256="117ce1a2805c1bc5ca753b3dc6f9d567732893b2294b827d3164261ee8f20267", url="https://pypi.org/packages/58/d9/b24e100915b85df8aa0e0ea88c7cc470d74b0909b6eab2ca020cbf896fdc/Faker-23.3.0-py3-none-any.whl")
    version("23.2.1", sha256="0520a6b97e07c658b2798d7140971c1d5bc4bcd5013e7937fe075fd054aa320c", url="https://pypi.org/packages/40/f7/c88578e2bbb7e8940dd552d175300a6e8e9ee2f8d84fddad8e6acfe0e6cf/Faker-23.2.1-py3-none-any.whl")
    version("23.2.0", sha256="2db4b60ef93d247a8fe5518d01ebafa8df3a5dffd40cbb9577b25c45b04a9952", url="https://pypi.org/packages/be/de/8bd27eb39eda9e06803b8ac89ae32edff0b7d206f4b69cd2f558ae24620e/Faker-23.2.0-py3-none-any.whl")
    version("23.1.0", sha256="60e89e5c0b584e285a7db05eceba35011a241954afdab2853cb246c8a56700a2", url="https://pypi.org/packages/cb/f4/0f8391297cdd8fdf15cac9895b844514024bc4d784023419d4ad9d6acf50/Faker-23.1.0-py3-none-any.whl")
    version("19.13.0", sha256="da880a76322db7a879c848a0771e129338e0a680a9f695fd9a3e7a6ac82b45e1", url="https://pypi.org/packages/18/d6/314868f573b09d9f0590a2c2f7dd7463153d3dab1049f0ba5e7008776d91/Faker-19.13.0-py3-none-any.whl")
    version("19.12.1", sha256="02ae846940cc1a4d65dbda510fbc63a0d7b7de980f746d581d0a763b300eab24", url="https://pypi.org/packages/1c/6c/1c7426e7b30936c1859958f3b0b5651e1728ec53af0b635ef026d26a34ba/Faker-19.12.1-py3-none-any.whl")
    version("19.12.0", sha256="5990380a8ee81cf189d6b85d5fdc1fb43772cb136aca0385a08ff24ef01b9fdf", url="https://pypi.org/packages/de/f4/1e0d8d5050671d5d72ec51494adf04723c73dc53642db292102b7954c617/Faker-19.12.0-py3-none-any.whl")
    version("19.11.1", sha256="037421c391b7f41dcc51fe62247adb10de9173be6aa684fb1987ffdccd87612b", url="https://pypi.org/packages/65/f5/3a25d3775030fc717720072d2fb1aabf90ae3f39851e860bc6cc4580188f/Faker-19.11.1-py3-none-any.whl")
    version("19.11.0", sha256="e28090068293c5a83e7f4d636417d45fae1031ca8a8136cc2415549ebc2111e2", url="https://pypi.org/packages/6a/e9/98fc3f589186f14b42765061a87c522f5461aeb77d71c354bc7dcad33ddb/Faker-19.11.0-py3-none-any.whl")
    version("19.10.0", sha256="f321e657ed61616fbfe14dbb9ccc6b2e8282652bbcfcb503c1bd0231ff834df6", url="https://pypi.org/packages/9b/69/fc3c9c30d406655d00f9b5737f0a27f7ba89d8fff61c14d5ecd223acf211/Faker-19.10.0-py3-none-any.whl")
    version("19.9.1", sha256="e7090ae0b8c179752dba69221124856e1472b06111e214e3e12cd5094a2000ff", url="https://pypi.org/packages/14/4f/575ab29850f32476d98828dc31d81c26970d5d64c462d0995c10067fa31d/Faker-19.9.1-py3-none-any.whl")
    version("19.9.0", sha256="85468e16d4a9a8712bfdb98ba55aaf17c60658266a76958d099aee6a18c0a6c5", url="https://pypi.org/packages/d8/76/0b6f85657b89b005f96c5f26310e6d23b28c95de9871ccba3caa02b0ef99/Faker-19.9.0-py3-none-any.whl")
    version("19.8.1", sha256="48c84f0c28fce51b7274bbd6a5c1c383b4a397634c75e8c7505a6e6b5cf6da6b", url="https://pypi.org/packages/f4/09/2b94a7e15507e995311a5bab86b588cd98d49b61e2c475d735ea07e2d3de/Faker-19.8.1-py3-none-any.whl")
    version("19.8.0", sha256="d86cb3150626bd642c6abd8a64107ddb0b154500252f46a56efe527a50594866", url="https://pypi.org/packages/56/a2/d83fe79324fc3019ed614f684a4e8f6057592ec2d9694783528828342cfa/Faker-19.8.0-py3-none-any.whl")
    version("9.9.1", sha256="ceda1ddd12ba4317145ff7f9a69024e0257564f53fd46a10128eb5f634687abb", url="https://pypi.org/packages/48/8a/5a60f5bf286e8b4b2e936ca38dca56afa57b341a99805b2c9fed902c9f54/Faker-9.9.1-py3-none-any.whl")
    version("9.9.0", sha256="049185d17ff95c4311557da6b72416c18732e5977dcfd116a323b6d620db5dca", url="https://pypi.org/packages/27/ab/0371598513e8179d9053911e814c4de4ec2d0dd47e725dca40aa664f994c/Faker-9.9.0-py3-none-any.whl")
    version("9.8.4", sha256="7a400eb059b070ff8bb50e90ad16363bc613137686c89cb5eb20f2c06b93569f", url="https://pypi.org/packages/96/cf/0f69912a12c5fd3048043344190d0236ba43c393490117884efc464bc1e3/Faker-9.8.4-py3-none-any.whl")
    version("9.8.3", sha256="76ad74cebe727affa1c108e17fc1d2c0be8f498ff71b25f464fb8241301fe6f2", url="https://pypi.org/packages/dc/8f/b6161e184fbc7f9269b3ddd698884172870423c83f304d4a34a368a40691/Faker-9.8.3-py3-none-any.whl")
    version("9.8.2", sha256="876ba213aaddd661a539ada2158917c1be17064b72792ee788b81c13528865d0", url="https://pypi.org/packages/0a/ec/97397fbb5f17c9bb571bab49f939b973ef79729e929449630b0ca771396a/Faker-9.8.2-py3-none-any.whl")
    version("9.8.1", sha256="b9ea5970f43c1fa05443d1885fbed822aba816facefa053d3d20168bfef4ae84", url="https://pypi.org/packages/aa/13/f5602338f89e83804bbb1e179fa3e2cfb3e928c3f22b26ead889b9ed4ef3/Faker-9.8.1-py3-none-any.whl")
    version("9.8.0", sha256="810182ef3597e0dfc4999a29f7cf17b99c70b361aae0f16743de6b926619ae21", url="https://pypi.org/packages/16/ba/3add40668ed95febdc43042ccc9f354b21ee44c10ac0af5dee469b464068/Faker-9.8.0-py3-none-any.whl")
    version("9.7.1", sha256="aad59a0cb82ac072f3109667fb2ba35ac45981ec22436c649d8fcdbf1c9e6927", url="https://pypi.org/packages/19/1c/0d3248616f697230305bf910669e3cf11898962a6a91757df6c07c1488f4/Faker-9.7.1-py3-none-any.whl")
    version("9.7.0", sha256="cfaa967791920c041b053716c1297ecef48bdccdbadc4a363ffdf7b2a4ee4db0", url="https://pypi.org/packages/0e/3c/ed7eaaf37412bf041eb1ebaf0f39f49bbc8e6330ba7f6342296b2c8730f1/Faker-9.7.0-py3-none-any.whl")
    version("9.6.0", sha256="8ffd1ca479364a2ea78fe23a5710d5f940c50576f45c3f62edf9f7f9242cec0b", url="https://pypi.org/packages/7b/9c/402c93c91eae893e6f213701ba055714cf5841c24e3f59ed532647f3455f/Faker-9.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil@2.4:", when="@0.7.3,0.7.6:")
        depends_on("py-text-unidecode@1.3:", when="@2.0.2:11")
        depends_on("py-typing-extensions@3.10.0.1:", when="@19: ^python@:3.8.0")
    # END DEPENDENCIES

