import aidge_core
import shutil
import os
from pathlib import Path
from .utils import supported_operators, OPERATORS_REGISTRY
from . import ROOT_EXPORT


from aidge_core import ExportNode, generate_file



def export(export_folder: str,
           graph_view: aidge_core.GraphView,
           enable_python_binding: bool = True,
           ):
    export_folder_path = Path(export_folder)
    export_name = export_folder_path.name

    ### Creating export folder ###
    # Create export directory
    os.makedirs(export_folder, exist_ok=True)

    ### Cpy static files ###
    shutil.copytree(ROOT_EXPORT / "static/include",
                    export_folder_path / "include", dirs_exist_ok=True)
    shutil.copytree(ROOT_EXPORT / "static/cmake",
                    export_folder_path / "cmake", dirs_exist_ok=True)
    shutil.copyfile(ROOT_EXPORT / "static/CMakeLists.txt",
                    export_folder_path / "CMakeLists.txt")
    shutil.copyfile(ROOT_EXPORT / "static/version.txt",
                    export_folder_path / "version.txt")
    shutil.copyfile(ROOT_EXPORT / "static/README.md",
                    export_folder_path / "README.md")
    shutil.copyfile(ROOT_EXPORT / "static/main.cpp",
                    export_folder_path / "main.cpp")
    shutil.copyfile(ROOT_EXPORT / "static/export-config.cmake.in",
                    export_folder_path / f"{export_name}-config.cmake.in")

    # Create project_name file
    with open(export_folder_path / "project_name.txt", "w") as f:
        f.write(export_name)

    # Add files related to python binding if
    if enable_python_binding:
        os.makedirs(export_folder_path / "python_binding", exist_ok=True)
        generate_file(
            export_folder_path / "python_binding/pybind.cpp",
            ROOT_EXPORT / "templates/pybind.jinja",
            name=export_name,
        )
        # TODO: Add a main.py file ?

    ### Generating an export for each nodes and dnn file ###
    list_configs = []  # List of headers to include in dnn.cpp to access attribute and parameters
    list_actions = []  # List of string to construct graph
    set_operator = set()
    # Queue of Aidge nodes to explore, guarantee a topological exploration of the graph
    open_nodes = list(graph_view.get_input_nodes())
    # List of Aidge nodes already explored
    closed_nodes = []

    while open_nodes:
        node = open_nodes.pop(0)
        if node in closed_nodes:
            continue  # Node already converted, moving on ...
        parents_not_converted = False
        # Check all parents have been converted
        for parent in node.get_parents():
            if parent is not None and \
                    parent not in closed_nodes:
                # If parents have not been converted, push back current node
                if not parents_not_converted:
                    open_nodes.insert(0, node)
                    parents_not_converted = True
                # Add to the stack the not converted parent as next node to convert
                open_nodes.insert(0, parent)
        if parents_not_converted:

            continue
        # Next nodes to treat are children of current node
        open_nodes += list(node.get_children())

        if node.type() in supported_operators():
            set_operator.add(node.type())
            op = OPERATORS_REGISTRY[node.type()](node)

            # TODO: list_configs and list_actions don't need to be passed by argument
            # Export the configuration
            list_configs = op.export(export_folder_path, list_configs)

            # Add forward kernel
            list_actions = op.forward(list_actions)
        else:
            raise RuntimeError(f"Operator: {node.type()} is not supported")
        closed_nodes.append(node)
    # Generate full dnn.cpp
    aidge_core.generate_file(
        export_folder_path / "src/dnn.cpp",
        ROOT_EXPORT / "templates/dnn.jinja",
        headers=list_configs,
        operators=set_operator,
        actions=list_actions,
    )
