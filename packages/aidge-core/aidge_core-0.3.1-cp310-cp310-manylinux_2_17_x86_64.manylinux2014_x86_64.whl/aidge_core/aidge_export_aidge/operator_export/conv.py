from aidge_core.aidge_export_aidge.utils import operator_register, parse_node_input
from aidge_core.aidge_export_aidge import ROOT_EXPORT
from aidge_core import ExportNode, generate_file, generate_str
from pathlib import Path

@operator_register("Conv")
class Conv(ExportNode):
    def __init__(self, node):
        super().__init__(node)

    def export(self, export_folder:Path, list_configs:list):
        include_path = f"attributes/{self.name}.hpp"
        filepath = export_folder / f"include/{include_path}"

        generate_file(
            filepath,
            ROOT_EXPORT / "templates/attributes/conv.jinja",
            name=self.name,
            **self.attributes
        )
        list_configs.append(include_path)
        return list_configs

    def forward(self, list_actions:list):
        list_actions.append(generate_str(
            ROOT_EXPORT /"templates/graph_ctor/conv.jinja",
            name=self.name,
            inputs=parse_node_input(self.node.inputs()),
            **self.attributes
        ))
        return list_actions
