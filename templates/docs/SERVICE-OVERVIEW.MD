# Overview

This page shows how to re-use data that was extracted by the [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) using the BTP CLI. All information is extracted from the [central json file of the btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator/blob/main/config/btp-base/entitledServices.json).

## Services with a free service plan

This lists shows all SAP BTP services with a free service plan:

{% for category in btpservicelist -%}{%- for service in category.list -%}{%- for plan in service.servicePlans -%}{% if 'free' in plan.name %}- [{{ service.name }}](services/{{ service.name }}.md) has the service plan **{{ plan.name }}**
{% endif %}{% endfor %}
{%- endfor -%}
{%- endfor -%}

{%- for category in btpservicelist %}
## All services of category {{ category.name }}

Services are listed and sorted by their technical name. The display name is added in parentheses.
{% for service in category.list %}
- [{{ service.name }}](services/{{ service.name }}.md)
{%- endfor %}

{%- endfor %}