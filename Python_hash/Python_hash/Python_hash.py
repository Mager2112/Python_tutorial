#Хеш-табли́ца — это структура данных, реализующая интерфейс ассоциативного массива,
#а именно, она позволяет хранить пары (ключ, значение) и выполнять три операции: 
#операцию добавления новой пары, 
#операцию удаления 
#и операцию поиска пары по ключу
#Класс Node помогает создать подобие односвязного списка
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def add_element(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            # Линейная проба: двигаемся к следующему слоту
            index = (index + 1) % self.size

        self.table[index] = (key, value)

        # Проверка на переполнение (если таблица слишком заполнена)
        if len([x for x in self.table if x is not None]) >= self.size * 0.7:
            print("error 1")
            self.resize()

    def resize(self):
        print("error 2")
        # Увеличьте размер таблицы и перехешируйте элементы
        self.size *= 2
        new_table = [None] * self.size

        for item in self.table:
            if item is not None:
                key, value = item
                index = self.hash_function(key)

                while new_table[index] is not None:
                    index = (index + 1) % self.size

                new_table[index] = (key, value)

        self.table = new_table

# Пример использования
hash_table = HashTable(10)
hash_table.add_element("key1", "value1")
hash_table.add_element("key2", "value1")
