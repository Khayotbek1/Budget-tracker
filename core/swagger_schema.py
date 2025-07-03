from drf_yasg.inspectors import SwaggerAutoSchema

class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        return [self.view.__class__.__name__]
