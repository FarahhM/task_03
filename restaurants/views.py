from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[{"resturant_name":"Ubon",
               "food_type":"Thai"
               },
               {"resturant_name":"Katsuya",
               "food_type":"Japanese"
               },
               {"resturant_name":"Melenzane",
               "food_type":"Italian"
               },

    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"resturant_name":"Melenzane",
               "food_type":"Italian"
               }

    }
    return render(request, 'detail.html', context)
