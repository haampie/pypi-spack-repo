# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCurrentscape(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.12", sha256="b1bef26352f240d09e413d312deb06d212afe158de85c9dcae96e371968d1d9c", url="https://pypi.org/packages/dd/de/423d92aff7c18e418672db238a379e0f7b5379508daeb1854996916ac371/currentscape-1.0.12-py3-none-any.whl")
    version("1.0.11", sha256="167a237a8e1cc21111cf66414a2aaf7dc095baa91f129c0c17a81cfb3d517be9", url="https://pypi.org/packages/82/63/8209c700fc82a3c3724584222358926b0ef9cdd843258b26f030469ff7cc/currentscape-1.0.11-py3-none-any.whl")
    version("1.0.10", sha256="90875c823148e831b5aa4ba6cb1b5f17cf76a73f578ed0bee1238c329b8906fa", url="https://pypi.org/packages/d5/1f/a26c44f2fd1ac6fafd20809f32516f6d589080fc8635125c735240a48990/currentscape-1.0.10-py3-none-any.whl")
    version("1.0.9", sha256="a497cb6e08c1bc842e081c0017c6e4bdeffa838d55e97f864ca46fdf2701d1a2", url="https://pypi.org/packages/e8/8e/6fe36081e7ec4bb24a73737ece2f8995f46838d1b30db07252b545bee2b3/currentscape-1.0.9-py3-none-any.whl")
    version("1.0.8", sha256="1fa7c920618b76b752305d9e7b6ebd31578a17d092d3cab3748975cd3fc0e0b0", url="https://pypi.org/packages/be/cc/053de78ec620ad659ea050fc0b4e691f1b54e00c74b071dd4f9f289d5c33/currentscape-1.0.8-py3-none-any.whl")
    version("1.0.7", sha256="a18cbdcec6050d45320aa491ebbfe9ecfbbdb7217617379bc3365c9f7678de97", url="https://pypi.org/packages/b1/4e/8c51699cfcb4eff272565f35c903118ada2f269c3dd0e467fde177f3659f/currentscape-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="02acfb4b2b2aa15612d4a3a893e1398642bf26613a36ef08ae0abb394d102f28", url="https://pypi.org/packages/b0/2e/b5f66f8f714abc2b63a06865634e066d8c6b8b82fc2afba28e05085e4f89/currentscape-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="560da95a286132eaece3b9e203591cba85f888187e6b8322a2ca2b28c9256666", url="https://pypi.org/packages/47/10/2ed448ab3480d9a8fdc04da33a8a097993b8401bff9f9155e786741ca59e/currentscape-1.0.5-py3-none-any.whl")
    version("1.0.3", sha256="1b68487916e868fd0cb274eae5981f44792828da13a02f22502c09db07367630", url="https://pypi.org/packages/24/39/42145ecde42cd318e8bbe9ec3b783a04cbd62e3a5d40dff29eba7f03895f/currentscape-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="2d87d25c1062a42d7c273ef1d28a060bb53ddf175499c81a9914e3959b9e229f", url="https://pypi.org/packages/90/1b/b964d6ce8ac9a03976ec15b289ac3b8a124c8e719bd27e794fc15da3c41c/currentscape-1.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-palettable")
    # END DEPENDENCIES

