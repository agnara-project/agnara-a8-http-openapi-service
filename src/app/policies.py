import agnara
from agnara.execution import ExecutionContext, PolicyResult, PolicySuccess, PolicyFailure, PolicyDeniedError

class DenyAllPolicy(agnara.Policy):
    def evaluate(self, context: ExecutionContext) -> PolicyResult:
        # Just an example policy that denies everything to test if policies run
        return PolicyFailure("Denied by DenyAllPolicy")
