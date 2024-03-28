# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRapidfuzz(PythonPackage):
    # BEGIN VERSIONS
    version("3.7.0", sha256="620df112c39c6d27316dc1e22046dc0382d6d91fd60d7c51bd41ca0333d867e9", url="https://pypi.org/packages/65/75/e52ee00ebf8c13f8ca60b61641dfc1b8786b0d0d2fd4065cb337c861fe3e/rapidfuzz-3.7.0.tar.gz")
    version("3.6.2", sha256="cf911e792ab0c431694c9bf2648afabfd92099103f2e31492893e078ddca5e1a", url="https://pypi.org/packages/11/7c/36511ff0e2e5f6cce4e854dfc1974a1519929214a38a165322f38dd01a19/rapidfuzz-3.6.2.tar.gz")
    version("3.6.1", sha256="35660bee3ce1204872574fa041c7ad7ec5175b3053a4cb6e181463fc07013de7", url="https://pypi.org/packages/d4/f4/039e35e99c967100d73616ec08d4c02325f67e0d5c32a6d5a49a7f620942/rapidfuzz-3.6.1.tar.gz")
    version("3.6.0", sha256="4cdf564c3eeb2d95148bd7199e7869fa927f47cc3aea42f299aa836cfb2b6cfd", url="https://pypi.org/packages/e1/79/42394ecd1b6176f2efa83ca7a32673aefbba51690e557a68cf6d49366d82/rapidfuzz-3.6.0.tar.gz")
    version("3.5.2", sha256="9e9b395743e12c36a3167a3a9fd1b4e11d92fb0aa21ec98017ee6df639ed385e", url="https://pypi.org/packages/8b/f3/bf5e82eca3b88853a5fe596bf8c94fb6f2775dc1b55b7bfee9de21afab03/rapidfuzz-3.5.2.tar.gz")
    version("3.5.1", sha256="24d7b6ba410f0fdcc1465d8d396929b724e361a0ce4a01e0180c90443020a38c", url="https://pypi.org/packages/fa/e6/ad5adae7965c95d5f3c7882d5106f2ac175308d247152b03f4d6ff48db7e/rapidfuzz-3.5.1.tar.gz")
    version("3.4.0", sha256="a74112e2126b428c77db5e96f7ce34e91e750552147305b2d361122cbede2955", url="https://pypi.org/packages/27/36/22741bb354505ca284c2149a4c7fdee396a6cdeae3f4c0614acf6b0ee27e/rapidfuzz-3.4.0.tar.gz")
    version("3.3.1", sha256="6783b3852f15ed7567688e2e358757a7b4f38683a915ba5edc6c64f1a3f0b450", url="https://pypi.org/packages/1a/bc/1475cf5a75bcdfdf59b3947e9ffdfab3518629110a662c20d90b67ce037f/rapidfuzz-3.3.1.tar.gz")
    version("3.3.0", sha256="5e71bc5829f41e78b2d009431aedeb308ee3699d2bbbc68b7739db9b40bd1465", url="https://pypi.org/packages/20/ab/f7f65cfeb2d9dda1fcf4190ccd3bfe8e4bfd4bce00375d90e20926fe7a28/rapidfuzz-3.3.0.tar.gz")
    version("3.2.0", sha256="448d031d9960fea7826d42bd4284156fc68d3b55a6946eb34ca5c6acf960577b", url="https://pypi.org/packages/77/76/224d6eeab59c705bb7c1986b91b3e756dd65efbcf5bda148d39c3cbf402b/rapidfuzz-3.2.0.tar.gz")
    version("2.15.2", sha256="bfc1d38a7adcbe8912f980a5f46f27a801dd8655582ff0d4a2c0431c02b7ce33", url="https://pypi.org/packages/5f/ec/8428b62c29dc9841acde7e2905d417a654d33c9eb59f9439d06af21d7bff/rapidfuzz-2.15.2.tar.gz")
    version("2.15.1", sha256="d62137c2ca37aea90a11003ad7dc109c8f1739bfbe5a9a217f3cdb07d7ac00f6", url="https://pypi.org/packages/44/19/a20bd17379cca3e0a63590a6473ecf6cdaa8351688de775afefffc701a79/rapidfuzz-2.15.1.tar.gz")
    version("2.15.0", sha256="1c7e439d1428882d297bdd0db5626fc4626cdebe50d3fbbf4ed898f775ca56d5", url="https://pypi.org/packages/01/8c/cad170708243488e2b2a2e727eb40f30018231efa7fa1a9a3a3dc82d9f42/rapidfuzz-2.15.0.tar.gz")
    version("2.14.0", sha256="a819146779f51494b8c6972652f12eb5288581f280e4bd62e45a239b61ee4d32", url="https://pypi.org/packages/5e/5a/8a3c70e6e354978d0b1a4f03a62e8893cf0ddb86ee28cf30dc2d03539ea0/rapidfuzz-2.14.0.tar.gz")
    version("2.13.7", sha256="8d3e252d4127c79b4d7c2ae47271636cbaca905c8bb46d80c7930ab906cf4b5c", url="https://pypi.org/packages/15/e5/2ab8375be6955aff1925b69c41429cbe54e32a67461c0b59f94c9b8b1cc5/rapidfuzz-2.13.7.tar.gz")
    version("2.13.6", sha256="948445a054d9fb30a93597c325d8836232bd68e61443a88779a57702aa35a007", url="https://pypi.org/packages/cc/42/f3bde4d6e5711b5ba266dc66c66bc0659e7c2f2016f46d1927c76d40ad57/rapidfuzz-2.13.6.tar.gz")
    version("2.13.5", sha256="1c425ffa7a3fbcaa4bb90b6d083dabc974b96c535b73f03fb6ef0ae3fb47b4a6", url="https://pypi.org/packages/69/14/a64b52cf0dac27605be649bb0c3c1facd88b354acfad1cdbfcc0c4893854/rapidfuzz-2.13.5.tar.gz")
    version("2.13.4", sha256="85f5e8667b8e6cb7687c86374c60b133abdc76b2af24455172388c5d7ab2787b", url="https://pypi.org/packages/87/d4/4fcd1d0f6b702969f2d1f1068d2bc618f2a1e859c8f4881f523687b855bd/rapidfuzz-2.13.4.tar.gz")
    version("2.13.3", sha256="c734d54b5fbdcfea605f7365dedb7083e7499d394fbd03378d663b398e9790ad", url="https://pypi.org/packages/57/93/8a975f8462fadffd1b608a1a5df2bb9feea569e5bcef5a6abfb154853e24/rapidfuzz-2.13.3.tar.gz")
    version("2.13.2", sha256="1c67007161655c59e13bba130a2db29d7c9e5c81bcecb8846a3dd7386065eb24", url="https://pypi.org/packages/7a/85/b880d556130d19ac415bfaf1af9406263f7597b5b7ba062db1f532e587b9/rapidfuzz-2.13.2.tar.gz")
    version("2.2.0", sha256="acb8839aac452ec61a419fdc8799e8a6e6cd21bed53d04678cdda6fba1247e2f", url="https://pypi.org/packages/80/2a/0841832a010c57b69a1d515fb9725ada03367a0d028acc960e65e6c31f5f/rapidfuzz-2.2.0.tar.gz")
    version("1.8.2", sha256="d6efbb2b6b18b3a67d7bdfbcd9bb72732f55736852bbef823bdf210f9e0c6c90", url="https://pypi.org/packages/21/c5/92864654ef66a451fd9d014213f56d9e9b62bde7415f6962e2ea51ae6d07/rapidfuzz-1.8.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

