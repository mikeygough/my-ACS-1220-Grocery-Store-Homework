from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.main.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################


@main.route("/")
def homepage():
    all_stores = GroceryStore.query.all()

    return render_template("home.html", all_stores=all_stores)


@main.route("/new_store", methods=["GET", "POST"])
def new_store():
    # new form
    form = GroceryStoreForm()

    # if form was submitted with no errors
    if form.validate_on_submit():
        new_store = GroceryStore(
            title=form.title.data,
            address=form.address.data,
        )

        db.session.add(new_store)
        db.session.commit()

        flash("New grocery store was created successfully.")
        return redirect(url_for("main.store_detail", store_id=new_store.id))

    return render_template("new_store.html", form=form)


@main.route("/new_item", methods=["GET", "POST"])
def new_item():
    # new form
    form = GroceryItemForm()

    # if form was submitted with no errors
    if form.validate_on_submit():
        new_item = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data,
        )
        item = db.session.merge(new_item)
        db.session.add(item)
        db.session.commit()
        flash("New item was created successfully.")
        return redirect(url_for("main.item_detail", item_id=item.id))
    return render_template("new_item.html", form=form)


@main.route("/store/<store_id>", methods=["GET", "POST"])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)

    # check if valid
    if form.validate_on_submit():
        # update values
        store.title = form.title.data
        store.address = form.address.data

        db.session.commit()

        flash("Store updated successfully.")
        return redirect(url_for("main.store_detail", store_id=store.id))

    return render_template("store_detail.html", store=store, form=form)


@main.route("/item/<item_id>", methods=["GET", "POST"])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)

    # check if valid
    if form.validate_on_submit():
        # update values
        item.name = form.name.data
        item.price = form.price.data
        item.category = form.category.data
        item.photo_url = form.photo_url.data
        item.store = form.store.data

        db.session.commit()

        flash("Item updated successfully.")
        return redirect(url_for("main.item_detail", item_id=item.id))

    return render_template("item_detail.html", item=item, form=form)
