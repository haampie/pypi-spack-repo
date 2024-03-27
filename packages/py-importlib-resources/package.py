##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImportlibResources(PythonPackage):
    version("6.4.0", sha256="50d10f043df931902d4194ea07ec57960f66a80449ff867bfe782b4c486ba78c", url="https://pypi.org/packages/75/06/4df55e1b7b112d183f65db9503bff189e97179b256e1ea450a3c365241e0/importlib_resources-6.4.0-py3-none-any.whl")
    version("6.3.2", sha256="f41f4098b16cd140a97d256137cfd943d958219007990b2afb00439fc623f580", url="https://pypi.org/packages/6e/f0/0632f7ae2d23aa34f1c5b09caf775376b9372e685c3841947dceef39919f/importlib_resources-6.3.2-py3-none-any.whl")
    version("6.3.1", sha256="4811639ca7fa830abdb8e9ca0a104dc6ad13de691d9fe0d3173a71304f068159", url="https://pypi.org/packages/18/4f/726c9cd8ca3327af96a8f808df3ac3327bf1452d68b06f96e1e3717f4b15/importlib_resources-6.3.1-py3-none-any.whl")
    version("6.3.0", sha256="783407aa1cd05550e3aa123e8f7cfaebee35ffa9cb0242919e2d1e4172222705", url="https://pypi.org/packages/de/79/7ad3b2831247db4f61e781f9164147b1ee20205c5230dcd177021caa266b/importlib_resources-6.3.0-py3-none-any.whl")
    version("6.2.0", sha256="8d035473d681d9bb95d06a31ad18594962933405519d36f4af1565fe6f998ad6", url="https://pypi.org/packages/97/2d/3a93490a3bcda38de4dc686c5eaacbdeecf6aa142811e53b9b68d9ebf72f/importlib_resources-6.2.0-py3-none-any.whl")
    version("6.1.3", sha256="4c0269e3580fe2634d364b39b38b961540a7738c02cb984e98add8b4221d793d", url="https://pypi.org/packages/f3/3e/a01c6de9853a7d73672926e01966f979723386f0ba83d62e5db3cdf4c097/importlib_resources-6.1.3-py3-none-any.whl")
    version("6.1.2", sha256="9a0a862501dc38b68adebc82970140c9e4209fc99601782925178f8386339938", url="https://pypi.org/packages/ba/0b/27d13042335942abc29a87f49f1ce6b56fa58e025e96454ef25929aeb603/importlib_resources-6.1.2-py3-none-any.whl")
    version("6.1.1", sha256="e8bf90d8213b486f428c9c39714b920041cb02c184686a3dee24905aaa8105d6", url="https://pypi.org/packages/93/e8/facde510585869b5ec694e8e0363ffe4eba067cb357a8398a55f6a1f8023/importlib_resources-6.1.1-py3-none-any.whl")
    version("6.1.0", sha256="aa50258bbfa56d4e33fbd8aa3ef48ded10d1735f11532b8df95388cc6bdb7e83", url="https://pypi.org/packages/65/6e/09d8816b5cb7a4006ef8ad1717a2703ad9f331dae9717d9f22488a2d6469/importlib_resources-6.1.0-py3-none-any.whl")
    version("6.0.1", sha256="134832a506243891221b88b4ae1213327eea96ceb4e407a00d790bb0626f45cf", url="https://pypi.org/packages/25/d4/592f53ce2f8dde8be5720851bd0ab71cc2e76c55978e4163ef1ab7e389bb/importlib_resources-6.0.1-py3-none-any.whl")
    version("5.12.0", sha256="7b1deeebbf351c7578e09bf2f63fa2ce8b5ffec296e0d349139d43cca061a81a", url="https://pypi.org/packages/38/71/c13ea695a4393639830bf96baea956538ba7a9d06fcce7cef10bfff20f72/importlib_resources-5.12.0-py3-none-any.whl")
    version("5.9.0", sha256="f78a8df21a79bcc30cfd400bdc38f314333de7c0fb619763f6b9dabab8268bb7", url="https://pypi.org/packages/d3/91/4df247dd4da18b72b5bbabe1fa2b85029c34e1d6f0afdd6329d15d6bf2b5/importlib_resources-5.9.0-py3-none-any.whl")
    version("5.3.0", sha256="7a65eb0d8ee98eedab76e6deb51195c67f8e575959f6356a6e15fd7e1148f2a3", url="https://pypi.org/packages/b1/8e/f29e92e403acda0e28789c0f994500239dff45065c3b28e3a2855afc4f9a/importlib_resources-5.3.0-py3-none-any.whl")
    version("5.2.3", sha256="ae35ed1cfe8c0d6c1a53ecd168167f01fa93b893d51a62cdf23aea044c67211b", url="https://pypi.org/packages/11/8e/84a6a778a1160cefcef1192a7bd26e4e6689981553aff13c2b2b6f1c352f/importlib_resources-5.2.3-py3-none-any.whl")
    version("5.2.2", sha256="2480d8e07d1890056cb53c96e3de44fead9c62f2ba949b0f2e4c4345f4afa977", url="https://pypi.org/packages/f2/6c/2f3b930513bb971172ffceb63cf4e910944e57451724e69b1dec97cfefa6/importlib_resources-5.2.2-py3-none-any.whl")
    version("5.2.1", sha256="b9a075a844a03e0fb0ab70e5b0ea138c92e9f07f3a21fc11a656cf9492dbf64f", url="https://pypi.org/packages/83/57/8456fe5bfc08d52e4001a94931e479dc3b10796ad5f24639ed3e2c6f062c/importlib_resources-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="a0143290bef3cbc99de9e40176e4987780939a955b8632f02ce6c935f42e9bfc", url="https://pypi.org/packages/c3/8d/cb49c07dd01e797e76e86f33c3472ebd861216b57296095f5c17be9b79e8/importlib_resources-5.2.0-py3-none-any.whl")
    version("5.1.4", sha256="e962bff7440364183203d179d7ae9ad90cb1f2b74dcb84300e88ecc42dca3351", url="https://pypi.org/packages/a4/30/b230b6586bcf6b80752ae42979f3b0da70bbde977d2b73eafd20c693b3db/importlib_resources-5.1.4-py3-none-any.whl")
    version("5.1.3", sha256="3b9c774e0e7e8d9c069eb2fe6aee7e9ae71759a381dec02eb45249fba7f38713", url="https://pypi.org/packages/b2/33/c74ccb6c48e4111f604f69ab102eba3fc126f143306f2efb0faba70c970a/importlib_resources-5.1.3-py3-none-any.whl")
    version("5.1.2", sha256="ebab3efe74d83b04d6bf5cd9a17f0c5c93e60fb60f30c90f56265fce4682a469", url="https://pypi.org/packages/f0/5e/69e6a0602c1f18d390952177de648468c4a380252858b0022affc3ce7811/importlib_resources-5.1.2-py3-none-any.whl")
    version("5.1.1", sha256="67bcf65e7b9f7f2ea54a342254c7e87607819955469034bc581fae26e1743306", url="https://pypi.org/packages/f5/6e/a5c7a7147407a318cb421d10d84bb2049e81d0b7472eb0a91a30b9ea24a6/importlib_resources-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="885b8eae589179f661c909d699a546cf10d83692553e34dca1bf5eb06f7f6217", url="https://pypi.org/packages/82/70/7bf5f275a738629a7252c30c8461502d3658a75363db9f4f88ddbeb9eeac/importlib_resources-5.1.0-py3-none-any.whl")
    version("5.0.7", sha256="2238159eb743bd85304a16e0536048b3e991c531d1cd51c4a834d1ccf2829057", url="https://pypi.org/packages/46/10/7cc167fe072037c3cd2a15a92bb963b86f2bab8ac0995fab95fb7a152b80/importlib_resources-5.0.7-py3-none-any.whl")
    version("1.0.2", sha256="6e2783b2538bd5a14678284a3962b0660c715e5a0f10243fd5e00a4b5974f50b", url="https://pypi.org/packages/2f/f7/b4aa02cdd3ee7ebba375969d77c00826aa15c5db84247d23c89522dccbfa/importlib_resources-1.0.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-zipp@3.1:", when="@5.1.4: ^python@:3.9")

