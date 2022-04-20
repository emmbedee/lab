import pytest
from classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_init(self):
        assert self.tv1.MIN_CHANNEL == 0
        assert self.tv1.MAX_CHANNEL == 3
        assert self.tv1.MIN_VOLUME == 0
        assert self.tv1.MAX_VOLUME == 2
        assert self.tv1.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

    def test_manipulate(self):
        # Test channel & volume increment/decrement as well as power bool state.
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV Status: Is on = True, Channel = 1, Volume = 1'
        self.tv1.channel_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV Status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

        # Test channel & volume attribute access when POWER = FALSE.
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        assert self.tv1.channel_up() is None
        assert self.tv1.volume_up() is None
        assert self.tv1.channel_down() is None
        assert self.tv1.volume_down() is None

        # Test channel looping & volume min/max attributes.
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert 'Channel = 0, Volume = 2' in self.tv1.__str__()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        assert 'Channel = 3, Volume = 0' in self.tv1.__str__()
