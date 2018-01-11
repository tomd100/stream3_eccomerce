from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page. 
    """
    
    # Load the session variable cart (a dictionary) into a local variable cart
    cart = request.session.get('cart', {})
    
    # Convert the dictionary of product Id: Quantity into a list of 
    # cart items. These expanded cart items include not just the ID and Qty,
    # But also the full product.
    
    # The list to host the cart items
    cart_items = []
    
    # The total cost of the cart
    total = 0
    
    # The number of products in the cart 
    product_count = 0
    
    #For each item in the ID:QTY dictionary
    for id, quantity in cart.items():
        #Load the product
        product = get_object_or_404(Product, pk=id)
        # Increment the total
        total += quantity * product.price
        # Incrememebnt the overall quantity
        product_count += quantity
        # Append the inflated cart item (Id, Quantity, Product) to the cart items list
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})


    # Return the cart items along with the total cost and total quantity
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }