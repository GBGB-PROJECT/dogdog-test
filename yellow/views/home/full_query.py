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
    
class Product:
    #############################################
    # pet product
    #############################################
    
    product_list_query\
        = """
        SELECT product_id, product_name
        FROM "OPD".product
        ORDER BY product_name ASC
        """

    product_search_query\
        = """
        SELECT product_id, product_name
        FROM "OPD".product
        WHERE LOWER(product_name) LIKE LOWER(%s)
        ORDER BY product_name ASC
        """