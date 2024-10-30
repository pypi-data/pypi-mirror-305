from __future__ import annotations

from typing import Any
from ckan.plugins.interfaces import Interface


class ITransmute(Interface):
    """
    Add extra transmutators to be used in tsm_transmute action
    """

    def get_transmutators(self):
        """Return the transmutator functions provided by this plugin.

        Return a dictionary mapping transmutator names (strings) to
        transmutator functions. For example::

            {'tsm_title_case': tsm_title_case,
             'tsm_is_email': tsm_is_email}

        These transmutator functions would then be available for
        tsm_schema.
        """

    def get_transmutation_schemas(self) -> dict[str, dict[str, Any]]:
        """Return definitions of named schemas.

        These schemas can be reffered by name in code. In this way you can
        define static schema and apply in multiple places it to arbitrary data.
        """

        return {}
