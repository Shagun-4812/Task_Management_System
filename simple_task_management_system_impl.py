from simple_task_management_system import SimpleTaskManagementSystem

class SimpleTaskManagementSystemImpl(SimpleTaskManagementSystem):
    def __init__(self):
        self.tasks = {}
        self.task_counter = 0
        self.users = {}
        self.assignments = []

    def add_task(self, timestamp: int, name: str, priority: int) -> str:
        self.task_counter += 1
        tid = f"task_id_{self.task_counter}"
        self.tasks[tid] = {"name": name, "priority": priority, "num": self.task_counter}
        return tid

    def update_task(self, timestamp: int, task_id: str, name: str, priority: int) -> bool:
        if task_id in self.tasks:
            self.tasks[task_id].update({"name": name, "priority": priority})
            return True
        return False

    def get_task(self, timestamp: int, task_id: str) -> str | None:
        if task_id not in self.tasks: return None
        t = self.tasks[task_id]
        return f'{{"name":"{t["name"]}","priority":{t["priority"]}}}'

    def search_tasks(self, timestamp: int, name_filter: str, max_results: int) -> list[str]:
        m = [tid for tid, d in self.tasks.items() if name_filter in d["name"]]
        m.sort(key=lambda tid: (-self.tasks[tid]["priority"], self.tasks[tid]["num"]))
        return m[:max_results]

    def list_tasks_sorted(self, timestamp: int, limit: int) -> list[str]:
        ids = sorted(self.tasks.keys(), key=lambda tid: (-self.tasks[tid]["priority"], self.tasks[tid]["num"]))
        return ids[:limit]

    def add_user(self, timestamp: int, user_id: str, quota: int) -> bool:
        if user_id in self.users: return False
        self.users[user_id] = quota
        return True

    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_time: int) -> bool:
        if task_id not in self.tasks or user_id not in self.users: return False
        active = sum(1 for a in self.assignments if a["uid"] == user_id and a["s"] <= timestamp < a["f"] and not a["comp"])
        if active >= self.users[user_id]: return False
        self.assignments.append({"tid": task_id, "uid": user_id, "s": timestamp, "f": finish_time, "comp": False})
        return True

    def complete_task(self, timestamp: int, task_id: str, user_id: str) -> bool:
        for a in self.assignments:
            if a["tid"] == task_id and a["uid"] == user_id and a["s"] <= timestamp < a["f"] and not a["comp"]:
                a["comp"] = True
                return True
        return False

    def get_user_tasks(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users: return []
        res = [a for a in self.assignments if a["uid"] == user_id and a["s"] <= timestamp < a["f"] and not a["comp"]]
        res.sort(key=lambda x: (x["f"], x["s"]))
        return [x["tid"] for x in res]

    def get_overdue_tasks(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users: return []
        res = [a for a in self.assignments if a["uid"] == user_id and timestamp >= a["f"] and not a["comp"]]
        res.sort(key=lambda x: (x["f"], x["s"]))
        return [x["tid"] for x in res]
