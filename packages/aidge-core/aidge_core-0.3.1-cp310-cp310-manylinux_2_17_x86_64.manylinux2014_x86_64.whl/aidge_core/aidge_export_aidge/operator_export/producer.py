from aidge_core.aidge_export_aidge.utils import operator_register
from aidge_core.aidge_export_aidge import ROOT_EXPORT
from aidge_core import dtype, ExportNode, generate_file, generate_str
import numpy as np
from pathlib import Path

# Convert aidge datatype to C++ type
datatype_converter = {
    dtype.float64 : "double",
    dtype.float32 : "float",
    dtype.float16 : "half_float::half",
    dtype.int8    : "int8_t",
    dtype.int16   : "int16_t",
    dtype.int32   : "int32_t",
    dtype.int64   : "int64_t",
    dtype.uint8   : "uint8_t",
    dtype.uint16  : "uint16_t",
    dtype.uint32  : "uint32_t",
    dtype.uint64  : "uint64_t"
}


@operator_register("Producer")
class Producer(ExportNode):
    """
    If there is a standardization of the export operators
    then this class should be just a inheritance of ProducerCPP
    """
    def __init__(self, node):
        super().__init__(node)
        child, in_idx = self.node.output(0)[0]
        self.tensor_name = f"{child.name()}_{in_idx}"
        self.values = np.array(self.operator.get_output(0))

    def export(self, export_folder:Path, list_configs:list):
        assert(len(self.node.output(0)) == 1)

        include_path = f"parameters/{self.tensor_name}.hpp"
        filepath = export_folder / f"include/{include_path}"

        aidge_tensor = self.operator.get_output(0)
        aidge_type = aidge_tensor.dtype()
        if aidge_type in datatype_converter:
            datatype = datatype_converter[aidge_type]
        else:
            raise RuntimeError(f"No conversion found for data type {aidge_type}.")
        generate_file(
            filepath,
            ROOT_EXPORT / "templates/parameter.jinja",
            dims = aidge_tensor.dims(),
            data_t = datatype, # TODO : get data from producer
            name = self.tensor_name,
            values = str(aidge_tensor)
        )
        list_configs.append(include_path)
        return list_configs

    def forward(self, list_actions:list):
        list_actions.append(generate_str(
            ROOT_EXPORT / "templates/graph_ctor/producer.jinja",
            name=self.name,
            tensor_name=self.tensor_name,
            **self.attributes
        ))
        return list_actions
