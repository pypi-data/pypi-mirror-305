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
from workflow_nodes.main import workflow_nodes


@workflow_nodes.group()
def system():
    """System wrapper tools."""


# pylint: disable=unused-import


from .awk import awk
from .bc import bc
from .cat import cat
from .chmod import chmod
from .compress import compress
from .cp import cp
from .echo import echo
from .ls import ls
from .mkdir import mkdir
from .mv import mv
from .paste import paste
from .rm import rm
from .scp import scp
from .sed import sed
from .sleep import sleep
from .sort import sort
from .ssh import ssh
from .unpack import unpack
from .wc import wc
