class Eshik:
    def __init__(self):
        self.ochiq = False

    def och(self):
        self.ochiq = True
        print("🚪 Eshik ochildi")

    def yop(self):
        self.ochiq = False
        print("🚪 Eshik yopildi")


eshik = Eshik()
eshik.och()
eshik.yop()
