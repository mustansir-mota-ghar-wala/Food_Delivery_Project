import os
import django
import random

# 1. SET UP
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_project.settings')
django.setup()

from food_delivery_app.models import Restaurant, Food_Items

def mass_seed():
    print("--- Starting Massive Database Seeding (100 Restaurants / 2000 Dishes) ---")
    
    # Clean up
    Restaurant.objects.all().delete()
    Food_Items.objects.all().delete()

    # Naming Pools
    adjectives = ["Gilded", "Rustic", "Spicy", "Velvet", "Golden", "Alpine", "Urban", "Saffron", "Azure", "Noble", "Wild", "Mellow", "Crispy", "Lunar", "Hidden", "Secret", "Artisan", "Vintage", "Solar", "Ocean", "Grand", "Little", "Blue", "Black", "Royal"]
    nouns = ["Bistro", "Kitchen", "Lab", "Pantry", "Studio", "Garden", "Table", "Corner", "Grill", "House", "Dinery", "Point", "Deck", "Roost", "Square", "Way", "Junction", "Market", "Vault", "Cellar"]
    cuisines = ["Pizza", "Burgers", "Sushi", "Tacos", "Noodles", "Steaks", "Curry", "Pasta", "Bakery", "Salads"]
    
    # Image Pools
    res_images = [
        "restaurants/burger_lab.png",
        "restaurants/milanese_garden.png",
        "restaurants/wok_and_roll.png",
        "restaurants/sushi_den.png",
        "restaurants/taco_fiesta.png",
        "restaurants/green_leaf.png"
    ]
    food_images = [
        "food_image/truffle_burger.png",
        "food_image/margherita_pizza.png",
        "food_image/miso_ramen.png",
        "food_image/sushi_platter.png",
        "food_image/street_tacos.png",
        "food_image/vegan_bowl.png"
    ]

    food_adjectives = ["Classic", "Imperial", "Gourmet", "Signature", "Double", "Roasted", "Smoked", "Garlic", "Spicy", "Honey", "Truffle", "Zesty", "Creamy", "Crispy", "Savory"]
    
    all_restaurants = []
    
    # CREATE 100 RESTAURANTS
    for i in range(1, 101):
        name = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(cuisines)}"
        if i == 1: name = "Global Food Hub" # One fixed for testing
        
        category = random.choice(["Veg", "Non-Veg", "Both"])
        image = random.choice(res_images)
        
        res = Restaurant(name=name, category=category, image=image)
        all_restaurants.append(res)
    
    # Save restaurants
    Restaurant.objects.bulk_create(all_restaurants)
    created_restaurants = Restaurant.objects.all()
    
    # CREATE 2000 FOOD ITEMS (20 per restaurant)
    all_food = []
    for res in created_restaurants:
        res_cuisine = res.name.split()[-1] # Get the cuisine type from name
        
        for j in range(1, 21):
            fname = f"{random.choice(food_adjectives)} {res_cuisine} {j}"
            desc = f"A delicious {fname} prepared with fresh ingredients at {res.name}."
            price = random.randint(150, 1200)
            fimage = random.choice(food_images)
            
            food = Food_Items(
                restaurant=res,
                food_name=fname,
                food_description=desc,
                food_price=price,
                food_image=fimage
            )
            all_food.append(food)
    
    # Bulk save food
    Food_Items.objects.bulk_create(all_food)
    
    print(f"--- SUCCESS: Created {Restaurant.objects.count()} Restaurants and {Food_Items.objects.count()} Food Items! ---")

if __name__ == "__main__":
    mass_seed()
