try:
    from src.lab10.structures import Stack, Queue
except ImportError:
    from structures import Stack, Queue

def test_stack():
    print("\n--- TECT: CTEK (Stack) ---")
    s = Stack()
    for i in [10, 20, 30]:
        print(f"Добавляем в стек: {i}")
        s.push(i)
    print(f"Извлекаем (ожидаем 30): {s.pop()}")
    print(f"Извлекаем (ожидаем 20): {s.pop()}")

def test_queue():
    print("\n--- TECT: OЧЕРЕДЬ (Queue) ---")
    q = Queue()
    for char in ['A', 'B', 'C']:
        print(f"Добавляем в очередь: {char}")
        q.enqueue(char)
    print(f"Извлекаем (ожидаем A): {q.dequeue()}")
    print(f"Извлекаем (ожидаем B): {q.dequeue()}")

def main():
    test_stack()
    test_queue()
    print("\nВсе тесты успешно пройдены!")

if __name__ == "__main__":
    main()