<img src="data:{{ service.iconFormat }};base64, {{ service.icon }}" alt="Icon for {{ service.name }}" width="80px" />
# {{ service.displayName }} (technical name: **{{ service.name }}**

Service category: **{{ category.name }}**

## Additional details
{% for link in service.links %}
- [{{ link.title }}]({{ link.linkURL }})
{%- endfor %}

## Service availability

| Plan name | Display name | Data center availability  |
|------|----------------|---------------------------|
{%- for plan in service.servicePlans %}
|  {{ plan.name }}  |  {{ plan.displayName }}  |  {%- for datacenter in plan.dataCenters %} {{ datacenter.region }} - {{ datacenter.displayName }}{% if not loop.last %}<br>{% endif %} {%- endfor %}  |
{%- endfor %}

## Sample configuration of **{{ service.displayName }}** for btp-setup-automator

The [btp-setup-automator](https://github.com/SAP-samples/btp-setup-automator) helps you setting up your SAP BTP account for a specific use case. Each use case is defined inside a `usecase.json` file listing all the services necessary to cover that use case. You can find a list of released use cases in the [usecase folder of bpt-setup-automator](https://github.com/SAP-samples/btp-setup-automator/tree/main/usecases).

You can setup a service instance for **{{ service.name }}** by configuring your `usecase.json` file.
{% for plan in service.servicePlans %}
### Using the service plan **{{ plan.name }}**{% if plan.name != plan.displayName %} ({{ plan.displayName }}){% endif %}

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json",
  "services": [
    {
      "category": "{{ category.name }}",
      "name": "{{ service.name }}",
      "plan": "{{ plan.name }}"{% if plan.jsonschemaproperties is defined %},
      "parameters": {
        {% for item in plan.jsonschemaproperties.properties %}
          "{{ item }}" : {{ plan.jsonschemaproperties.properties[item].get('default') | tojson}}{% if not loop.last %}, {% endif %}
        {%- endfor %}
      }{% endif %}
    }
  ]
}
```
{% endfor %}
## Related categories
{% for serviceCategory in service.serviceCategories %}
- {{ serviceCategory }}
{%- endfor %}
{%- for businessCategory in service.businessCategories %}
- {{ businessCategory }}
{% endfor %}
