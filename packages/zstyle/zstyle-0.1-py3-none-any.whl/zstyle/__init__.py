import time, os

class z:

  RESET = '\033[0m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  PINK = '\033[35m'

  @staticmethod
  def type(text:str, delay:float=0.15):
    for i in text:
      print(i, end='', flush=True)
      time.sleep(delay)
    print("\n")

  @staticmethod
  def type_input(text:str, delay:float=0.15):
    for i in text:
      print(i, end='', flush=True)
      time.sleep(delay)
    return input()

  @staticmethod
  def color(text:str, color:str):
    color = getattr(z, color.upper(), z.RESET)
    return color + text + z.RESET

  @staticmethod
  def _getwidth():
    return os.get_terminal_size().columns

  @staticmethod
  def center(text:str):
    width = z._getwidth(z)
    return text.center(width)


