class TaskList {
  constructor() {
    this.tasks = []
  }

  add_task(task) {
    this.tasks.push(task);
  }

  remove_task(task) {
    const i = this.tasks.indexOf(task);
    if (i !== -1) {
      this.tasks.splice(i, 1);
    }
  }

  count_tasks() {
    return this.tasks.length;
  }
}