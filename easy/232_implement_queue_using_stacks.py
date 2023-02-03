# https://leetcode.com/problems/implement-queue-using-stacks
# easy
# practice - missed daily
class MyQueue:
    def __init__(self):
        self.primary = list()
        self.secondary = list()
        self.push_mode = True

    def _swap_stacks(self, push_mode=True):
        if self.push_mode != push_mode:
            while self.primary:
                self.secondary.append(self.primary.pop())
            self.primary, self.secondary = self.secondary, self.primary
            self.push_mode = not self.push_mode

    def push(self, x: int) -> None:
        self._swap_stacks()
        self.primary.append(x)

    def pop(self) -> int:
        self._swap_stacks(False)
        return self.primary.pop()

    def peek(self) -> int:
        self._swap_stacks(False)
        return self.primary[-1]

    def empty(self) -> bool:
        return not self.primary

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
