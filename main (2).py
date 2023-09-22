class Player:
  def play(self):
      print("the player is playing cricket")
    
class Batsman(Player):
  def play(self):
      print("the batsman is batting")
    
class Bowler(Player):
  def play(self):
      print("the bowler is bowlling")


batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()