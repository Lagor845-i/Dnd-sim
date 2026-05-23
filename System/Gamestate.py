from Entity import Creature

class GameState:
    def __init__(self) -> None:
        self._current_creatures = {}
        self._game_packets = []
        self._input_packets = []
        self._current_turn:str | None = None
        self._initiative_order:list[str] = [] # Creature IDs
        self._in_battle = False
    
    def addGamePacket(self,packet):
        self._game_packets.append(packet)

    def getGamePackets(self):
        return self._game_packets
    
    def addCreature(self,creature:Creature):
        self._current_creatures[creature._Creature_id] = creature

    def removeCreature(self,creature_id:str):
        if self._current_turn == creature_id:
            self.nextTurn()
        self._current_creatures.pop(creature_id,None)
    
    def nextTurn(self):
        if len(self._initiative_order) != 0 and self._current_turn in self._initiative_order:
            index = self._initiative_order.index(self._current_turn)
            if index+1 > len(self._initiative_order)-1:
                self._current_turn = self._initiative_order[0]
            else:
                self._current_turn = self._initiative_order[index+1]
        
        elif len(self._initiative_order) == 0:
            self._in_battle = False
        
        elif self._current_turn == None:
            self._current_turn = self._initiative_order[0]
        
        if not self._in_battle:
            self._initiative_order = []


    def startBattle(self):
        pass

    def firstRound(self):
        pass