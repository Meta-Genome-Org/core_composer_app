"""Url router for the administration site
"""
from django.contrib import admin
from django.conf.urls import url

from views.admin import views as admin_views, ajax as admin_ajax


admin_urls = [
    url(r'^types$', admin_views.manage_types,
        name='core_composer_app_types'),
    url(r'^type/upload$', admin_views.upload_type,
        name='core_composer_app_upload_type'),
    url(r'^type/upload/(?P<version_manager_id>\w+)', admin_views.upload_type_version,
        name='core_composer_app_upload_type_version'),
    url(r'^type/versions/(?P<version_manager_id>\w+)', admin_views.manage_type_versions,
        name='core_composer_app_manage_type_versions'),
    url(r'^type/buckets/(?P<version_manager_id>\w+)', admin_views.manage_type_buckets,
        name='core_composer_app_type_buckets'),

    url(r'^buckets$', admin_views.manage_buckets,
        name='core_composer_app_buckets'),
    url(r'^bucket/upload$', admin_views.upload_bucket,
        name='core_composer_app_upload_bucket'),
    url(r'^bucket/delete$', admin_ajax.delete_bucket,
        name='core_composer_app_delete_bucket'),
    url(r'^type/resolve-dependencies', admin_ajax.resolve_dependencies,
        name='core_composer_app_resolve_dependencies'),
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls