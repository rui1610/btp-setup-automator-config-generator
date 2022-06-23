# Services with a free service plan

This lists shows all SAP BTP services with a free service plan:
{% for category in services %}
# {{ category.name }}

{% for service in category.list -%}{%- for plan in service.servicePlans -%}{% if 'free' in plan.name %}- [{{ service.name }}](services/{{ service.name }}.md) (plan **{{ plan.name }})**
{% endif %}{% endfor %}
{%- endfor -%}
{%- endfor -%}
