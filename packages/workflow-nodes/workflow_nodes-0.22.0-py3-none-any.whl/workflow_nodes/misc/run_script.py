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
import os
import shutil
import subprocess
import sys
from pathlib import Path
from shlex import split

import click
from xmlhelpy import argument
from xmlhelpy import option

from .main import misc


@misc.command()
@argument("arg0", description="Executable shell script")
@option(
    "arguments",
    char="a",
    description="Arguments to run the shell script with. Multiple arguments will be"
    " split according to the specified separator",
)
@option(
    "separator",
    char="s",
    description="Separator used to split multiple arguments",
    default=" ",
)
@option(
    "execute-in",
    char="e",
    description="Overrides the path where the script will be executed (CWD)",
)
@option(
    "interpreter",
    char="i",
    description="Use an interpreter command to run the script, e.g. 'bash -c'",
)
@option(
    "ignore-exitcode",
    description="Ignore the exit code and always exit with success (code 0)",
    is_flag=True,
)
def run_script(arg0, arguments, separator, execute_in, interpreter, ignore_exitcode):
    """Run a shell script."""
    path = Path(arg0).expanduser()
    cwd = os.getcwd()

    if not shutil.which(path) and not interpreter:
        if shutil.which(path, path=cwd):
            path = f"./{path}"
        else:
            click.echo(
                "The specified program or script can not be found, or is not an"
                f" executable file:\n\t{path}"
            )
            sys.exit(1)

    click.echo(f"Running {path}...", err=True)
    cmd = [str(path)]

    if separator.strip() == "":
        separator = " "
    else:
        separator = separator.strip()

    if arguments:
        if separator == " ":
            cmd += split(arguments)
        else:
            cmd += arguments.split(separator)

    if interpreter:
        cmd = interpreter.split(" ") + cmd
    if execute_in:
        exec_dir = str(Path(execute_in).expanduser())
        exit_code = subprocess.run(cmd, cwd=exec_dir).returncode
    else:
        exit_code = subprocess.run(cmd).returncode

    if ignore_exitcode:
        sys.exit(0)
    else:
        sys.exit(exit_code)
