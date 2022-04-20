class Television:
    """
    A class representing a Television object.
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of Television object.
        :rtype: None
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to access and set POWER STATE of Television object.
        :rtype: None
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> bool:
        """
        Method to set INCREMENT channel of Television object.
        :return FALSE if the self.__status is false.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
        else:
            return self.__status

    def channel_down(self) -> bool:
        """
        Method to set DECREMENT channel of Television object.
        :return FALSE if the self.__status is false.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
        else:
            return self.__status

    def volume_up(self) -> bool:
        """
        Method to set INCREMENT volume of Television object.
        :return FALSE if the self.__status is false.
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME
        else:
            return self.__status

    def volume_down(self) -> bool:
        """
        Method to set DECREMENT channel of Television object.
        :return FALSE if the self.__status is false.
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME
        else:
            return self.__status

    def __str__(self) -> str:
        """
        __str__ method to return all attributes of a Television object.
        :return  A string which gets each attribute so that it may be easily accessed.
        """
        return f'TV Status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
