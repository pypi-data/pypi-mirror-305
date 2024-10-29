# -----------------------------------------------------------------------------

from gitlabcis import __version__

import re

# -----------------------------------------------------------------------------


def test_gitlabcis_version():
    assert re.match(r'^\d+\.\d+\.\d+$', __version__) is not None
