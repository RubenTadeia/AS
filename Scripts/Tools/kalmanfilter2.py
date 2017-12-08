# coding=utf-8

# Esse codigo é nosso, só o comentario do commit que foi automatico (igual do ultimo).
# The Error from Laser is 30 mm


class KalmanFilter(object):

    KalmanGain = 0
    Estimativa = 0
    ErroDaEstimativa = 0
    ErroDoValorEstimadoAnterior = 10000

    def __init__(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido):

        self.ValorEstimado = ValorEstimado
        self.ErroDoValorEstimado = ErroDoValorEstimado

        self.ValorMedido = ValorMedido
        self.ErroDoValorMedido = ErroDoValorMedido

    # def __kalmangain__ (self):

        self.KalmanGain = self.ErroDoValorEstimado / (self.ErroDoValorEstimado + self.ErroDoValorMedido)

    # def __estimativa__(self):

        self.Estimativa = self.ValorEstimado + self.KalmanGain * (self.ValorMedido - self.ValorEstimado)

    # def __errodaestimativa__(self):
    #     print(self.ErroDoValorEstimadoAnterior)
    #     print(self.KalmanGain)

        self.ErroDaEstimativa = (1 - self.KalmanGain) * self.ErroDoValorEstimadoAnterior
        self.ErroDoValorEstimadoAnterior = self.ErroDaEstimativa

        """
        Atualiza a função com base nos valores já criados.
        """

    def update(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido):

        self.__init__(ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido)

    def getEstimativa(self):

        return self.Estimativa

    def getErroDaEstimativa(self):

        return self.ErroDaEstimativa

# Erro inicial 10000
# [pos1, error da pos1, pos2, erro da pos2]


lista = [[13, 3, 12.2, 0.9],
         [17, 3, 18, 0.9],
         [21, 3, 21.3, 0.9],
         [25, 3, 25.3, 0.9],
         [29, 3, 29.8, 0.9],
         [33, 3, 32.4, 0.9]]

lista2 = [[13, 3.2, 12, 0.9],
          [17, 3.4, 18, 0.9],
          [21, 2, 21, 0.9],
          [24, 1, 25.3, 0.9],
          [30, 7.2, 29.8, 0.9],
          [38, 4.6, 38.4, 0.9]]

kf = KalmanFilter(*[13, 3, 12, 0.9])
print (kf.ErroDaEstimativa)
for l in lista:
    kf.update(*l)
    print (kf.ErroDaEstimativa)

print ("------------")

kf = KalmanFilter(*[13, 3, 12, 0.9])
print (kf.ErroDaEstimativa)
for l in lista2:
    kf.update(*l)
    print (kf.ErroDaEstimativa)
