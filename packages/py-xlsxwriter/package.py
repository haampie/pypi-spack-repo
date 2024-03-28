# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXlsxwriter(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.0", sha256="ecfd5405b3e0e228219bcaf24c2ca0915e012ca9464a14048021d21a995d490e", url="https://pypi.org/packages/a7/ea/53d1fe468e63e092cf16e2c18d16f50c29851242f9dd12d6a66e0d7f0d02/XlsxWriter-3.2.0-py3-none-any.whl")
    version("3.1.9", sha256="b61c1a0c786f82644936c0936ec96ee96cd3afb9440094232f7faef9b38689f0", url="https://pypi.org/packages/f7/3e/05ba2194cd5073602422859c949a4f21310a3c49bf8dccde9e03d4522b11/XlsxWriter-3.1.9-py3-none-any.whl")
    version("3.1.8", sha256="2d8d1f392b3e041adf90042dd2f7b5f7468181a45e5e9a7d8376e64b374104f1", url="https://pypi.org/packages/c8/aa/6162e6842f1853ebb9d60621c0b889a534510eb3e3bcff608f9cf7dc86aa/XlsxWriter-3.1.8-py3-none-any.whl")
    version("3.1.7", sha256="8c730c4beb468696c4160aa1d6d168fb4c1a20dd972b212cd8cc1e74ddeab1b6", url="https://pypi.org/packages/51/ba/f6982db11e17b43da310a2169dcfbda166e8c509d8358ec8310219ca9732/XlsxWriter-3.1.7-py3-none-any.whl")
    version("3.1.6", sha256="fc3838232f9f50763c1e81a3b381c6ad559dcdcd0983ee239bf54556392b4f3f", url="https://pypi.org/packages/4f/64/42063c82918475ce0a63fa19063607e60969b1498ccd4220274cf808fc60/XlsxWriter-3.1.6-py3-none-any.whl")
    version("3.1.5", sha256="a6d95556f96d6908885523554b3a468d74a711010d0a25b63d47e9ef4ba3bb94", url="https://pypi.org/packages/07/ff/d15408ef73f4bfec117fb2c39284c5fc2d4c3b745cf40f0e166830c2468d/XlsxWriter-3.1.5-py3-none-any.whl")
    version("3.1.4", sha256="29c7bf5ade4de1f0bb487882eb45d4845eebc3ff72a68b2090df94d83e10b92e", url="https://pypi.org/packages/dc/6b/db1de39818f4f5e6615fe972ef165cf62f4a1078048533cd00ebea4adc48/XlsxWriter-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="b1fde9b60dc25fff589f3baf58e95178048ba87a7916d45f6e3bce4a61f56e64", url="https://pypi.org/packages/6a/8c/5982a902521519d3f671bd24bce63eda474d7f16502c78ac2bb5ab889aa0/XlsxWriter-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="331508ff39d610ecdaf979e458840bc1eab6e6a02cfd5d08f044f0f73636236f", url="https://pypi.org/packages/37/94/25d3ec8587974de7ebd790232aa3155abfe44ed23df7ccaa4645977a1cbe/XlsxWriter-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="b50e3bd905d7dafa6ea45210e2cc5600b4ccd104a0d3a4d4d7cf813b78426440", url="https://pypi.org/packages/86/c1/d58c9dc59c6e1683158af49cd9fca28b99f7a9f2887c572ae11d1132bce6/XlsxWriter-3.1.1-py3-none-any.whl")
    version("3.0.3", sha256="df0aefe5137478d206847eccf9f114715e42aaea077e6a48d0e8a2152e983010", url="https://pypi.org/packages/ef/95/30f6ee57f10232e2055a85c3e4c8db7d38ab5f1349b6cdced85cb8acd5e6/XlsxWriter-3.0.3-py3-none-any.whl")
    version("1.4.3", sha256="1a7fac99687020e76aa7dd0d7de4b9b576547ed748e5cd91a99d52a6df54ca16", url="https://pypi.org/packages/2c/ce/74fd8d638a5b82ea0c6f08a5978f741c2655a38c3d6e82f73a0f084377e6/XlsxWriter-1.4.3-py2.py3-none-any.whl")
    version("1.2.2", sha256="00e9c337589ec67a69f1220f47409146ab1affd8eb1e8eaad23f35685bd23e47", url="https://pypi.org/packages/25/88/a38f35b00ce4dd166a20e1a0a25e438e19e332e680df52af4aeac0df0f03/XlsxWriter-1.2.2-py2.py3-none-any.whl")
    version("1.0.2", sha256="279220b1c58cef2d35b8fd99030945a740a4fde65c0c8598b34177f7e2cd8ffc", url="https://pypi.org/packages/c7/86/748cb5f6ef5ff2d95a7f189ef1c5124f9badc1d1293dbc214c128595e57e/XlsxWriter-1.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

