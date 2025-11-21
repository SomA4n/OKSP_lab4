# calculator.py
class PriceCalculator:
    """Класс для расчета стоимостей"""
    
    def __init__(self):
        self.base_prices = {
            50: 300,
            100: 1000,
            300: 2000
        }
        self.manual_lift_cost_per_floor = 300
    
    def get_base_price(self, weight):
        """Получить базовую стоимость в зависимости от веса"""
        if weight <= 50:
            return self.base_prices[50]
        elif weight <= 100:
            return self.base_prices[100]
        else:
            return self.base_prices[300]
    
    def calculate_manual_cost(self, weight, floor):
        """Рассчитать стоимость ручного подъема"""
        floors_to_lift = floor - 1 if floor > 1 else 0
        weight_factor = (weight + 99) // 100  # Округление вверх до ближайших 100 кг
        return self.manual_lift_cost_per_floor * floors_to_lift * weight_factor
    
    def calculate_total_cost(self, weight, floor, has_elevator):
        """Рассчитать общую стоимость подъема"""
        base_cost = self.get_base_price(weight)
        
        if has_elevator:
            return base_cost
        else:
            manual_cost = self.calculate_manual_cost(weight, floor)
            return base_cost + manual_cost