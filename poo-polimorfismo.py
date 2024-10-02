class Character:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, personagem):
        if self.ataque > personagem.defesa:
            dano = self.ataque - personagem.defesa
            personagem.vida -= dano
            print(f"{self.nome} causou {dano} e a vida atual do {personagem.nome} é de {personagem.vida}")
        else:
            print("Dano insuficiente")


class Thief(Character):
    def atacar(self, personagem):
        if self.ataque > personagem.defesa:
            dano = (self.ataque - personagem.defesa) * 2
            personagem.vida -= dano
            print(f"{self.nome} causou {dano} e a vida atual do {personagem.nome} é de {personagem.vida}")
        else:
            print("Dano insuficiente")


class Mage(Character):
    def __init__(self, nome, magia, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.magia = magia

    def atacar(self, personagem):
        if self.magia > personagem.defesa:
            dano = self.magia + self.ataque - personagem.defesa
            personagem.vida -= dano
            print(f"{self.nome} causou {dano} e a vida atual do {personagem.nome} é de {personagem.vida}")
        else:
            print("Dano insuficiente.")

    def healar(self, personagem):
        personagem.vida += self.magia * 2
        print(f"{self.nome} encheu a vida do {personagem.nome} e a vida atual é de {personagem.vida}")


class Warrior(Character):
    def __init__(self, nome, escudo, posicao, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.escudo = escudo
        self.posicao = posicao

    def atacar(self, personagem):
        if self.posicao == "ataque" and self.ataque > personagem.defesa:
            dano = self.ataque - personagem.defesa
            personagem.vida -= dano
            print(f"{self.nome} causou {dano} e a vida atual do {personagem.nome} é de {personagem.vida}")
        elif self.posicao == "defesa":
            print("Você precisa mudar sua posição para ataque para poder atacar.")
        else:
            print("Dano insuficiente.")

    def muda_posicao(self):
        if self.posicao == "ataque":
            self.posicao = "defesa"
            self.defesa += self.escudo
        else:
            self.posicao = "ataque"
            self.defesa -= self.escudo


# Testando as classes
viktor = Character("Viktor", 100, 15, 15)
sion = Thief("Sion", 100, 60, 10)
lux = Mage("Lux", 50, 100, 5, 20)
kayn = Warrior("Kayn", 5, "ataque", 200, 20, 50)

# Exibindo informações iniciais
print(f"Vida inicial de {viktor.nome}: {viktor.vida}")
print(f"Vida inicial de {sion.nome}: {sion.vida}")
print(f"Vida inicial de {lux.nome}: {lux.vida}")
print(f"Vida inicial de {kayn.nome}: {kayn.vida}")

# Testando ataques
viktor.atacar(sion)
sion.atacar(viktor)
lux.atacar(kayn)
kayn.atacar(lux)

# Testando habilidades especiais
lux.healar(viktor)
kayn.muda_posicao()
kayn.atacar(lux)
