from urllib.parse import quote

def build_afas_query_params(filters):
    def _build(filters, date_fields=None):
        params = "skip=-1&take=-1"
        if filters:
            fields = [f["field"] for f in filters]
            separator = ";" if len(set(fields)) == 1 else ","
            field_ids = separator.join(fields)
            values = separator.join([
                quote(f"{f['value']}T00:00:00", safe="") if date_fields and f["field"] in date_fields else f["value"]
                for f in filters
            ])
            operators = separator.join(["1"] * len(filters))
            params = f"filterfieldids={field_ids}&filtervalues={values}&operatortypes={operators}&{params}"
        return params

    medewerker_filters = [f for f in filters if f["field"] == "medewerker"]

    medewerker_params = _build(medewerker_filters)
    nacalc_hours = _build(filters, date_fields={"datum"})

    return medewerker_params, nacalc_hours