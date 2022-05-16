from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# -------------1st methord-------------
# def index(request):
#     return HttpResponse("yup its works!")


# def index1(request):
#     return HttpResponse("yup its FEBRUARY")


# def index2(request):
#     return HttpResponse("yup its MARCH")


# def index3(request):
#     return HttpResponse("yup its APRIL")


# -------------2nd methord------------------

# def monthly_challanetext(request, month):
#     monthly_text = "none"
#     if month == 'january':
#         monthly_text = "its january very cold"
#     elif month == 'february':
#         monthly_text = "its the month of love"
#     elif month == 'march':
#         monthly_text = "month of exam"

#     else:
#         return HttpResponseNotFound()

#     return HttpResponse(monthly_text)


# def monthlty_challanges_by_num(request, month):
#    return HttpResponse(month)

#  return HttpResponse(num_var)


# -------------3rd methord-------------

monthly_challenges = {"january": "starting of year",
                      "FEBRUARY": "February brings the rain",
                      "March": "March is the month of expectation",
                      "April": "The April winds are magical",
                      "May": "What potent blood hath modest May",
                      "June ": "A cold in the head in June is an immoral thing.",
                      "July": "Hot July brings cooling showers",
                      "August": "August rain: the best of the summer gone",
                      "September": "September: it was the most beautiful of words",
                      "Octobers": "I’m so glad I live in a world where there are Octobers.",
                      "November": "In November, the earth is growing quiet",
                      "December": "God gave us memory so that we might have roses in December",

                      }


def index(request):
   item_list=""
   months = list(monthly_challenges.keys())
   
   for month in months:
           capitalised_month=month.capitalize()
           dynamic_url = reverse("month_challane", args=[month])
           item_list+=f"<li><a href='{dynamic_url}'>{capitalised_month}</a></li>"
   
   response_data=f"<ul>{item_list}</ul>"
   return HttpResponse(response_data)                      

# ------------------1st try

# def monthlty_challanges_by_num(request, month):
#         months=list(monthly_challenges.keys())
#         if month>len(months):
#                 return HttpResponseNotFound("this is not valid")
#         forward_month=months[month-1]

#         return HttpResponseRedirect("/challanges/"+forward_month)


# def monthly_challanetext(request, month):
#     try:
#       monthly_text = monthly_challenges[month]
#       return_data=f"<h1>{monthly_text}</h1>"
#       return HttpResponse( return_data)
#     except:
#         return HttpResponseNotFound("<h1>this month is not supported</h1>")



def monthly_challanetext(request, month):
    try:
        monthly_text = monthly_challenges[month]
        return_data = f"<h1>{monthly_text}</h1>"
        # return_data=render_to_string("challages/challange.html")
        # return HttpResponse(return_data)
        # return render(request,"challages/challange.html")
    except:
        return HttpResponseNotFound("<h1>this page is not found</h1>")


def monthlty_challanges_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>this is not valid</h1>")
    forward_month = months[month-1]
    forward_url = reverse("month_challane", args=[forward_month])
    return HttpResponseRedirect(forward_url)
