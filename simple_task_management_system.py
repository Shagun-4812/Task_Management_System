from abc import ABC, abstractmethod

class SimpleTaskManagementSystem(ABC):
    @abstractmethod
    def add_task(self, timestamp: int, name: str, priority: int) -> str: pass
    @abstractmethod
    def update_task(self, timestamp: int, task_id: str, name: str, priority: int) -> bool: pass
    @abstractmethod
    def get_task(self, timestamp: int, task_id: str) -> str | None: pass
    @abstractmethod
    def search_tasks(self, timestamp: int, name_filter: str, max_results: int) -> list[str]: pass
    @abstractmethod
    def list_tasks_sorted(self, timestamp: int, limit: int) -> list[str]: pass
    @abstractmethod
    def add_user(self, timestamp: int, user_id: str, quota: int) -> bool: pass
    @abstractmethod
    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_time: int) -> bool: pass
    @abstractmethod
    def complete_task(self, timestamp: int, task_id: str, user_id: str) -> bool: pass
    @abstractmethod
    def get_user_tasks(self, timestamp: int, user_id: str) -> list[str]: pass
    @abstractmethod
    def get_overdue_tasks(self, timestamp: int, user_id: str) -> list[str]: pass
