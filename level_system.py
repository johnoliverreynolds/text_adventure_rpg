class level_system:
  total_xp = None
  xp_until_next_level_up = None
  current_level = 1
  xp_modifer = 1

  def __init__(self, total_xp, xp_until_next_level_up):
    self.total_xp = total_xp
    self.xp_until_next_level_up = xp_until_next_level_up

  def gain_experience(self, xp): 
    self.total_xp += xp
    if self.total_xp >= self.xp_until_next_level_up:
      self.level_up()

  def level_up(self):
    self.current_level += 1
    self.xp_until_next_level_up = self.total_xp + (
      self.xp_until_next_level_up * self.xp_modifer
    )
    self.xp_modifer += 0.25



def test_level_up():
  print(f"player_level_system.total_xp: {player_level_system.total_xp}")
  print(f"player_level_system.current_level: {player_level_system.current_level}")
  print(f"player_level_system.xp_until_next_level_up: {player_level_system.xp_until_next_level_up}\n")
  player_level_system.gain_experience(5)

# Initialize 
player_level_system = level_system(0, 10)
test_level_up()
test_level_up()
test_level_up()

