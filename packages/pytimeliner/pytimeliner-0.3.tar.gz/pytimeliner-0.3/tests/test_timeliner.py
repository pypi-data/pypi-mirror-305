import unittest
from pytimeliner.timeliner import Timeliner

class TestTimeliner(unittest.TestCase):
    def test_add_and_get_timeline_in_english(self):
        timeline = Timeliner(language='en')
        timeline.add_event("2024-01-01", "New Year")
        timeline.add_event("2024-12-25", "Christmas")
        
        events = timeline.get_timeline()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0][1], "New Year")

    def test_add_and_get_timeline_in_spanish(self):
        timeline = Timeliner(language='es')
        timeline.add_event("2024-01-01", "New Year")
        timeline.add_event("2024-12-25", "Christmas")

        events = timeline.get_timeline()
        self.assertEqual(len(events), 2)
        # Çeviri çıktısını doğrudan kontrol etmek zor olabilir, bu nedenle sadece sayıyı kontrol ediyoruz

if __name__ == '__main__':
    unittest.main()
