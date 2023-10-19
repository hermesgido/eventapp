from .models import Event

def seed_data():
    events_data = [
    {
        "name": "Serengeti Adventure",
        "location": "Serengeti Park, Tanzania",
        "price": "15000",
        "time": "2023-11-15 08:00:00",
        "maximum_people": 50,
        "hosts": "Tanzania Adventures",
        "description": "Embark on a thrilling safari adventure in the heart of the Serengeti. Witness the incredible wildlife, stunning landscapes, and unforgettable moments."
    },
    {
        "name": "Zanzibar Retreat",
        "location": "Zanzibar, Tanzania",
        "price": "2500",
        "time": "2023-12-02 10:00:00",
        "maximum_people": 40,
        "hosts": "Zanzibar Getaways",
        "description": "Relax on the pristine beaches of Zanzibar. Enjoy crystal-clear waters, cultural experiences, and a tranquil beachfront retreat."
    },
    {
        "name": "Kilimanjaro Expedition",
        "location": "Kilimanjaro Tanzania",
        "price": "3000",
        "time": "2024-01-10 06:30:00",
        "maximum_people": 20,
        "hosts": "Kilimanjaro Explorers",
        "description": "Conquer the highest peak in Africa. Join us on an epic journey to the summit of Mount Kilimanjaro and witness breathtaking views."
    },
    {
        "name": "Cultural Festival",
        "location": "Arusha, Tanzania",
        "price": "6000",
        "time": "2024-02-20 14:00:00",
        "maximum_people": 100,
        "hosts": "Arusha Cultural Society",
        "description": "Celebrate the rich culture and heritage of Tanzania at this vibrant cultural festival. Enjoy traditional music, dance, and cuisine."
    },
    {
        "name": "Ngorongoro Crater",
        "location": "Ngorongoro Tanzania",
        "price": "$250",
        "time": "2024-03-15 09:30:00",
        "maximum_people": 30,
        "hosts": "Ngorongoro Adventures",
        "description": "Explore the unique Ngorongoro Crater, a UNESCO World Heritage Site. Encounter diverse wildlife and stunning landscapes."
    },
    {
        "name": "Wildlife Photography Tour",
        "location": "Manyara, Tanzania",
        "price": "50000",
        "time": "2024-04-05 07:45:00",
        "maximum_people": 25,
        "hosts": "Wildlife Captures",
        "description": "Capture the beauty of Tanzanian wildlife on a photography tour. Get up close to majestic animals and picturesque landscapes."
    },
    ]

    for event_data in events_data:
        event = Event(
            name=event_data["name"],
            location=event_data["location"],
            price=event_data["price"],
            time=event_data["time"],
            maximum_people=event_data["maximum_people"],
            hosts=event_data["hosts"],
            description=event_data["description"],
        )
        event.save()


if __name__ == '__main__':
    seed_data()