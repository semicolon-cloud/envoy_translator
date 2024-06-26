# Copyright (C) 2019 Catalyst Cloud Ltd
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

from confspirator import groups
from confspirator import fields
from confspirator import types


config_group = groups.ConfigGroup("identity")

config_group.register_child_config(
    fields.IntConfig(
        "token_cache_time",
        help_text="Cache time for Keystone Tokens in the Keystone Middleware.",
        default=-1,
        required=True,
        required_for_tests=False,
    )
)

_auth_group = groups.ConfigGroup("auth")
_auth_group.register_child_config(
    fields.StrConfig(
        "username",
        help_text="Username for Adjutant Keystone admin user.",
        required=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.StrConfig(
        "password",
        help_text="Password for Adjutant Keystone admin user.",
        required=True,
        secret=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.StrConfig(
        "project_name",
        help_text="Project name for Adjutant Keystone admin user.",
        required=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.StrConfig(
        "project_domain_id",
        help_text="Project domain id for Adjutant Keystone admin user.",
        default="default",
        required=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.StrConfig(
        "user_domain_id",
        help_text="User domain id for Adjutant Keystone admin user.",
        default="default",
        required=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.URIConfig(
        "auth_url",
        help_text="Keystone auth url that Adjutant will use.",
        schemes=["https", "http"],
        required=True,
        required_for_tests=False,
    )
)
_auth_group.register_child_config(
    fields.StrConfig(
        "interface",
        help_text="Keystone endpoint interface type.",
        default="public",
        required=True,
    )
)
config_group.register_child_config(_auth_group)
