"""Create database models to represent tables."""
from grocery_app import db
from flask_login import UserMixin
from sqlalchemy_utils import URLType
from grocery_app.utils import FormEnum


class ItemCategory(FormEnum):
    """Categories of grocery items."""

    PRODUCE = "Produce"
    DELI = "Deli"
    BAKERY = "Bakery"
    PANTRY = "Pantry"
    FROZEN = "Frozen"
    OTHER = "Other"


class GroceryStore(db.Model):
    """Grocery Store model."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    items = db.relationship("GroceryItem", back_populates="store")
    created_by = db.relationship("User")

    def __str__(self):
        return f"<Grocery Store: {self.title}, {self.address}>"

    def __repr__(self):
        return f"<Grocery Store: {self.title}, {self.address}>"


class GroceryItem(db.Model):
    """Grocery Item model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(db.Integer, db.ForeignKey("grocery_store.id"), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    store = db.relationship("GroceryStore", back_populates="items")
    created_by = db.relationship("User")

    def __str__(self):
        return f"<Item: {self.name}, {self.price}, {self.category}>"

    def __repr__(self):
        return f"<Item: {self.name}, {self.price}, {self.category}>"


class User(UserMixin, db.Model):
    """User model."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
