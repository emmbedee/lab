import pytest
from classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.MIN_CHANNEL == 0
        assert self.tv1.MAX_CHANNEL == 3
        assert self.tv1.MIN_VOLUME == 0
        assert self.tv1.MAX_VOLUME == 2
        assert self.tv1.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        self.tv1.power()
        assert 'TV Status: Is on = True' in self.tv1.__str__()

    def test_channel_up(self):
        # Check access when POWER = FALSE.
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        assert self.tv1.channel_up() is False
        # Check increment.
        self.tv1.power()
        self.tv1.channel_up()
        assert 'Channel = 1' in self.tv1.__str__()
        # Check channel looping.
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert 'Channel = 0' in self.tv1.__str__()
        self.tv1.power()

    def test_channel_down(self):
        # Check access when POWER = FALSE.
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        assert self.tv1.channel_down() is False
        # Check decrement.
        self.tv1.power()
        self.tv1.channel_down()
        assert 'Channel = 3' in self.tv1.__str__()
        # Check channel looping.
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        assert 'Channel = 3' in self.tv1.__str__()
        self.tv1.power()

    def test_volume_up(self):
        # Check access when POWER = FALSE.
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        assert self.tv1.volume_up() is False
        # Check increment.
        self.tv1.power()
        self.tv1.volume_up()
        assert 'Volume = 1' in self.tv1.__str__()
        # Check volume max behavior.
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert 'Volume = 2' in self.tv1.__str__()
        self.tv1.power()

    def test_volume_down(self):
        # Check access when POWER = FALSE.
        assert 'TV Status: Is on = False' in self.tv1.__str__()
        assert self.tv1.volume_down() is False
        # Check decrement.
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert 'Volume = 1' in self.tv1.__str__()
        # Check volume min behavior.
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert 'Volume = 0' in self.tv1.__str__()
        self.tv1.power()

    def test_string(self):
        assert self.tv1.__str__() == 'TV Status: Is on = False, Channel = 0, Volume = 0'
