from typing import List, Union, Optional, Dict, Callable, Any, Tuple
import os
import sys
import glob
import json
import shutil
import importlib
import importlib.util

import quickstats

__all__ = ["compile_macros", "get_all_macros",
           "set_verbosity", "get_root_version",
           "get_workspace_extensions",
           "get_workspace_extension_config",
           "add_macro", "remove_macro",
           "load_corelib", "load_extensions",
           "load_processor_methods", "module_exist",
           "cached_import", "get_module_version"]

module_registry: Dict[str, Any] = {}

def cached_import(module_name: str) -> Any:
    """
    Import a module by its name as a string and cache the result.
    
    If the module is already in the cache, it returns the cached module.
    If the module is not in the cache, it imports the module, stores it in the cache, and then returns it.
    
    Args:
        module_name (str): The name of the module to import.
        
    Returns:
        Any: The imported module.
        
    Raises:
        ModuleNotFoundError: If the module does not exist.
        ImportError: If there is an issue with the import.
        Exception: For any other unexpected errors.
    """
    if module_name not in module_registry:
        try:
            module = importlib.import_module(module_name)
            module_registry[module_name] = module
        except ModuleNotFoundError:
            quicsktats.stdout.error(f"Module '{module_name}' not found.")
            raise
        except ImportError as e:
            quicsktats.stdout.error(f"Import error: {e}")
            raise
        except Exception as e:
            quicsktats.stdout.error(f"An unexpected error occurred while importing module '{module_name}': {e}")
            raise
    elif module_name == "ROOT":
        ROOT = module_registry[module_name]
        ROOT.gROOT.SetBatch(True)
    return module_registry[module_name]

def compile_macros(macros:Optional[Union[str, List[str]]]=None):
    """
    Compile ROOT macros
    
    Arguments:
        macros: (Optional) str or list of str
            If str, it is a string containing comma delimited list of macro names to be compiled.
            If list of str, it is the list of macro names to be compiled.
    """
    custom_list = True
    if macros is None:
        macros = get_all_macros(required_only=True)
        custom_list = False
    elif isinstance(macros, str):
        from quickstats.utils.string_utils import split_str
        macros = split_str(macros, sep=',', remove_empty=True)
    from quickstats.utils.root_utils import compile_macro
    for macro in macros:
        if ((macro == "FlexibleInterpVarMkII") and (quickstats.root_version >= (6, 26, 0))) and (not custom_list):
            quickstats.stdout.info("INFO: Skip compiling macro \"FlexibleInterpVarMkII\" which is "
                                    "deprecated since ROOT 6.26/00")
            continue
        compile_macro(macro)
        
def get_all_macros(required_only:bool=False):
    """
    Get the list of macros names
    
    Note: Only macros ending in .cxx will be considered
    """
    
    if required_only:
        macro_names = ['AsymptoticCLsTool', 'QuickStatsCore']
        macro_names.extend(get_workspace_extensions())
        return macro_names
    
    macro_dir = quickstats.macro_path
    macro_subdirs = [path for path in glob.glob(os.path.join(macro_dir, "*")) if os.path.isdir(path)]
    macro_names = []
    for macro_subdir in macro_subdirs:
        macro_name = os.path.basename(macro_subdir)
        macro_path = os.path.join(macro_subdir, f"{macro_name}.cxx")
        if os.path.exists(macro_path):
            macro_names.append(macro_name)
    return macro_names

def set_verbosity(verbosity:Union[str, int]="INFO"):
    quickstats.stdout.verbosity = verbosity
    
def get_root_version() -> "quickstats.ROOTVersion":
    from quickstats.root_checker import ROOTChecker, ROOTVersion
    try:
        root_config_cmd = ROOTChecker.get_root_config_cmd()
        root_version = ROOTChecker.get_installed_root_version(root_config_cmd)
    except Exception:
        root_version = ROOTVersion((0, 0, 0))
    return root_version

def is_root_installed(name:str=None):
    return get_root_version() > (0, 0, 0)

def get_workspace_extensions():
    extension_config = get_workspace_extension_config()
    extensions = extension_config['required']
    if not extension_config['strict']:
        # deprecated extension
        if (quickstats.root_version >= (6, 26, 0)) and 'FlexibleInterpVarMkII' in extensions:
            extensions.remove('FlexibleInterpVarMkII')
    return extensions

def get_workspace_extension_config():
    resource_path = quickstats.resource_path
    extension_config_file = os.path.join(resource_path, "workspace_extensions.json")
    if not os.path.exists(extension_config_file):
        extension_config_file = os.path.join(resource_path, "default_workspace_extensions.json")
    with open(extension_config_file, "r") as file:
        extension_config = json.load(file)
    return extension_config

