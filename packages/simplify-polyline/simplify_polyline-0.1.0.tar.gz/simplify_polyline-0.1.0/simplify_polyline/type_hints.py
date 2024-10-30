"""Type hints for the package.

:author: Shay Hill
:created: 2023-03-18
"""

from typing import Annotated

import numpy as np
import numpy.typing as npt

# one polyline / polygon point
Vertex = Annotated[npt.NDArray[np.float64], "(d,)"]

# a polyline / polygon
Vertices = Annotated[npt.NDArray[np.float64], "(-1, d)"]

# numpy equivalent of a list of floats
Vector = Annotated[npt.NDArray[np.float64], (-1,)]
