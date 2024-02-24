# Homework 3: Grocery Store

_For instructions on how to complete this assignment, see [here](https://github.com/Tech-at-DU/ACS-1220-Authentication-and-Associations/blob/master/Assignments/grocery-store-part-2.md)._

## Setup

Clone this repository to your computer.

**Take a look at the code** - it looks a bit different than what you're used to. Namely, the code is now separated out into several files rather than being written in a single `app.py` file. Since we're now writing model and form code as well as route code, this will help us to maintain some structure and separation.

**To run the code**, navigate to the project folder and run the following to create a virtual environment and install the required packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then rename the `.env.example` file as `.env`:

```
cp .env.example .env
```

Then you can run the server:

```
python app.py
```

#### Dummy Data

**Stores**

Trader Joe's

1147 S Wabash Ave, Chicago, IL 60605

Whole Foods

1550 N Kingsbury St, Chicago, IL 60642

**Grocery Items**

Happy Trekking Trail Mix

7.99

Pantry

https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQFQ16emV3jQNLcr9kCpVUrYcJu7ltrDCIYVpzR5AG6h_5LZ1sTTNNxmvh1I05oJMGL9IgN3HxJLAUwD5KDv39nL7TBvzGB6EiWM-uFU-B-6P7pBCYN9BvAsCuCw_0K7dWi0b6mxQ&usqp=CAc

Trader Joe's

---

Justin's Classic Almond Butter

12.99

Pantry

https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTZVWlDJrgeCNGRliS-O-O8xA8NyjRtwfsglDDeQpeNeRaenyraZsiFO6AcAqkn6FzdQ7IVVH__3joid0FC5FoLQuZc2ZNCTqsdIdIny9QMlYChEDDR92XNY_EVhn5Uz8vWwoNsbDtS2pI&usqp=CAc

Whole Foods
