import os
import django

# 1. SET UP DJANGO ENVIRONMENT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_project.settings')
django.setup()

from food_delivery_app.models import Restaurant, Food_Items

def seed_data():
    print("--- Starting Database Seeding ---")
    
    # 2. Clean up old data to ensure a fresh, professional look
    Restaurant.objects.all().delete()
    Food_Items.objects.all().delete()

    # 3. CREATE RESTAURANTS
    burger_lab = Restaurant.objects.create(
        name="The Burger Lab",
        category="Non-Veg",
        image="restaurants/burger_lab.png"
    )

    milanese = Restaurant.objects.create(
        name="Milanese Garden",
        category="Veg",
        image="restaurants/milanese_garden.png"
    )

    wok_roll = Restaurant.objects.create(
        name="Wok & Roll",
        category="Both",
        image="restaurants/wok_and_roll.png"
    )

    # 4. CREATE FOOD ITEMS
    # Burger Lab Menu
    Food_Items.objects.create(
        restaurant=burger_lab,
        food_name="Black Truffle Slider",
        food_description="Double wagyu beef with shaved black truffles and melted swiss.",
        food_price=850,
        food_image="food_image/truffle_burger.png"
    )
    Food_Items.objects.create(
        restaurant=burger_lab,
        food_name="Lab Fries",
        food_description="Hand-cut fries with rosemary salt and signature dip.",
        food_price=250,
        food_image="food_image/truffle_burger.png"
    )

    # Milanese Garden Menu
    Food_Items.objects.create(
        restaurant=milanese,
        food_name="Margherita Royale",
        food_description="Buffalo mozzarella, fresh basil, and San Marzano tomatoes.",
        food_price=650,
        food_image="food_image/margherita_pizza.png"
    )
    Food_Items.objects.create(
        restaurant=milanese,
        food_name="Pesto Gnocchi",
        food_description="Soft pillows of potato pasta in home-made Genovese pesto.",
        food_price=580,
        food_image="food_image/margherita_pizza.png"
    )

    # Wok & Roll Menu
    Food_Items.objects.create(
        restaurant=wok_roll,
        food_name="Imperial Miso Ramen",
        food_description="48-hour broth, soy-marinated egg, and tender chasu pork.",
        food_price=720,
        food_image="food_image/miso_ramen.png"
    )
    Food_Items.objects.create(
        restaurant=wok_roll,
        food_name="Crispy Gyoza",
        food_description="Pork and cabbage dumplings pan-seared to perfection.",
        food_price=390,
        food_image="food_image/miso_ramen.png"
    )

    print("--- Database successfully seeded with Gourmet Data! ---")

if __name__ == "__main__":
    try:
        seed_data()
    except Exception as e:
        print(f"Error during seeding: {e}")
