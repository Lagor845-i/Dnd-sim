class GameState:
    def __init__(self) -> None:
        self._current_creatures = []
        self._packets = []
    
    def addPacket(self,packet):
        self._packets.append(packet)

    def getPackets(self):
        return self._packets