
from utils import *
from typing import Callable, Any
from tests import equals
from exceptions import TestFunctionError

def testify():
    _passed_tests_counter = 0
    _failed_tests_counter = 0
    _total_tests_counter = 0
    _failure_message: list[str] = []
    _success_message: list[str] = []
    _stacks: list[str] = []
    
    def summary()-> str:
        return get_summary(_total_tests_counter, _passed_tests_counter, _failed_tests_counter)
    
    def report()-> str:
        _report = ""
        for msg in _failure_message:
            _report = msg + _report
        for msg in _success_message:
            _report = msg + "\n" + _report
        return _report
    
    def failure_stack()-> list[str]:
        return _stacks[:] if len(_stacks) > 0 else [f"{GREEN}No failures{RESET}"]
    
    def run_test[T](
        expected:T, 
        result: T, 
        description:str="",
        test_function: Callable[..., Any] = equals,
        *args: Any,
        **kwargs: Any
    ):
        if not callable(test_function):
            raise TestFunctionError("The provided test function is not a valid function.")

        nonlocal _total_tests_counter
        nonlocal _passed_tests_counter
        nonlocal _failed_tests_counter
        nonlocal _success_message
        nonlocal _failure_message
        nonlocal _stacks
        
        _total_tests_counter += 1
        
        passed, msg, stack = test_function(expected, result, _total_tests_counter, description, *args, **kwargs)
        
        if stack is not None:
            _stacks.append(stack)
            
        if passed:
            _passed_tests_counter += 1
            _success_message.append(msg)
        else:
            _failed_tests_counter += 1
            _failure_message.append(msg)
    
    def core[T](
        expected:T, 
        result: T, 
        description:str="",
        test_function: Callable[..., Any] = equals,
        *args:list[Any], 
        **kwargs:dict[str,Any]
    ):

        run_test(expected, result, description, test_function, *args, **kwargs)
    
    return core, summary, report, failure_stack

# Inicialização das funções do módulo testify
core, summary, report, failure_stack = testify()

# O teste de igualdade é implicitamente chamado quando o quarto parâmetro de core é omitido.
core(1, 1, "Testando igualdade de inteiros")
core("Hello", "Hello", "Testando igualdade de strings")
core(4.0, 4.0, "Testando igualdade de números com ponto flutuante")

from tests import not_equals, greater_than, less_than, raises_exception

core(1, 3, "Testando desigualdade de inteiros", not_equals)
core(3, 2, "Testando se é maior que", greater_than)
core(2, 3, "Testando se é menor que", less_than)

def func (a: int):
    raise TestFunctionError("Teste de exceção")

# O quinto parâmetro de core é uma lista de argumentos que são passados pela função testada. Neste caso, a função `func`.
core(TestFunctionError, func, "test8", raises_exception, [1])


print(report()) # Imprime o relatório de testes
print(failure_stack()[0]) # Imprime o stack da primeira falha, caso haja falhas. Se não houver falhas, imprime "No failures".
print(summary()) # Imprime o resumo dos testes