from pathlib import Path
import os
import sys
from typing import Optional


def evaluate_module(root_path: Path, workspace: Optional[Path] = None):
    """
    Recursively imports Python modules found within the specified root directory.

    :param root_path: The root directory from which to start searching for Python modules.
    :type root_path: Path
    :param workspace: The optional workspace directory. If provided, module paths will be relative to
                      this directory. Defaults to None.
    :type workspace: Optional[Path], optional
    """
    sys.path.append(root_path.__str__())
    for path, _, files in os.walk(root_path):
        path_o = Path(path).relative_to(workspace or root_path)
        for file in filter(lambda x: x.endswith(".py"), files):
            path_list = (
                path_o.__str__().strip("/").split("/")
                if path_o.__str__() != "."
                else []
            )
            file = file.rstrip(".py")
            path_list.extend(file.split("/"))
            __import__(".".join(path_list))
    sys.path.remove(root_path.__str__())
