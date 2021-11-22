# Filter-MSMARCO
# @File:   Node.py
# @Time:   21/11/2021
# @Author: Gabriel O.

from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import Dict, List

from src.utils.list_dict_operations import drop_empty


@dataclass
class Node:
    type: str = "standard"
    title: str = None
    output: Dict = None
    context: Dict = None
    conditions: str = None
    dialog_node: str = f"node_{uuid.uuid4().hex[:16]}"
    parent: str = None
    next_step: Dict[str, str] = None
    fonte: str = None
    intent: str = None
    modificador: str = None
    substantivo: str = None
    recipiente: str = None
    children: List["Node"] = None

    def add_child(self, node: Node):
        node.parent = self.dialog_node
        self.children.append(node)

    def to_list(self):
        return [node.to_dict() for node in self.children]

    def to_dict(self):
        return drop_empty(self.__dict__)
