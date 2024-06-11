

def introspection_info(obj):
    obj_type_info = type(obj).__name__   # типа объекта
    attributes_info = dir(obj)   # атрибутов объекта
    methods_info = [method for method in attributes_info if callable(getattr(obj, method))]   # Получение методов объекта
    module_info = obj.__class__.__module__   # Модуль обьекта
    info = {'type': obj_type_info, 'attributes': attributes_info, 'methods': methods_info, 'module': module_info},
    # Словарь с информацией

    return info


number_info = introspection_info(42)
print(number_info)

