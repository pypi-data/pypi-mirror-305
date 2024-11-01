from scipy._typing import Untyped
from ._optimize import OptimizeResult as OptimizeResult

izip = zip

def synchronized(func: Untyped) -> Untyped: ...
def fmin_cobyla(
    func: Untyped,
    x0: Untyped,
    cons: Untyped,
    args: Untyped = (),
    consargs: Untyped | None = None,
    rhobeg: float = 1.0,
    rhoend: float = 0.0001,
    maxfun: int = 1000,
    disp: Untyped | None = None,
    catol: float = 0.0002,
    *,
    callback: Untyped | None = None,
) -> Untyped: ...
