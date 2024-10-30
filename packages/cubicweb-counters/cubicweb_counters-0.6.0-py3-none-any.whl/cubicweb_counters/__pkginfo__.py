# pylint: disable=W0622
"""cubicweb-counters application packaging information"""

modname = "cubicweb_counters"
distname = "cubicweb-counters"

numversion = (0, 6, 0)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
author = "LOGILAB S.A. (Paris, FRANCE)"
author_email = "contact@logilab.fr"
description = "sequence/counter classes"
web = f"https://forge.extranet.logilab.fr/cubicweb/cubes/{distname}"

__depends__ = {
    "cubicweb[postgresql]": ">=4.0.0, < 5.0",
}
__recommends__ = {}

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python :: 3",
]
