class DisplayManager:
    """Класс для управления отображением информации"""
    "new comment"
    "one more new comment"
    
    def __init__(self, calculator):
        self.calculator = calculator
    
    def display_price_table(self):
        """Показать таблицу базовых цен"""
        print("\n" + "="*50)
        print("ТАБЛИЦА БАЗОВЫХ СТОИМОСТЕЙ")
        print("="*50)
        print(f"Масса груза до 50 кг: {self.calculator.base_prices[50]} руб.")
        print(f"Масса груза до 100 кг: {self.calculator.base_prices[100]} руб.")
        print(f"Масса груза до 300 кг: {self.calculator.base_prices[300]} руб.")
        print("="*50)
    
    def display_result(self, weight, floor, has_elevator, total_cost):
        """Показать результаты расчета"""
        base_cost = self.calculator.get_base_price(weight)
        
        print("\n" + "="*40)
        print("РЕЗУЛЬТАТ РАСЧЕТА:")
        print("="*40)
        print(f"Вес груза: {weight} кг")
        print(f"Этаж: {floor}")
        print(f"Лифт: {'Да' if has_elevator else 'Нет'}")
        print(f"Базовая стоимость: {base_cost} руб.")
        
        if not has_elevator and floor > 1:
            manual_cost = self.calculator.calculate_manual_cost(weight, floor)
            print(f"Стоимость ручного подъема: {manual_cost} руб.")
            
        print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost} руб.")
        print("="*40)
    
    def display_example_from_task(self):
        """Показать пример расчета из задания"""
        print("\nПРИМЕР ИЗ ЗАДАНИЯ (250 кг на 3 этаж без лифта):")
        base_cost = self.calculator.get_base_price(250)
        manual_cost = self.calculator.calculate_manual_cost(250, 3)
        
        print(f"Базовая стоимость: {base_cost} руб.")
        print(f"Ручной подъем (300 руб/этаж × 2 этажа × 3 ед. по 100 кг): {manual_cost} руб.")
        print(f"ИТОГО: {base_cost + manual_cost} руб.")
    
    def display_test_cases(self):
        """Показать тестовые примеры"""
        test_cases = [
            (50, 1, True, "50кг, 1 этаж, с лифтом"),
            (50, 5, False, "50кг, 5 этаж, без лифта"),
            (100, 3, True, "100кг, 3 этаж, с лифтом"),
            (100, 3, False, "100кг, 3 этаж, без лифта"),
            (250, 3, False, "250кг, 3 этаж, без лифта (пример из задания)"),
            (300, 10, False, "300кг, 10 этаж, без лифта")
        ]
        
        print("\nТЕСТОВЫЕ РАСЧЕТЫ:")
        print("="*60)
        
        for weight, floor, elevator, description in test_cases:
            cost = self.calculator.calculate_total_cost(weight, floor, elevator)
            base = self.calculator.get_base_price(weight)
            manual = self.calculator.calculate_manual_cost(weight, floor) if not elevator else 0
            
            print(f"{description}:")
            print(f"  Базовая: {base} руб. + Ручной подъем: {manual} руб. = ИТОГО: {cost} руб.")


# main.py
class LiftCalculatorApp:
    """Главный класс приложения, объединяющий все компоненты"""
    
    def __init__(self):
        self.calculator = PriceCalculator()
        self.input_handler = InputHandler()
        self.display_manager = DisplayManager(self.calculator)
    
    def run(self):
        """Основной метод запуска приложения"""
        print("КАЛЬКУЛЯТОР СТОИМОСТИ ПОДЪЁМА ГРУЗА")
        print("=" * 40)
        
        # Показать тестовые примеры
        self.display_manager.display_test_cases()
        
        while True:
            # Получение данных от пользователя
            weight, floor, has_elevator = self.input_handler.get_user_input()
            
            if weight is None:
                continue
            
            # Расчет стоимости
            total_cost = self.calculator.calculate_total_cost(weight, floor, has_elevator)
            
            # Вывод результатов
            self.display_manager.display_result(weight, floor, has_elevator, total_cost)
            
            # Показать пример из задания если совпадают параметры
            if not has_elevator and floor == 3 and weight == 250:
                self.display_manager.display_example_from_task()
            
            # Меню продолжения
            choice = input("\n1 - Новый расчет\n2 - Показать таблицу цен\n3 - Выход\nВыберите действие: ")
            
            if choice == '2':
                self.display_manager.display_price_table()
            elif choice == '3':
                print("До свидания!")
                break


if __name__ == "__main__":
    app = LiftCalculatorApp()
    app.run()