# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMako(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.4", sha256="c97c79c018b9165ac9922ae4f32da095ffd3c4e6872b45eded42926deea46818", url="https://pypi.org/packages/03/3b/68690a035ba7347860f1b8c0cde853230ba69ff41df5884ea7d89fe68cd3/Mako-1.2.4-py3-none-any.whl")
    version("1.2.2", sha256="8efcb8004681b5f71d09c983ad5a9e6f5c40601a6ec469148753292abc0da534", url="https://pypi.org/packages/90/12/eb62db8bc346bc41a7ec8fbccd525e91d2747f9acfa6fbfd978948640a85/Mako-1.2.2-py3-none-any.whl")
    version("1.1.6", sha256="afaf8e515d075b22fad7d7b8b30e4a1c90624ff2f3733a06ec125f5a5f043a57", url="https://pypi.org/packages/b4/4d/e03d08f16ee10e688bde9016bc80af8b78c7f36a8b37c7194da48f72207e/Mako-1.1.6-py2.py3-none-any.whl")
    version("1.1.5", sha256="6804ee66a7f6a6416910463b00d76a7b25194cd27f1918500c5bd7be2a088a23", url="https://pypi.org/packages/75/69/c3ab0db9234fa5681a85a1c55203763a62902d56ad76b6d9b9bfa2c83694/Mako-1.1.5-py2.py3-none-any.whl")
    version("1.1.4", sha256="aea166356da44b9b830c8023cd9b557fa856bd8b4035d6de771ca027dfc5cc6e", url="https://pypi.org/packages/f3/54/dbc07fbb20865d3b78fdb7cf7fa713e2cba4f87f71100074ef2dc9f9d1f7/Mako-1.1.4-py2.py3-none-any.whl")
    version("1.0.4", sha256="fed99dbe4d0ddb27a33ee4910d8708aca9ef1fe854e668387a9ab9a90cbf9059", url="https://pypi.org/packages/7a/ae/925434246ee90b42e8ef57d3b30a0ab7caf9a2de3e449b876c56dcb48155/Mako-1.0.4.tar.gz")
    version("1.0.1", sha256="45f0869febea59dab7efd256fb451c377cbb7947bef386ff0bb44627c31a8d1c", url="https://pypi.org/packages/8e/a4/aa56533ecaa5f22ca92428f74e074d0c9337282933c722391902c8f9e0f8/Mako-1.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markupsafe@0.9.2:", when="@1.1.4:")
    # END DEPENDENCIES

