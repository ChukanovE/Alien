class Settings():
    def __init__(self):
        """Иницилизирует статические настройки игры"""
        # Настройка экрана
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        # Настройки коробля
        self.ships_limit = 3
        # Настройка пуль
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Настройка прищельцев
        self.fleet_drop_speed = 10
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости прищельца
        self.score_scale = 1.5
        self.initialize_dinamic_settings()

    def initialize_dinamic_settings(self):
        """Инициализирует настройки игры изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Подсчет очков
        self.alien_points = 50
        # fleet_direction = 1 - означает движение вправо, а -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
