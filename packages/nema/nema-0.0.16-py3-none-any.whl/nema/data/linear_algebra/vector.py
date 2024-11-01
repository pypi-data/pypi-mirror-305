from dataclasses import dataclass
import numpy as np

from nema.data.data_properties import DataProperties


@dataclass
class FloatVector(DataProperties):
    vector: np.array

    @property
    def data_type(self):
        return "FLOAT_VECTOR.V0"

    def __nema_marshall__(self):
        return {"vector": self.value.tolist()}

    @classmethod
    def __nema_unmarshall__(cls, data: dict):
        return cls(value=np.array(data["value"]))


@dataclass
class FloatMatrix(DataProperties):
    matrix: np.ndarray

    @property
    def data_type(self):
        return "FLOAT_MATRIX.V0"

    def __nema_marshall__(self):
        return {"matrix": self.matrix.tolist()}

    @classmethod
    def __nema_unmarshall__(cls, data: dict):
        return cls(value=np.array(data["matrix"]))
