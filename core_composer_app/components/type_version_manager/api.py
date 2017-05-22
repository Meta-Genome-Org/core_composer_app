"""
Type Version Manager API
"""
from core_composer_app.components.type import api as type_api
from core_composer_app.components.type_version_manager.models import TypeVersionManager
from core_composer_app.components.bucket import api as bucket_api
from core_main_app.components.template import api as template_api
from core_main_app.components.version_manager import api as version_manager_api
from core_main_app.components.version_manager.utils import get_latest_version_name


def insert(type_version_manager, type_object, list_bucket_ids=None):
    """Adds a version to a type version manager

    Args:
        type_version_manager:
        type_object:
        list_bucket_ids:

    Returns:

    """
    # save the type in database
    type_api.upsert(type_object)
    try:
        # insert the initial template in the version manager
        version_manager_api.insert_version(type_version_manager, type_object)
        # insert the version manager in database
        version_manager_api.upsert(type_version_manager)
        # Add to the selected buckets
        bucket_api.add_type_to_buckets(type_version_manager, list_bucket_ids)
        # get type display name
        display_name = get_latest_version_name(type_version_manager)
        # update saved template
        template_api.set_display_name(type_object, display_name)
        # update saved type
        return type_version_manager
    except Exception, e:
        type_api.delete(type_object)
        raise e


def get_global_version_managers():
    """Gets all global version managers of a type

    Returns:

    """
    return TypeVersionManager.get_global_version_managers()


def get_version_managers_by_user(user_id):
    """Gets all global version managers of a user

    Returns:

    """
    return TypeVersionManager.get_version_managers_by_user(user_id)


def get_no_buckets_types():
    """Gets list of available types not inside a bucket

    Returns:

    """
    # build list of types
    bucket_types = []
    for bucket in bucket_api.get_all():
        bucket_types += bucket.types

    all_types = get_global_version_managers()
    no_bucket_types = [type_version_manager for type_version_manager in all_types
                       if type_version_manager not in bucket_types]
    return no_bucket_types