def add_macro(path:str, name:Optional[str]=None, copy_files:bool=True,
              workspace_extension:bool=True, force:bool=False):
    if not os.path.isdir(path):
        raise ValueError("macro path must be a directory")
    if name is None:
        name = os.path.basename(os.path.abspath(path))
    source_path = os.path.join(path, f"{name}.cxx")
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"macro path must contain a source file named {name}.cxx")
    macro_path = quickstats.macro_path
    if copy_files:
        dest_path = os.path.join(macro_path, name)
        if os.path.exists(dest_path):
            if force or input(f'WARNING: The macro already exists in {dest_path}, overwrite? [Y/N]') == "Y":
                shutil.rmtree(dest_path)
                shutil.copytree(path, dest_path)
                quickstats.stdout.info(f'INFO: Overwritten contents for the macro "{name}" from {path} to {dest_path}.')
            else:
                quickstats.stdout.info('INFO: Overwrite cancelled.')
        else:
            shutil.copytree(path, dest_path)
            quickstats.stdout.info(f'INFO: Copied contents for the macro "{name}" from {path} to {dest_path}.')
    if workspace_extension:
        resource_path = quickstats.resource_path
        extension_config_file = os.path.join(resource_path, "workspace_extensions.json")
        extension_config = get_workspace_extension_config()
        if name not in extension_config['required']:
            extension_config['required'].append(name)
            with open(extension_config_file, "w") as file:
                json.dump(extension_config, file, indent=2)
        quickstats.stdout.info(f'INFO: The macro "{name}" has been added to the workspace extension list.')
        
def remove_macro(name:str, remove_files:bool=True, force:bool=False):
    resource_path = quickstats.resource_path
    extension_config_file = os.path.join(resource_path, "workspace_extensions.json")
    extension_config = get_workspace_extension_config()
    if (name not in extension_config):
        quickstats.stdout.info(f'WARNING: Extension "{name}" not found in the workspace extension list. Skipped.')
    else:
        extension_config.remove(name)
        with open(extension_config_file, "w") as file:
            json.dump(extension_config, file, indent=2)
        quickstats.stdout.info(f'INFO: The extension "{name}" has been removed from the workspace extension list.')
    if remove_files:
        macro_path = quickstats.macro_path
        extension_path = os.path.abspath(os.path.join(macro_path, name))
        if force or input(f'WARNING: Attempting to remove files from {extension_path}, confirm? [Y/N]') == "Y":
            quickstats.stdout.info(f'INFO: Files for the macro "{name}" has been removed from {extension_path}.')
            shutil.rmtree(extension_path)
        else:
            quickstats.stdout.info('INFO: Macro files removal cancelled.')

def load_corelib():
    if not quickstats.corelib_loaded:
        from quickstats.utils.root_utils import load_library
        load_library("QuickStatsCore")
        quickstats.corelib_loaded = True
        
def load_extensions():
    extensions = get_workspace_extensions()
    extensions.extend(["QuickStatsCore", "AsymptoticCLsTool"])
    from quickstats.utils.root_utils import load_library
    for extension in extensions:
        load_library(extension)
        
def load_processor_methods():
    from quickstats.components.processors.builtin_methods import BUILTIN_METHODS
    from quickstats.utils.root_utils import declare_expression
    for name, definition in BUILTIN_METHODS.items():
        declare_expression(definition, name)
        
def module_exist(name: str) -> bool:
    if name == 'ROOT':
        return is_root_installed()
    return importlib.util.find_spec(name) is not None

def get_module_version(name:str) -> "quickstats.concepts.Version":
    from quickstats.concepts import Version
    if name == 'python':
        return Version(sys.version.split()[0])
    elif name == 'ROOT':
        return get_root_version()
    if not module_exist(name):
        raise RuntimeError(f'Module not installed: {name}')
    module = cached_import(name)
    if not hasattr(module, '__version__'):
        raise RuntimeError(f'Failed to retrieve version information for the module: {name}')
    return Version(module.__version__)

def _require_module(name: str, fn:Optional[Callable]=None):
    if name == 'python':
        return True
    elif name == 'ROOT':
        return is_root_installed()
    if fn is None:
        fn = module_exist
    if not fn(name):
        raise ImportError(f"The module '{name}' is required but not found. Please install it to proceed.")

def _require_module_version(name:str, version:Tuple, fn:Optional[Callable]=None):
    _require_module(name, fn=fn)
    module_version = get_module_version(name)
    if not (module_version >= version):
        from quickstats.concepts import Version
        raise RuntimeError(f'The module "{name}" is required to have a minimum version of {Version(version)} '
                           f'but got {module_version}')