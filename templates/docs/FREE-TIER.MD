# Services with a free service plan

This page lists all SAP BTP services with a free service plan.

{% for category in btpservicelist -%}{%- for service in category.list -%}{%- for plan in service.servicePlans -%}{% if 'free' in plan.name %}- [{{ service.name }}](services/{{ service.name }}.md) has the service plan **{{ plan.name }}**
{% endif %}{% endfor %}
{%- endfor -%}
{%- endfor -%}
