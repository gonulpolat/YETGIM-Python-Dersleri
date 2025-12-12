"""
    **To-Do List Uygulaması**: Görev ekleme, silme, tamamlandı işaretleme

    tasks = [
        {
            "task_id": 1,
            "name": "Oje sür",
            "state": 0-1 # Yapılacak / Tamamlandı
        },
    ]
"""

class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.state = 0

    def __repr__(self):
        pass

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._id_counter = 1

    def add_task(self, name):
        task = Task(self._id_counter, name)
        self.tasks.append(task)
        self._id_counter += 1
        print(f"Görev eklendi: {name}")

    def show_tasks(self):
        """
        Sadece tamamlanmamış görevleri göster
        """
        unfinished = [task for task in self.tasks if task.state == 0]
        if not unfinished:
            print("   ⚪ Görev yok!")
        else:
            for task in unfinished:
                print(f"   🔴 ID: {task.task_id} | {task.name}")

    def show_all_tasks(self):
        """
        Burada ise bütün görevler görünür
        """
        if not self.tasks:
            print("   ⚪ Görev listesi boş!")
        else:
            for task in self.tasks:
                icon = "🟢" if task.state == 1 else "🔴"
                print(f"   {icon} ID: {task.task_id} | {task.name}")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                deleted_name = task.name
                self.tasks.pop(i)
                print(f"✅ Görev silindi: '{deleted_name}' (ID: {task_id})")
                return
        print(f"❌ Görev bulunamadı! ID: {task_id}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.state == 1:
                    print(f"❗ Görev zaten tamamlanmış: '{task.name}'")
                else:
                    task.state = 1
                    print(f"✅ Görev tamamlandı: '{task.name}'")
                return
        print(f"❌ Görev bulunamadı! ID: {task_id}")


if __name__ == "__main__":
    gorevler = TaskManager()

    gorevler.show_tasks()

    gorevler.add_task("Oje Sür")
    gorevler.add_task("Kitap oku")
    gorevler.add_task("Tiktok izle")

    gorevler.show_tasks()

    gorevler.complete_task(2)
    gorevler.show_tasks()
    gorevler.show_all_tasks()
