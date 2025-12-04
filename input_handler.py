#coding=windows-1251

class InputHandler:
    """Класс для обработки пользовательского ввода и валидации"""
    
    @staticmethod
    def get_yes_no_input(prompt):
        """Получить ввод да/нет от пользователя"""
        while True:
            response = input(prompt).lower().strip()
            if response in ['да', 'д', 'yes', 'y']:
                return True
            elif response in ['нет', 'н', 'no', 'n']:
                return False
            else:
                print("Пожалуйста, введите 'да' или 'нет'")
    
    @staticmethod
    def validate_input(weight, floor):
        """Валидация входных данных"""
        errors = []
        if weight <= 0:
            errors.append("Вес должен быть положительным числом")
        if floor <= 0:
            errors.append("Этаж должен быть положительным числом")
        if weight > 300:
            errors.append("Максимальный вес для расчета - 300 кг")
        return errors
    
    def get_user_input(self):
        """Получить и проверить данные от пользователя"""
        try:
            weight = float(input("\nВведите вес груза (кг): "))
            floor = int(input("Введите этаж: "))
            has_elevator = self.get_yes_no_input("Возможен подъем на лифте? (да/нет): ")
            
            errors = self.validate_input(weight, floor)
            if errors:
                for error in errors:
                    print(f"Ошибка: {error}")
                return None, None, None
            
            return weight, floor, has_elevator
            
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числовые значения!")
            return None, None, None