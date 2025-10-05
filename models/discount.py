class Discount:
    """Represents a discount with a description and percentage."""

    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    def __repr__(self):
        return f"Discount(description=\"{self.description}\", discount_percent={self.discount_percent})"

    def apply(self, price: float) -> float:
        """Calculates the discount amount based on the price."""
        return Discount.apply_discount(price, self.discount_percent)

# STATIC MEMBERS

    __DISCOUNT_SEASONAL: float = 10.0  # private static attribute for seasonal discount percentage
    __DISCOUNTS_PROMO: dict[str, float] = {  # private static attribute for promotional discounts
        "black friday": 20.0,
        "cyber monday": 15.0,
        "christmas": 25.0,
        "new year": 30.0,
    }

    @staticmethod
    def apply_discount(price: float, discount_percent: float) -> float:
        """Calculates the discount amount based on the price and discount percentage."""
        return (1.0 - discount_percent / 100) * price

    @staticmethod
    def apply_seasonal_discount(price: float) -> float:
        """Calculates the discount amount based on the price and discount percentage."""
        return (1.0 - Discount.__DISCOUNT_SEASONAL / 100) * price

    @staticmethod
    def apply_promo_discount(price: float, promo_code: str) -> float:
        """Calculates the discount amount based on the price and discount percentage."""
        discount_percent = Discount.__DISCOUNTS_PROMO.get(promo_code.lower(), 0.0)
        return (1.0 - discount_percent / 100) * price
