# Copyright 2021 Karlsruhe Institute of Technology
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

import click
from xmlhelpy import Choice
from xmlhelpy import option

from .main import system


@system.command()
@option(
    "compresstarget",
    char="c",
    description="Folder or file to be compressed.",
    required=True,
)
@option(
    "outputpath",
    char="p",
    description="Name and path of target folder. Defaults to current folder and name"
    " 'compressedfile'",
)
@option(
    "compressiontype",
    char="t",
    param_type=Choice(["targz", "zip"]),
    description="Type of compression",
    default="zip",
)
@option("force_overwrite", char="o", is_flag=True)
def compress(compresstarget, outputpath, compressiontype, force_overwrite):
    """Wrapper node for compressing files of folders."""
    if outputpath:
        if compressiontype == "targz":
            if ".targz" in outputpath:
                outputpath = outputpath[: -(len(compressiontype) + 1)]
            elif ".tar.gz" in outputpath:
                outputpath = outputpath[:-7]
            compressiontype = "gztar"
        elif ".zip" in outputpath:
            outputpath = outputpath[: -(len(compressiontype) + 1)]
        tpath = outputpath
    else:
        tpath = os.path.join(os.getcwd(), "compressedfile")

    compresstarget = os.path.realpath(compresstarget)
    compressitem = os.path.basename(compresstarget)
    compresspath = os.path.dirname(compresstarget)

    if force_overwrite or not os.path.isfile(tpath + "." + compressiontype):
        shutil.make_archive(tpath, compressiontype, compresspath, compressitem)
        click.echo(
            f"Created {compressiontype} file"
            f" '{os.path.basename(tpath)}.{compressiontype}' from the folder/file"
            f" '{compressitem}' on path '{compresspath}'.",
            err=True,
        )
    elif os.path.isfile(tpath + "." + compressiontype):
        click.echo(
            "File already exists and won't be overwritten! If you want to overwrite it,"
            " please use the flag 'force_overwrite'.",
            err=True,
        )
