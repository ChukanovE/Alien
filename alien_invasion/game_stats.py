class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_settings):
        """Иницилизирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии
        self.game_active = False
        # Рекорд не должен сбрасываться
        self.high_score = 0

    def reset_stats(self):
        """Иницилизирует статитстику, изменяющиеся в ходе игры"""
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1