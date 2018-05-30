# from nami.models import CustomUser as User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class MyUserChangeForm(UserChangeForm):

#     class Meta:
#         model = get_user_model()

# class MyUserCreationForm(UserCreationForm):

#     class Meta:
#         model = get_user_model()

#     def clean_username(self):
#         username = self.cleaned_data["username"]
#         try:
#             get_user_model().objects.get(username=username)
#         except get_user_model().DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])

# class MyUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     fieldsets = (
#         (None, {'fields': [('username', 'password'),]}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                    'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         )

# admin.site.register(MyUser, MyUserAdmin)
