# coding=utf-8
import numpy as np

# Esse codigo é nosso, só o comentario do commit que foi automatico (igual do ultimo).
# The Error from Laser is 30 mm


class KF(object):

    KalmanGain = 0
    Estimativa = 0
    ErroDaEstimativa = 0

    def __init__ (self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido, ValorEstimadoAnterior, ErroDoValorEstimadoAnterior):

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

