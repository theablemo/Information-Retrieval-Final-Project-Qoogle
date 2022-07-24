from django.shortcuts import render

from information_retrieval.forms import QueryForm


def search_query(request):
    error = None
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, request.FILES)
        expense_form.fields['payer'].queryset.queryset = selected_group.members.all()
        expense_form.fields['group'].widget = forms.HiddenInput()
        member_share_form_set = MemberShareFormSet(request.POST)
        for form in member_share_form_set:
            assert isinstance(form, MemberShareForm)
            form.fields['user'].queryset = selected_group.members.all()
        if expense_form.is_valid() and member_share_form_set.is_valid():
            try:
                with transaction.atomic():
                    expense = expense_form.save()
                    member_shares = member_share_form_set.save()
                    for member_share in member_shares:
                        member_share.set_expense(expense)
                        user_group_net, _ = UserGroupNet.objects.get_or_create(user=member_share.user.user,
                                                                               group=expense.group)
                        user_group_net.add_net_value(-member_share.get_amount())
                    expense.is_valid()
                    if expense.group.is_for_two_member:
                        ids = list(map(int, expense.group.name.split('_')))
                        if ids[0] == int(request.user.profile.id):
                            id = ids[1]
                        else:
                            id = ids[0]
                        return redirect(f'/app/friends/{id}')
                    return redirect(f'/app/groups/{expense.group.id}')
            except ValidationError as ve:
                error = ve.message
        else:
            print(expense_form.errors, member_share_form_set.errors)
            error = "Please fill the form correctly!"

    form = QueryForm()
    return render(request, 'search_bar.html', {'form': form,
                                                  'error': error})

def search_results(request):
    error = None
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, request.FILES)
        expense_form.fields['payer'].queryset.queryset = selected_group.members.all()
        expense_form.fields['group'].widget = forms.HiddenInput()
        member_share_form_set = MemberShareFormSet(request.POST)
        for form in member_share_form_set:
            assert isinstance(form, MemberShareForm)
            form.fields['user'].queryset = selected_group.members.all()
        if expense_form.is_valid() and member_share_form_set.is_valid():
            try:
                with transaction.atomic():
                    expense = expense_form.save()
                    member_shares = member_share_form_set.save()
                    for member_share in member_shares:
                        member_share.set_expense(expense)
                        user_group_net, _ = UserGroupNet.objects.get_or_create(user=member_share.user.user,
                                                                               group=expense.group)
                        user_group_net.add_net_value(-member_share.get_amount())
                    expense.is_valid()
                    if expense.group.is_for_two_member:
                        ids = list(map(int, expense.group.name.split('_')))
                        if ids[0] == int(request.user.profile.id):
                            id = ids[1]
                        else:
                            id = ids[0]
                        return redirect(f'/app/friends/{id}')
                    return redirect(f'/app/groups/{expense.group.id}')
            except ValidationError as ve:
                error = ve.message
        else:
            print(expense_form.errors, member_share_form_set.errors)
            error = "Please fill the form correctly!"

    form = QueryForm()
    return render(request, 'search_bar.html', {'form': form,
                                                  'error': error})
