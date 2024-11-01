from typing import Any, Dict, List, Tuple

from typing import Set
from typing import overload
import numpy

class FermionOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex]) -> None:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[List[Tuple[int,bool]],str],complex]]:
        """
        Get the data of the fermion operator.
        
        Args:
             None
        
        Returns:
             A data structure representing the fermion operator's data.
        
        """
        ...

    def error_threshold(self) -> float:
        """
        Retrieve the error threshold for the fermion operator.
        
        Args:
             None
        
        Returns:
             A double representing the error threshold.
        
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the fermion operator is empty.
        
        Args:
             None
        
        Returns:
             A boolean indicating whether the operator is empty.
        
        """
        ...

    def normal_ordered(self) -> FermionOperator:
        """
        Returns the normal ordered form of the fermion operator.
        
        Args:
             None
        
        Returns:
             A new FermionOperator in normal ordered form.
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        Set the error threshold for the fermion operator.
        
        Args:
             threshold: A double representing the new error threshold.
        
        Returns:
             None.
        
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_string(self) -> str:
        """
        Convert the fermion operator to a string representation.
        
        Args:
             None
        
        Returns:
             A string representing the fermion operator.
        
        """
        ...

    @overload
    def __add__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __iadd__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    def __imul__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    def __isub__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...


class PauliOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, matrix: numpy.ndarray[numpy.float64[m,n]], is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    @overload
    def __init__(self, key: str, value: complex, is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    @overload
    def __init__(self, pauli_map: Dict[str,complex], is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    def dagger(self) -> PauliOperator:
        """
        Returns the adjoint (dagger) of the Pauli operator.
        
        This function computes and returns the adjoint of the current operator.
        
        Args:
             None
        
        Returns:
             A new instance of PauliOperator representing the adjoint.
        
        """
        ...

    def data(self) -> List[Tuple[Tuple[Dict[int,str],str],complex]]:
        """
        Retrieves the data representation of the Pauli operator.
        
        This function returns the internal data structure representing the operator.
        
        Args:
             None
        
        Returns:
             The data representation of the Pauli operator.
        
        """
        ...

    def error_threshold(self) -> float:
        """
        Retrieves the current error threshold for the operator.
        
        This function returns the error threshold value set for the operator.
        
        Args:
             None
        
        Returns:
             A double representing the error threshold.
        
        """
        ...

    def getMaxIndex(self) -> int:
        """
        """
        ...

    def get_max_index(self) -> int:
        """
        Retrieves the maximum qubit index used in the operator.
        
        This function returns the highest index of qubits present in the Pauli operator.
        
        Args:
             None
        
        Returns:
             An integer representing the maximum qubit index.
        
        """
        ...

    def isAllPauliZorI(self) -> bool:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_all_pauli_z_or_i(self) -> bool:
        """
        Checks if all terms are either Pauli Z or identity.
        
        This function evaluates whether all components of the operator are either Pauli Z or the identity operator.
        
        Args:
             None
        
        Returns:
             A boolean indicating if all terms are Pauli Z or identity (true) or not (false).
        
        """
        ...

    def is_empty(self) -> bool:
        """
        Checks if the Pauli operator is empty.
        
        This function determines whether the current operator contains any terms.
        
        Args:
             None
        
        Returns:
             A boolean indicating if the operator is empty (true) or not (false).
        
        """
        ...

    def reduce_duplicates(self) -> None:
        """
        Reduces duplicates in the Pauli operator representation.
        
        This function modifies the operator to remove duplicate elements.
        
        Args:
             None
        
        Returns:
             None.
        
        """
        ...

    def remapQubitIndex(self, arg0: Dict[int,int]) -> PauliOperator:
        """
        """
        ...

    def remap_qubit_index(self, arg0: Dict[int,int]) -> PauliOperator:
        """
        Remaps the qubit indices in the operator.
        
        This function updates the qubit indices according to the provided mapping.
        
        Args:
             const std::map<int, int>& index_map: A mapping of old indices to new indices.
        
        Returns:
             None.
        
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        Sets the error threshold for the operator.
        
        This function allows the user to define a new error threshold value.
        
        Args:
             double threshold: The new error threshold value to set.
        
        Returns:
             None.
        
        """
        ...

    def toHamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_hamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        Converts the Pauli operator to its Hamiltonian representation.
        
        This function transforms the current Pauli operator into its corresponding Hamiltonian form.
        
        Args:
             None
        
        Returns:
             A new Hamiltonian representation of the operator.
        
        """
        ...

    def to_matrix(self) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Converts the Pauli operator to a matrix form.
        
        This function transforms the Pauli operator into its matrix representation.
        
        Args:
             None
        
        Returns:
             An EigenMatrixX representing the matrix form of the operator.
        
        """
        ...

    def to_string(self) -> str:
        """
        Converts the Pauli operator to a string representation.
        
        This function provides a human-readable format of the Pauli operator.
        
        Args:
             None
        
        Returns:
             A string representing the Pauli operator.
        
        """
        ...

    @overload
    def __add__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __iadd__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    def __imul__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    def __isub__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...


class VarFermionOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex_var]) -> None:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[List[Tuple[int,bool]],str],complex_var]]:
        """
        Get the data of the variable fermion operator.
        
        Args:
             None
        
        Returns:
             A data structure representing the variable fermion operator's data.
        
        """
        ...

    def error_threshold(self) -> float:
        """
        Retrieve the error threshold for the variable fermion operator.
        
        Args:
             None
        
        Returns:
             A double representing the error threshold.
        
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the variable fermion operator is empty.
        
        Args:
             None
        
        Returns:
             A boolean indicating whether the operator is empty.
        """
        ...

    def normal_ordered(self) -> VarFermionOperator:
        """
        Returns the normal ordered form of the variable fermion operator.
        
        Args:
             None
        
        Returns:
             A new VarFermionOperator in normal ordered form.
        
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        Set the error threshold for the variable fermion operator.
        
        Args:
             threshold (double): A double representing the new error threshold.
        
        Returns:
             None.
        
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_string(self) -> str:
        """
        Convert the variable fermion operator to a string representation.
        
        Args:
             None
        
        Returns:
             A string representing the variable fermion operator.
        
        """
        ...

    @overload
    def __add__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __iadd__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    def __imul__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    def __isub__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...


class VarPauliOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex_var]) -> None:
        """
        """
        ...

    def dagger(self) -> VarPauliOperator:
        """
        Return the adjoint (dagger) of the Pauli operator.
        
        Args:
             None
        
        Returns:
             A new VarPauliOperator representing the adjoint.
        
        """
        ...

    def data(self) -> List[Tuple[Tuple[Dict[int,str],str],complex_var]]:
        """
        Get the data of the variable Pauli operator.
        
        Args:
             None
        
        Returns:
             A data structure representing the variable Pauli operator's data.
        
        """
        ...

    @overload
    def error_threshold(self) -> float:
        """
        """
        ...

    @overload
    def error_threshold(self) -> float:
        """
        Retrieve the error threshold for the variable Pauli operator.
        
        Args:
             None
        
        Returns:
             A double representing the error threshold.
        
        """
        ...

    def getMaxIndex(self) -> int:
        """
        """
        ...

    def get_maxIndex(self) -> int:
        """
        Retrieve the maximum index used in the Pauli operator.
        
        Args:
             None
        
        Returns:
             An integer representing the maximum index.
        
        """
        ...

    def isAllPauliZorI(self) -> bool:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_all_pauli_z_or_i(self) -> bool:
        """
        Check if the operator consists only of Pauli Z or identity.
        
        Args:
             None
        
        Returns:
             A boolean indicating if all operators are Z or I.
        
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the variable Pauli operator is empty.
        
        Args:
             None
        
        Returns:
             A boolean indicating whether the operator is empty.
        
        """
        ...

    def remapQubitIndex(self, arg0: Dict[int,int]) -> VarPauliOperator:
        """
        """
        ...

    def remap_qubit_index(self, arg0: Dict[int,int]) -> VarPauliOperator:
        """
        Remap the qubit indices of the variable Pauli operator.
        
        Args:
             A mapping of old indices to new indices.
        
        Returns:
             None.
        
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        Set the error threshold for the variable Pauli operator.
        
        Args:
             threshold (double): A double representing the new error threshold.
        
        Returns:
             None.
        
        """
        ...

    def toHamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_hamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        Convert the variable Pauli operator to a Hamiltonian representation.
        
        Args:
             None
        
        Returns:
             A Hamiltonian representation of the operator.
        
        """
        ...

    def to_string(self) -> str:
        """
        Convert the variable Pauli operator to a string representation.
        
        Args:
             None
        
        Returns:
             A string representing the variable Pauli operator.
        
        """
        ...

    @overload
    def __add__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __iadd__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    def __imul__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    def __isub__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...


class complex_var:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0, arg1) -> None:
        """
        """
        ...

    def imag(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def real(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def __add__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __mul__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __sub__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __truediv__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...


def i(arg0: int) -> PauliOperator:
    """
    Construct a Pauli I operator.
    
    Args:
         index (int): Pauli operator index.
    
    Returns:
         Pauli operator I.
    
    """
    ...

def matrix_decompose_hamiltonian(arg0: numpy.ndarray[numpy.float64[m,n]]) -> PauliOperator:
    """
    Decompose matrix into Hamiltonian.
    
    Args:
         matrix (EigenMatrixX): 2^N * 2^N double matrix.
    
    Returns:
         Decomposed Hamiltonian representation.
    
    """
    ...

def trans_Pauli_operator_to_vec(arg0: PauliOperator) -> List[float]:
    """
    Transform Pauli operator to vector.
    
    Args:
         operator: Input Pauli operator to be transformed.
    
    Returns:
         Vector equivalent of the input Pauli operator.
    
    """
    ...

def trans_vec_to_Pauli_operator(arg0: List[float]) -> PauliOperator:
    """
    Transform vector to Pauli operator.
    
    Args:
         vector: Input vector to be transformed.
    
    Returns:
         Pauli operator equivalent of the input vector.
    
    """
    ...

def x(index: int) -> PauliOperator:
    """
    Construct a Pauli X operator.
    
    Args:
         index (int): Pauli operator index.
    
    Returns:
         Pauli operator X.
    
    """
    ...

def y(arg0: int) -> PauliOperator:
    """
    Construct a Pauli Y operator.
    
    Args:
         index (int): Pauli operator index.
    
    Returns:
         Pauli operator Y.
    
    """
    ...

def z(arg0: int) -> PauliOperator:
    """
    Construct a Pauli Z operator.
    
    Args:
         index (int): Pauli operator index.
    
    Returns:
         Pauli operator Z.
    
    """
    ...

