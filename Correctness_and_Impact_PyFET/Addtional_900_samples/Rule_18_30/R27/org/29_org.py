def deposit(self, money):
    # 先获取锁才能执行后续的代码
    self._lock.acquire()
    try:
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance
    finally:
        # 这段代码放在finally中保证释放锁的操作一定要执行
        self._lock.release()
