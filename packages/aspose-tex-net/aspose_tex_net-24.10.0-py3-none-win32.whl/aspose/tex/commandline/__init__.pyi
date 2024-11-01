import aspose.tex
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Base64Exec(aspose.tex.commandline.Executable):
    '''An implementation of
    Base64
    
     command emulation.'''
    
    def __init__(self):
        ...
    
    def execute(self, args: list[str]) -> None:
        '''The method implementing the executable's behavior.
        
        :param args: The array of command line arguments.'''
        ...
    
    @property
    def command_name(self) -> str:
        '''Gets the name of the executable (command).'''
        ...
    
    ...

class Executable:
    '''The base class for classes that emulate the behavior of OS executables,
    which can be run by the occurrences of Object TeX's
    \write18
    
     primitive.'''
    
    def execute(self, args: list[str]) -> None:
        '''The method implementing the executable's behavior.
        
        :param args: The array of command line arguments.'''
        ...
    
    @property
    def command_name(self) -> str:
        '''Gets the name of the executable (command).'''
        ...
    
    ...

class ExecutablesList:
    '''Encapsulates a collection of objects that emulate executables,
    which can be executed using the
    \write18
    
     commands in ObjectTeX.'''
    
    def add(self, exec: aspose.tex.commandline.Executable) -> None:
        '''Adds a new executable to the collection.
        
        :param exec: An instance of :class:`Executable`'s subclass.'''
        ...
    
    def remove(self, command_name: str) -> None:
        '''Removes an executable by its name.
        
        :param command_name: The name of an executable.'''
        ...
    
    ...

class Write18Exception(RuntimeError):
    '''The exception that has to be thrown when something goes wrong while an executable is running.'''
    
    def __init__(self, message: str):
        '''Creates a new instance.
        
        :param message: The message to be displayed on the terminal.'''
        ...
    
    ...

