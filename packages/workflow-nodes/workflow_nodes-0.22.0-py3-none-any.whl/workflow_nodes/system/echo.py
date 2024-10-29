# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import subprocess
import sys

from xmlhelpy import argument
from xmlhelpy import option

from workflow_nodes.utils import check_binary

from .main import system


@system.command()
@argument("message", description="Message to be echoed")
@option(
    "no-newline",
    char="n",
    is_flag=True,
    description="Do not output the trailing newline",
)
@option(
    "enable-backslash-escapes",
    char="e",
    is_flag=True,
    description="Enable interpretation of backslash escapes",
)
@option(
    "disable-backslash-escapes",
    char="E",
    is_flag=True,
    description="Disable interpretation of backslash escapes",
)
def echo(message, no_newline, enable_backslash_escapes, disable_backslash_escapes):
    """Wrapper node for echo."""
    check_binary("echo")

    cmd = ["echo"]

    if no_newline:
        cmd.append("-n")
    if enable_backslash_escapes:
        cmd.append("-e")
    if disable_backslash_escapes:
        cmd.append("-E")

    cmd.append(message)
    sys.exit(subprocess.run(cmd).returncode)
