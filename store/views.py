from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Stock
from .forms import (
        StockCreateForm,
        StockUpdateForm,
        IssueForm,
        ReceiveForm
        )
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

def stock_list(request):
    queryset = Stock.objects.all().order_by('location', 'container_id')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
            'page_obj': page_obj
            }

    query = request.GET.get('q')
    if query:
        queryset = Stock.objects.filter(
                Q(color__icontains=query) |
                Q(category__icontains=query) |
                Q(stock_code__icontains=query) |
                Q(condition__icontains=query) |
                Q(location__icontains=query) |
                Q(container_id__icontains=query) |
                Q(quantity__icontains=query) |
                Q(size__icontains=query) |
                Q(shelf_id__icontains=query) 
                )
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj
            }
    return render(request, "store/stock_list.html", context)  


def stock_create(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item Added')
        return redirect(stock_create)
    context = {
            "form": form,
            "title": "Add Stock Item"
            }
    return render(request, "store/stock_create.html", context)


def stock_update(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Updated')
            return redirect(stock_list)
    context = {
            'form':form
	}
    return render(request, "store/stock_update.html", context)


def stock_delete(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Item Deleted')
        return redirect(stock_list)
    return render(request, 'store/stock_delete.html')


def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
            "title": queryset.category,
            "color": queryset.color,
            "queryset": queryset,
            }
    return render(request, "store/stock_detail.html", context)


def stock_issue(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.issue_quantity <= instance.quantity:
            instance.quantity -= instance.issue_quantity
            # instance.issue_by = str(request.user)
            messages.success(request, "Issued successfully. " +
                    str(instance.quantity) + " " +
                    str(instance.unit) + " now left in Store")
            instance.save()
            return redirect(stock_list)
		# return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.success(request, "Not enough " + str(instance.category))
            return redirect(stock_list)

    context = {
            "title": 'Issue ' + str(queryset.category),
            "queryset": queryset,
            "form": form,
            # "username": 'Issue By: ' + str(request.user),
	}
    return render(request, "store/stock_issue.html", context)


def stock_receive(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.receive_quantity
        instance.save()
        messages.success(request, "Received successfully. " +
                str(instance.quantity) + " " +
                str(instance.unit)+" now in Store")
        return redirect(stock_list)
		# return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "title": 'Receive ' + str(queryset.category),
            "instance": queryset,
            "form": form,
            }
    return render(request, "store/stock_receive.html", context)
