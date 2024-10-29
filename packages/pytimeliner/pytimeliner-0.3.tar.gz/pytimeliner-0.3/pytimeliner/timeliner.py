from datetime import datetime
from googletrans import Translator

class Timeliner:
    def __init__(self, language='en'):
        self.events = []
        self.language = language
        self.translator = Translator()

    def add_event(self, date, description):
        """Verilen tarihi ve açıklamayı bir olay olarak ekler."""
        if isinstance(date, str):
            date = datetime.strptime(date, '%Y-%m-%d')
        
        # Açıklamayı belirtilen dile çevir
        if self.language != 'en':
            description = self.translate_text(description, self.language)
        
        self.events.append((date, description))

    def translate_text(self, text, target_language):
        """Metni hedef dile çevirir."""
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    def get_timeline(self):
        """Olayları tarih sırasına göre sıralar ve bir liste olarak döndürür."""
        return sorted(self.events, key=lambda event: event[0])

    def display_timeline(self):
        """Zaman çizelgesini gösterir."""
        for date, description in self.get_timeline():
            print(f"{date.strftime('%Y-%m-%d')}: {description}")
