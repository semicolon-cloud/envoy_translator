# Copyright (C) 2015 Catalyst IT Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

from confspirator.exceptions import InvalidConf


def management_command():
    """Entry-point for the 'adjutant' command-line admin utility."""
    import os
    import sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "envoy_translator.settings")

    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line(sys.argv)
    except InvalidConf as e:
        print("This command requires a valid config, see following errors:")
        print(json.dumps(e.errors["adjutant"], indent=2))
        sys.exit(1)
