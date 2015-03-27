from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.template import loader, RequestContext
from frontend.email import send_confirmation_message, send_interest_message
from frontend.forms import OrderForm
from frontend.models import Order
import stripe

def get_order(request):
    return Order.objects.get(pk=request.session['order'])

@login_required()
def list(request):
    images = Order.objects.all()
    template = loader.get_template('list.html')
    context = RequestContext(request, {
                       'images': images})
    return HttpResponse(template.render(context))

def order(request):
    stripe.api_key = ''
    try:
        order = get_order(request)
    except KeyError:
        return HttpResponseRedirect(reverse('index'))
    if order.paid:
        return HttpResponseRedirect(reverse('success'))
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
              amount=2500, # amount in cents, again
              currency="usd",
              source=token,
              description=str(order.id)
            )
            send_confirmation_message(order)
            order.paid = True
            order.save()
        except stripe.CardError, e:
          return HttpResponse('The card was not accepted', status=400)
        return HttpResponseRedirect(reverse('success'))
    template = loader.get_template('order.html')
    context = RequestContext(request, {
                       'order': order})
    return HttpResponse(template.render(context))
def index(request):
    previous = False
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            newImage = form.save()
            request.session['order'] = newImage.id
            send_interest_message(newImage)
            return HttpResponseRedirect(reverse('order'))
    else:
        form = OrderForm()
        try:
            get_order(request)
            previous = True
        except KeyError:
            pass
    template = loader.get_template('index.html')
    context = RequestContext(request, {
                       'form': form,
                       'previous': previous})
    return HttpResponse(template.render(context))

def success(request):
    try:
        order = get_order(request)
        if order.paid:
            template = loader.get_template('success.html')
            context = RequestContext(request, {
                               'order': order})
            return HttpResponse(template.render(context))
    except KeyError:
        return HttpResponseRedirect(reverse('index'))