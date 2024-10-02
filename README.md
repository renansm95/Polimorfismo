<h2>Sistema de Batalha com POO</h2>
Este projeto demonstra o uso de Programação Orientada a Objetos (POO) em Python, criando um sistema de batalha entre personagens com diferentes habilidades. O código implementa quatro classes de personagens: Character, Thief, Mage e Warrior, cada uma com métodos de ataque e características únicas.

<h3>Descrição do Projeto</h3>
O projeto consiste em um sistema de batalha simples com os seguintes conceitos:

- Herança: As classes Thief, Mage e Warrior herdam da classe Character, estendendo suas funcionalidades.
- Polimorfismo: Cada classe pode modificar o método atacar para realizar ataques específicos, de acordo com suas habilidades.
- Métodos personalizados: Cada classe possui métodos próprios, como healar para o Mago e muda_posicao para o Guerreiro.

<h3>Classes Implementadas</h3>
O projeto teve classes com informações fictícias:

- Character: Classe base que define os atributos e o método de ataque comum a todos os personagens.
- Thief: Classe que herda de Character e duplica o dano ao atacar.
- Mage: Classe que herda de Character, utiliza magia para causar dano e pode curar outros personagens.
- Warrior: Classe que herda de Character, possui um escudo e pode alternar entre modos de ataque e defesa.
