import pickle


TREE = {
    'name': 'ТЕЛО',
    'ves': 30,
    'elements': [
        {
            'name': 'Голова',
            'elements': [
                {
                    'name': 'Глаза'
                }
            ]
        },
        {
            'name': 'Рука'
        }
    ]
}

# Тело
# |
# --- Голова
#       |
#       --- Глаза


pickle.dump(TREE, open('read_write.data', 'wb'))