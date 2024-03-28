# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterlabWidgets(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.10", sha256="dd61f3ae7a5a7f80299e14585ce6cf3d6925a96c9103c978eda293197730cb64", url="https://pypi.org/packages/24/da/db1cb0387a7e4086780aff137987ee924e953d7f91b2a870f994b9b1eeb8/jupyterlab_widgets-3.0.10-py3-none-any.whl")
    version("3.0.9", sha256="3cf5bdf5b897bf3bccf1c11873aa4afd776d7430200f765e0686bd352487b58d", url="https://pypi.org/packages/e8/05/0ebab152288693b5ec7b339aab857362947031143b282853b4c2dd4b5b40/jupyterlab_widgets-3.0.9-py3-none-any.whl")
    version("3.0.8", sha256="4715912d6ceab839c9db35953c764b3214ebbc9161c809f6e0510168845dfdf5", url="https://pypi.org/packages/74/5e/2475ac62faf2e342b2bf20b8d8e375f49400ecb38f52e4e0a7557eb1cedb/jupyterlab_widgets-3.0.8-py3-none-any.whl")
    version("3.0.7", sha256="c73f8370338ec19f1bec47254752d6505b03601cbd5a67e6a0b184532f73a459", url="https://pypi.org/packages/46/98/e7ce879b7b5d4871b80e291be967d22e5e66fa43474c476a95fe6231f50d/jupyterlab_widgets-3.0.7-py3-none-any.whl")
    version("3.0.6", sha256="e95d08adf4f9c37a57da5fff8a65d00480199885fd2ecd2583fd9560b594b4e9", url="https://pypi.org/packages/45/e9/9ab05b131992a705ede4eef7a52de46dae6e7406ac05b657caae6c60cf60/jupyterlab_widgets-3.0.6-py3-none-any.whl")
    version("3.0.5", sha256="a04a42e50231b355b7087e16a818f541e53589f7647144ea0344c4bf16f300e5", url="https://pypi.org/packages/df/82/4576cbc07ebace8c7734fe08b2c2f9123b7ebecd29e932a3b839b6bee2cb/jupyterlab_widgets-3.0.5-py3-none-any.whl")
    version("3.0.4", sha256="4c9275daa6d20fc96c3aea45756ece7110850d035b0b93a6a40e918016b927da", url="https://pypi.org/packages/c4/a2/c140ec0fa915c7e93934128465a433a657ed588581783142cb51a92e8eae/jupyterlab_widgets-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="6aa1bc0045470d54d76b9c0b7609a8f8f0087573bae25700a370c11f82cb38c8", url="https://pypi.org/packages/d8/52/2f4b8f5975312fb58f4eacab2e6f6cfd2efd05704514a60a151a4e69d608/jupyterlab_widgets-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="98303a281f4004670cdcea2ef4aecba19c580adc297664c593f967025625c8c5", url="https://pypi.org/packages/d3/dc/f3aaf9fe0bf6bfba3cf85a65656c11eba7324456600082c63686d9ae5831/jupyterlab_widgets-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="1b937f448bddf88576864b3fd189430d7a181994bd59a50280791285803b5e11", url="https://pypi.org/packages/6b/97/86c62be347d7e927db7dc5ed096c2c96ff592d93f9659bd074730f0bde08/jupyterlab_widgets-3.0.1-py3-none-any.whl")
    version("1.1.7", sha256="0c4548cf42032e490447e4180f2c7d49ba5c30b42164992b38fb8c9d56c4e1b2", url="https://pypi.org/packages/06/c9/50a16b6e7410d661ea16160f8c650c444ab83740b437b3c202ca7d8e2b73/jupyterlab_widgets-1.1.7-py3-none-any.whl")
    version("1.1.6", sha256="1109fc847de2e46ba131643ff2c88bfcac9620e154e8ca135491fd09a1664f9f", url="https://pypi.org/packages/aa/a4/d6e4a72a50f33aba2b9701210952067ff34cc8acc4c1ae0a7712ccc8cf90/jupyterlab_widgets-1.1.6-py3-none-any.whl")
    version("1.1.5", sha256="7bc9a5642f6741945e873183695c28b02665a7f075aa36f7cca8b52ab984e581", url="https://pypi.org/packages/65/10/dfe39b23de3625e2afb293b3f1dbc8edae2d42459ceeea7f3142ccad6543/jupyterlab_widgets-1.1.5-py3-none-any.whl")
    version("1.1.4", sha256="769eb7bfef7e8ab70a7737104555531b09bcfba982f89465d2ae67b99b3f3e81", url="https://pypi.org/packages/47/78/b8db068414b354da1abd01dfc2326b8b3123d334173683941a075d36e3da/jupyterlab_widgets-1.1.4-py3-none-any.whl")
    version("1.1.3", sha256="93f59c2f848ebdb3c87195c18bc7360eddbc05ddb17f676ea1d8bfba9229b1f5", url="https://pypi.org/packages/28/fc/9020b1c4e9a9c81a153a6a8cac7924ec4c962b2b653f76a18171940af348/jupyterlab_widgets-1.1.3-py3-none-any.whl")
    version("1.1.2", sha256="e7562e9d4ecb282f36f69fa4f1d0b23bda12db306b7aa981d47ba2a532e2ebe9", url="https://pypi.org/packages/31/28/99a86634451a40f89ebf6b35e24e529fa5829f23784b9bdd5fa8e9386aa6/jupyterlab_widgets-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="90ab47d99da03a3697074acb23b2975ead1d6171aa41cb2812041a7f2a08177a", url="https://pypi.org/packages/a5/bb/210ce9e56cad3b9e7a0468582a3f22b06bb209430d6481031f05fafafad6/jupyterlab_widgets-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="c2a9bd3789f120f64d73268c066ed3b000c56bc1dda217be5cdc43e7b4ebad3f", url="https://pypi.org/packages/5f/2c/7331aa9c5041e8b107d712d853268e137f55014b858407816b5487289d11/jupyterlab_widgets-1.1.0-py3-none-any.whl")
    version("1.0.2", sha256="f5d9efface8ec62941173ba1cffb2edd0ecddc801c11ae2931e30b50492eb8f7", url="https://pypi.org/packages/18/4d/22a93473bca99c80f2d23f867ebbfee2f6c8e186bf678864eec641500910/jupyterlab_widgets-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="841925a349bd9a9197c5506bd5461a321b09e6659a9b179a0096b561a92898c3", url="https://pypi.org/packages/a6/c8/84e487bd89d8f444299adf2656bcfe4cee0223ccd69b1206a83fe7c45427/jupyterlab_widgets-1.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

