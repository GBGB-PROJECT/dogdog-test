class Breed:
    #############################################
    # pet breed
    #############################################

    breed_list_query\
        = """
        SELECT breed_id, breed
        FROM "Companion".breed
        ORDER BY breed ASC
        """

    breed_search_query\
        = """
        SELECT breed_id, breed
        FROM "Companion".breed
        WHERE LOWER(breed) LIKE LOWER(%s)
        ORDER BY breed ASC
        """