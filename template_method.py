# шаблонный метод, показывает этапы формирования звука в устройствах аналоговой и цифровой передачи речи.
import abc

class Transmitter(metaclass=abc.ABCMeta):
    def _voice_record(self):
        print('Запись фрагмента речи')

    def _simpling(self):
        pass

    def _digitization(self):
        pass

    @abc.abstractmethod
    def _modulation(self):
        pass

    def _transmission(self):
        print('Передача сигнала по радиоканалу')

    def process_start(self):
        self._voice_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self._transmission()

class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print('Модуляция аналогового сигнала')

class DigitTransmitter(Transmitter):
    def _simpling(self):
        print('Дискредизация записанного фрагмента')

    def _digitization(self):
        print('Оцифровка')

    def _modulation(self):
        print('Модуляция цифрового сигнала')

if __name__ == '__main__':
    analog_transmitter = AnalogTransmitter()
    analog_transmitter.process_start()

    print()

    digit_transmitter = DigitTransmitter()
    digit_transmitter.process_start()