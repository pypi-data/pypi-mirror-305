from typing import List, Tuple, Optional, Iterable
import numpy as np

class Tensor:
    """
        Class to repesent a Tensor.

        Attributes
        ----------
        data : List | Tuple | np.array | int | float
            Any Iterable 
        
        require_grad: Optional[bool] = False
            if `True` the gradient caculation is happend

        Methods
        ----------
        item:
            return the item of the tensor in list from.
        shape:
            return the shape of the tensor in tuple from.
        ndim:
            return the dim of the tensor in int from.

        add(other):
            other: Tensor | int | float
            add the Tensor or number.

        sub(other):
            other: Tensor | int | float
            sub the Tensor or number.

        mul(other):
            other: Tensor | int | float
            mul the Tensor or number.

        div(other):
            other: Tensor | int | float
            div the Tensor or number.

        pow(other):
            other: Tensor | int | float
            pow the Tensor or number.
            
        matmul(other):
            other: Tensor
            matrix multiplication of the Two valid shape tensor.
        
    """
    def __init__(self, data: List[float] | List[int] | Tuple[float] | Tuple[int] | Iterable | int| float, require_grad : Optional[bool] = False) -> None: ...
    """
            Function that initalize the tensor using List, Tuple, np.array, int or float
            Attributes
            ----------
            data : list | tuple | np.array | int | float
                Any Iterable 
                
            require_grad: Optional[bool] = False
                if `True` the gradient caculation is happend
    """
    @property
    def item(self) -> List[float]: ...
    @property
    def shape(self) -> Tuple[int]: ...
    @property
    def ndim(self) -> int: ...
    
    @property
    def grad(self, value:Tensor) -> Tensor: ...
    @property
    def require_grad(): ...
    
    def __add__(self, other:Tensor | int | float) -> Tensor: ...
    def __radd__(self, other:Tensor | int| float) -> Tensor: ...
    def __sub__(self, other:Tensor | int| float) -> Tensor: ...
    def __rsub__(self, other:Tensor | int| float) -> Tensor: ...
    def __mul__(self, other:Tensor | int| float) -> Tensor: ...
    def __rmul__(self, other:Tensor | int| float) -> Tensor: ...
    def __truediv__(self, other:Tensor | int| float) -> Tensor: ...
    def __rtruediv__(self, other:Tensor | int| float) -> Tensor: ...
    def __pow__(self, other:Tensor | int| float) -> Tensor: ...
    def __matmul__(self, other:Tensor) -> Tensor: ...

    
    def add(self, other:Tensor | int| float) -> Tensor: ...
    """
        Function for adding tensors or adding a scalar to a tensor.
        internally call the self + other
    """
    def sub(self, other:Tensor | int| float) -> Tensor: ...
    """
        Subtraction of a tensor or scalar from self.
        internally call the self - other
    """
    def mul(self, other:Tensor | int| float) -> Tensor: ...
    """
        Function for multiply tensors or multiply a scalar to a tensor.
        internally call the self * other
    """
    def div(self, other:Tensor | int| float) -> Tensor: ...
    """
        Function for do the power of any tenor
        internally call the self ** other
    """
    def pow(self, other:Tensor | int| float) -> Tensor: ...
    """
        Function for devide the two tensor and scaler
        interally call the self / other
    """ 
    def matmul(self, other:Tensor) -> Tensor: ...
    """
        Function for mutiply the N dim matrix
        internally call the self @ other
    """
    def transpose(self) -> Tensor: ...
    """
        Transpose the tensor for all batch.
    """
    def backward(self) -> None: ...
    """
        Caculate the backward pass when if require_grad is True
    """