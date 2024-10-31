from typing import Union, Any, Dict, List, Optional, Tuple
from copy import deepcopy
from collections.abc import Mapping

from .typing import NOTSET

def update_nested_dict(d: Dict, u: Dict) -> Dict:
    """
    Recursively updates nested dictionaries.

    Parameters
    ----------
    d : Dict
        The dictionary to be updated.
    u : Dict
        The dictionary containing updates.

    Returns
    -------
    Dict
        The updated dictionary.
    """
    for k, v in u.items():
        if isinstance(d.get(k), Mapping) and isinstance(v, Mapping):
            d[k] = update_nested_dict(d[k], v)
        else:
            d[k] = v
    return d

def _populate_tree(tree: 'DataTree', data: Dict[str, Any],
                   current_depth: int = 0, max_depth: int = -1):
    for key, value in data.items():
        if isinstance(value, dict) and (max_depth == -1 or current_depth < max_depth):
            subtree = tree.new()
            _populate_tree(subtree, value, current_depth + 1, max_depth)
            tree.set(key, subtree)
        else:
            tree.set(key, value)

TreeLikeType = Union["DataTree", Dict[str, Any]]

def _recursive_merge(a: "DataTree", b: Optional[TreeLikeType] = None) -> Dict[str, Any]:
    # force conversion to a data tree of the same kind
    b = a.new() | b
    return update_nested_dict(a.dict(nested=False), b.dict(nested=False))
    
