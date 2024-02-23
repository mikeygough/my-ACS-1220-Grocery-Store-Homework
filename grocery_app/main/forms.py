from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    SelectField,
    SubmitField,
    FloatField,
)
from wtforms.fields.html5 import URLField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, NumberRange
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField(
        "Grocery Store Title",
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=80,
                message="Your grocery store needs a title between 2 and 80 characters.",
            ),
        ],
    )

    address = StringField(
        "Grocery Store Address",
        validators=[
            DataRequired(),
            Length(
                min=5,
                max=200,
                message="Your grocery store needs an address between 5 and 200 characters.",
            ),
        ],
    )

    submit = SubmitField("Submit")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField(
        "Grocery Item Name",
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=80,
                message="Your grocery store item needs a name between 2 and 80 characters.",
            ),
        ],
    )

    price = FloatField(
        "Grocery Store Item Price",
        validators=[
            DataRequired(),
            NumberRange(
                min=0,
                message="Your grocery store item needs a minimum price of at least 0.",
            ),
        ],
    )

    category = SelectField(
        "Grocery Store Item Category", choices=ItemCategory.choices()
    )

    photo_url = URLField(
        "Grocery Store Item Photo URL",
    )

    store = QuerySelectField(
        "Grocery Store", query_factory=lambda: GroceryStore.query, allow_blank=False
    )

    submit = SubmitField("Submit")
