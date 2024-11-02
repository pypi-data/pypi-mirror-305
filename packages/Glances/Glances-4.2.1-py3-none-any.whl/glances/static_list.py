#
# This file is part of Glances.
#
# SPDX-FileCopyrightText: 2022 Nicolas Hennion <nicolas@nicolargo.com>
#
# SPDX-License-Identifier: LGPL-3.0-only
#

"""Manage the Glances server static list."""

from socket import gaierror, gethostbyname

from glances.logger import logger

DEFAULT_COLUMNS = "system:hr_name,load:min5,cpu:total,mem:percent"


class GlancesStaticServer:
    """Manage the static servers list for the client browser."""

    _section = "serverlist"

    def __init__(self, config=None, args=None):
        # server_list is a list of dict (JSON compliant)
        # [ {'key': 'zeroconf name', ip': '172.1.2.3', 'port': 61209, 'cpu': 3, 'mem': 34 ...} ... ]
        # Load server list from the Glances configuration file
        self._server_list = self.load_server_list(config)
        # Load columns to grab/display in the browser mode
        self._columns = self.load_columns(config)

    def load_server_list(self, config):
        """Load the server list from the configuration file."""
        server_list = []

        if config is None:
            logger.debug("No configuration file available. Cannot load server list.")
        elif not config.has_section(self._section):
            logger.warning(f"No [{self._section}] section in the configuration file. Cannot load server list.")
        else:
            logger.info(f"Start reading the [{self._section}] section in the configuration file")
            for i in range(1, 256):
                new_server = {}
                postfix = f'server_{str(i)}_'
                # Read the server name (mandatory)
                for s in ['name', 'port', 'alias']:
                    new_server[s] = config.get_value(self._section, f'{postfix}{s}')
                if new_server['name'] is not None:
                    # Manage optional information
                    if new_server['port'] is None:
                        new_server['port'] = '61209'
                    new_server['username'] = 'glances'
                    # By default, try empty (aka no) password
                    new_server['password'] = ''
                    try:
                        new_server['ip'] = gethostbyname(new_server['name'])
                    except gaierror as e:
                        logger.error("Cannot get IP address for server {} ({})".format(new_server['name'], e))
                        continue
                    new_server['key'] = new_server['name'] + ':' + new_server['port']

                    # Default status is 'UNKNOWN'
                    new_server['status'] = 'UNKNOWN'

                    # Server type is 'STATIC'
                    new_server['type'] = 'STATIC'

                    # Add the server to the list
                    logger.debug("Add server {} to the static list".format(new_server['name']))
                    server_list.append(new_server)

            # Server list loaded
            logger.info(f"{len(server_list)} server(s) loaded from the configuration file")
            logger.debug(f"Static server list: {server_list}")

        return server_list

    def load_columns(self, config):
        """Load columns definition from the configuration file.
        Read:   'system:hr_name,load:min5,cpu:total,mem:percent,sensors:value:Ambient'
        Return: [{'plugin': 'system', 'field': 'hr_name'},
                 {'plugin': 'load', 'field': 'min5'},
                 {'plugin': 'cpu', 'field': 'total'},
                 {'plugin': 'mem', 'field': 'percent'},
                 {'plugin': 'sensors', 'field': 'value', 'key': 'Ambient'}]
        """
        if config is None:
            logger.debug("No configuration file available. Cannot load columns definition.")
        elif not config.has_section(self._section):
            logger.warning(f"No [{self._section}] section in the configuration file. Cannot load columns definition.")

        columns_def = (
            config.get_value(self._section, 'columns')
            if config.get_value(self._section, 'columns')
            else DEFAULT_COLUMNS
        )

        return [dict(zip(['plugin', 'field', 'key'], i.split(':'))) for i in columns_def.split(',')]

    def get_servers_list(self):
        """Return the current server list (list of dict)."""
        return self._server_list

    def set_server(self, server_pos, key, value):
        """Set the key to the value for the server_pos (position in the list)."""
        self._server_list[server_pos][key] = value

    def get_columns(self):
        """Return the columns definitions"""
        return self._columns
