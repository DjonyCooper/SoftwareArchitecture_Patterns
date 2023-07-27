import abc

class IWorker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        pass
    @abc.abstractmethod
    def execute(self, command: str) -> str:
        pass

class AbsWorker(IWorker):
    def __init__(self):
        self.__next_worker: IWorker = None

    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        self.__next_worker = worker
        return worker

    def execute(self, command: str) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        return ''

class Designer(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'спроектировать дом':
            return f'Проектировщик выполнил команду: {command}'
        else:
            return super().execute(command)

class Carpenters(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'класть кирпич':
            return f'Плотник выполнил команду: {command}'

        else:
            return super().execute(command)

class FinishingWorker(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'клеить обои':
            return f'Рабочий внутренней отделки выполнил команду: {command}'
        else:
            return super().execute(command)

def give_command(worker: IWorker, command: str):
    string: str = worker.execute(command)
    if string == '':
        print(f'Работа не выполнена: {command} - никто не умеет делать')
    else:
        print(string)

if __name__ == '__main__':
    designer = Designer()
    carpenters = Carpenters()
    finishingWorker = FinishingWorker()

    designer.set_next_worker(carpenters).set_next_worker(finishingWorker)

    give_command(designer, 'спроектировать дом')
    give_command(designer, 'класть кирпич')
    give_command(designer, 'клеить обои')
    give_command(designer, 'провести проводку')
