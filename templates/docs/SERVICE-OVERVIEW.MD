{% for category in services %}
# All services of category {{ category.name }}

Services are listed and sorted by their technical name. The display name is added in parentheses.
{% for service in category.list %}
- [{{ service.name }}](services/{{ service.name }}.md) ({{ service.displayName }})
{%- endfor %}
{% endfor %}