# Copyright 2022 Karlsruhe Institute of Technology
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

import click
from xmlhelpy import argument
from xmlhelpy import option

from workflow_nodes.utils import check_binary

from .main import system


@system.command()
@argument("file", description="First file")
@option(name="recursive", description="Remove files recursively.", is_flag=True)
def rm(file, recursive):
    """Wrapper node for rm."""
    check_binary("rm")

    cmd = ["rm", file, "-f"]

    if recursive:
        cmd += ["-r"]

    # Do not write to stdout to keep output intact for piping.
    click.echo(" ".join(cmd), err=True)
    sys.exit(subprocess.run(cmd).returncode)
