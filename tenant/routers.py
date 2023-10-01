class TenantRouter:
    """
    A router to route database requests based on the tenant.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read from the tenant's database.
        """
        tenant = get_current_tenant()
        if tenant:
            return tenant.database

    def db_for_write(self, model, **hints):
        """
        Attempts to write to the tenant's database.
        """
        tenant = get_current_tenant()
        if tenant:
            return tenant.database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure migrations are only applied to the tenant's database.
        """
        tenant = get_current_tenant()
        if tenant:
          return db == tenant.database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the same tenant's database.
        """
        if obj1._meta.app_label == 'your_app' and obj2._meta.app_label == 'your_app':
            tenant1 = get_tenant_from_obj(obj1)
            tenant2 = get_tenant_from_obj(obj2)
            return tenant1 == tenant2
        return None