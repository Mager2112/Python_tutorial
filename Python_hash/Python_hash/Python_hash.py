#Хеш-табли́ца — это структура данных, реализующая интерфейс ассоциативного массива,
#а именно, она позволяет хранить пары (ключ, значение) и выполнять три операции: 
#операцию добавления новой пары, 
#операцию удаления 
#и операцию поиска пары по ключу
#Класс Node помогает создать подобие односвязного списка
class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None
  
#Класс HashTable - это и есть реализация Хэш-таблицы
class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity 
  
    def _hash(self, key): 
        return hash(key) % self.capacity 
  
    def insert(self, key, value): 
        index = self._hash(key) 
  
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.value = value 
                    return
                current = current.next
            new_node = Node(key, value) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1
  
    def search(self, key): 
        index = self._hash(key) 
  
        current = self.table[index] 
        while current: 
            if current.key == key: 
                return current.value 
            current = current.next
  
        raise KeyError(key) 
  
    def remove(self, key): 
        index = self._hash(key) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        raise KeyError(key) 
  
    def __len__(self): 
        return self.size 
  
    def __contains__(self, key): 
        try: 
            self.search(key) 
            return True
        except KeyError: 
            return False
  
  
# main
if __name__ == '__main__': 
  
    #Создание хэш-таблицы, максимум элементов - 5
    ht = HashTable(5) 
    ht.insert("Пикулин", 5)
    ht.insert("Тищенко", 4)
    ht.insert("Бог-император", 9)
    print ("Бог-император" in ht) #true
    print("Смит" in ht) #false
    print(ht.search("Бог-император"))