from aidge_core.aidge_export_aidge.utils import operator_register, parse_node_input
from aidge_core import ExportNode, generate_str
from aidge_core.aidge_export_aidge import ROOT_EXPORT
from pathlib import Path

@operator_register("ReLU")
class ReLU(ExportNode):
    def __init__(self, node):
        super().__init__(node)

    def export(self, export_folder:Path, list_configs:list):
        return list_configs

    def forward(self, list_actions:list):
        list_actions.append(generate_str(
            ROOT_EXPORT / "templates/graph_ctor/relu.jinja",
            name=self.name,
            inputs=parse_node_input(self.node.inputs()),
            **self.attributes
        ))
        return list_actions
