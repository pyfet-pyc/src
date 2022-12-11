def deposit(self, money):
    # 获得锁后代码才能继续执行
    self._lock.acquire()
    try:
        new_balance = self._balance + money
        time.sleep(0.01)
        self._balance = new_balance
    finally:
        # 操作完成后一定要记着释放锁
        self._lock.release()