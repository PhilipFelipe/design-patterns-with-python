"""
O Padrão de Projeto State é um padrão comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. Parecerá como se o objeto mudasse de classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass


class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("PaymentPending: The order is already in pending payment state.")

    def approve(self) -> None:
        self.order.state = PaymentApprove(self.order)
        print("PaymentPending: The order is now in approve payment state.")

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print("PaymentPending: The order is now in reject payment state.")


class PaymentApprove(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("PaymentApprove: The order is now in pending payment state.")

    def approve(self) -> None:
        print("PaymentApprove: The order is already in approve payment state.")

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print("PaymentApprove: The order is now in reject payment state.")


class PaymentReject(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("PaymentReject: The order can't be moved to pending payment state.")

    def approve(self) -> None:
        print("PaymentReject: The order can't be moved to approved payment state.")

    def reject(self) -> None:
        print("PaymentReject: The order is already in reject payment state.")


class Order:
    """Context"""

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self) -> None:
        self.state.approve()

    def reject(self) -> None:
        self.state.reject()


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.reject()
    order.reject()
    order.pending()
    order.approve()
