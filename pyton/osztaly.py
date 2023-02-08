class Formula:
    def __init__(self, list):
      self.nev = list[0]
      self.elsop = list[1]
      self.utolsop = list[2]
      self.magassag = list[3]
      self.suly = list[4]

      def __str__(self):
          return self.nev, self.elsop, self.utolsop, self.magassag, self.suly
