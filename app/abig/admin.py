from django.contrib.admin import AdminSite

class SuperAdminSite(AdminSite):
    site_header = 'STATUS Админ панель'
    site_title ='Панель администратора STATUS'
    index_title = 'Администратор'


class ManagerAdminSite(AdminSite):
    site_header = 'STATUS Админ панель'
    site_title ='Панель менеджера STATUS'
    index_title = 'Менеджер'


admin_site = SuperAdminSite(name='admin')
manager_site = SuperAdminSite(name='manager')