# Filter-MSMARCO
# @File:   unit.py
# @Time:   22/11/2021
# @Author: Gabriel O.

from pathlib import Path

from src.io.file_operations import load_skill
import pandas as pd


def main():
    skill_path = Path(__file__).parent / "../results/skill-Amazônia-Azul2.json"
    skill = load_skill(skill_path.resolve().as_posix())
    df = pd.DataFrame(skill["dialog_nodes"])

    dup = df[df.dialog_node.duplicated()]
    empty = df[df.dialog_node.isna()]
    is_self_parent = df[df.dialog_node == df.parent]
    is_self_sibling = df[df.dialog_node == df.previous_sibling]

    print("Running tests...")
    assert dup.shape[0] == 0, "There are nodes with duplicated dialog_node"
    assert empty.shape[0] == 0, "There are nodes without dialog_node"
    assert is_self_parent.shape[0] == 0, "There are nodes which are their own parent"
    assert (
        is_self_sibling.shape[0] == 0
    ), "There are nodes which are their own previous_sibling"
    print("Tests finished.")


if __name__ == "__main__":
    main()
