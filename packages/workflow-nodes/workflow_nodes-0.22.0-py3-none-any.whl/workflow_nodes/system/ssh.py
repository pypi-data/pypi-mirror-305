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
import click
from xmlhelpy import Integer
from xmlhelpy import option

from workflow_nodes.utils import missing_extra

from .main import system


@system.command()
@option("hostname", char="h", description="Hostname", required=True)
@option("port", char="P", description="Port", default=22, param_type=Integer)
@option("username", char="u", description="Username")
@option("password", char="p", description="Password")
@option("command", char="c", description="Command")
@option("blocking", char="b", description="Blocking channel", is_flag=True)
def ssh(hostname, port, username, password, command, blocking):
    """Establish a SSH connection and execute a command."""
    try:
        import paramiko
    except ImportError:
        missing_extra("ssh")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname,
        port=port,
        username=username,
        password=password,
    )

    if command:
        _stdin, stdout, _stderr = client.exec_command("echo $$; " + command)

        _stdin.close()
        _stderr.close()

        pid = stdout.readline()
        click.echo(f"Process-ID: {pid}", err=True)

        if blocking:
            click.echo("Blocking process", err=True)
            stdout.channel.recv_exit_status()