class DataTree:
    """
    A tree-like data structure with hierarchical key-value storage, 
    supporting nested namespaces and flexible key lookups.

    Attributes
    ----------
    separator : str
        The default separator used to split keys and namespaces.
    _data : Dict[str, Any]
        Internal storage for key-value pairs and sub-namespaces.
    """

    def __init__(self, data: Optional[TreeLikeType] = None,
                 max_depth: int = -1, copy: bool = True, separator: str = '.'):
        """
        Initializes the DataTree instance.

        Parameters
        ----------
        data : dict or DataTree, optional
            The data to initialize the DataTree with (default is None).
        max_depth : int, optional
            The maximum depth for namespace nesting (default is -1, meaning no limit).
        copy : bool
            Whether to create a deep copy of the data (default is True).
        separator : str, optional
            The separator to use for splitting keys and namespaces (default is '.').
        """
        self._separator: str = separator
        self._max_depth: int = max_depth
        self._data: Dict[str, Any] = {}
        self.update(data)

    def __setitem__(self, key: str, value: Any) -> None:
        """Sets a value for the given key."""
        self.set(key, value)

    def __getitem__(self, key: str) -> Any:
        """Gets the value for the given key."""
        value = self.get(key, NOTSET)
        if value is NOTSET:
            raise KeyError(f'key "{key}" not found in tree')
        return value

    def __contains__(self, key: str) -> bool:
        """Checks if the key exists in the tree."""
        return self.get(key, NOTSET) is not NOTSET

    def __copy__(self) -> 'DataTree':
        """
        Creates a shallow copy of the DataTree.
        """
        return self.copy(deep=False)

    def __deepcopy__(self, memo) -> 'DataTree':
        """
        Creates a deep copy of the tree.
        """
        return self.copy(deep=True)

    def __or__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        """
        Combines two DataTree instances using the | operator.
        """
        result = self.copy()
        result.update(other)
        return result

    def __ior__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        self.update(other)
        return self

    def __ror__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        if not isinstance(other, DataTree):
            other = self.cast(other)
        return other.__or__(self)

    def __and__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        merged_data = _recursive_merge(self, other)
        result = self.new()
        for key, value in merged_data.items():
            result.set(key, value)
        return result

    def __iand__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        merged_data = _recursive_merge(self, other)
        for key, value in merged_data.items():
            self.set(key, value)
        return self

    def __rand__(self, other: Optional[TreeLikeType] = None) -> 'DataTree':
        if not isinstance(other, DataTree):
            other = self.cast(other)
        return other.__and__(self)

    def __repr__(self) -> str:
        """String representation of the tree object."""
        return f"<DataTree: {self._data}>"
        
    def _split_key(self, key: str, domain: Optional[str] = None) -> Tuple[List[str], str]:
        """
        Splits a full key into namespaces and the final key part.
        """
        if domain:
            key = f'{domain}{self._separator}{key}'
        *namespaces, key = key.split(self._separator)
        return namespaces, key

    def _split_domain(self, domain: Optional[str] = None) -> List[str]:
        """
        Splits the domain into individual namespaces.

        Parameters
        ----------
        domain : Optional[str], optional
            The domain to split (default is None).

        Returns
        -------
        List[str]
            A list of namespaces from the domain.
        """
        return domain.split(self._separator) if domain else []

    def _domain_depth(self, domain: Optional[str] = None) -> int:
        return domain.count(self._separator) if domain else 0

    def new(self, **kwargs) -> 'DataTree':
        """Creates a new empty instance of the data tree."""
        kwargs.setdefault('max_depth', self._max_depth)
        kwargs.setdefault('separator', self._separator)
        return type(self)(**kwargs)

    def traverse(self, *namespaces: str, create: bool = False) -> Optional['DataTree']:
        """
        Traverses through namespaces to reach the target subtree.
        """
        tree = self
        for namespace in namespaces:
            subtree = tree._data.get(namespace, NOTSET)
            if not isinstance(subtree, DataTree):
                if create:
                    subtree = tree.new()
                    tree._data[namespace] = subtree
                else:
                    return None
            tree = subtree
        return tree

    def traverse_domain(self, domain: Optional[str] = None, create: bool = False) -> Optional['DataTree']:
        """
        Traverses through a domain's namespaces.

        Parameters
        ----------
        domain : Optional[str], optional
            The domain to traverse (default is None).
        create : bool, optional
            Whether to create missing namespaces (default is False).

        Returns
        -------
        Optional[DataTree]
            The tree at the end of the traversal or None.
        """
        namespaces = self._split_domain(domain)
        return self.traverse(*namespaces, create=create)

    def update(self, data: Optional[TreeLikeType] = None) -> None:
        """
        Updates the tree with the given data.
        """
        if data is None:
            data = {}

        if isinstance(data, DataTree):
            self._data.update(data._data)
        elif isinstance(data, dict):
            _populate_tree(self, data, 0, self._max_depth)
        else:
            raise ValueError(f'invalid data format: {type(data)}')

    def clear(self) -> None:
        self._data = {}

    def copy(self, deep: bool = False) -> 'DataTree':
        """
        Copies the DataTree. If deep is True, it performs a deep copy; otherwise, a shallow copy.
        """
        new_tree = self.new()
        new_tree._data = deepcopy(self._data) if deep else self._data.copy()
        return new_tree

    def set(self, key: str, value: Any, domain: Optional[str] = None) -> None:
        """
        Sets a value in the DataTree under the given key.
        """
        namespaces, key = self._split_key(key, domain=domain)
        tree = self.traverse(*namespaces, create=True)
        if tree is not None:
            tree._data[key] = value

    def get(self, key: str, default: Any = None, domain: Optional[str] = None) -> Any:
        """
        Gets the value for a key in the DataTree.
        """
        namespaces, key = self._split_key(key, domain=domain)
        tree = self.traverse(*namespaces, create=False)
        return tree._data.get(key, default) if tree else default

    def cast(self, data: Optional[TreeLikeType] = None) -> 'TreeData':
        return self.new() | data

    def data(self, domain: Optional[str] = None, copy: bool = False) -> Optional[Dict[str, Any]]:
        """
        Retrieves all key-value pairs in the specified domain.

        Parameters
        ----------
        domain : Optional[str], optional
            The domain to retrieve data from (default is None).

        Returns
        -------
        Optional[Dict[str, Any]]
            A dictionary of key-value pairs or None.
        """
        tree = self.traverse_domain(domain, create=False)
        if tree is None:
            return None
        result = {k: v for k, v in tree._data.items() if not isinstance(v, DataTree)}
        return deepcopy(result) if copy else result

    @property
    def namespaces(self) -> List[str]:
        """Lists all namespaces within the current tree."""
        return [k for k, v in self._data.items() if isinstance(v, DataTree)]

    def set_domain_data(self, domain: str, data: Union['DataTree', Dict[str, Any]], copy: bool = True) -> None:
        """
        Sets data for the specified domain in the DataTree.
        """
        data_tree = type(self)(data, max_depth=0, copy=copy, separator=self._separator)
        self.set(domain, data_tree)

    def merge_domain_data(self, source: str, target: Optional[str] = None) -> Dict[str, Any]:
        """
        Merges data from the source domain into the target domain.

        Parameters
        ----------
        source : str
            The source domain from which to merge data.
        target : Optional[str], optional
            The target domain where the data will be merged (default is None).

        Returns
        -------
        Dict[str, Any]
            The merged dictionary.
        """
        source_data = self.data(source, copy=True)
        if source_data is None:
            raise ValueError(f'domain not found: {source}')
        target_data = self.data(target, copy=True)
        if target_data is None:
            raise ValueError(f'domain not found: {target}')
        return update_nested_dict(target_data, source_data)

    def chain(self, *sources, max_depth: int = 0, 
              recursive_update: bool = True) -> 'DataTree':
        tree = self.new(max_depth=max_depth)
        for source in sources:
            if isinstance(source, str):
                source_tree = self.traverse_domain(source)
                if source_tree is None:
                    raise ValueError(f'invalid domain: {source}')
            else:
                source_tree = source
            if recursive_update:
                tree &= source_tree
            else:
                tree |= source_tree
        return tree

    def dict(self, nested: bool = False, separator: Optional[str] = None) -> Dict[str, Any]:
        """
        Converts the data tree into a dictionary.
        """
        result = {}
        data = deepcopy(self._data)
        if nested:
            for key, value in data.items():
                if isinstance(value, DataTree):
                    result[key] = value.dict(nested=True)
                else:
                    result[key] = value
        else:
            separator = separator or self._separator
            for key, value in data.items():
                if isinstance(value, DataTree):
                    subdict = value.dict(nested=False, separator=separator)
                    for subkey, subvalue in subdict.items():
                        result[f'{key}{separator}{subkey}'] = subvalue
                else:
                    result[key] = value
        return result