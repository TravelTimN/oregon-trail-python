# https://stackoverflow.com/a/41852266

# what the emigrant "wants" (take from player)
wants_choices = [
    {
        "item": "nobody",
    },
    {
        "qty": 1,
        "item": "ox",
        "inventory_name": "oxen"
    },
    {
        "qty": 1,
        "item": "set of clothing",
        "inventory_name": "clothing"
    },
    {
        "qty": 1,
        "item": "wagon axle",
        "inventory_name": "axles"
    },
    {
        "qty": 1,
        "item": "wagon tongue",
        "inventory_name": "tongues"
    },
    {
        "qty": 1,
        "item": "wagon wheel",
        "inventory_name": "wheels"
    },
    {
        "qty": 100,
        "item": "pounds of food",
        "inventory_name": "food"
    },
    {
        "qty": 100,
        "item": "bullets",
        "inventory_name": "bullets"
    },
    {
        "qty": 2,
        "item": "wagon tongues",
        "inventory_name": "tongues"
    },
    {
        "qty": 2,
        "item": "wagon wheels",
        "inventory_name": "wheels"
    },
    {
        "qty": 3,
        "item": "sets of clothing",
        "inventory_name": "clothing"
    },
    {
        "qty": 3,
        "item": "wagon wheels",
        "inventory_name": "wheels"
    },
    {
        "qty": 4,
        "item": "sets of clothing",
        "inventory_name": "clothing"
    },
    {
        "qty": 4,
        "item": "wagon tongues",
        "inventory_name": "tongues"
    },
    {
        "qty": 4,
        "item": "wagon wheels",
        "inventory_name": "wheels"
    },
]

# ratios/weights of the items above
want_weights = [0.2, 0.1, 0.08, 0.03, 0.16, 0.1, 0.03, 0.07, 0.03, 0.05, 0.02, 0.02, 0.01, 0.01, 0.02]  # noqa

# gender of the emigrant
gender_choices = ["He", "She"]
# ratio/weights of the emigrant gender
gender_weights = [0.75, 0.25]

# what the emigrant will "trade" in return (give to player)
gives_choices = [
    {
        "qty": 1,
        "item": "ox",
        "inventory_name": "oxen"
    },
    {
        "qty": 1,
        "item": "set of clothing",
        "inventory_name": "clothing"
    },
    {
        "qty": 1,
        "item": "wagon axle",
        "inventory_name": "axles"
    },
    {
        "qty": 1,
        "item": "wagon wheel",
        "inventory_name": "wheels"
    },
    {
        "qty": 1,
        "item": "bullets",
        "inventory_name": "bullets"
    },
    {
        "qty": 1,
        "item": "pounds of food",
        "inventory_name": "food"
    }
]

# ratios/weights of the items above
gives_weights = [0.12, 0.17, 0.03, 0.01, 0.17, 0.16]
