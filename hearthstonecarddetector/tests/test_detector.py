from unittest import TestCase
from PIL import Image
from hearthstonecarddetector import card_image_to_id
import os


class TestDetector(TestCase):
    def test_detector(self):

        for i in range(1, 10):
            with Image.open(os.path.join(os.path.dirname(__file__), "images/AT_00%d.png" % i)) as img:
                self.assertEquals("AT_00%d" % i, card_image_to_id(img))

