##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyElasticsearchDsl(PythonPackage):
    version("7.4.0", sha256="046ea10820b94c075081b528b4526c5bc776bda4226d702f269a5f203232064b", url="https://pypi.org/packages/12/1e/c59c873cc63643b277e80efec0c5a9714798e4716ca43e97fba35b94e811/elasticsearch_dsl-7.4.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-elasticsearch@7", when="@7.2:7")
        depends_on("py-python-dateutil", when="@7.2:")
        depends_on("py-six", when="@7.2:7")

