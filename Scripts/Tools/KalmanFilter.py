# coding=utf-8
import numpy as np

# Esse codigo é nosso, só o comentario do commit que foi automatico (igual do ultimo).
# The Error from Laser is 30 mm


class KalmanFilter(object):

    KalmanGain = 0
    Estimativa = 0
    ErroDaEstimativa = 0

    def __init__(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido, ValorEstimadoAnterior, ErroDoValorEstimadoAnterior):

        self.ValorEstimado = ValorEstimado
        self.ErroDoValorEstimado = ErroDoValorEstimado

        self.ValorMedido = ValorMedido
        self.ErroDoValorMedido = ErroDoValorMedido

        self.ValorEstimadoAnterior = ValorEstimadoAnterior
        self.ErroDoValorEstimadoAnterior = ErroDoValorEstimadoAnterior

    # def __kalmangain__ (self):

        self.KalmanGain = self.ErroDoValorEstimado / (self.ErroDoValorEstimado + self.ErroDoValorMedido)

    # def __estimativa__(self):

        self.Estimativa = self.ValorEstimado + self.KalmanGain * (self.ValorMedido - self.ValorEstimado)

    # def __errodaestimativa__(self):

        self.ErroDaEstimativa = (1 - self.KalmanGain) * self.ErroDoValorEstimadoAnterior

        """
        Atualiza a função com base nos valores já criados.
        """

    def update(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido):

        self.__init__(ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido, self.Estimativa, self.ErroDaEstimativa)

    def getEstimativa(self):

        return self.Estimativa

    def getErroDaEstimativa(self):

        return self.ErroDaEstimativa


Valor1 = np.array([16.5, 10])
Valor1Error = np.array([2, 1])
Valor2 = np.array([15, 11])
Valor2Error = np.array([0.5, 0.1])
Valor3 = np.array([10, 6])
Valor3Error = np.array([1, 0.5])

kf = KalmanFilter(Valor1, Valor1Error, Valor2, Valor2Error, Valor3, Valor3Error)

print(kf.getEstimativa())

Valor1 = np.array([33, 10])
Valor1Error = np.array([2, 1])
Valor2 = np.array([30, 11])
Valor2Error = np.array([0.5, 0.1])

kf.update(Valor1, Valor1Error, Valor2, Valor2Error)
print(kf.getEstimativa())

Valor1 = np.array([85, 10])
Valor1Error = np.array([2, 1])
Valor2 = np.array([91, 11])
Valor2Error = np.array([0.5, 0.1])

kf.update(Valor1, Valor1Error, Valor2, Valor2Error)
print(kf.getEstimativa())
