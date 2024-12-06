""" INTERFACES EN PYTHON """

# En las subclases de la interfaz se deben implementar todos los métodos de la interfaz

from abc import ABC, abstractmethod


class PaymentProcess(ABC):

    @abstractmethod
    def paymentProcess(self, amount: float) -> None:
        pass

    @abstractmethod
    def refundProcess(self, transactionId: str) -> None:
        pass


class Paypal(PaymentProcess):

    def paymentProcess(self, amount: float) -> None:
        print(f"Se ha procesado un pago de {amount} por Paypal")

    def refundProcess(self, transactionId: str) -> None:
        print(f"Se ha realizado un reembolso a la transacción {transactionId} ")


class Strip(PaymentProcess):

    def paymentProcess(self, amount: float) -> None:
        print(f"Se ha procesado un pago de {amount} por Stripe")

    def refundProcess(self, transactionId: str) -> None:
        print(f"Se ha realizado un reembolso a la transacción {transactionId} ")


if __name__ == "__main__":

    paypalProcess = Paypal()
    stripeProcess = Strip()

    paypalProcess.paymentProcess(500.0)
    paypalProcess.refundProcess("ALSKDJHLAKSJD")

    stripeProcess.paymentProcess(1000.0)
    stripeProcess.refundProcess("ÑLKAJHDÑVKAJ")
