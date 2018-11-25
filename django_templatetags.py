from django import template
register = template.Library()

# django template filter to add attributes to html tags
# format:
# form.field|add_attrs:"attr=value,attr=value...."
#
# example of use:
# {% for field in form %}
#  {{ field|add_attrs:"class=my_class,style=color:red"}}
# {% endfor %}


@register.filter
def add_attrs(field, attrs):
    new_attrs = {}
    attrs = attrs.split(",")
    for attr in attrs:
        attr_name, attr_value = attr.split("=")
        old_attr_value = field.field.widget.attrs.get(attr_name, None)
        if old_attr_value:
            new_attr_value = old_attr_value + ' ' + attr_value  
        else:
            new_attr_value = attr_value
        new_attrs[attr_name]=new_attr_value
    return field.as_widget(attrs=new_attrs)
