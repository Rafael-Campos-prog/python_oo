import carro

uno_vermelho = carro.Carro('vermelho', 4, 'Flex', 1.0, 0, False, 0)
help(uno_vermelho.abastecer)
help(carro.Carro)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
print(f'A quantidade de combustível do uno vermelho é:{uno_vermelho.qtd_combustivel}')


uno_preto = carro.Carro('preto', 4, 'Flex', 1.4, 0, False, 0)
uno_preto.desligar()
uno_preto.abastecer(5)
print(f'A quantidade de combustivel do uno preto é:{uno_preto.qtd_combustivel}')
uno_preto.acelerar(20)
uno_preto.ligar()
uno_preto.acelerar(20)
print(uno_preto.velocidade)


