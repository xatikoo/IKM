class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve_merchant_problem(N, M, K):
    total = 2 * N
    if total == 0:
        return []

    head = Node(0)
    current = head
    for i in range(1, total):
        current.next = Node(0)
        current = current.next
    current.next = head  

    start_index = (M - 1) % total
    current = head
    for _ in range(start_index):
        current = current.next

    remaining = total
    while remaining > N:
        current.data = -1
        remaining -= 1

        if remaining > 0:
            steps = K
            while steps > 0:
                current = current.next
                if current.data != -1:
                    steps -= 1

    safe_positions = []
    current = head
    for i in range(total):
        if current.data != -1:
            safe_positions.append(i + 1)  
        current = current.next

    return safe_positions

def visualize_arrangement(positions, total):
    """Визуализирует расстановку тюков с нумерацией с 1"""
    arrangement = ['-'] * total  
    
    for pos in positions:
        arrangement[pos - 1] = '+' 
    
    result = "Расстановка тюков (позиции 1-{}):\n\n".format(total)
    for i in range(0, total, 10):
        chunk = arrangement[i:i+10]
        start = i + 1
        end = min(i + len(chunk), total)
        result += f"{' '.join(chunk)}\n"
    return result

def main():
    print("=" * 100)
    print("РЕШЕНИЕ ЗАДАЧИ 'ХИТРЫЙ КУПЕЦ'")
    print("=" * 100)
    print("Описание задачи:")
    print("Два купца везут по N тюков каждый. Чтобы спасти корабль от затопления,")
    print("капитан приказывает выбросить половину груза по следующему правилу:")
    print("1. Тюки нумеруются по часовой стрелке, начиная с носа корабля (1, 2, 3, ...)")
    print("2. Первым выбрасывается тюк с номером M (текущее число месяца)")
    print("3. Затем каждый K-й тюк из оставшихся")
    print("=" * 100)
    
    while True:
        try:
            N = int(input("Введите количество тюков у каждого купца (N): "))
            if N <= 0:
                print("Ошибка: N должно быть положительным целым числом!")
                continue
                
            M = int(input("Введите текущее число месяца (M): "))
            if M <= 0:
                print("Ошибка: M должно быть положительным целым числом!")
                continue
                
            K = int(input("Введите шаг выбрасывания (K): "))
            if K <= 0:
                print("Ошибка: K должно быть положительным целым числом!")
                continue

            total = 2 * N
            positions = solve_merchant_problem(N, M, K)
            
            print("\n" + "=" * 100)
            print("РЕЗУЛЬТАТ:")
            
            print(visualize_arrangement(positions, total))
            
            print("Рекомендация для купца:")
            print(f"Разместите свои {N} тюков на позициях: {positions}")
            print("=" * 100)
            
            choice = input("\nЖелаете решить еще одну задачу? (да/нет): ").lower()
            if choice not in ['да', 'д', 'yes', 'y']:
                print("\nПрограмма завершена. До свидания!")
                break
                
        except ValueError:
            print("\nОшибка: Введите целое число!")
        except Exception as e:
            print(f"\nНеожиданная ошибка: {e}")
            print("Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()