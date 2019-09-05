# Context Manager in Python
## with statement
- [with.py](./with.py): basic context manager using `with`
- [with-as.py](./with-as.py): combine `with` with `as`
- [with-exception.py](./with-exception.py): exception handle in `with`
- [with-async.py](./with-async.py): An asynchronous context manager is a context manager that is able to suspend execution in its enter and exit methods.

## contextlib
- [context_lib.py](./context_lib.py): a decorator that can be used to define a factory function for with statement context managers, without needing to create a class or separate `__enter__()` and `__exit__()` methods.
- [context_lib_decorator.py](./context_lib_decorator.py): A base class that enables a context manager to also be used as a decorator.
- [context_lib_exitstack.py](./context_lib_exitstack.py): ExitStack makes it possible to instead register a callback for execution at the end of a with statement, and then later decide to skip executing that callback:
- [context_lin_reentrant.py](./context_lin_reentrant.py):  Reentrant context managers can not only be used in multiple with statements, but may also be used inside a with statement that is already using the same context manager.
